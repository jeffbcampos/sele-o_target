import json

with open('faturamento.json') as f:
    fatura = json.load(f)
    
def valor_total(fatura):
    valor_total = 0    
    for i in range(len(fatura)):        
        valor_total += fatura[i]['valor']    
    return valor_total

print(valor_total(fatura))

sao_paulo = (fatura[0]['valor'] * 100) / valor_total(fatura)
rio_janeiro = (fatura[1]['valor'] * 100) / valor_total(fatura) 
minas_gerais = (fatura[2]['valor'] * 100) / valor_total(fatura)
espirito_santo = (fatura[3]['valor'] * 100) / valor_total(fatura)
outros_estados = (fatura[4]['valor'] * 100) / valor_total(fatura)

print(f"São Paulo: {sao_paulo:.2f}%\n Rio de Janeiro: {rio_janeiro:.2f}%\n Minas Gerais: {minas_gerais:.2f}%\n Espírito Santo: {espirito_santo:.2f}%\n Outros Estados: {outros_estados:.2f}%")



