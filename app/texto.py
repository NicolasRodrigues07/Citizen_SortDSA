ACENTOS = {
    "á": "a", "à": "a", "ã": "a", "â": "a", "ä": "a",
    "é": "e", "è": "e", "ê": "e", "ë": "e",
    "í": "i", "ì": "i", "î": "i", "ï": "i",
    "ó": "o", "ò": "o", "õ": "o", "ô": "o", "ö": "o",
    "ú": "u", "ù": "u", "û": "u", "ü": "u",
    "ç": "c",
}


def normalizar(texto):
    resultado = ""
    for letra in texto.lower():
        resultado += ACENTOS.get(letra, letra)
    return " ".join(resultado.split())


def contem(texto, termo):
    base = normalizar(texto)
    padrao = normalizar(termo)
    if len(padrao) == 0:
        return False
    for inicio in range(len(base) - len(padrao) + 1):
        j = 0
        while j < len(padrao) and base[inicio + j] == padrao[j]:
            j += 1
        if j == len(padrao):
            return True
    return False


def cortar(texto, tamanho):
    if len(texto) <= tamanho:
        return texto
    return texto[:tamanho - 3] + "..."
