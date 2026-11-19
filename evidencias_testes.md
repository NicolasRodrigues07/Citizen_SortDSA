# Evidências de testes

- Gerado em: 19/11/2026 21:25
- Python: 3.12.3 (Linux)
- Comando: `python testes.py`
- Resultado geral: **45/45 cenários aprovados**

Cada cenário usa entradas simuladas no terminal. As linhas do bloco **Observado** são a saída real do programa, com o texto digitado aparecendo logo após cada pergunta. Após cada cenário o teste também confere a integridade da lista encadeada (quantidade de nós igual ao tamanho registrado e ponteiro do final apontando para o último nó).

## Resumo

| Código | Cenário | Resultado |
|---|---|---|
| C01 | Listar com a lista vazia | Aprovado |
| C02 | Consultar com a lista vazia | Aprovado |
| C03 | Atualizar com a lista vazia | Aprovado |
| C04 | Excluir com a lista vazia | Aprovado |
| C05 | Pesquisar com a lista vazia | Aprovado |
| C06 | Ordenar com a lista vazia | Aprovado |
| C07 | Cadastrar serviço válido (ID 30) | Aprovado |
| C08 | Cadastrar segundo serviço (ID 10) | Aprovado |
| C09 | Cadastrar terceiro serviço (ID 20) | Aprovado |
| C10 | Cadastrar com identificador duplicado (ID 10) e depois corrigir para 40 | Aprovado |
| C11 | Identificador inválido (texto, negativo, vazio) e cancelamento com 0 | Aprovado |
| C12 | Campo obrigatório vazio no título (ID 50) | Aprovado |
| C13 | Consultar ID existente (20) | Aprovado |
| C14 | Consultar ID inexistente (99) | Aprovado |
| C15 | Listar vários registros | Aprovado |
| C16 | Atualizar título e canal do ID 40 (demais campos mantidos com Enter) | Aprovado |
| C17 | Atualizar ID inexistente (99) | Aprovado |
| C18 | Atualizar sem informar nenhuma alteração (ID 10) | Aprovado |
| C19 | Pesquisar título 'emissao' (sem acento e minúsculo) | Aprovado |
| C20 | Pesquisar categoria 'educ' | Aprovado |
| C21 | Pesquisar termo sem correspondência | Aprovado |
| C22 | Pesquisar com termo vazio e depois 'gratuita' | Aprovado |
| C23 | Pesquisar com opção inválida e voltar | Aprovado |
| C24 | Ordenar por identificador | Aprovado |
| C25 | Ordenar por título (ignora acentos e maiúsculas) | Aprovado |
| C26 | Ordenar por categoria | Aprovado |
| C27 | Ordenar com opção inválida e voltar | Aprovado |
| C28 | Excluir registro do meio (ID 10) | Aprovado |
| C29 | Excluir primeiro registro (ID 40) | Aprovado |
| C30 | Excluir último registro (ID 30) | Aprovado |
| C31 | Cadastrar após remover o último (ID 60 entra no final) | Aprovado |
| C32 | Cancelar exclusão com 'n' (ID 50) | Aprovado |
| C33 | Confirmação inválida e depois 'n' | Aprovado |
| C34 | Excluir ID inexistente (99) | Aprovado |
| C35 | Excluir todos os registros até esvaziar a lista (IDs 20, 50, 60) | Aprovado |
| C36 | Listar após esvaziar a lista | Aprovado |
| C37 | Carregar 10 serviços de exemplo | Aprovado |
| C38 | Carregar os exemplos novamente (IDs duplicados) | Aprovado |
| C39 | Ordenar 10 registros por título | Aprovado |
| C40 | Ordenar 10 registros por identificador | Aprovado |
| C41 | Pesquisar categoria 'saude' (sem acento) nos 10 registros | Aprovado |
| C42 | Ordenar lista com um único registro | Aprovado |
| C43 | Excluir o único registro (início e fim passam a ser vazios) | Aprovado |
| C44 | Opções inexistentes no menu principal e saída | Aprovado |
| C45 | Sessão completa pelo menu principal (listar vazia, carregar, consultar, pesquisar, ordenar, atualizar, excluir, sair) | Aprovado |

## Detalhamento

### C01 - Listar com a lista vazia

- **Entrada:** `(nenhuma entrada)`
- **Resultado esperado:** Mensagem informando que a lista está vazia.
- **Resultado:** Aprovado

**Observado:**

```text

--- Serviços cadastrados ---
A lista está vazia. Cadastre um serviço ou carregue os dados de exemplo.
```

### C02 - Consultar com a lista vazia

- **Entrada:** `(nenhuma entrada)`
- **Resultado esperado:** Mensagem de lista vazia, sem pedir identificador.
- **Resultado:** Aprovado

**Observado:**

```text

--- Consultar serviço ---
A lista está vazia. Cadastre um serviço ou carregue os dados de exemplo.
```

### C03 - Atualizar com a lista vazia

- **Entrada:** `(nenhuma entrada)`
- **Resultado esperado:** Mensagem de lista vazia.
- **Resultado:** Aprovado

