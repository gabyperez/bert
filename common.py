def agregar_punto_al_final(oracion):
  nueva = oracion.strip()
  if oracion[-1] != ".":
    nueva = oracion + "."
  return nueva

def descargar_archivo(ruta_archivo):
  with open(ruta_archivo, 'r') as archivo:
    contenido = archivo.read()
  lista = contenido.splitlines()
  return lista
  
def imprimir_lista(lista):
    for indice, oracion in enumerate(lista):
      print(f"Escenario {indice+1}: {oracion}")
