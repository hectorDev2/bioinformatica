
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
