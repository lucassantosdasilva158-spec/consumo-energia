aparelho = input ("Digite o nome do aparelho: ")
potencia = float (input("Digite a potencia do aparelho em watts (W) usando apenas numeros, exemplo 50: "))
consumo_em_horas = float (input("Digite o consumo em horas do aparelho apenas com numero, exemplo: 12: "))
consumo_mensal = (potencia * consumo_em_horas * 30) / 1000

print (f"Aparelho: {aparelho}")
print (f"Consumo mensal: {consumo_mensal:.2f} kWh/mes")



       