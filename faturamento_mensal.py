faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_mensal = 0
for estado, faturamento in faturamento_estados.items():
    total_mensal += faturamento
for estado, faturamento in faturamento_estados.items():
    percentual = (faturamento / total_mensal) * 100
    print(f'{estado}: {percentual:.2f}%')
