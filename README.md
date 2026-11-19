# Citizen Assist AI: Gerenciador de Serviços (DSA)

Global Solution 2026.2 | Citizen Tech | Data Structures and Algorithms

## Integrantes

* Nícolas Andrade Rodrigues - RM 572782
* Lucas Caram Bueno - RM 570158

## 1. Objetivo

Protótipo em Python para cadastrar, consultar, atualizar, excluir, pesquisar e ordenar serviços e orientações do interesse publico geral. Os registros ficam em uma **lista encadeada implementada**, e a busca e a ordenação usam algoritmos escritos no próprio código. O sistema funciona por menu no terminal, não usa IA generativa e os dados de teste são fictícios.

## 2. Campos dos registros

| Campo | Descrição | Regra |
|---|---|---|
| `identificador` | Número único do serviço | Inteiro positivo, até 9 dígitos, sem repetição |
| `titulo` | Nome do serviço | Obrigatório |
| `categoria` | Área do serviço (por exemplo, Saúde) | Obrigatório |
| `descricao` | O que o serviço oferece | Obrigatório |
| `publico_alvo` | Quem pode usar o serviço | Obrigatório |
| `canal` | Canal ou local de atendimento | Obrigatorio |

O identificador não pode ser alterado depois do cadastro. Os demais campos podem ser atualizados.

## 3. Como executar

Requisito: Python 3.8 ou superior. Nenhuma biblioteca externa é necessária.

```bash
python main.py
```

Para rodar os testes e gerar as evidências:

```bash
python testes.py
```

A lista começa vazia. A opção **8** do menu carrega 10 serviços fictícios para facilitar a demonstração.

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

* Opção de menu inexistente ou vazia.
* Identificador com letras, negativo, zero, vazio ou grande demais.
* Identificador duplicado no cadastro.
* Campos obrigatórios vazios ou só com espaços (o campo é pedido de novo).
* Registro não encontrado em consulta, atualização e exclusão.
* Operações sobre lista vazia (mensagem clara, sem erro).
* Confirmação de exclusão diferente de `s` ou `n`.
* Termo de pesquisa vazio.

Nos pedidos de identificador, digitar `0` cancela a operação.

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

É uma lista **simplesmente encadeada**. Cada `No` guarda um `Servico` e uma referência explicita ao próximo nó (`proximo`). A `ListaEncadeada` mantém três atributos: `inicio` (primeiro nó), `fim` (último nó) e `tamanho`. Uma lista vazia tem `inicio` e `fim` iguais a `None`. Nenhuma lista nativa do Python guarda os registros.

**Operações:**

* **Inserção (`inserir_final`)**: cria o nó, liga-o ao `proximo` do último nó e atualiza `fim` e `tamanho`. Se a lista estava vazia, o novo nó vira `inicio` e `fim`.
* **Percurso (`percorrer`)**: parte de `inicio` e segue `proximo` até `None`, entregando um serviço por vez.
* **Atualização (`atualizar`)**: localiza o serviço pelo identificador e troca apenas os campos informados.
* **Remoção (`remover`)**: percorre guardando o nó anterior e religa a lista. Há três casos: remover o primeiro nó (`inicio` avança), o do meio (o anterior passa a apontar para o seguinte) e o último (`fim` volta para o anterior). Se a lista ficar vazia, `inicio` e `fim` viram `None`. O nó removido é desligado da lista e o `tamanho` diminui.

**Duplicidade de identificador:** a verificação é feita no menu (`buscar_por_id` antes de `inserir_final`), assim a inserção em si continua com custo constante.

## 6. Algoritmos de busca e ordenação

### Busca sequencial por identificador (`buscar_por_id`)

Percorre a lista do início ao fim comparando o identificador de cada nó. Para ao encontrar. A busca sequencial é adequada porque a lista encadeada não permite acessar uma posição diretamente e os dados não ficam ordenados.

### Busca de trecho em título ou categoria (`buscar_por_texto`)

Percorre todos os nós e, para cada um, procura o termo dentro do campo escolhido com uma busca ingênua de substring escrita em `app/texto.py` (`contem`): alinha o termo em cada posição do texto e compara caractere por caractere. Antes, texto e termo são normalizados (minúsculas, sem acentos e sem espaços repetidos), então `saude` encontra `Saúde`. Os resultados formam uma nova `ListaEncadeada`.

### Ordenação por Merge Sort em lista encadeada (`ordenar`)

Escolha: o Merge Sort funciona melhor em lista encadeada porque só **religa nós**, sem precisar de acesso por índice nem de cópia dos dados.

1. **Dividir (`_dividir`)**: dois ponteiros percorrem a lista, um avançando um nó e outro dois nós por vez. Quando o rápido chega ao fim, o lento está no meio e a lista é cortada em duas metades.
2. **Resolver**: cada metade é ordenada recursivamente. Lista vazia ou com um nó já está ordenada (caso base).
3. **Mesclar (`_mesclar`)**: compara os primeiros nós das duas metades ordenadas e religa sempre o menor ao fim da lista resultante, até acabar uma das metades. O restante da outra é anexado de uma vez.
4. Ao final, o `fim` da lista é recalculado com um percurso.

Critérios disponíveis: identificador (número), título e categoria (texto normalizado, ignorando acentos e maiúsculas). A ordenação é estável (empates mantêm a ordem anterior) e **crescente**.

## 7. Análise Big-O

**Hipóteses:**

* `n` é a quantidade de nós da lista.
* Comparar identificadores custa O(1).
* Os textos (título e categoria) têm tamanho limitado e pequeno. Por isso o custo de normalizar e comparar um texto é tratado como constante. Sem essa hipótese, a comparação de texto custa O(L) e a busca de trecho custa O(L·p) por nó, em que L é o tamanho do campo e p o tamanho do termo.
* "Melhor caso" é quando o registro procurado é o primeiro nó. o "Pior caso" é quando ele é o último ou não existe.

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

O arquivo `testes.py` executa **45 cenários** com entradas simuladas no terminal e confere o resultado de cada um. Depois de cada cenário ele também verifica a integridade da lista (número de nós igual ao `tamanho` e `fim` apontando para o último nó).

Cenários cobertos:

* Operações sobre **lista vazia** (listar, consultar, atualizar, excluir, pesquisar e ordenar).
* Cadastro válido, identificador duplicado, identificador inválido, campo obrigatório vazio e cancelamento.
* Consulta de registro existente e inexistente; listagem com vários registros.
* Atualização completa, parcial, sem alterações e de registro inexistente.
* Pesquisa por título e categoria (com e sem acento), sem resultado, termo vazio e opção inválida.
* Ordenação por identificador, título e categoria, com 5 e com 10 registros, e com um único registro.
* Exclusão do início, do meio e do fim, cancelada, com confirmação inválida, de registro inexistente e até esvaziar a lista.
* Inserção depois de remover o último nó.
* Opções inexistentes no menu principal e uma sessão completa de ponta a ponta.

Resultados em `evidencias/`:

* `evidencias_testes.md`: para cada cenário, a **entrada**, o **resultado esperado** e o **resultado observado** (saída real do terminal).
* `sessao_terminal.txt`: sessão completa pelo menu.

Para gerar de novo, rode `python testes.py`.

## 9. Limitações

* Os dados ficam só em memória e se perdem ao fechar o programa.
* A ordenação é sempre crescente.
* A busca de trecho diferencia apenas letras e números. Erros de digitação não são corrigidos.
