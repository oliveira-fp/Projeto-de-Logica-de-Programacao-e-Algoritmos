# Sistema de Gerenciamento de Funcionários da Empresa
lista_funcionarios = []

def cadastrar_funcionario(id):
    """
    Cadastra um novo funcionário no sistema
    Args:
        id (int): Identificador único do funcionário
    """
    print('--------------------------------------------------------')
    print('---------------MENU CADASTRAR FUNCIONÁRIO---------------')
    print(f'Id do Funcionário: {id}')

    # Coleta dados do funcionário
    nome = input('Por favor entre com o nome do Funcionário: ')
    setor = input('Por favor entre com o setor do Funcionário: ')
    salario = input('Por favor entre com o salário do Funcionário: ')

    # Cria dicionário com os dados do funcionário
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salário': salario
    }

    # Adiciona funcionário à lista global
    lista_funcionarios.append(funcionario)
    print('Funcionário cadastrado com sucesso!')
    print('--------------------------------------------------------\n')

def consultar_funcionario():
    """
    Consulta funcionários cadastrados no sistema com várias opções de filtro
    """
    while True:
        print('''--------------------------------------------------------
---------------MENU CONSULTAR FUNCIONÁRIO---------------
Escolha a opção desejada:
1 - Consultar Todos os Funcionários
2 - Consultar Funcionário por id
3 - Consultar Funcionário(s) por setor
4 - Retornar''')

        consulta = input('>>')

        if consulta == '1':
            # Consulta todos os funcionários cadastrados
            print('----------------')
            if not lista_funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                for funcionario in lista_funcionarios:
                    for chave, valor in funcionario.items():
                        print(f'{chave}: {valor}')
                    print('\n----------------')

        elif consulta == '2':
            # Consulta por ID específico
            try:
                idBusca = int(input('Digite o id do funcionário: '))
                print('----------------')
                encontrado = False
                for funcionario in lista_funcionarios:
                    if funcionario['id'] == idBusca:
                        for chave, valor in funcionario.items():
                            print(f'{chave}: {valor}')
                        encontrado = True
                        print('\n----------------')
                        break
                if not encontrado:
                    print("Funcionário não encontrado.")
            except ValueError:
                print("ID deve ser um número inteiro.")

        elif consulta == '3':
            # Consulta por setor (case insensitive)
            print('----------------')
            setorBusca = input('Digite o setor do(s) funcionário(s): ').upper()
            encontrados = False
            for funcionario in lista_funcionarios:
                if funcionario['setor'].upper() == setorBusca:
                    for chave, valor in funcionario.items():
                        print(f'{chave}: {valor}')
                    print('')
                    encontrados = True
            if not encontrados:
                print("Nenhum funcionário encontrado neste setor.")

        elif consulta == '4':
            # Retorna ao menu principal
            return
        else:
            print('Opção inválida. Tente novamente.\n')

def remover_funcionario():
    """
    Remove um funcionário do sistema com base no ID
    """
    print('--------------------------------------------------------')
    print('----------------MENU REMOVER FUNCIONÁRIO----------------')

    while True:
        try:
            id = int(input('Digite o id do funcionário a ser removido: '))
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id:
                    lista_funcionarios.remove(funcionario)
                    print('Funcionário removido com sucesso!')
                    return
            print('Id inválido ou funcionário não encontrado.\n')
        except ValueError:
            print("Por favor, digite um ID válido (número inteiro).")

def main():
    """
    Função principal que gerencia o fluxo do programa
    """
    id_global = 2955202

    print('-- Bem-vindo a Empresa--')

    while True:
        print('''--------------------------------------------------------
---------------------MENU PRINCIPAL---------------------
Escolha a opção desejada:
1 - Cadastrar Funcionário
2 - Consultar Funcionário(s)
3 - Remover Funcionário
4 - Sair''')

        opcao = input('>>')

        if opcao == '1':
            cadastrar_funcionario(id_global)
            id_global += 1  # Incrementa ID para próximo funcionário
        elif opcao == '2':
            consultar_funcionario()
        elif opcao == '3':
            remover_funcionario()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print('Opção inválida. Tente novamente.\n')

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
