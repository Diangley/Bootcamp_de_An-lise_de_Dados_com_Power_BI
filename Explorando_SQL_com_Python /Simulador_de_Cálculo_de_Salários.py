def calcular_salarios(funcionarios):
    # Calcula os salários com base nas horas trabalhadas e no valor por hora
    salarios = []
    for funcionario in funcionarios:
        salario = funcionario["horas_trabalhadas"] * funcionario["valor_hora"]
        salarios.append(f'{funcionario["nome"]}: {salario:.1f}')
    return salarios

# Função para entrada do usuário
def main_salario():
    n = int(input())  # Quantidade de funcionários
    funcionarios = []

    for _ in range(n):
        nome = input()  # Nome do funcionário
        horas_trabalhadas = int(input())  # Horas trabalhadas pelo funcionário
        valor_hora = float(input())  # Valor por hora do funcionário
        
        # Adiciona um dicionário com as informações do funcionário à lista 'funcionarios'
        funcionarios.append({
            "nome": nome,
            "horas_trabalhadas": horas_trabalhadas,
            "valor_hora": valor_hora
        })

    resultado = calcular_salarios(funcionarios)
    
    # Exibe o resultado
    for salario in resultado:
        print(salario)

# Executando a função
main_salario()
