def criar_tarefa(nome, descricao, prioridade, categoria, concluida = False):
    return {'nome': nome, 'descricao': descricao, 'prioridade': prioridade, 'categoria': categoria, 'concluida': concluida}

def adicionar_tarefa(lista_tarefas, tarefa):
    lista_tarefas.append(tarefa)
    print(f"Tarefa '{tarefa['nome']}' adicionada com sucesso!")

def listar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Não há tarefas cadastradas.")
    else:
        for i, tarefa in enumerate(lista_tarefas, 1):
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            print(f"{i}. {tarefa['nome']} - {status}, Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}")

def marcar_como_concluida(lista_tarefas, nome_tarefa):
    for tarefa in lista_tarefas:
        if tarefa['nome'] == nome_tarefa:
            tarefa['concluida'] = True
            print(f"Tarefa '{nome_tarefa}' marcada como concluída.")
            return
    print(f"Tarefa '{nome_tarefa}' não encontrada.")

def exibir_por_prioridade(lista_tarefas, prioridade):
    tarefas_prioridade = [tarefa for tarefa in lista_tarefas if tarefa['prioridade'] == prioridade]
    listar_tarefas(tarefas_prioridade)

def exibir_por_categoria(lista_tarefas, categoria):
    tarefas_categoria = [tarefa for tarefa in lista_tarefas if tarefa['categoria'] == categoria]
    listar_tarefas(tarefas_categoria)

tarefas = []
controle = True

while controle:
    print("\n***** Gerenciador de Tarefas *****")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Exibir Tarefas por Prioridade")
    print("5. Exibir Tarefas por Categoria")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        prioridade = input("Digite a prioridade da tarefa: ")
        categoria = input("Digite a categoria da tarefa: ")
        nova_tarefa = criar_tarefa(nome, descricao, prioridade, categoria)
        adicionar_tarefa(tarefas, nova_tarefa)

    elif opcao == '2':
        listar_tarefas(tarefas)

    elif opcao == '3':
        nome_tarefa = input("Digite o nome da tarefa a ser marcada como concluída: ")
        marcar_como_concluida(tarefas, nome_tarefa)

    elif opcao == '4':
        prioridade = input("Digite a prioridade para filtrar: ")
        exibir_por_prioridade(tarefas, prioridade)

    elif opcao == '5':
        categoria = input("Digite a categoria para filtrar: ")
        exibir_por_categoria(tarefas, categoria)

    elif opcao == '6':
        print("Saindo do programa. Até mais!")
        controle = False

    else:
        print("Opção inválida. Tente novamente.")