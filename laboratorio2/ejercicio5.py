def unir_y_reemplazar_adn(cadenas):
    # Unir todas las cadenas de ADN en una sola usando un bucle
    cadena_unida = ""
    for cadena in cadenas:
        cadena_unida += cadena
    
    # Reemplazar 'A' por 'T' usando una lista y un bucle
    cadena_modificada = []
    for nucleotido in cadena_unida:
        if nucleotido == 'A':
            cadena_modificada.append('T')
        else:
            cadena_modificada.append(nucleotido)
    
    return ''.join(cadena_modificada)

cadenas_adn = ["ACGT", "TGCA", "GATC", "AAGC"]

cadena_resultante = unir_y_reemplazar_adn(cadenas_adn)
print(cadena_resultante)
