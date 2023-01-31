"""   
      Programa6
      Nombre: Marcos Eduardo I. H.
      Fecha: 31/01/2023 
      Descripcion: Cuadrado y Circulo
"""


def area_del_Cuadrado(l):
  # Perímetro
  p = l + l + l + l

  # Area
  area = l * l

  return area, p


area, p = area_del_Cuadrado(29)
print("Cuadrado")
print("El área es:", area)
print("El perímetro es:", p)


def area_del_Cirulo(r):
  # Perímetro
  p = 2 * 3.1416 * r

  # Area
  area = 3.1416 * r**2

  return area, p


area, p = area_del_Cirulo(5)
print("Circulo")
print("El área de un circulo de", area, "de radio es", 5)
print("El perimetro de un circulo de", p, "de radio es", 5)
