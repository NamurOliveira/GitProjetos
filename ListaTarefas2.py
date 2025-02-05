class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluida = False

    def __str__(self):
        status = "[x]" if self.concluida else "[ ]"
        return f"{status} {self.titulo}"

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo):
        nova_tarefa = Tarefa(titulo)
        self.tarefas.append(nova_tarefa)
        print(f"Tarefa adicionada: {titulo}")

    def marcar_como_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluida = True
            print(f"Tarefa concluída: {self.tarefas[indice].titulo}")
        else:
            print("Índice inválido.")

    def visualizar_tarefas_pendentes(self):
        tarefas_pendentes = [tarefa for tarefa in self.tarefas if not tarefa.concluida]
        if tarefas_pendentes:
            print("Tarefas pendentes:")
            for i, tarefa in enumerate(tarefas_pendentes, start=1):
                print(f"{i}. {tarefa}")
        else:
            print("Nenhuma tarefa pendente.")

# Testando o sistema
lista_tarefas = ListaDeTarefas()
lista_tarefas.adicionar_tarefa("Estudar para a prova de matemática")
lista_tarefas.adicionar_tarefa("Fazer exercícios de programação")
lista_tarefas.adicionar_tarefa("Comprar mantimentos")

lista_tarefas.marcar_como_concluida(1)

lista_tarefas.visualizar_tarefas_pendentes()
