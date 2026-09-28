# Verificador de Receitas Médicas com OCR

Projeto desenvolvido para a disciplina de Algoritmos, com o objetivo de automatizar a verificação de receitas médicas e a baixa de estoque de medicamentos a partir do processamento de imagens.

## Descrição

O sistema recebe a imagem de uma receita médica, extrai as informações relevantes por meio de OCR (Reconhecimento Óptico de Caracteres), valida o CRM do médico prescritor e, caso a validação seja bem-sucedida, realiza a baixa dos medicamentos prescritos em um banco de dados de estoque.

## Funcionamento

1. **Upload da receita** — a imagem da receita médica é fornecida ao sistema.
2. **Extração via OCR** — o texto é extraído, com foco no CRM do médico e nos medicamentos prescritos.
3. **Validação do CRM** — o CRM e a UF extraídos são verificados em um banco de dados de médicos cadastrados.
4. **Baixa em estoque** — se o médico for validado, os medicamentos identificados têm sua quantidade reduzida no banco de dados de estoque.

## Módulos do projeto

| Módulo | Responsabilidade |
|---|---|
| OCR / Extração | Processa a imagem da receita e extrai texto (CRM, UF, medicamentos) via regex |
| Validação de CRM | Confere se o CRM e a UF extraídos existem no banco de médicos cadastrados |
| Banco de dados de médicos | Armazena os médicos cadastrados (SQLite) |
| Verificação de medicamentos | Confronta os medicamentos extraídos com o estoque cadastrado |
| Estoque | Realiza a baixa dos medicamentos validados |

## Tecnologias e dependências

- Python
- [OpenCV](https://opencv.org/) (`opencv-python`) — pré-processamento de imagem
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) + `pytesseract`
- `numpy`
- SQLite — banco de dados de médicos e medicamentos

### Instalação

```bash
pip install opencv-python pytesseract numpy
```

> É necessário instalar o Tesseract OCR separadamente no sistema operacional (Windows, Linux ou macOS) e garantir que esteja acessível no PATH ou configurado no `pytesseract`.

## Validação de CRM

A função de validação recebe o CRM e a UF extraídos da receita e consulta o banco de dados de médicos cadastrados, utilizando a chave composta `(crm, uf)`. Ela retorna um valor booleano indicando se o médico está cadastrado e apto a prescrever.

Casos tratados:
- CRM e UF encontrados e correspondentes → validação bem-sucedida
- CRM não encontrado no banco
- CRM encontrado, mas UF divergente
- Falha do OCR/regex ao extrair CRM ou UF da receita (tratado sem consultar o banco)

## Limitações conhecidas

- A verificação de medicamentos depende de correspondência exata entre o nome extraído pelo OCR (ex.: "DIPIRONA GOTAS 500 ML") e o nome cadastrado no banco de estoque (ex.: "Dipirona 500mg"), o que pode gerar falsos negativos.
- Receitas com artefatos de OCR incomuns (como caracteres de traço duplicados no CRM) podem não ser reconhecidas corretamente pelo regex de extração.
- A validação do nome do médico (além do CRM) ainda não foi implementada.

## Autores

- Murilo Costa
- Bento Cordeiro
- Cauã Max
- Gutemberg Melo
- Guilherme Silveira

Projeto desenvolvido em grupo para a disciplina de Algoritmos — UEPB.

## Licença

Projeto acadêmico, sem licença de uso comercial definida.