**Observado:**

```text

--- Atualizar serviço ---
A lista está vazia. Cadastre um serviço ou carregue os dados de exemplo.
```

### C04 - Excluir com a lista vazia

- **Entrada:** `(nenhuma entrada)`
- **Resultado esperado:** Mensagem de lista vazia.
- **Resultado:** Aprovado

**Observado:**

```text

--- Excluir serviço ---
A lista está vazia. Cadastre um serviço ou carregue os dados de exemplo.
```

### C05 - Pesquisar com a lista vazia

- **Entrada:** `(nenhuma entrada)`
- **Resultado esperado:** Mensagem de lista vazia.
- **Resultado:** Aprovado

**Observado:**

```text

--- Pesquisar serviços ---
A lista está vazia. Cadastre um serviço ou carregue os dados de exemplo.
```

### C06 - Ordenar com a lista vazia

- **Entrada:** `(nenhuma entrada)`
- **Resultado esperado:** Mensagem de lista vazia.
- **Resultado:** Aprovado

**Observado:**

```text

--- Ordenar lista ---
A lista está vazia. Cadastre um serviço ou carregue os dados de exemplo.
```

### C07 - Cadastrar serviço válido (ID 30)

- **Entrada:** `30 | Atendimento Psicossocial | Saúde | Acolhimento e escuta para pessoas em sofrimento emocional. | Qualquer cidadão | CAPS do bairro`
- **Resultado esperado:** Mensagem de sucesso; lista passa a ter 1 registro.
- **Resultado:** Aprovado

**Observado:**

```text

--- Cadastrar serviço ---
Identificador (inteiro positivo, 0 para cancelar): 30
Título: Atendimento Psicossocial
Categoria: Saúde
Descrição: Acolhimento e escuta para pessoas em sofrimento emocional.
Público-alvo: Qualquer cidadão
Canal/Local de atendimento: CAPS do bairro
Serviço cadastrado com sucesso.
```

### C08 - Cadastrar segundo serviço (ID 10)

- **Entrada:** `10 | Emissão de CPF | Documentos | Emissão e regularização do CPF. | Qualquer cidadão | Agências dos Correios`
- **Resultado esperado:** Mensagem de sucesso; lista com 2 registros.
- **Resultado:** Aprovado

**Observado:**

```text

--- Cadastrar serviço ---
Identificador (inteiro positivo, 0 para cancelar): 10
Título: Emissão de CPF
Categoria: Documentos
Descrição: Emissão e regularização do CPF.
Público-alvo: Qualquer cidadão
Canal/Local de atendimento: Agências dos Correios
Serviço cadastrado com sucesso.
```

### C09 - Cadastrar terceiro serviço (ID 20)

- **Entrada:** `20 | Orientação Jurídica Gratuita | Atendimento Comunitário | Atendimento jurídico para quem não pode pagar um advogado. | Pessoas de baixa renda | Defensoria Pública`
- **Resultado esperado:** Mensagem de sucesso; lista com 3 registros.
- **Resultado:** Aprovado

**Observado:**

```text

--- Cadastrar serviço ---
Identificador (inteiro positivo, 0 para cancelar): 20
Título: Orientação Jurídica Gratuita
Categoria: Atendimento Comunitário
Descrição: Atendimento jurídico para quem não pode pagar um advogado.
Público-alvo: Pessoas de baixa renda
Canal/Local de atendimento: Defensoria Pública
Serviço cadastrado com sucesso.
```

### C10 - Cadastrar com identificador duplicado (ID 10) e depois corrigir para 40

- **Entrada:** `10 | 40 | Isenção de Tarifa no Transporte Público | Assistência Social | Gratuidade na tarifa de ônibus. | Idosos e pessoas com deficiência | Terminais de integração`
- **Resultado esperado:** Aviso de identificador já existente, novo pedido de ID e cadastro do ID 40.
- **Resultado:** Aprovado

**Observado:**

```text

--- Cadastrar serviço ---
Identificador (inteiro positivo, 0 para cancelar): 10
Já existe um serviço com o identificador 10. Informe outro.
Identificador (inteiro positivo, 0 para cancelar): 40
Título: Isenção de Tarifa no Transporte Público
Categoria: Assistência Social
Descrição: Gratuidade na tarifa de ônibus.
Público-alvo: Idosos e pessoas com deficiência
Canal/Local de atendimento: Terminais de integração
Serviço cadastrado com sucesso.
```

### C11 - Identificador inválido (texto, negativo, vazio) e cancelamento com 0

- **Entrada:** `abc | -5 | (Enter) | 0`
- **Resultado esperado:** Três avisos de identificador inválido e cancelamento; nada é cadastrado.
- **Resultado:** Aprovado

**Observado:**

