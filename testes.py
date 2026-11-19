import builtins
import contextlib
import io
import os
import platform
import sys
from datetime import datetime

from app.dados_exemplo import SERVICOS_EXEMPLO
from app.lista_encadeada import ListaEncadeada
from app.menu import Menu
from app.servico import Servico
from app.texto import normalizar

PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_EVIDENCIAS = os.path.join(PASTA, "evidencias")

menu = Menu()
resultados = []


def rodar(acao, entradas):
    restantes = iter(entradas)
    saida = io.StringIO()

    def entrada_simulada(prompt=""):
        try:
            resposta = next(restantes)
        except StopIteration:
            raise AssertionError("O programa pediu mais entradas do que o cenário forneceu.")
        print(prompt + resposta)
        return resposta

    original = builtins.input
    builtins.input = entrada_simulada
    consumiu_tudo = True
    try:
        with contextlib.redirect_stdout(saida):
            acao()
    except AssertionError as erro:
        saida.write(f"\n[FALHA] {erro}\n")
        consumiu_tudo = False
    finally:
        builtins.input = original
    if next(restantes, None) is not None:
        consumiu_tudo = False
    return saida.getvalue(), consumiu_tudo


def integro(lista):
    contados = 0
    ultimo = None
    atual = lista.inicio
    while atual is not None:
        contados += 1
        ultimo = atual
        atual = atual.proximo
    return contados == lista.tamanho and ultimo is lista.fim


def ids(lista):
    return [servico.identificador for servico in lista.percorrer()]


def descrever(entradas):
    if not entradas:
        return "(nenhuma entrada)"
    return " | ".join("(Enter)" if e == "" else e for e in entradas)


def cenario(codigo, nome, acao, entradas, esperado, condicao, alvo=None):
    saida, consumiu = rodar(acao, entradas)
    lista = (alvo or menu).lista
    ok = consumiu and integro(lista) and bool(condicao(saida))
    resultados.append({
        "codigo": codigo,
        "nome": nome,
        "entrada": descrever(entradas),
        "esperado": esperado,
        "observado": saida.rstrip(),
        "ok": ok,
    })
    return saida


def tem(*trechos):
    return lambda saida: all(trecho in saida for trecho in trechos)


# ---------- Lista vazia ----------
vazia = "A lista está vazia."
cenario("C01", "Listar com a lista vazia", menu.listar, [],
        "Mensagem informando que a lista está vazia.", tem(vazia))
cenario("C02", "Consultar com a lista vazia", menu.consultar, [],
        "Mensagem de lista vazia, sem pedir identificador.", tem(vazia))
cenario("C03", "Atualizar com a lista vazia", menu.atualizar, [],
        "Mensagem de lista vazia.", tem(vazia))
cenario("C04", "Excluir com a lista vazia", menu.excluir, [],
        "Mensagem de lista vazia.", tem(vazia))
cenario("C05", "Pesquisar com a lista vazia", menu.pesquisar, [],
        "Mensagem de lista vazia.", tem(vazia))
cenario("C06", "Ordenar com a lista vazia", menu.ordenar, [],
        "Mensagem de lista vazia.", tem(vazia))

# ---------- Cadastro ----------
cenario("C07", "Cadastrar serviço válido (ID 30)", menu.cadastrar,
        ["30", "Atendimento Psicossocial", "Saúde",
         "Acolhimento e escuta para pessoas em sofrimento emocional.",
         "Qualquer cidadão", "CAPS do bairro"],
        "Mensagem de sucesso; lista passa a ter 1 registro.",
        lambda s: "Serviço cadastrado com sucesso." in s and ids(menu.lista) == [30])
cenario("C08", "Cadastrar segundo serviço (ID 10)", menu.cadastrar,
        ["10", "Emissão de CPF", "Documentos",
         "Emissão e regularização do CPF.", "Qualquer cidadão", "Agências dos Correios"],
        "Mensagem de sucesso; lista com 2 registros.",
        lambda s: "Serviço cadastrado com sucesso." in s and ids(menu.lista) == [30, 10])
cenario("C09", "Cadastrar terceiro serviço (ID 20)", menu.cadastrar,
        ["20", "Orientação Jurídica Gratuita", "Atendimento Comunitário",
         "Atendimento jurídico para quem não pode pagar um advogado.",
         "Pessoas de baixa renda", "Defensoria Pública"],
        "Mensagem de sucesso; lista com 3 registros.",
        lambda s: "Serviço cadastrado com sucesso." in s and ids(menu.lista) == [30, 10, 20])
