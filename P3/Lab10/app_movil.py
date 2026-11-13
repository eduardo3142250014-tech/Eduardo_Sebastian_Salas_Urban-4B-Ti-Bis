class SuscripcionExpiradaError(Exception):
    """Se lanza cuando se intenta usar una función Pro sin suscripción activa."""


class PuntosInsuficientesError(Exception):
    """Se lanza cuando no hay gemas suficientes para completar una operación."""


class PerfilMovil:
    def __init__(
        self,
        username: str,
        gemas: int = 50,
        racha_dias: int = 1,
        notificaciones_activas: bool = True,
    ):
        if not isinstance(gemas, int) or isinstance(gemas, bool):
            raise TypeError("Las gemas deben ser un número entero.")
        if gemas < 0:
            raise ValueError("Las gemas no pueden ser negativas.")

        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    def ganar_gemas(self, cantidad: int) -> int:
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise TypeError("La cantidad debe ser un número entero.")
        if cantidad <= 0:
            raise ValueError("La cantidad de gemas debe ser positiva.")

        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise TypeError("La cantidad debe ser un número entero.")
        if cantidad <= 0:
            raise ValueError("La cantidad de gemas debe ser positiva.")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError("No tienes gemas suficientes.")

        self.gemas -= cantidad
        return self.gemas


class PerfilPro(PerfilMovil):
    def __init__(
        self,
        username: str,
        meses_suscripcion: int,
        gemas: int = 50,
        racha_dias: int = 1,
        notificaciones_activas: bool = True,
    ):
        super().__init__(
            username=username,
            gemas=gemas,
            racha_dias=racha_dias,
            notificaciones_activas=notificaciones_activas,
        )

        if (
            not isinstance(meses_suscripcion, int)
            or isinstance(meses_suscripcion, bool)
        ):
            raise TypeError("Los meses de suscripción deben ser un número entero.")
        if meses_suscripcion <= 0:
            raise ValueError("El periodo inicial debe ser mayor que cero.")

        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError("La suscripción Pro ha expirado.")

        return "Descarga de contenido offline realizada correctamente."
