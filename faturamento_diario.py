import json

with open('faturamento.json') as f:
    data = json.load(f)

menor_faturamento = float('inf')
maior_faturamento = float('-inf')

soma_faturamento = 0
dias_com_faturamento = 0
dias_acima_media = 0

for dia in data:
    valor = dia['valor']
    if valor != 0:
        soma_faturamento += valor
        dias_com_faturamento += 1
        if valor < menor_faturamento:
            menor_faturamento = valor
        if valor > maior_faturamento:
            maior_faturamento = valor

media_mensal = soma_faturamento / dias_com_faturamento

for dia in data:
    if dia['valor'] > media_mensal:
        dias_acima_media += 1

print("Menor valor de faturamento: ", menor_faturamento)
print("Maior valor de faturamento: ", maior_faturamento)
print("Número de dias acima da média: ", dias_acima_media)
