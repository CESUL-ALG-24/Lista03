valor = float(input("Informe o valor original: "))
dias_atraso = int(input("Informe o número de dias de atraso: "))

multa = valor * 0.05 * dias_atraso
valor_final = valor + multa

print("O valor final a pagar é R$", valor_final)
