def transcribir_adn_a_arn(cadena_adn):
    # Reemplazar todas las 'T' por 'U' para transcribir a ARN
    cadena_arn = cadena_adn.replace('T', 'U')
    return cadena_arn

# Ejemplo de uso:
if __name__ == "__main__":
    cadena_adn = "GATTACA"
    cadena_arn = transcribir_adn_a_arn(cadena_adn)
    print(f"Cadena de ADN: {cadena_adn}")
    print(f"Cadena transcrita de ARN: {cadena_arn}")
