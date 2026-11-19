from .texto import contem

CRITERIOS_ORDENACAO = ("identificador", "titulo", "categoria")
CAMPOS_BUSCA = ("titulo", "categoria")
CAMPOS_EDITAVEIS = ("titulo", "categoria", "descricao", "publico_alvo", "canal")


class No:
    def __init__(self, servico):
        self.servico = servico
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def esta_vazia(self):
        return self.inicio is None

    def inserir_final(self, servico):
        novo = No(servico)
        if self.fim is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self.tamanho += 1

    def percorrer(self):
        atual = self.inicio
        while atual is not None:
            yield atual.servico
            atual = atual.proximo

    def buscar_por_id(self, identificador):
        atual = self.inicio
        while atual is not None:
            if atual.servico.identificador == identificador:
                return atual.servico
            atual = atual.proximo
        return None

    def buscar_por_texto(self, campo, termo):
        if campo not in CAMPOS_BUSCA:
            raise ValueError("Campo de busca inválido: " + campo)
        resultado = ListaEncadeada()
        atual = self.inicio
        while atual is not None:
            if contem(getattr(atual.servico, campo), termo):
                resultado.inserir_final(atual.servico)
            atual = atual.proximo
        return resultado

    def atualizar(self, identificador, novos_dados):
        for campo in novos_dados:
            if campo not in CAMPOS_EDITAVEIS:
                raise ValueError("Campo não editável: " + campo)
        servico = self.buscar_por_id(identificador)
        if servico is None:
            return False
        for campo, valor in novos_dados.items():
            setattr(servico, campo, valor)
        return True

    def remover(self, identificador):
        anterior = None
        atual = self.inicio
        while atual is not None and atual.servico.identificador != identificador:
            anterior = atual
            atual = atual.proximo
        if atual is None:
            return None
        if anterior is None:
            self.inicio = atual.proximo
        else:
            anterior.proximo = atual.proximo
        if atual is self.fim:
            self.fim = anterior
        atual.proximo = None
        self.tamanho -= 1
        return atual.servico

    def ordenar(self, criterio):
        if criterio not in CRITERIOS_ORDENACAO:
            raise ValueError("Critério de ordenação inválido: " + criterio)
        self.inicio = self._merge_sort(self.inicio, criterio)
        self.fim = None
        atual = self.inicio
        while atual is not None:
            self.fim = atual
            atual = atual.proximo

    def _merge_sort(self, cabeca, criterio):
        if cabeca is None or cabeca.proximo is None:
            return cabeca
        segunda_metade = self._dividir(cabeca)
        esquerda = self._merge_sort(cabeca, criterio)
        direita = self._merge_sort(segunda_metade, criterio)
        return self._mesclar(esquerda, direita, criterio)

    def _dividir(self, cabeca):
        lento = cabeca
        rapido = cabeca.proximo
        while rapido is not None and rapido.proximo is not None:
            lento = lento.proximo
            rapido = rapido.proximo.proximo
        segunda_metade = lento.proximo
        lento.proximo = None
        return segunda_metade

    def _mesclar(self, a, b, criterio):
        base = No(None)
        cauda = base
        while a is not None and b is not None:
            if a.servico.chave(criterio) <= b.servico.chave(criterio):
                cauda.proximo = a
                a = a.proximo
            else:
                cauda.proximo = b
                b = b.proximo
            cauda = cauda.proximo
        cauda.proximo = a if a is not None else b
        return base.proximo
