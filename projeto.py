def ajuste_termico(upc):
    if upc > 150:
        return upc + (upc * 0.08)
    else:
        return upc + (upc * 0.04)

def classificar(upc):
    if upc >= 250:
        return "Vermelho"
    elif upc > 180:
        return "Amarelo"
    elif upc >= 120:
        return "Verde"
    else:
        print("Pressão baixa - Risco de entupimento do duto.")
        return "Aviso"

def pressao_min(upc, minimo):
    if upc < minimo:
        return upc
    else:
        return minimo

def percent(verde, num):
    return (verde/num) * 100

def percent_travamento(i, qtd):
    return (i/qtd) * 100

def calc_risco(risco, i):
    risco /= i
    if risco < 1.5:
        return "Atividade normal"
    elif risco <= 2:
        return "Oscilação detectada"
    else:
        return "Risco de acidente"
    return risco/i

def metricas(total, num, leituras, percent_verde, menor, risco):
    print(risco)
    print(f"Media: {total / num :.2f}")
    print(f"Porcentagem de zonas verdes:  {percent_verde:.2f}")
    print(f'Menor valor lido: {menor:.2f}')
    if leituras == 0:
        print("Conclusão normal")
    else:
        print("Conclusão por travamento")
        print(f"Porcentagem de leituras: {leituras:.2f}")


total = 0
travamento = 0
i = 0
menor = int
verde = 0
risco = 0

qtd = int(input("Digite o numero de leituras: "))
while travamento != 2 and i < qtd:
    upc = int(input("Digite o valor em UPC: "))

    upc = ajuste_termico(upc)
    zona = classificar(upc)

    if zona == "Vermelho" or zona == "Aviso":
        risco += 3
        travamento += 1
    else:
        if zona == "Verde":
            verde += 1
            risco += 1
        else:
            risco += 2
        travamento = 0
    
    if i == 0:
        menor = upc
    else:
        menor = pressao_min(upc, menor)
    
    total += upc
    i += 1

if travamento == 2:
    leituras = percent_travamento(i, qtd)
else:
    leituras = 0

percent_verde = percent(verde, i)
risco = calc_risco(risco, i)
metricas(total, i, leituras, percent_verde, menor, risco)