```text

--- Cadastrar serviço ---
Identificador (inteiro positivo, 0 para cancelar): abc
Identificador inválido. Use apenas números inteiros positivos.
Identificador (inteiro positivo, 0 para cancelar): -5
Identificador inválido. Use apenas números inteiros positivos.
Identificador (inteiro positivo, 0 para cancelar): 
Identificador inválido. Use apenas números inteiros positivos.
Identificador (inteiro positivo, 0 para cancelar): 0
Operação cancelada.
```

### C12 - Campo obrigatório vazio no título (ID 50)

- **Entrada:** `50 | (Enter) |     | Passe Livre Estudantil | Educação | Gratuidade no transporte para estudantes. | Estudantes da rede pública | Secretaria de Educação`
- **Resultado esperado:** Aviso de campo obrigatório duas vezes; cadastro concluído após informar o título.
- **Resultado:** Aprovado

**Observado:**

```text

--- Cadastrar serviço ---
Identificador (inteiro positivo, 0 para cancelar): 50
Título: 
Campo obrigatório. Digite um valor.
Título:    
Campo obrigatório. Digite um valor.
Título: Passe Livre Estudantil
Categoria: Educação
Descrição: Gratuidade no transporte para estudantes.
Público-alvo: Estudantes da rede pública
Canal/Local de atendimento: Secretaria de Educação
Serviço cadastrado com sucesso.
```

### C13 - Consultar ID existente (20)

- **Entrada:** `20`
- **Resultado esperado:** Exibe todos os campos do serviço 20.
- **Resultado:** Aprovado

**Observado:**

```text

--- Consultar serviço ---
Identificador (0 para cancelar): 20

Identificador: 20
Título: Orientação Jurídica Gratuita
Categoria: Atendimento Comunitário
Descrição: Atendimento jurídico para quem não pode pagar um advogado.
Público-alvo: Pessoas de baixa renda
Canal/Local de atendimento: Defensoria Pública
```

### C14 - Consultar ID inexistente (99)

- **Entrada:** `99`
- **Resultado esperado:** Mensagem de serviço não encontrado.
- **Resultado:** Aprovado

**Observado:**

```text

--- Consultar serviço ---
Identificador (0 para cancelar): 99
Serviço com identificador 99 não encontrado.
```

### C15 - Listar vários registros

- **Entrada:** `(nenhuma entrada)`
- **Resultado esperado:** Tabela com 5 registros na ordem de inserção.
- **Resultado:** Aprovado

**Observado:**

```text

--- Serviços cadastrados ---
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
30    Atendimento Psicossocial            Saúde                     CAPS do bairro
10    Emissão de CPF                      Documentos                Agências dos Correios
20    Orientação Jurídica Gratuita        Atendimento Comunitário   Defensoria Pública
40    Isenção de Tarifa no Transporte...  Assistência Social        Terminais de integração
50    Passe Livre Estudantil              Educação                  Secretaria de Educação
Total: 5 serviço(s).
```

### C16 - Atualizar título e canal do ID 40 (demais campos mantidos com Enter)

- **Entrada:** `40 | Isenção de Tarifa no Transporte Coletivo | (Enter) | (Enter) | (Enter) | Terminais e site da prefeitura`
- **Resultado esperado:** Mensagem de sucesso; título e canal alterados, categoria preservada.
- **Resultado:** Aprovado

**Observado:**

```text

--- Atualizar serviço ---
Identificador (0 para cancelar): 40

Registro atual:
Identificador: 40
Título: Isenção de Tarifa no Transporte Público
Categoria: Assistência Social
Descrição: Gratuidade na tarifa de ônibus.
Público-alvo: Idosos e pessoas com deficiência
Canal/Local de atendimento: Terminais de integração

Digite o novo valor ou apenas Enter para manter o atual.
Título [Isenção de Tarifa no Transporte Público]: Isenção de Tarifa no Transporte Coletivo
Categoria [Assistência Social]: 
Descrição [Gratuidade na tarifa de ônibus.]: 
Público-alvo [Idosos e pessoas com deficiência]: 
Canal/Local de atendimento [Terminais de integração]: Terminais e site da prefeitura
Serviço atualizado com sucesso.
```

### C17 - Atualizar ID inexistente (99)

- **Entrada:** `99`
- **Resultado esperado:** Mensagem de serviço não encontrado.
- **Resultado:** Aprovado

**Observado:**

```text

--- Atualizar serviço ---
Identificador (0 para cancelar): 99
Serviço com identificador 99 não encontrado.
```

### C18 - Atualizar sem informar nenhuma alteração (ID 10)

- **Entrada:** `10 | (Enter) | (Enter) | (Enter) | (Enter) | (Enter)`
- **Resultado esperado:** Aviso de que nada foi alterado.
- **Resultado:** Aprovado

**Observado:**

```text

--- Atualizar serviço ---
Identificador (0 para cancelar): 10

Registro atual:
Identificador: 10
Título: Emissão de CPF
Categoria: Documentos
Descrição: Emissão e regularização do CPF.
Público-alvo: Qualquer cidadão
Canal/Local de atendimento: Agências dos Correios

Digite o novo valor ou apenas Enter para manter o atual.
Título [Emissão de CPF]: 
Categoria [Documentos]: 
Descrição [Emissão e regularização do CPF.]: 
Público-alvo [Qualquer cidadão]: 
Canal/Local de atendimento [Agências dos Correios]: 
Nenhuma alteração informada. O registro permanece igual.
```

