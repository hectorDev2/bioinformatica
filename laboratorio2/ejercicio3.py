
def ComplementoInverso(patron):
  return invertir(Complemento_dna(patron))

def Complemento_dna(patron):
  return "".join(map(complemento_caracter_dna,patron))

def invertir(s):
  return s if len(s)==0 else invertir(s[1:])+s[0]

def complemento_caracter_dna(caracter):
  return {"A":"T","T":"A","G":"C","C":"G"}[caracter]

text="GACGTAT"

print(ComplementoInverso(text))
