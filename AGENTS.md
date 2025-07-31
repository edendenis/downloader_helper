# Instruções Gerais

* O usuário irá fornecer uma tarefa.
* A tarefa envolve trabalhar com repositórios Git no seu diretório de trabalho atual.
* Aguarde até que todos os comandos de terminal sejam concluídos (ou cancelados) antes de finalizar.

## Git

Se para executar a tarefa for necessário criar ou modificar arquivos:

* **Não** crie novos `branches` e, se for preciso criar, comece o nome da branch com `codex` e não utilize caracteres especiais no nome da branch.
* Use o Git para **commitar** suas alterações.
* Se o *pre-commit* falhar, corrija os problemas e tente novamente.
* Verifique `git status` para confirmar que sua *worktree* está limpa.
* Apenas o código **committed** será avaliado.
* **Não** modifique ou altere *commits* existentes.
* Sempre faça as alterações baseadas no último `commit` da branch `main`.

## Especificação de `AGENTS.md`

* Repositórios podem conter arquivos `AGENTS.md` em `/`, `~` ou pastas internas.
* Eles orientam humanos sobre convenções de código, organização e execução do projeto.
* Se contiverem instruções sobre mensagens de Pull Request, **respeite-as**.
* O escopo é a árvore de diretórios a partir de onde estão.
* `AGENTS.md` aninhados têm precedência sobre os mais gerais.
* Instruções de sistema/desenvolvedor/usuário na conversa têm precedência sobre o `AGENTS.md`.
* Se o `AGENTS.md` define checagens programáticas, **execute-as** e certifique-se de que passam.

## Instruções de Citação

* Se navegar em arquivos ou usar comandos de terminal, **cite** no texto final:

  * **Arquivo**: `【F:<caminho_do_arquivo>†L<linha_inicial>(-L<linha_final>)?】`
  * **Terminal**: `【<chunk_id>†L<linha_inicial>(-L<linha_final>)?】`
* Prefira citações de **arquivo**.
* Não cite commits nem URLs diretas.

## Convenções de Código e Documentação

### Python

1. **Cabeçalho**:

```python
# -*- coding: utf-8 -*-
```

2. **Linguagem**:

* Texto da resposta: **português brasileiro**.
* Comentários: **português brasileiro**.
* Identificadores: **inglês (EUA)**.
* Saídas (`print`, `input`): **inglês (EUA)**.

3. **Estilo PEP8 / PEP257**:

* Sem espaços em branco no final.
* 100 colunas por linha.

4. **Docstrings & Sphinx**:

```python
r"""
Docstring em pt-BR com bloco Sphinx:

.. math:: \dfrac{u}{v}
"""
```

5. **Gráficos em preto e branco**:

* Use marcadores distintos para impressão sem cores.
* Posicione a legenda à direita do gráfico com `bbox_to_anchor=(1.02, 0.5)`
  para evitar sobreposição.

### LaTeX

1. **Cabeçalho**:

```latex
\documentclass[12pt, a4paper]{article}
\input{preamble.tex}
\begin{document}
```

Finalize com:

```latex
\end{document}
```

2. **Linguagem**:

* Comentários: **português brasileiro**.
* Variáveis: **inglês (EUA)**.
* Traduzir automaticamente `Figure`, `Table`, etc.

3. **Formatação**:

* Sempre usar `\dfrac` no lugar de `\frac` ou `/`.
* Unidades devem estar em `\mathrm{}`.
* Use `\autoref` em vez de `\ref` ou `\eqref`.
* Equações em sistema devem alinhar o `=` com `&` em ambientes `aligned` ou `cases`.
* Separador decimal é `,`.
* Figuras devem estar em `\fbox`, exceto capas e diagramas.
* Tabelas em `tables/` com `\input`.
* Variáveis devem ser descritas com `\begin{itemize}`.

4. **Nomenclaturas**:

* Ordenar em ordem alfabética.
* Remover unidades.
* Pode agrupar por categoria: cinemáticas, térmicas etc.
* Variáveis de **figuras e diagramas** também devem ser incluídas.
* Adicionar:

```latex
\addcontentsline{toc}{section}{Lista de Nomenclaturas}
\printnomenclature
```

5. **Padronização**:

* Verificar se todas variáveis seguem mesmo padrão.
* Corrigir palavras separadas erroneamente (ex: `temper-atura`).
* Corrigir ortografia.
* Todas as listagens de código devem ser centralizadas em `appendix.tex`.
  Os arquivos `main*.tex` precisam incluir esse apêndice com `\input{appendix.tex}`.

6. **Referências ABNT**:

* Autores em CAIXA ALTA.
* Títulos com apenas a primeira letra maiúscula.
* Ano ao final.
* Exemplo:

```latex
\bibitem{fox2010}
FOX, R. W.; McDONALD, A. T.; PRITCHARD, P. J.. \textbf{\textit{Introdu\c{c}\~ao \`a mec\^anica dos fluidos}}. 8. ed. Rio de Janeiro: LTC. p. 426--430, 2010.
```

* Ordenar as referências pela aparição.
* Trocar citações `AUTOR ANO` por `Autor (ANO)`.

7. **Validações**:

* Verificar se seções têm citações.
* Verificar se todas referências listadas são citadas.
* Atualizar acrônimos, definições e nomenclaturas com ordem alfabética e remoção de não usados.
* Manter identação correta.
* Explicar gráficos inseridos.

## Organização dos trechos LaTeX

O documento principal deve incluir `preamble.tex` para a configuração de pacotes e comandos gerais e `variable_oficial_names.tex` para as macros institucionais.

### Exemplos para `preamble.tex`
* Ajustes de hifenização.
* Todas as chamadas `\usepackage{...}`.
* Ambientes e comandos como `\newtheorem` e `\DeclarePairedDelimiter`.
* Configurações do `hyperref` (`\hypersetup{...}`).
* Definições de espaçamento (`\onehalfspacing`, `\doublespacing` etc.).
* Criação da lista de nomenclaturas conforme as instruções deste arquivo.

### Exemplos para `variable_oficial_names.tex`
* `\course{...}`, `\area{...}`.
* `\author{...}{...}`, `\itaauthoraddress{...}{...}{...}`.
* `\title{...}`.
* `\advisor{...}{...}{...}`, `\coadvisor{...}{...}{...}`.
* `\boss{...}{...}`, `\bosscourse{...}{...}`.
* Palavras‑chave (`\kwcip{...}`).
* `\examiner{...}{...}{...}{...}`.
* `\date{...}{...}{...}`.
* `\cdu{...}`.

### Seções
* Iniciar cada capítulo com `\chapter{...}` antes de qualquer `\section`, exceto capa, folha de rosto, dedicatória, agradecimentos, epígrafo, resumo, apêndice ou anexo.

* Não alterar a Seção `## 1. Configurar/Instalar/usar o `Git` [1]` do arquivo `README.ipynb`.

# Codex Instructions

- After updating `README.ipynb`, run `python convert_ipynb_to_md_and_py.py` to regenerate `README.md` and `README.py`.
- No additional tests are required for this repository.
- Include the command output from the conversion script in the PR testing section.