### C19 - Pesquisar título 'emissao' (sem acento e minúsculo)

- **Entrada:** `1 | emissao`
- **Resultado esperado:** Encontra 'Emissão de CPF' (ID 10).
- **Resultado:** Aprovado

**Observado:**

```text

--- Pesquisar serviços ---
[1] Por título
[2] Por categoria
[0] Voltar
Pesquisar por: 1
Termo de pesquisa: emissao

1 serviço(s) encontrado(s):
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
10    Emissão de CPF                      Documentos                Agências dos Correios
Total: 1 serviço(s).
```

### C20 - Pesquisar categoria 'educ'

- **Entrada:** `2 | educ`
- **Resultado esperado:** Encontra apenas o ID 50 (categoria Educação).
- **Resultado:** Aprovado

**Observado:**

```text

--- Pesquisar serviços ---
[1] Por título
[2] Por categoria
[0] Voltar
Pesquisar por: 2
Termo de pesquisa: educ

1 serviço(s) encontrado(s):
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
50    Passe Livre Estudantil              Educação                  Secretaria de Educação
Total: 1 serviço(s).
```

### C21 - Pesquisar termo sem correspondência

- **Entrada:** `1 | xyz`
- **Resultado esperado:** Mensagem de nenhum serviço encontrado.
- **Resultado:** Aprovado

**Observado:**

```text

--- Pesquisar serviços ---
[1] Por título
[2] Por categoria
[0] Voltar
Pesquisar por: 1
Termo de pesquisa: xyz
Nenhum serviço encontrado para 'xyz'.
```

### C22 - Pesquisar com termo vazio e depois 'gratuita'

- **Entrada:** `1 | (Enter) | gratuita`
- **Resultado esperado:** Aviso de termo vazio e, em seguida, resultado do ID 20.
- **Resultado:** Aprovado

**Observado:**

```text

--- Pesquisar serviços ---
[1] Por título
[2] Por categoria
[0] Voltar
Pesquisar por: 1
Termo de pesquisa: 
O termo de pesquisa não pode ser vazio.
Termo de pesquisa: gratuita

1 serviço(s) encontrado(s):
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
20    Orientação Jurídica Gratuita        Atendimento Comunitário   Defensoria Pública
Total: 1 serviço(s).
```

### C23 - Pesquisar com opção inválida e voltar

- **Entrada:** `7 | 0`
- **Resultado esperado:** Aviso de opção inválida e retorno ao menu.
- **Resultado:** Aprovado

**Observado:**

```text

--- Pesquisar serviços ---
[1] Por título
[2] Por categoria
[0] Voltar
Pesquisar por: 7
Opção inválida. Escolha uma das opções listadas.
[1] Por título
[2] Por categoria
[0] Voltar
Pesquisar por: 0
```

### C24 - Ordenar por identificador

- **Entrada:** `1`
- **Resultado esperado:** Ordem dos IDs: 10, 20, 30, 40, 50.
- **Resultado:** Aprovado

**Observado:**

```text

--- Ordenar lista ---
[1] Por identificador
[2] Por título
[3] Por categoria
[0] Voltar
Ordenar por: 1
Lista ordenada por identificador.
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
10    Emissão de CPF                      Documentos                Agências dos Correios
20    Orientação Jurídica Gratuita        Atendimento Comunitário   Defensoria Pública
30    Atendimento Psicossocial            Saúde                     CAPS do bairro
40    Isenção de Tarifa no Transporte...  Assistência Social        Terminais e site da prefeitura
50    Passe Livre Estudantil              Educação                  Secretaria de Educação
Total: 5 serviço(s).
```

### C25 - Ordenar por título (ignora acentos e maiúsculas)

- **Entrada:** `2`
- **Resultado esperado:** Ordem dos IDs: 30 (Atendimento), 10 (Emissão), 40 (Isenção), 20 (Orientação), 50 (Passe).
- **Resultado:** Aprovado

**Observado:**

```text

--- Ordenar lista ---
[1] Por identificador
[2] Por título
[3] Por categoria
[0] Voltar
Ordenar por: 2
Lista ordenada por título.
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
30    Atendimento Psicossocial            Saúde                     CAPS do bairro
10    Emissão de CPF                      Documentos                Agências dos Correios
40    Isenção de Tarifa no Transporte...  Assistência Social        Terminais e site da prefeitura
20    Orientação Jurídica Gratuita        Atendimento Comunitário   Defensoria Pública
50    Passe Livre Estudantil              Educação                  Secretaria de Educação
Total: 5 serviço(s).
```

### C26 - Ordenar por categoria

- **Entrada:** `3`
- **Resultado esperado:** Ordem dos IDs: 40 (Assistência), 20 (Atendimento), 10 (Documentos), 50 (Educação), 30 (Saúde).
- **Resultado:** Aprovado

