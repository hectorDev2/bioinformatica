def dividir_adn(texto, tamano):
    return [texto[i:i+tamano] for i in range(0, len(texto), tamano)]

# Ejemplo de uso:
texto_adn = "ACGTTGCATGTCGCATGATGAGAGCT"
tamano_subcadena = 4

subcadenas = dividir_adn(texto_adn, tamano_subcadena)
print(subcadenas)
