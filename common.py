def descargar_datos():
  print("Hola")


def leer_datos():
  ruta_archivo = '/content/bert/escenarios_elegidos.txt'
  with open(ruta_archivo, 'r') as archivo:
    contenido = archivo.read()
  lista = contenido.splitlines()
  for indice, oracion in enumerate(lista):
    print(f"Escenario {indice+1}: {oracion}")