**Observado:**

```text

--- Ordenar lista ---
[1] Por identificador
[2] Por título
[3] Por categoria
[0] Voltar
Ordenar por: 3
Lista ordenada por categoria.
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
40    Isenção de Tarifa no Transporte...  Assistência Social        Terminais e site da prefeitura
20    Orientação Jurídica Gratuita        Atendimento Comunitário   Defensoria Pública
10    Emissão de CPF                      Documentos                Agências dos Correios
50    Passe Livre Estudantil              Educação                  Secretaria de Educação
30    Atendimento Psicossocial            Saúde                     CAPS do bairro
Total: 5 serviço(s).
```

### C27 - Ordenar com opção inválida e voltar

- **Entrada:** `9 | 0`
- **Resultado esperado:** Aviso de opção inválida; ordem da lista não muda.
- **Resultado:** Aprovado

**Observado:**

```text

--- Ordenar lista ---
[1] Por identificador
[2] Por título
[3] Por categoria
[0] Voltar
Ordenar por: 9
Opção inválida. Escolha uma das opções listadas.
[1] Por identificador
[2] Por título
[3] Por categoria
[0] Voltar
Ordenar por: 0
```

### C28 - Excluir registro do meio (ID 10)

- **Entrada:** `10 | s`
- **Resultado esperado:** Serviço removido; ordem restante 40, 20, 50, 30.
- **Resultado:** Aprovado

**Observado:**

```text

--- Excluir serviço ---
Identificador (0 para cancelar): 10

Identificador: 10
Título: Emissão de CPF
Categoria: Documentos
Descrição: Emissão e regularização do CPF.
Público-alvo: Qualquer cidadão
Canal/Local de atendimento: Agências dos Correios

Confirma a exclusão? (s/n): s
Serviço removido com sucesso.
```

### C29 - Excluir primeiro registro (ID 40)

- **Entrada:** `40 | s`
- **Resultado esperado:** Serviço removido; ordem restante 20, 50, 30.
- **Resultado:** Aprovado

**Observado:**

```text

--- Excluir serviço ---
Identificador (0 para cancelar): 40

Identificador: 40
Título: Isenção de Tarifa no Transporte Coletivo
Categoria: Assistência Social
Descrição: Gratuidade na tarifa de ônibus.
Público-alvo: Idosos e pessoas com deficiência
Canal/Local de atendimento: Terminais e site da prefeitura

Confirma a exclusão? (s/n): s
Serviço removido com sucesso.
```

### C30 - Excluir último registro (ID 30)

- **Entrada:** `30 | s`
- **Resultado esperado:** Serviço removido; ordem restante 20, 50.
- **Resultado:** Aprovado

**Observado:**

```text

--- Excluir serviço ---
Identificador (0 para cancelar): 30

Identificador: 30
Título: Atendimento Psicossocial
Categoria: Saúde
Descrição: Acolhimento e escuta para pessoas em sofrimento emocional.
Público-alvo: Qualquer cidadão
Canal/Local de atendimento: CAPS do bairro

Confirma a exclusão? (s/n): s
Serviço removido com sucesso.
```

### C31 - Cadastrar após remover o último (ID 60 entra no final)

- **Entrada:** `60 | Mutirão de Cidadania | Atendimento Comunitário | Ações itinerantes de documentação e saúde. | Moradores da região | Praça central`
- **Resultado esperado:** Cadastro concluído; ordem 20, 50, 60 (ponteiro do final atualizado).
- **Resultado:** Aprovado

**Observado:**

```text

--- Cadastrar serviço ---
Identificador (inteiro positivo, 0 para cancelar): 60
Título: Mutirão de Cidadania
Categoria: Atendimento Comunitário
Descrição: Ações itinerantes de documentação e saúde.
Público-alvo: Moradores da região
Canal/Local de atendimento: Praça central
Serviço cadastrado com sucesso.
```

### C32 - Cancelar exclusão com 'n' (ID 50)

- **Entrada:** `50 | n`
- **Resultado esperado:** Exclusão cancelada; registro permanece.
- **Resultado:** Aprovado

**Observado:**

```text

--- Excluir serviço ---
Identificador (0 para cancelar): 50

Identificador: 50
Título: Passe Livre Estudantil
Categoria: Educação
Descrição: Gratuidade no transporte para estudantes.
Público-alvo: Estudantes da rede pública
Canal/Local de atendimento: Secretaria de Educação

Confirma a exclusão? (s/n): n
Exclusão cancelada.
```

### C33 - Confirmação inválida e depois 'n'

- **Entrada:** `50 | talvez | n`
- **Resultado esperado:** Aviso para responder s/n; exclusão cancelada.
- **Resultado:** Aprovado

**Observado:**

```text

--- Excluir serviço ---
Identificador (0 para cancelar): 50

Identificador: 50
Título: Passe Livre Estudantil
Categoria: Educação
Descrição: Gratuidade no transporte para estudantes.
Público-alvo: Estudantes da rede pública
Canal/Local de atendimento: Secretaria de Educação

Confirma a exclusão? (s/n): talvez
Responda com 's' para sim ou 'n' para não.

Confirma a exclusão? (s/n): n
Exclusão cancelada.
```