cenario("C10", "Cadastrar com identificador duplicado (ID 10) e depois corrigir para 40", menu.cadastrar,
        ["10", "40", "Isenção de Tarifa no Transporte Público", "Assistência Social",
         "Gratuidade na tarifa de ônibus.", "Idosos e pessoas com deficiência", "Terminais de integração"],
        "Aviso de identificador já existente, novo pedido de ID e cadastro do ID 40.",
        lambda s: "Já existe um serviço com o identificador 10" in s and ids(menu.lista) == [30, 10, 20, 40])
antes = len(menu.lista)
cenario("C11", "Identificador inválido (texto, negativo, vazio) e cancelamento com 0", menu.cadastrar,
        ["abc", "-5", "", "0"],
        "Três avisos de identificador inválido e cancelamento; nada é cadastrado.",
        lambda s: s.count("Identificador inválido.") == 3 and "Operação cancelada." in s
        and len(menu.lista) == antes)
cenario("C12", "Campo obrigatório vazio no título (ID 50)", menu.cadastrar,
        ["50", "", "   ", "Passe Livre Estudantil", "Educação",
         "Gratuidade no transporte para estudantes.", "Estudantes da rede pública", "Secretaria de Educação"],
        "Aviso de campo obrigatório duas vezes; cadastro concluído após informar o título.",
        lambda s: s.count("Campo obrigatório.") == 2 and ids(menu.lista) == [30, 10, 20, 40, 50])

# ---------- Consulta e listagem ----------
cenario("C13", "Consultar ID existente (20)", menu.consultar, ["20"],
        "Exibe todos os campos do serviço 20.",
        tem("Orientação Jurídica Gratuita", "Defensoria Pública"))
cenario("C14", "Consultar ID inexistente (99)", menu.consultar, ["99"],
        "Mensagem de serviço não encontrado.",
        tem("Serviço com identificador 99 não encontrado."))
cenario("C15", "Listar vários registros", menu.listar, [],
        "Tabela com 5 registros na ordem de inserção.",
        tem("Total: 5 serviço(s).", "Atendimento Psicossocial", "Passe Livre Estudantil"))

# ---------- Atualização ----------
cenario("C16", "Atualizar título e canal do ID 40 (demais campos mantidos com Enter)", menu.atualizar,
        ["40", "Isenção de Tarifa no Transporte Coletivo", "", "", "", "Terminais e site da prefeitura"],
        "Mensagem de sucesso; título e canal alterados, categoria preservada.",
        lambda s: "Serviço atualizado com sucesso." in s
        and menu.lista.buscar_por_id(40).titulo == "Isenção de Tarifa no Transporte Coletivo"
        and menu.lista.buscar_por_id(40).canal == "Terminais e site da prefeitura"
        and menu.lista.buscar_por_id(40).categoria == "Assistência Social")
cenario("C17", "Atualizar ID inexistente (99)", menu.atualizar, ["99"],
        "Mensagem de serviço não encontrado.",
        tem("Serviço com identificador 99 não encontrado."))
cenario("C18", "Atualizar sem informar nenhuma alteração (ID 10)", menu.atualizar,
        ["10", "", "", "", "", ""],
        "Aviso de que nada foi alterado.",
        tem("Nenhuma alteração informada."))

# ---------- Pesquisa ----------
cenario("C19", "Pesquisar título 'emissao' (sem acento e minúsculo)", menu.pesquisar, ["1", "emissao"],
        "Encontra 'Emissão de CPF' (ID 10).",
        lambda s: "1 serviço(s) encontrado(s)" in s and "Emissão de CPF" in s)
cenario("C20", "Pesquisar categoria 'educ'", menu.pesquisar, ["2", "educ"],
        "Encontra apenas o ID 50 (categoria Educação).",
        lambda s: "1 serviço(s) encontrado(s)" in s and "Passe Livre Estudantil" in s)
cenario("C21", "Pesquisar termo sem correspondência", menu.pesquisar, ["1", "xyz"],
        "Mensagem de nenhum serviço encontrado.",
        tem("Nenhum serviço encontrado para 'xyz'."))
cenario("C22", "Pesquisar com termo vazio e depois 'gratuita'", menu.pesquisar, ["1", "", "gratuita"],
        "Aviso de termo vazio e, em seguida, resultado do ID 20.",
        tem("O termo de pesquisa não pode ser vazio.", "Orientação Jurídica Gratuita"))
cenario("C23", "Pesquisar com opção inválida e voltar", menu.pesquisar, ["7", "0"],
        "Aviso de opção inválida e retorno ao menu.",
        tem("Opção inválida."))

# ---------- Ordenação ----------
cenario("C24", "Ordenar por identificador", menu.ordenar, ["1"],
        "Ordem dos IDs: 10, 20, 30, 40, 50.",
        lambda s: ids(menu.lista) == [10, 20, 30, 40, 50] and "Lista ordenada por identificador." in s)
