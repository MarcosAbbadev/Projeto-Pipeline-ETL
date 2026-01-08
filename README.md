# ETL Pipeline com IA Generativa (Python)

## 📌 Visão Geral

Este projeto demonstra a construção de um **pipeline ETL (Extract, Transform, Load)** em Python, seguindo o modelo clássico utilizado em ambientes corporativos, com um diferencial moderno:  
a **etapa de transformação é enriquecida com IA generativa**.

O objetivo é mostrar domínio de:
- fundamentos de engenharia de dados
- organização de código
- integração conceitual com IA
- boas práticas para projetos de portfólio

---

## 🏗️ Arquitetura do Pipeline

O pipeline segue a estrutura tradicional:

**EXTRACT → TRANSFORM → LOAD**

---

### 1️⃣ Extract

Os dados de entrada são simulados por uma **lista de usuários em memória**, representando dados vindos de uma API ou banco de dados.

---

### 2️⃣ Transform

Nesta etapa, cada usuário recebe uma **mensagem personalizada gerada por IA**, simulando um processo de *data enrichment*, prática comum em áreas como marketing, finanças e CRM.

Caso a IA não esteja disponível (ex.: limite de requisições), o pipeline utiliza um **fallback automático**, garantindo robustez.

---

### 3️⃣ Load

O carregamento é simulado por uma função que imprime o payload final, representando:
- envio para uma API externa
- persistência em banco de dados
- integração com outro sistema

---

## 🧠 Uso de IA no Projeto

A IA é utilizada **como ferramenta de transformação**, não como dependência crítica.

Isso reflete um cenário real de mercado, onde sistemas precisam continuar operando mesmo quando serviços externos estão indisponíveis.

> ⚠️ Este projeto tem finalidade **educacional e demonstrativa**.  
> A integração com IA pode ser adaptada conforme o ambiente real.

---

## 📂 Estrutura do Projeto

```text
.
├── pipeline.py
├── README.md
├── requirements.txt
└── .gitignore
```

## ▶️ Como Executar
### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/etl-ai-marketing-pipeline.git
cd etl-ai-marketing-pipeline
```

### 2. Criar ambiente virtual (opcional, recomendado)
```
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências
```
pip install -r requirements.txt
```

### 4. Executar o pipeline
```
python pipeline.py
```

---

## 📦 Tecnologias Utilizadas

- Python 3.10+

- Conceitos de ETL

- IA Generativa (OpenAI API – uso ilustrativo)

- Estruturação de projetos para portfólio

## 🎯 Objetivo do Projeto

- Este projeto não visa produção, mas sim:

- Demonstrar compreensão sólida de pipelines ETL

- Mostrar como IA pode ser integrada de forma consciente

- Servir como projeto de portfólio técnico

- Apoiar candidaturas para vagas júnior ou estágio em tecnologia/dados

## 📌 Possíveis Evoluções

- Persistência real em banco de dados

- Consumo de API externa no Extract

- Logs estruturados

- Versionamento de dados

- Pipeline agendado (cron / Airflow)

## 👤 Autor

Marcos Abbade
Estudante de Tecnologia

LinkedIn: https://www.linkedin.com/in/marcos-abbade/

GitHub: https://github.com/MarcosAbbadev/

Projeto desenvolvido para fins educacionais e de portfólio.