### C34 - Excluir ID inexistente (99)

- **Entrada:** `99`
- **Resultado esperado:** Mensagem de serviço não encontrado.
- **Resultado:** Aprovado

**Observado:**

```text

--- Excluir serviço ---
Identificador (0 para cancelar): 99
Serviço com identificador 99 não encontrado.
```

### C35 - Excluir todos os registros até esvaziar a lista (IDs 20, 50, 60)

- **Entrada:** `20 | s | 50 | s | 60 | s`
- **Resultado esperado:** Três remoções com sucesso; lista fica vazia.
- **Resultado:** Aprovado

**Observado:**

```text

--- Excluir serviço ---
Identificador (0 para cancelar): 20

Identificador: 20
Título: Orientação Jurídica Gratuita
Categoria: Atendimento Comunitário
Descrição: Atendimento jurídico para quem não pode pagar um advogado.
Público-alvo: Pessoas de baixa renda
Canal/Local de atendimento: Defensoria Pública

Confirma a exclusão? (s/n): s
Serviço removido com sucesso.

--- Excluir serviço ---
Identificador (0 para cancelar): 50

Identificador: 50
Título: Passe Livre Estudantil
Categoria: Educação
Descrição: Gratuidade no transporte para estudantes.
Público-alvo: Estudantes da rede pública
Canal/Local de atendimento: Secretaria de Educação

Confirma a exclusão? (s/n): s
Serviço removido com sucesso.

--- Excluir serviço ---
Identificador (0 para cancelar): 60

Identificador: 60
Título: Mutirão de Cidadania
Categoria: Atendimento Comunitário
Descrição: Ações itinerantes de documentação e saúde.
Público-alvo: Moradores da região
Canal/Local de atendimento: Praça central

Confirma a exclusão? (s/n): s
Serviço removido com sucesso.
```

### C36 - Listar após esvaziar a lista

- **Entrada:** `(nenhuma entrada)`
- **Resultado esperado:** Mensagem de lista vazia.
- **Resultado:** Aprovado

**Observado:**

```text

--- Serviços cadastrados ---
A lista está vazia. Cadastre um serviço ou carregue os dados de exemplo.
```

### C37 - Carregar 10 serviços de exemplo

- **Entrada:** `(nenhuma entrada)`
- **Resultado esperado:** 10 serviços carregados, nenhum ignorado.
- **Resultado:** Aprovado

**Observado:**

```text

--- Carregar dados de exemplo ---
10 serviço(s) de exemplo carregado(s). 0 já existiam e foram ignorado(s).
```

### C38 - Carregar os exemplos novamente (IDs duplicados)

- **Entrada:** `(nenhuma entrada)`
- **Resultado esperado:** Nenhum novo carregado; 10 ignorados; lista continua com 10.
- **Resultado:** Aprovado

**Observado:**

```text

--- Carregar dados de exemplo ---
0 serviço(s) de exemplo carregado(s). 10 já existiam e foram ignorado(s).
```

### C39 - Ordenar 10 registros por título

- **Entrada:** `2`
- **Resultado esperado:** IDs na ordem alfabética dos títulos: 1, 5, 8, 7, 3, 2, 12, 4, 11, 9.
- **Resultado:** Aprovado

**Observado:**

```text

--- Ordenar lista ---
[1] Por identificador
[2] Por título
[3] Por categoria
[0] Voltar
Ordenar por: 2
Lista ordenada por título.
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
1     Agendamento de Consulta na UBS      Saúde                     Unidade Básica de Saúde
5     Carteira de Trabalho Digital        Documentos                Aplicativo oficial ou posto d...
8     Curso Profissionalizante Gratuito   Educação                  Centro de Capacitação Municipal
7     Emissão de Segunda Via de Certi...  Documentos                Cartório de Registro Civil
3     Inscrição no Cadastro Único         Assistência Social        CRAS do bairro
2     Isenção de Tarifa no Transporte...  Assistência Social        Terminais de integração
12    Matrícula na Rede Municipal de ...  Educação                  Secretaria Municipal de Educação
4     Mutirão de Atendimento Comunitário  Atendimento Comunitário   Praças e escolas da comunidade
11    Orientação Jurídica Gratuita        Atendimento Comunitário   Defensoria Pública
9     Vacinação do Calendário Nacional    Saúde                     UBS e postos de vacinação
Total: 10 serviço(s).
```

### C40 - Ordenar 10 registros por identificador

- **Entrada:** `1`
- **Resultado esperado:** IDs em ordem crescente: 1, 2, 3, 4, 5, 7, 8, 9, 11, 12.
- **Resultado:** Aprovado

**Observado:**