cenario("C25", "Ordenar por título (ignora acentos e maiúsculas)", menu.ordenar, ["2"],
        "Ordem dos IDs: 30 (Atendimento), 10 (Emissão), 40 (Isenção), 20 (Orientação), 50 (Passe).",
        lambda s: ids(menu.lista) == [30, 10, 40, 20, 50] and "Lista ordenada por título." in s)
cenario("C26", "Ordenar por categoria", menu.ordenar, ["3"],
        "Ordem dos IDs: 40 (Assistência), 20 (Atendimento), 10 (Documentos), 50 (Educação), 30 (Saúde).",
        lambda s: ids(menu.lista) == [40, 20, 10, 50, 30] and "Lista ordenada por categoria." in s)
cenario("C27", "Ordenar com opção inválida e voltar", menu.ordenar, ["9", "0"],
        "Aviso de opção inválida; ordem da lista não muda.",
        lambda s: "Opção inválida." in s and ids(menu.lista) == [40, 20, 10, 50, 30])

# ---------- Exclusão ----------
cenario("C28", "Excluir registro do meio (ID 10)", menu.excluir, ["10", "s"],
        "Serviço removido; ordem restante 40, 20, 50, 30.",
        lambda s: "Serviço removido com sucesso." in s and ids(menu.lista) == [40, 20, 50, 30])
cenario("C29", "Excluir primeiro registro (ID 40)", menu.excluir, ["40", "s"],
        "Serviço removido; ordem restante 20, 50, 30.",
        lambda s: "Serviço removido com sucesso." in s and ids(menu.lista) == [20, 50, 30])
cenario("C30", "Excluir último registro (ID 30)", menu.excluir, ["30", "s"],
        "Serviço removido; ordem restante 20, 50.",
        lambda s: "Serviço removido com sucesso." in s and ids(menu.lista) == [20, 50])
cenario("C31", "Cadastrar após remover o último (ID 60 entra no final)", menu.cadastrar,
        ["60", "Mutirão de Cidadania", "Atendimento Comunitário",
         "Ações itinerantes de documentação e saúde.", "Moradores da região", "Praça central"],
        "Cadastro concluído; ordem 20, 50, 60 (ponteiro do final atualizado).",
        lambda s: ids(menu.lista) == [20, 50, 60])
cenario("C32", "Cancelar exclusão com 'n' (ID 50)", menu.excluir, ["50", "n"],
        "Exclusão cancelada; registro permanece.",
        lambda s: "Exclusão cancelada." in s and ids(menu.lista) == [20, 50, 60])
cenario("C33", "Confirmação inválida e depois 'n'", menu.excluir, ["50", "talvez", "n"],
        "Aviso para responder s/n; exclusão cancelada.",
        lambda s: "Responda com 's' para sim ou 'n' para não." in s and ids(menu.lista) == [20, 50, 60])
cenario("C34", "Excluir ID inexistente (99)", menu.excluir, ["99"],
        "Mensagem de serviço não encontrado.",
        tem("Serviço com identificador 99 não encontrado."))


def esvaziar():
    menu.excluir()
    menu.excluir()
    menu.excluir()


cenario("C35", "Excluir todos os registros até esvaziar a lista (IDs 20, 50, 60)", esvaziar,
        ["20", "s", "50", "s", "60", "s"],
        "Três remoções com sucesso; lista fica vazia.",
        lambda s: s.count("Serviço removido com sucesso.") == 3 and menu.lista.esta_vazia())
cenario("C36", "Listar após esvaziar a lista", menu.listar, [],
        "Mensagem de lista vazia.", tem(vazia))

# ---------- Dados de exemplo e volume maior ----------
cenario("C37", "Carregar 10 serviços de exemplo", menu.carregar_exemplos, [],
        "10 serviços carregados, nenhum ignorado.",
        lambda s: "10 serviço(s) de exemplo carregado(s). 0 já existiam" in s and len(menu.lista) == 10)
cenario("C38", "Carregar os exemplos novamente (IDs duplicados)", menu.carregar_exemplos, [],
        "Nenhum novo carregado; 10 ignorados; lista continua com 10.",
        lambda s: "0 serviço(s) de exemplo carregado(s). 10 já existiam" in s and len(menu.lista) == 10)
esperado_titulo = [d[0] for d in sorted(SERVICOS_EXEMPLO, key=lambda d: normalizar(d[1]))]
esperado_id = sorted(d[0] for d in SERVICOS_EXEMPLO)
cenario("C39", "Ordenar 10 registros por título", menu.ordenar, ["2"],
        "IDs na ordem alfabética dos títulos: " + ", ".join(map(str, esperado_titulo)) + ".",
        lambda s: ids(menu.lista) == esperado_titulo)
cenario("C40", "Ordenar 10 registros por identificador", menu.ordenar, ["1"],
        "IDs em ordem crescente: " + ", ".join(map(str, esperado_id)) + ".",
        lambda s: ids(menu.lista) == esperado_id)
