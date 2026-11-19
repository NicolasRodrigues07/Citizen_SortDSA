DIGITOS = "0123456789"
TAMANHO_MAXIMO_ID = 9


def preenchido(texto):
    return len(texto.strip()) > 0


def interpretar_identificador(texto):
    texto = texto.strip()
    if len(texto) == 0 or len(texto) > TAMANHO_MAXIMO_ID:
        return None
    for caractere in texto:
        if caractere not in DIGITOS:
            return None
    valor = int(texto)
    if valor <= 0:
        return None
    return valor
