def inverter_texto(texto):
    resultado = ''
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

texto = "Texto para inverter"

# Chamar a função e imprimir o resultado
print(inverter_texto(texto))
