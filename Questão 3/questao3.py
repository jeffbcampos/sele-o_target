import json

with open('faturamento.json') as f:
    fatura = json.load(f)

def maior_valor(fatura):
    maior = fatura[0]    
    for valor in fatura:
        if valor['valor'] > maior['valor']:
            maior = valor
    return maior

def menor_valor(fatura):
    maior = fatura[0]    
    for valor in fatura:
        if valor['valor'] < maior['valor']:
            maior = valor
    return maior

def dia_maior_fatura_mensal(fatura, soma):
    dias = 0
    for dia in fatura:
        if dia['valor'] > soma:
            dias += 1
    return dias

def media_mensal(fatura):
    soma = 0
    for valor in fatura:
        soma += valor['valor']
    media_mensal = soma/len(fatura)    
    return round((soma/len(fatura)), 2)      

dia_maior_valor = maior_valor(fatura)
dia_menos_valor = menor_valor(fatura)
media_mensal = media_mensal(fatura)
dias = dia_maior_fatura_mensal(fatura, media_mensal)
print(f"A media mensal de vendas é de R$ {media_mensal:.2f}")
print(f"O dia com maior fatura foi {dia_maior_valor['dia']}")
print(f"o dia com menor fatura foi {dia_menos_valor['dia']}")
print(f"O numero de dias com fatura acima da media mensal é de {dias} dias")
