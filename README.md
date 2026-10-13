# Verificador de Receitas Médicas com OCR

Sistema para automatizar a verificação de receitas médicas e a baixa de estoque de medicamentos a partir do processamento de imagens, desenvolvido em Python.

## Contexto
Projeto desenvolvido em grupo para a disciplina de Algoritmos (UEPB). O nosso objetivo foi resolver um problema do mundo real: a lentidão e a margem de erro na verificação manual de receitas em farmácias. O sistema recebe a imagem da receita, extrai os dados via OCR, valida as credenciais do médico e, se aprovado, atualiza o inventário da farmácia automaticamente.

## Funcionalidades

- **Upload e Processamento:** Leitura da imagem da receita médica.
- **Extração via OCR:** Identificação e extração do texto (focando no CRM do médico e nos medicamentos) utilizando Regex.
- **Validação de CRM:** Consulta automática do CRM e da UF extraídos contra um banco de dados de médicos autorizados.
- **Baixa em Estoque:** Redução automática da quantidade de medicamentos no banco de dados de estoque após a validação positiva.

## Decisões de Engenharia e Regras de Negócio

Lidar com extração de texto de imagens introduziu o desafio de trabalhar com "dados sujos". Para garantir a integridade do sistema, implementámos as seguintes lógicas:

- **Chave Composta para Validação:** A validação do médico não confia apenas no número do CRM. Utilizamos uma chave composta `(crm, uf)` para consultar a base SQLite, prevenindo fraudes ou conflitos de médicos de estados diferentes com o mesmo número.
- **Tratamento de Exceções do OCR:** O reconhecimento de imagem falha frequentemente. Se o Regex não conseguir extrair um formato válido de CRM/UF devido a artefactos na imagem (ex: traços duplicados), o sistema interrompe o fluxo de forma segura e não onera o banco de dados com consultas inválidas.
- **Condicional de Estoque Rigorosa:** A baixa no estoque é a última etapa do funil. O sistema confronta a string exata extraída com o banco e só realiza a dedução se houver *match* perfeito e se o médico tiver passado em todas as validações anteriores.
- **Criação Automática da Base de Dados:** As bases SQLite de médicos e estoque são inicializadas dinamicamente (`CREATE TABLE IF NOT EXISTS`) e populadas com dados iniciais de teste na primeira execução, dispensando o versionamento de arquivos `.db` binários no Git.

## Estrutura do Projeto

```text
projeto_algoritmos/
├── Funcoes/
│   ├── BD/
│   │   ├── medicos.py              # Script de criação/validação do banco de médicos
│   │   └── medicamentos.py         # Script de controle e baixa de estoque
│   └── Leitura_Processamento/
│       ├── ocr.py                  # Integração com OpenCV e Tesseract
│       ├── processamento.py        # Extração Regex dos campos
│       └── config.py               # Configurações globais
├── Receitas_Ficticias/             # Imagens de amostra para testes do OCR
│   ├── Receita_1.jpeg
│   ├── Receita_Invalida.jpeg
│   └── Receita_UF_AL.jpeg
├── main.py                         # Ponto de entrada e fluxo do sistema
├── requirements.txt                # Dependências do projeto
└── .gitignore
```

## Por que esta Stack?

- **Python:** A escolha ideal para a orquestração do projeto devido ao seu vasto ecossistema de bibliotecas para manipulação de dados e automação.
- **OpenCV + Tesseract:** Utilizamos o OpenCV para o pré-processamento das imagens, preparando o terreno para que o Tesseract (motor de OCR padrão de mercado) pudesse extrair os caracteres com a maior precisão possível.
- **SQLite:** Adotado para simular os bancos de dados de médicos e de estoque localmente, garantindo persistência leve e sem necessidade de infraestrutura de rede durante o desenvolvimento académico.

## O que aprendemos e o que faríamos diferente (Próximos Passos)

1. **Flexibilidade na Busca de Medicamentos:** A verificação atual depende de correspondência exata. Se o OCR extrair "DIPIRONA GOTAS 500 ML" e o banco tiver "Dipirona 500mg", o sistema falha. Numa V2, o desafio seria estudar e implementar uma forma de comparar textos por similaridade em vez de igualdade exata, reduzindo os falsos negativos.
2. **Pré-processamento de Imagem Avançado:** Receitas com artefatos de OCR incomuns quebram o Regex de extração. O próximo passo seria adicionar filtros no OpenCV antes de enviar a imagem para o Tesseract.
3. **Validação do Nome:** A validação do nome do médico (além do CRM) ainda não foi implementada, o que adicionaria mais uma camada de segurança.

## Módulos do projeto

| Módulo | Responsabilidade |
|---|---|
| OCR / Extração | Processa a imagem da receita e extrai texto (CRM, UF, medicamentos) via regex |
| Validação de CRM | Confere se o CRM e a UF extraídos existem no banco de médicos cadastrados |
| Banco de dados de médicos | Armazena os médicos cadastrados (SQLite) |
| Verificação de medicamentos | Confronta os medicamentos extraídos com o estoque cadastrado |
| Estoque | Realiza a baixa dos medicamentos validados |

## Validação de CRM em Detalhe

A função de validação recebe o CRM e a UF extraídos da receita e consulta o banco de dados de médicos cadastrados. Ela retorna um valor booleano indicando se o médico está cadastrado e apto a prescrever.

**Casos tratados na lógica:**
- CRM e UF encontrados e correspondentes → validação bem-sucedida.
- CRM não encontrado no banco → bloqueado.
- CRM encontrado, mas UF divergente → bloqueado.
- Falha do OCR/regex ao extrair CRM ou UF da receita → fluxo interrompido sem consultar o banco.

## Tecnologias e dependências

- Python 3.14.6+: Linguagem principal do projeto.
- OpenCV (opencv-python): Pré-processamento e manipulação de imagens.
- PyTesseract: Wrapper Python para o motor de OCR Tesseract.
- NumPy: Suporte ao processamento de matrizes de imagens.
- SQLite3: Banco de dados relacional leve para persistência local de médicos e estoque.

## Como Executar o Projeto

1. Pré-requisitos
Certifique-se de ter o Python e o motor Tesseract OCR instalados no seu sistema operacional:

> É necessário instalar o Tesseract OCR separadamente no sistema operacional (Windows, Linux ou macOS) e garantir que esteja acessível no PATH ou configurado no `pytesseract`.

2. Instalação de Dependências
Clone o repositório e instale as bibliotecas necessárias:

```bash
git clone https://github.com/bcord1/projeto_algoritmos.git
cd projeto_algoritmos

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

3. Executando o Sistema
Para iniciar a aplicação, execute o script principal:

```bash
python main.py
```
> Nota: As tabelas e registros de teste dos bancos de dados serão gerados automaticamente no primeiro acesso.

## Autores

- Murilo Costa
- Bento Cordeiro
- Cauã Max
- Gutemberg Melo
- Guilherme Silveira

## Licença

Projeto acadêmico, sem licença de uso comercial definida.
