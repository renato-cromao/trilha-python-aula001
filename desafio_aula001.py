# DESAFIO DA AULA 001
# 1) Solicita ao usuário que digite seu nome.
# 2) Solicita ao usuário que digite o valor do seu salário. Converta a entrada para um número de ponto flutuante.
# 3) Solicita ao usuário que digite o valor do bônus recebido. Converta a entrada para um número de ponto flutuante.
# 4) Calcule o valor do bônus final. Fórmula "1000 + salário * bônus"
# 5) Imprima o cálculo do KPI para o usuário.
# 6) Imprime uma mensagem personalizada incluindo o nome do usuário, salário e bônus.

# Plus: Quantos bugs e riscos você consegue identificar nesse programa?


# RESOLUÇÃO

nome = input('Digite o seu nome: ')
salario = float(input('Digite o seu salário: '))
bonus = float(input('Digite o seu bônus: '))

valor_kpi = 1000 + (salario * bonus)

print(f'O cálculo do KPI será:  1000 + ({salario} * {bonus})')

print(f'Olá, {nome}! O valor do seu KPI será de {valor_kpi}.')