```text

--- Ordenar lista ---
[1] Por identificador
[2] Por título
[3] Por categoria
[0] Voltar
Ordenar por: 1
Lista ordenada por identificador.
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
1     Agendamento de Consulta na UBS      Saúde                     Unidade Básica de Saúde
2     Isenção de Tarifa no Transporte...  Assistência Social        Terminais de integração
3     Inscrição no Cadastro Único         Assistência Social        CRAS do bairro
4     Mutirão de Atendimento Comunitário  Atendimento Comunitário   Praças e escolas da comunidade
5     Carteira de Trabalho Digital        Documentos                Aplicativo oficial ou posto d...
7     Emissão de Segunda Via de Certi...  Documentos                Cartório de Registro Civil
8     Curso Profissionalizante Gratuito   Educação                  Centro de Capacitação Municipal
9     Vacinação do Calendário Nacional    Saúde                     UBS e postos de vacinação
11    Orientação Jurídica Gratuita        Atendimento Comunitário   Defensoria Pública
12    Matrícula na Rede Municipal de ...  Educação                  Secretaria Municipal de Educação
Total: 10 serviço(s).
```

### C41 - Pesquisar categoria 'saude' (sem acento) nos 10 registros

- **Entrada:** `2 | saude`
- **Resultado esperado:** Encontra os 2 serviços da categoria Saúde (IDs 1 e 9).
- **Resultado:** Aprovado

**Observado:**

```text

--- Pesquisar serviços ---
[1] Por título
[2] Por categoria
[0] Voltar
Pesquisar por: 2
Termo de pesquisa: saude

2 serviço(s) encontrado(s):
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
1     Agendamento de Consulta na UBS      Saúde                     Unidade Básica de Saúde
9     Vacinação do Calendário Nacional    Saúde                     UBS e postos de vacinação
Total: 2 serviço(s).
```

### C42 - Ordenar lista com um único registro

- **Entrada:** `2`
- **Resultado esperado:** Lista permanece com 1 registro, sem erro.
- **Resultado:** Aprovado

**Observado:**

```text

--- Ordenar lista ---
[1] Por identificador
[2] Por título
[3] Por categoria
[0] Voltar
Ordenar por: 2
Lista ordenada por título.
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
1     Único                               Teste                     Balcão
Total: 1 serviço(s).
```

### C43 - Excluir o único registro (início e fim passam a ser vazios)

- **Entrada:** `1 | s`
- **Resultado esperado:** Serviço removido; lista vazia com início e fim nulos.
- **Resultado:** Aprovado

**Observado:**

```text

--- Excluir serviço ---
Identificador (0 para cancelar): 1

Identificador: 1
Título: Único
Categoria: Teste
Descrição: Descrição
Público-alvo: Todos
Canal/Local de atendimento: Balcão

Confirma a exclusão? (s/n): s
Serviço removido com sucesso.
```

### C44 - Opções inexistentes no menu principal e saída

- **Entrada:** `9 | abc | (Enter) | 0`
- **Resultado esperado:** Três avisos de opção inválida e mensagem de encerramento.
- **Resultado:** Aprovado

**Observado:**

```text
=== Citizen Assist AI | Gerenciador de Serviços ===

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 9
Opção inválida. Digite um número de 0 a 8.

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: abc
Opção inválida. Digite um número de 0 a 8.

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 
Opção inválida. Digite um número de 0 a 8.

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 0
Encerrando o sistema. Até logo!
```

### C45 - Sessão completa pelo menu principal (listar vazia, carregar, consultar, pesquisar, ordenar, atualizar, excluir, sair)

- **Entrada:** `3 | 8 | 3 | 2 | 7 | 6 | 2 | saude | 7 | 2 | 4 | 3 | (Enter) | (Enter) | Atendimento ampliado para toda a família | (Enter) | (Enter) | 2 | 3 | 5 | 2 | s | 3 | 0`
- **Resultado esperado:** Fluxo completo sem erros, terminando com a mensagem de encerramento.
- **Resultado:** Aprovado

**Observado:**

