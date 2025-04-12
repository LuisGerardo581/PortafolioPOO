from animal import Animal

class Perro(Animal):
  def __init__(self, nombre, edad, raza):
   super().__init__(nombre, edad)
   self.raza=raza

  def hacer_sonido(self):
    print(f'{self.nombre} estaladrando')
    
  def es_cahorro(self):
    return self.edad < 2