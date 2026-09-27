# lab1 
class cat:
  def __init__(self, color, size, name):
    self.color = color
    self.size = size
    self.name = name

  def run(self):
    print("the cat is running")
  def sleep(self):
    print("the cat is sleeping")
  def show_color(self):
    print(f"the color of the cat is: {self.color}")


# self: se utiliza para decirle a python a que objet pertenecen los atributos
# create an instance using the class "cat"
cat1 = cat("gray", "small", "luna")
cat2 = cat("black", "large", "batman")

#first instance
print(cat1.size)
print(cat1.name)
cat1.run()
cat1.show_color()

#second instance
print(cat2.size)
print(cat2.name)
cat2.run()
cat2.show_color()
