from .texto import normalizar

ROTULOS = {
    "identificador": "Identificador",
    "titulo": "Título",
    "categoria": "Categoria",
    "descricao": "Descrição",
    "publico_alvo": "Público-alvo",
    "canal": "Canal/Local de atendimento",
}


class Servico:
    def __init__(self, identificador, titulo, categoria, descricao, publico_alvo, canal):
        self.identificador = identificador
        self.titulo = titulo
        self.categoria = categoria
        self.descricao = descricao
        self.publico_alvo = publico_alvo
        self.canal = canal

    def chave(self, criterio):
        if criterio == "identificador":
            return self.identificador
        return normalizar(getattr(self, criterio))

    def formatar(self):
        linhas = []
        for campo in ROTULOS:
            linhas.append(f"{ROTULOS[campo]}: {getattr(self, campo)}")
        return "\n".join(linhas)
