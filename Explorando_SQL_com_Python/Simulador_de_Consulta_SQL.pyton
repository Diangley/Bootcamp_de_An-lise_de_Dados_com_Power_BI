def filtrar_funcionarios(funcionarios, cargo):
    # Filtra os funcionários pelo cargo especificado
    return [funcionario["nome"] for funcionario in funcionarios if funcionario["cargo"] == cargo]

# Função para entrada do usuário
def main_filtro():
    n = int(input())  # Número de funcionários
    funcionarios = []

    for _ in range(n):
        id_funcionario = int(input())  # ID do funcionário
        nome = input()  # Nome do funcionário
        cargo = input()  # Cargo do funcionário
        funcionarios.append({"id": id_funcionario, "nome": nome, "cargo": cargo})

    cargo_filtro = input()  # Cargo a ser filtrado
    resultado = filtrar_funcionarios(funcionarios, cargo_filtro)
    
    print(resultado)

# Executando a função
main_filtro()
