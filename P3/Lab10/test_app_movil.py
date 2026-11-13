import pytest

from app_movil import (
    PerfilMovil,
    PerfilPro,
    PuntosInsuficientesError,
    SuscripcionExpiradaError,
)


@pytest.fixture
def perfil():
    """Proporciona un perfil estándar y nuevo para cada prueba."""
    return PerfilMovil("usuario_prueba")


def test_atributos_iniciales(perfil):
    assert perfil.username == "usuario_prueba"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_ganar_gemas(perfil):
    resultado = perfil.ganar_gemas(20)
    assert resultado == 70
    assert perfil.gemas == 70


@pytest.mark.parametrize("cantidad", [1, 10, 50, 100])
def test_ganar_gemas_con_varias_cantidades(perfil, cantidad):
    assert perfil.ganar_gemas(cantidad) == 50 + cantidad


@pytest.mark.parametrize("cantidad", [0, -1, -50])
def test_ganar_gemas_rechaza_cantidades_no_positivas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)


def test_gastar_gemas(perfil):
    resultado = perfil.gastar_gemas(15)
    assert resultado == 35
    assert perfil.gemas == 35


def test_gastar_mas_gemas_de_las_disponibles(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(51)

    assert perfil.gemas == 50


@pytest.mark.parametrize("cantidad", [0, -1, -20])
def test_gastar_gemas_rechaza_cantidades_no_positivas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(cantidad)


def test_perfil_rechaza_gemas_iniciales_negativas():
    with pytest.raises(ValueError):
        PerfilMovil("usuario", gemas=-1)


def test_perfil_pro_hereda_de_perfil_movil():
    perfil_pro = PerfilPro("usuario_pro", meses_suscripcion=3)

    assert isinstance(perfil_pro, PerfilMovil)
    assert isinstance(perfil_pro, PerfilPro)
    assert perfil_pro.es_pro is True
    assert perfil_pro.meses_suscripcion == 3


def test_perfil_pro_rechaza_periodo_inicial_cero():
    with pytest.raises(ValueError):
        PerfilPro("usuario_pro", meses_suscripcion=0)


def test_descargar_contenido_offline_con_suscripcion_activa():
    perfil_pro = PerfilPro("usuario_pro", meses_suscripcion=2)

    resultado = perfil_pro.descargar_contenido_offline()

    assert resultado == "Descarga de contenido offline realizada correctamente."
    assert perfil_pro.es_pro is True


def test_suscripcion_expirada_cambia_estado_y_lanza_excepcion():
    perfil_pro = PerfilPro("usuario_pro", meses_suscripcion=1)
    perfil_pro.meses_suscripcion = 0

    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()

    assert perfil_pro.es_pro is False
