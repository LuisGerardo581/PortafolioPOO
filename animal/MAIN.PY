from animal import Animal
from perro import Perro
from gato import Gato
from ave import Ave
from murcielgo import Murcielago
from ornitorrinco import Ornitorrinco

def main():
  #leon = Animal("Leon", 5)
  #print(leon)
  #leon.hacer_sonido()
  
  perro = Perro("Churro", 3, "Salchicha")
  perro.hacer_sonido()
  print(perro.es_cachorro())
  
  gato = Gato("Michi", 2, 7)
  gato.hacer_sonido()
  print("Vidas (s) restante(s):", gato.vidas)
  print("Atropellado 😿" if not gato.sobrevive() else "Vive 😺")
  print("Vidas (s) restante(s):", gato.vidas)
  print("Intoxicado 😿" if not gato.sobrevive() else "Vive 😺")
  print("Vidas (s) restante(s):", gato.vidas)
  print("Electrocutado 😿" if not gato.sobrevive() else "Vive 😺")
  print("Vidas (s) restante(s):", gato.vidas)
  
  ave = Ave("LuPe", 1)
  ave.hacer_sonido()
  
  dracula = Murcielago("Dracula", 100, "Vampiro")
  dracula.hacer_sonido()
  dracula.soy_un()
  
  perry=Ornitorrinco("Perry", 5)
  perry.hacer_sonido()
  print(f"{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevos(s)")
  perry.poner_huevo()
  print(f"{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevos(s)")
  
if __name__ == '__main__':
  main()