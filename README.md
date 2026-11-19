# Citizen Assist AI: Gerenciador de Serviços (DSA)

Global Solution 2026.2 | Citizen Tech | Data Structures and Algorithms

## Integrantes

- Nícolas Andrade Rodrigues - RM 572782
- Lucas Caram Bueno - RM 570158

## 1. Objetivo

Protótipo em Python para cadastrar, consultar, atualizar, excluir, pesquisar e ordenar serviços e orientações de interesse público geral. Os dados ficam em uma **lista encadeada própria**, e tanto a busca quanto a ordenação usam algoritmos escritos no projeto. O sistema roda no terminal por menu, não usa IA generativa e usa dados fictícios de teste.

## 2. Campos dos registros

| Campo | Descrição | Regra |
|---|---|---|
| `identificador` | Número único do serviço | Inteiro positivo, até 9 dígitos, sem repetição |
| `titulo` | Nome do serviço | Obrigatório |
| `categoria` | Área do serviço (ex.: Saúde) | Obrigatório |
| `descricao` | O que o serviço oferece | Obrigatório |
| `publico_alvo` | Quem pode usar o serviço | Obrigatório |
| `canal` | Canal ou local de atendimento | Obrigatório |

O `identificador` não muda após o cadastro. Os outros campos podem ser atualizados.

## 3. Como executar

Requisito: Python 3.8 ou superior (sem bibliotecas externas).

```bash
python main.py
```

Para rodar os testes e gerar as evidências:

```bash
python testes.py
```

A lista começa vazia. A opção **8** carrega 10 serviços fictícios para facilitar o teste.

### Menu

| Opção | Função |
|---|---|
| 1 | Cadastrar serviço |
| 2 | Consultar por identificador |
| 3 | Listar todos |
| 4 | Atualizar serviço (Enter mantém o valor atual) |
| 5 | Excluir serviço (pede confirmação) |
| 6 | Pesquisar por título ou categoria |
| 7 | Ordenar por identificador, título ou categoria |
| 8 | Carregar dados de exemplo |
| 0 | Sair |

### Validações tratadas

- Opção de menu inválida ou vazia.
- Identificador com letras, negativo, zero, vazio ou maior que o limite.
- Identificador duplicado no cadastro.
- Campos obrigatórios vazios ou só com espaços (o programa pede de novo).
- Registro não encontrado em consulta, atualização e exclusão.
- Operações em lista vazia (mensagem simples, sem erro).
- Confirmação de exclusão diferente de `s` ou `n`.
- Termo de busca vazio.

Ao pedir o identificador, digitar `0` cancela a operação.

## 4. Organização do código

```text
citizen-assist-dsa/
├── main.py                    ponto de entrada
├── testes.py                  cenários de teste e geração das evidências
├── app/
│   ├── servico.py             classe Servico (registro)
│   ├── lista_encadeada.py     classes No e ListaEncadeada (estrutura, busca e ordenação)
│   ├── menu.py                menu interativo e validação das entradas
│   ├── texto.py               normalização de texto e busca de trecho
│   ├── validacao.py           validação de identificador e de campos
│   └── dados_exemplo.py       10 serviços fictícios
└── evidencias/
    ├── evidencias_testes.md   entrada, esperado e observado de cada cenário
    └── sessao_terminal.txt    sessão completa pelo menu
```

| Requisito do enunciado | Onde está |
|---|---|
| Lista encadeada própria | `No` e `ListaEncadeada` em `app/lista_encadeada.py` |
| Inserção | `inserir_final` |
| Percurso | `percorrer` |
| Atualização | `atualizar` |
| Remoção | `remover` |
| Consulta por identificador | `buscar_por_id` |
| Pesquisa por atributo | `buscar_por_texto` (título ou categoria) |
| Ordenação | `ordenar`, com `_merge_sort`, `_dividir` e `_mesclar` |
| Menu e tratamento de entradas | `app/menu.py` |

## 5. A lista encadeada

É uma lista **simplesmente encadeada**. Cada `No` guarda um `Servico` e o ponteiro `proximo` para o próximo nó. A `ListaEncadeada` tem três atributos: `inicio`, `fim` e `tamanho`. Quando está vazia, `inicio` e `fim` são `None`. O código não usa lista nativa do Python para armazenar os registros.

**Operações:**

- **Inserção (`inserir_final`)**: cria o nó, liga ao final e atualiza `fim` e `tamanho`. Se a lista estiver vazia, o novo nó vira `inicio` e `fim`.
- **Percurso (`percorrer`)**: começa em `inicio` e avança por `proximo` até `None`, retornando um serviço por vez.
- **Atualização (`atualizar`)**: acha o registro pelo identificador e altera só os campos preenchidos.
- **Remoção (`remover`)**: percorre guardando o nó anterior e ajusta os ponteiros. Trata três casos: primeiro nó (`inicio` avança), nó do meio (anterior aponta para o seguinte) e último nó (`fim` volta para o anterior). Se esvaziar, `inicio` e `fim` viram `None`. Desliga o nó removido e diminui `tamanho`.

**Duplicidade de identificador:** o menu checa com `buscar_por_id` antes de chamar `inserir_final`, mantendo a inserção em si com custo constante.