```text
=== Citizen Assist AI | Gerenciador de Serviços ===

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 3

--- Serviços cadastrados ---
A lista está vazia. Cadastre um serviço ou carregue os dados de exemplo.

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 8

--- Carregar dados de exemplo ---
10 serviço(s) de exemplo carregado(s). 0 já existiam e foram ignorado(s).

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 3

--- Serviços cadastrados ---
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
7     Emissão de Segunda Via de Certi...  Documentos                Cartório de Registro Civil
3     Inscrição no Cadastro Único         Assistência Social        CRAS do bairro
12    Matrícula na Rede Municipal de ...  Educação                  Secretaria Municipal de Educação
1     Agendamento de Consulta na UBS      Saúde                     Unidade Básica de Saúde
9     Vacinação do Calendário Nacional    Saúde                     UBS e postos de vacinação
5     Carteira de Trabalho Digital        Documentos                Aplicativo oficial ou posto d...
11    Orientação Jurídica Gratuita        Atendimento Comunitário   Defensoria Pública
2     Isenção de Tarifa no Transporte...  Assistência Social        Terminais de integração
8     Curso Profissionalizante Gratuito   Educação                  Centro de Capacitação Municipal
4     Mutirão de Atendimento Comunitário  Atendimento Comunitário   Praças e escolas da comunidade
Total: 10 serviço(s).

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 2

--- Consultar serviço ---
Identificador (0 para cancelar): 7

Identificador: 7
Título: Emissão de Segunda Via de Certidão de Nascimento
Categoria: Documentos
Descrição: Solicitação de segunda via da certidão de nascimento.
Público-alvo: Qualquer cidadão
Canal/Local de atendimento: Cartório de Registro Civil

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 6

--- Pesquisar serviços ---
[1] Por título
[2] Por categoria
[0] Voltar
Pesquisar por: 2
Termo de pesquisa: saude

2 serviço(s) encontrado(s):
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
1     Agendamento de Consulta na UBS      Saúde                     Unidade Básica de Saúde
9     Vacinação do Calendário Nacional    Saúde                     UBS e postos de vacinação
Total: 2 serviço(s).

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 7

--- Ordenar lista ---
[1] Por identificador
[2] Por título
[3] Por categoria
[0] Voltar
Ordenar por: 2
Lista ordenada por título.
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
1     Agendamento de Consulta na UBS      Saúde                     Unidade Básica de Saúde
5     Carteira de Trabalho Digital        Documentos                Aplicativo oficial ou posto d...
8     Curso Profissionalizante Gratuito   Educação                  Centro de Capacitação Municipal
7     Emissão de Segunda Via de Certi...  Documentos                Cartório de Registro Civil
3     Inscrição no Cadastro Único         Assistência Social        CRAS do bairro
2     Isenção de Tarifa no Transporte...  Assistência Social        Terminais de integração
12    Matrícula na Rede Municipal de ...  Educação                  Secretaria Municipal de Educação
4     Mutirão de Atendimento Comunitário  Atendimento Comunitário   Praças e escolas da comunidade
11    Orientação Jurídica Gratuita        Atendimento Comunitário   Defensoria Pública
9     Vacinação do Calendário Nacional    Saúde                     UBS e postos de vacinação
Total: 10 serviço(s).

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 4

--- Atualizar serviço ---
Identificador (0 para cancelar): 3

Registro atual:
Identificador: 3
Título: Inscrição no Cadastro Único
Categoria: Assistência Social
Descrição: Cadastro de famílias de baixa renda para acesso a programas sociais.
Público-alvo: Famílias de baixa renda
Canal/Local de atendimento: CRAS do bairro

Digite o novo valor ou apenas Enter para manter o atual.
Título [Inscrição no Cadastro Único]: 
Categoria [Assistência Social]: 
Descrição [Cadastro de famílias de baixa renda para acesso a programas sociais.]: Atendimento ampliado para toda a família
Público-alvo [Famílias de baixa renda]: 
Canal/Local de atendimento [CRAS do bairro]: 
Serviço atualizado com sucesso.

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 2

--- Consultar serviço ---
Identificador (0 para cancelar): 3

Identificador: 3
Título: Inscrição no Cadastro Único
Categoria: Assistência Social
Descrição: Atendimento ampliado para toda a família
Público-alvo: Famílias de baixa renda
Canal/Local de atendimento: CRAS do bairro

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 5

--- Excluir serviço ---
Identificador (0 para cancelar): 2

Identificador: 2
Título: Isenção de Tarifa no Transporte Público
Categoria: Assistência Social
Descrição: Cadastro para gratuidade ou desconto na tarifa de ônibus.
Público-alvo: Idosos e pessoas com deficiência
Canal/Local de atendimento: Terminais de integração

Confirma a exclusão? (s/n): s
Serviço removido com sucesso.

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 3

--- Serviços cadastrados ---
ID    Título                              Categoria                 Canal/Local
----------------------------------------------------------------------------------------------------
1     Agendamento de Consulta na UBS      Saúde                     Unidade Básica de Saúde
5     Carteira de Trabalho Digital        Documentos                Aplicativo oficial ou posto d...
8     Curso Profissionalizante Gratuito   Educação                  Centro de Capacitação Municipal
7     Emissão de Segunda Via de Certi...  Documentos                Cartório de Registro Civil
3     Inscrição no Cadastro Único         Assistência Social        CRAS do bairro
12    Matrícula na Rede Municipal de ...  Educação                  Secretaria Municipal de Educação
4     Mutirão de Atendimento Comunitário  Atendimento Comunitário   Praças e escolas da comunidade
11    Orientação Jurídica Gratuita        Atendimento Comunitário   Defensoria Pública
9     Vacinação do Calendário Nacional    Saúde                     UBS e postos de vacinação
Total: 9 serviço(s).

--- Menu Principal ---
[1] Cadastrar serviço
[2] Consultar por identificador
[3] Listar todos
[4] Atualizar serviço
[5] Excluir serviço
[6] Pesquisar por título ou categoria
[7] Ordenar lista
[8] Carregar dados de exemplo
[0] Sair
Escolha uma opção: 0
Encerrando o sistema. Até logo!
```
