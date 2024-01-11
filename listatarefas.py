class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def inserir_tarefa(self, tarefa):
        self.tarefas.append(tarefa)   
        print(f'Tarefa "{tarefa}" adicionada com sucesso.')

    def editar_tarefa(self, indice, nova_tarefa):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice] = nova_tarefa
            print(f'Tarefa no índice {indice} editada para "{nova_tarefa}".')
        else:
            print('Índice inválido. Tarefa não encontrada.')


    def listar_tarefas(self):
        print('\nLista de Tarefas:')
        for i, tarefa in enumerate(self.tarefas):
            print(f'{i}. {tarefa}')


    def marcar_concluido(self, indice):
        if 0 <= indice < len(self.tarefas):
            print(f'Tarefa "{self.tarefas[indice]}" marcada como concluída.')
            self.tarefas.pop(indice)
        else:
            print('Índice inválido. Tarefa não encontrada.')



listar_tarefas = ListaDeTarefas()

while True:
    print('Seu CheckList')
    print('\nOpções:')
    print('1. Inserir tarefa')
    print('2. Editar tarefa')
    print('3. Listar tarefas')
    print('4. Marcar como concluída')
    print('5. Remover tarefa')
    print('0. Sair')


    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        tarefa = input('Digite a nova tarefa: ')
        listar_tarefas.inserir_tarefa(tarefa)

    elif opcao == '2':
        listar_tarefas.listar_tarefas()
        indice = int(input('Digite o índice da tarefa que deseja editar: ')) 
        nova_tarefa = input('Digite a nova descrição da tarefa: ')

    elif opcao == '3':
        listar_tarefas.listar_tarefas()

    elif opcao == '4':
        listar_tarefas.listar_tarefas()
        indice = int(input('Digite o índice da tarefa concluída: ')) 
        listar_tarefas.marcar_concluido(indice) 

    elif opcao == '5':
        listar_tarefas.listar_tarefas()
        indice = int(input('Digite o índice da tarefa que deseja remover: '))

    elif opcao == '0':
        break
    else:
        print('Opção inválida. Tente novamente.')                 