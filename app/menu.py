from .dados_exemplo import SERVICOS_EXEMPLO
from .lista_encadeada import ListaEncadeada
from .servico import Servico, ROTULOS
from .texto import cortar
from .validacao import interpretar_identificador, preenchido

MSG_LISTA_VAZIA = "A lista está vazia. Cadastre um serviço ou carregue os dados de exemplo."
MSG_OPCAO_INVALIDA = "Opção inválida. Escolha uma das opções listadas."

NOMES_CRITERIO = {"identificador": "identificador", "titulo": "título", "categoria": "categoria"}


class Menu:
    def __init__(self, lista=None):
        self.lista = lista if lista is not None else ListaEncadeada()

    def executar(self):
        print("=== Citizen Assist AI | Gerenciador de Serviços ===")
        acoes = {
            "1": self.cadastrar,
            "2": self.consultar,
            "3": self.listar,
            "4": self.atualizar,
            "5": self.excluir,
            "6": self.pesquisar,
            "7": self.ordenar,
            "8": self.carregar_exemplos,
        }
        while True:
            self._mostrar_opcoes()
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "0":
                print("Encerrando o sistema. Até logo!")
                break
            acao = acoes.get(opcao)
            if acao is None:
                print("Opção inválida. Digite um número de 0 a 8.")
                continue
            acao()

    def _mostrar_opcoes(self):
        print("\n--- Menu Principal ---")
        print("[1] Cadastrar serviço")
        print("[2] Consultar por identificador")
        print("[3] Listar todos")
        print("[4] Atualizar serviço")
        print("[5] Excluir serviço")
        print("[6] Pesquisar por título ou categoria")
        print("[7] Ordenar lista")
        print("[8] Carregar dados de exemplo")
        print("[0] Sair")

    def _ler_identificador(self, mensagem):
        while True:
            texto = input(mensagem).strip()
            if texto == "0":
                return None
            identificador = interpretar_identificador(texto)
            if identificador is not None:
                return identificador
            print("Identificador inválido. Use apenas números inteiros positivos.")

    def _ler_obrigatorio(self, mensagem):
        while True:
            texto = input(mensagem).strip()
            if preenchido(texto):
                return texto
            print("Campo obrigatório. Digite um valor.")

    def _mostrar_tabela(self, lista):
        print(f"{'ID':<6}{'Título':<36}{'Categoria':<26}{'Canal/Local'}")
        print("-" * 100)
        for servico in lista.percorrer():
            print(
                f"{servico.identificador:<6}"
                f"{cortar(servico.titulo, 34):<36}"
                f"{cortar(servico.categoria, 24):<26}"
                f"{cortar(servico.canal, 32)}"
            )
        print(f"Total: {len(lista)} serviço(s).")

    def cadastrar(self):
        print("\n--- Cadastrar serviço ---")
        while True:
            identificador = self._ler_identificador("Identificador (inteiro positivo, 0 para cancelar): ")
            if identificador is None:
                print("Operação cancelada.")
                return
            if self.lista.buscar_por_id(identificador) is None:
                break
            print(f"Já existe um serviço com o identificador {identificador}. Informe outro.")

        titulo = self._ler_obrigatorio("Título: ")
        categoria = self._ler_obrigatorio("Categoria: ")
        descricao = self._ler_obrigatorio("Descrição: ")
        publico_alvo = self._ler_obrigatorio("Público-alvo: ")
        canal = self._ler_obrigatorio("Canal/Local de atendimento: ")

        self.lista.inserir_final(Servico(identificador, titulo, categoria, descricao, publico_alvo, canal))
        print("Serviço cadastrado com sucesso.")

    def consultar(self):
        print("\n--- Consultar serviço ---")
        if self.lista.esta_vazia():
            print(MSG_LISTA_VAZIA)
            return
        identificador = self._ler_identificador("Identificador (0 para cancelar): ")
        if identificador is None:
            print("Operação cancelada.")
            return
        servico = self.lista.buscar_por_id(identificador)
        if servico is None:
            print(f"Serviço com identificador {identificador} não encontrado.")
            return
        print()
        print(servico.formatar())

    def listar(self):
        print("\n--- Serviços cadastrados ---")
        if self.lista.esta_vazia():
            print(MSG_LISTA_VAZIA)
            return
        self._mostrar_tabela(self.lista)

    def atualizar(self):
        print("\n--- Atualizar serviço ---")
        if self.lista.esta_vazia():
            print(MSG_LISTA_VAZIA)
            return
        identificador = self._ler_identificador("Identificador (0 para cancelar): ")
        if identificador is None:
            print("Operação cancelada.")
            return
        servico = self.lista.buscar_por_id(identificador)
        if servico is None:
            print(f"Serviço com identificador {identificador} não encontrado.")
            return

        print("\nRegistro atual:")
        print(servico.formatar())
        print("\nDigite o novo valor ou apenas Enter para manter o atual.")
        novos_dados = {}
        for campo in ("titulo", "categoria", "descricao", "publico_alvo", "canal"):
            novo = input(f"{ROTULOS[campo]} [{getattr(servico, campo)}]: ").strip()
            if preenchido(novo):
                novos_dados[campo] = novo

        if not novos_dados:
            print("Nenhuma alteração informada. O registro permanece igual.")
            return
        self.lista.atualizar(identificador, novos_dados)
        print("Serviço atualizado com sucesso.")

    def excluir(self):
        print("\n--- Excluir serviço ---")
        if self.lista.esta_vazia():
            print(MSG_LISTA_VAZIA)
            return
        identificador = self._ler_identificador("Identificador (0 para cancelar): ")
        if identificador is None:
            print("Operação cancelada.")
            return
        servico = self.lista.buscar_por_id(identificador)
        if servico is None:
            print(f"Serviço com identificador {identificador} não encontrado.")
            return

        print()
        print(servico.formatar())
        while True:
            resposta = input("\nConfirma a exclusão? (s/n): ").strip().lower()
            if resposta in ("s", "n"):
                break
            print("Responda com 's' para sim ou 'n' para não.")

        if resposta == "n":
            print("Exclusão cancelada.")
            return
        self.lista.remover(identificador)
        print("Serviço removido com sucesso.")

    def pesquisar(self):
        print("\n--- Pesquisar serviços ---")
        if self.lista.esta_vazia():
            print(MSG_LISTA_VAZIA)
            return
        campo = None
        while campo is None:
            print("[1] Por título")
            print("[2] Por categoria")
            print("[0] Voltar")
            opcao = input("Pesquisar por: ").strip()
            if opcao == "0":
                return
            if opcao == "1":
                campo = "titulo"
            elif opcao == "2":
                campo = "categoria"
            else:
                print(MSG_OPCAO_INVALIDA)

        termo = input("Termo de pesquisa: ").strip()
        while not preenchido(termo):
            print("O termo de pesquisa não pode ser vazio.")
            termo = input("Termo de pesquisa: ").strip()

        resultado = self.lista.buscar_por_texto(campo, termo)
        if resultado.esta_vazia():
            print(f"Nenhum serviço encontrado para '{termo}'.")
            return
        print(f"\n{len(resultado)} serviço(s) encontrado(s):")
        self._mostrar_tabela(resultado)

    def ordenar(self):
        print("\n--- Ordenar lista ---")
        if self.lista.esta_vazia():
            print(MSG_LISTA_VAZIA)
            return
        criterio = None
        while criterio is None:
            print("[1] Por identificador")
            print("[2] Por título")
            print("[3] Por categoria")
            print("[0] Voltar")
            opcao = input("Ordenar por: ").strip()
            if opcao == "0":
                return
            if opcao == "1":
                criterio = "identificador"
            elif opcao == "2":
                criterio = "titulo"
            elif opcao == "3":
                criterio = "categoria"
            else:
                print(MSG_OPCAO_INVALIDA)

        self.lista.ordenar(criterio)
        print(f"Lista ordenada por {NOMES_CRITERIO[criterio]}.")
        self._mostrar_tabela(self.lista)

    def carregar_exemplos(self):
        print("\n--- Carregar dados de exemplo ---")
        adicionados = 0
        ignorados = 0
        for dados in SERVICOS_EXEMPLO:
            if self.lista.buscar_por_id(dados[0]) is None:
                self.lista.inserir_final(Servico(*dados))
                adicionados += 1
            else:
                ignorados += 1
        print(f"{adicionados} serviço(s) de exemplo carregado(s). {ignorados} já existiam e foram ignorado(s).")