## 6. Algoritmos de busca e ordenação

### Busca sequencial por identificador (`buscar_por_id`)

Percorre do início ao fim comparando o identificador de cada nó e para ao achar. É adequada porque a lista não tem acesso direto por índice e não está sempre ordenada.

### Busca de trecho em título ou categoria (`buscar_por_texto`)

Percorre todos os nós e procura o termo no campo escolhido usando uma busca ingênua de substring em `app/texto.py` (`contem`), testando posição por posição e caractere por caractere. Antes disso, normaliza texto e termo (sem acentos, minúsculas e sem espaços extras), então `saude` encontra `Saúde`. Os achados vão para uma nova `ListaEncadeada`.

### Ordenação por Merge Sort em lista encadeada (`ordenar`)

O Merge Sort se adapta bem a listas encadeadas porque apenas **reaponta nós**, sem precisar de índices nem copiar os registros.

1. **Dividir (`_dividir`)**: usa dois ponteiros (um anda 1 nó e o outro 2 nós); quando o rápido chega ao fim, o lento está no meio e separa as duas metades.
2. **Resolver**: ordena cada metade recursivamente; 0 ou 1 nó já está ordenado.
3. **Mesclar (`_mesclar`)**: compara a cabeça das duas metades ordenadas e liga sempre o menor ao resultado até uma acabar; depois liga o resto da outra metade.
4. Ao terminar, refaz um percurso para atualizar `fim`.

Ordena de forma **crescente** e **estável** (mantém a ordem em caso de empate) por identificador (numérico), título ou categoria (texto normalizado).

## 7. Análise Big-O

**Hipóteses:**

- `n` é a quantidade de nós da lista.
- Comparar identificadores custa O(1).
- Os textos (título e categoria) têm tamanho limitado e pequeno. Por isso o custo de normalizar e comparar um texto é tratado como constante. Sem essa hipótese, a comparação de texto custa O(L) e a busca de trecho custa O(L·p) por nó, em que L é o tamanho do campo e p o tamanho do termo.
- "Melhor caso" é quando o registro procurado é o primeiro nó. o "Pior caso" é quando ele é o último ou não existe.

| Operação | Método | Melhor caso | Pior caso | Justificativa |
|---|---|---|---|---|
| Inserção no final | `inserir_final` | O(1) | O(1) | O ponteiro `fim` evita percorrer a lista |
| Cadastro completo | `cadastrar` | O(n) | O(n) | Verifica duplicidade percorrendo toda a lista (o identificador novo não existe) e depois insere em O(1) |
| Busca por identificador | `buscar_por_id` | O(1) | O(n) | Busca sequencial |
| Busca por título ou categoria | `buscar_por_texto` | O(n) | O(n) | Sempre percorre todos os nós para reunir todos os resultados |
| Atualização | `atualizar` | O(1) | O(n) | Custo da busca; trocar os campos é O(1) |
| Exclusão | `remover` | O(1) | O(n) | Percorre até achar o nó e religa em O(1) |
| Percurso e listagem | `percorrer` | O(n) | O(n) | Visita cada nó uma vez |
| Ordenação | `ordenar` | O(n log n) | O(n log n) | Merge Sort: ver abaixo |

**Ordenação:** a lista é dividida ao meio log n vezes. Em cada nível da recursão, dividir e mesclar visitam cada nó uma vez, somando O(n) por nível. A recorrência é T(n) = 2T(n/2) + O(n), que resulta em O(n log n) em todos os casos. O recálculo final do `fim` custa O(n) e não altera o resultado. O espaço extra é O(log n), apenas a pilha da recursão, pois os nós são religados sem criar cópias. Se a comparação for por texto, cada comparação custa O(L) e o total passa a O(L · n log n).

## 8. Testes e evidências

`testes.py` roda **45 cenários** com entradas simuladas e verifica o resultado de cada um. Após cada cenário, checa também a integridade da lista (`tamanho` igual ao total de nós e `fim` no último nó).

Cenários cobertos:

- Operações em **lista vazia** (listar, consultar, atualizar, excluir, pesquisar e ordenar).
- Cadastro válido, identificador duplicado, identificador inválido, campo obrigatório vazio e cancelamento.
- Consulta de item existente ou não; listagem com vários itens.
- Atualização total, parcial, sem mudanças e de item inexistente.
- Busca por título e categoria (com e sem acento), sem resultado, termo vazio e opção inválida.
- Ordenação por identificador, título e categoria, com 5, 10 ou 1 registro.
- Exclusão do início, meio e fim, cancelada, com confirmação inválida, de item inexistente e até esvaziar a lista.
- Inserção após remover o último nó.
- Opções inválidas no menu principal e fluxo completo do início ao fim.

Arquivos gerados em `evidencias/`:

- `evidencias_testes.md`: entrada, resultado esperado e resultado observado em cada cenário.
- `sessao_terminal.txt`: execução completa pelo menu.

Para gerar novamente, execute `python testes.py`.

## 9. Limitações

- Os dados ficam só na memória e somem ao fechar o programa.
- A ordenação é sempre crescente.
- A busca só considera letras e números normalizados; não corrige erros de digitação.