cenario("C41", "Pesquisar categoria 'saude' (sem acento) nos 10 registros", menu.pesquisar, ["2", "saude"],
        "Encontra os 2 serviços da categoria Saúde (IDs 1 e 9).",
        lambda s: "2 serviço(s) encontrado(s)" in s and "Agendamento de Consulta na UBS" in s
        and "Vacinação do Calendário Nacional" in s)

# ---------- Lista com um único elemento ----------
unica = Menu()
unica.lista.inserir_final(Servico(1, "Único", "Teste", "Descrição", "Todos", "Balcão"))
cenario("C42", "Ordenar lista com um único registro", unica.ordenar, ["2"],
        "Lista permanece com 1 registro, sem erro.",
        lambda s: ids(unica.lista) == [1] and "Lista ordenada por título." in s, alvo=unica)
cenario("C43", "Excluir o único registro (início e fim passam a ser vazios)", unica.excluir, ["1", "s"],
        "Serviço removido; lista vazia com início e fim nulos.",
        lambda s: unica.lista.esta_vazia() and unica.lista.fim is None, alvo=unica)

# ---------- Menu principal ----------
sessao_curta = Menu()
cenario("C44", "Opções inexistentes no menu principal e saída", sessao_curta.executar,
        ["9", "abc", "", "0"],
        "Três avisos de opção inválida e mensagem de encerramento.",
        lambda s: s.count("Opção inválida. Digite um número de 0 a 8.") == 3
        and "Encerrando o sistema. Até logo!" in s, alvo=sessao_curta)

sessao = Menu()
entradas_sessao = [
    "3",
    "8",
    "3",
    "2", "7",
    "6", "2", "saude",
    "7", "2",
    "4", "3", "", "", "Atendimento ampliado para toda a família", "", "",
    "2", "3",
    "5", "2", "s",
    "3",
    "0",
]
saida_sessao = cenario(
    "C45", "Sessão completa pelo menu principal (listar vazia, carregar, consultar, pesquisar, ordenar, atualizar, excluir, sair)",
    sessao.executar, entradas_sessao,
    "Fluxo completo sem erros, terminando com a mensagem de encerramento.",
    lambda s: "Encerrando o sistema. Até logo!" in s and "Serviço atualizado com sucesso." in s
    and "Serviço removido com sucesso." in s and len(sessao.lista) == 9, alvo=sessao)


# ---------- Relatório ----------
def gravar_evidencias():
    os.makedirs(PASTA_EVIDENCIAS, exist_ok=True)
    passou = sum(1 for r in resultados if r["ok"])

    linhas = [
        "# Evidências de testes",
        "",
        f"- Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        f"- Python: {platform.python_version()} ({platform.system()})",
        "- Comando: `python testes.py`",
        f"- Resultado geral: **{passou}/{len(resultados)} cenários aprovados**",
        "",
        "Cada cenário usa entradas simuladas no terminal. As linhas do bloco **Observado** são a saída real do programa, "
        "com o texto digitado aparecendo logo após cada pergunta. Após cada cenário o teste também confere a integridade "
        "da lista encadeada (quantidade de nós igual ao tamanho registrado e ponteiro do final apontando para o último nó).",
        "",
        "## Resumo",
        "",
        "| Código | Cenário | Resultado |",
        "|---|---|---|",
    ]
    for r in resultados:
        linhas.append(f"| {r['codigo']} | {r['nome']} | {'Aprovado' if r['ok'] else 'REPROVADO'} |")

    linhas += ["", "## Detalhamento", ""]
    for r in resultados:
        linhas += [
            f"### {r['codigo']} - {r['nome']}",
            "",
            f"- **Entrada:** `{r['entrada']}`",
            f"- **Resultado esperado:** {r['esperado']}",
            f"- **Resultado:** {'Aprovado' if r['ok'] else 'REPROVADO'}",
            "",
            "**Observado:**",
            "",
            "```text",
            r["observado"],
            "```",
            "",
        ]

    with open(os.path.join(PASTA_EVIDENCIAS, "evidencias_testes.md"), "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(linhas))

    with open(os.path.join(PASTA_EVIDENCIAS, "sessao_terminal.txt"), "w", encoding="utf-8") as arquivo:
        arquivo.write(saida_sessao)

    return passou


if __name__ == "__main__":
    passou = gravar_evidencias()
    total = len(resultados)
    for r in resultados:
        print(f"{r['codigo']} {'OK   ' if r['ok'] else 'FALHA'} {r['nome']}")
    print(f"\n{passou}/{total} cenários aprovados.")
    print("Evidências gravadas em evidencias/evidencias_testes.md e evidencias/sessao_terminal.txt")
    sys.exit(0 if passou == total else 1)

# Gerado em conjunto com deepseek