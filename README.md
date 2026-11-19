
# 💰 Sistema Financeiro com Python e Docker

## 📌 Sobre o projeto

Aplicação simples desenvolvida em Python para calcular
o saldo financeiro a partir de receitas e despesas.

Este projeto faz parte do meu aprendizado de
Docker, Linux, Git e Cloud Engineering.

## 🛠️ Tecnologias utilizadas

- Python 3.13
- Docker
- Linux (Ubuntu / WSL2)
- Git

## 📁 Estrutura do projeto

```text
financeiro-python/
├── app.py
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## ⚙️ Variáveis de ambiente

| Variável | Descrição | Valor padrão |
|----------|-----------|--------------|
| RECEITA | Receita total | 5000 |
| DESPESAS | Despesas totais | 3200 |

## 🚀 Como executar com Docker

### 1. Construir a imagem

```bash
docker build -t financeiro-python:v3 .
```

### 2. Executar com valores padrão

```bash
docker run --rm financeiro-python:v3
```

### 3. Executar com valores personalizados

```bash
docker run --rm \
  -e RECEITA=10000 \
  -e DESPESAS=6000 \
  financeiro-python:v3
```

### 4. Executar usando arquivo .env

Crie um arquivo chamado `.env`:

```dotenv
RECEITA=15000
DESPESAS=8500
```

Depois execute:

```bash
docker run --rm --env-file .env financeiro-python:v3
```

## ✅ Resultado esperado

```text
=== SISTEMA FINANCEIRO ===
Receita: R$ 15000.00
Despesas: R$ 8500.00
Saldo: R$ 6500.00
```

## 🔐 Segurança

- Arquivos .env são ignorados pelo Git.
- O .dockerignore exclui arquivos desnecessários do build.
- Não armazenar senhas ou tokens no código-fonte.
- Utilizar valores fictícios nos exemplos.

## 📚 Conceitos praticados

- Construção de imagens Docker
- Execução de containers
- Variáveis de ambiente
- Arquivos .env
- Git e controle de versões
- Boas práticas de segurança

## 🔮 Próximas melhorias

- Entrada de dados pelo usuário
- Validação dos valores financeiros
- Persistência dos registros
- Testes automatizados
- Automação com CI/CD
