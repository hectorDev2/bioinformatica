# def contar_ocurrencias(texto,patron):
#   return len(list(filter(lambda i:texto[i:i+len(patron)]==patron,range(len(texto)-len(patron)+1))))

# def contar_ocurrencias2(texto,patron):
#   return sum(1 for i in range(len(texto)-len(patron)+1) if texto[i:i+len(patron)]==patron)

# texto = "CACCGTCACAC"
# patron = "CAC"

# print(contar_ocurrencias(texto,patron))
# print(contar_ocurrencias2(texto,patron))

def MapaFrecuencia(texto,k):
  frecuencia={}
  n=len(texto)
  for i in range(n-k+1):
    Patron=texto[i:i+k]
    frecuencia[Patron]=0
  for i in range(n-k+1):
    Patron=texto[i:i+k]
    frecuencia[Patron]+=1
  return frecuencia

def PalabrasFrecuentes(texto,k):
  palabras=[]
  frecuencia=MapaFrecuencia(texto,k)
  max_frecuencia=max(frecuencia.values())
  for clave in frecuencia:
    if frecuencia[clave]==max_frecuencia:
      palabras.append(clave)
  return palabras

texto = "ACGTTGCATGTCGCATGATGAGAGCT"
k=4

print(PalabrasFrecuentes(texto,k))

