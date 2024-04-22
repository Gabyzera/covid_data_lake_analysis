# 🦠 Análise AWS COVID-19 

## 👓 Visão Geral
Este projeto visa construir rotas web interativa usando Flask que se conecta ao AWS COVID-19 data lake para visualizar dados atualizados sobre a pandemia. As rotas oferecem gráficos e mapas para explorar tendências de casos, disponibilidade de leitos hospitalares e dados de vacinação, facilitando a compreensão dos diversos aspectos da pandemia.

## 🏗️ Etapas do Projeto
### 1. Configuração Inicial
Utilização do Amazon CloudFormation para configurar o Data Catalog no AWS Athena, garantindo acesso fácil aos datasets relevantes do COVID-19 data lake.

### 2. Exploração de Dados
Identificação e seleção dos conjuntos de dados mais relevantes, como números de casos, mortes, dados de leitos hospitalares e informações sobre vacinação.

### 3. Desenvolvimento de Consultas SQL
Elaboração de consultas SQL para extrair os dados necessários do AWS Athena para as visualizações planejadas.

### 4. Salvar resultados das consultas na Amazon S3
As consultas de SQL através da Amazon Athena possuem os dados de retorno armazanados em um bucket da Amazon S3.

### 5. Criação da Aplicação Flask
Desenvolvimento de uma aplicação Flask que serve como a base, gerenciando conexões e execuções de consultas ao Athena.

### 6. Visualização de Dados
Criação de gráficos e mapas interativos usando a biblioteca Plotly para representar visualmente os dados.

### 7. Roteamento
Rotas contendo visualizações na aplicação Flask, assegurando uma interface interativa para os usuários.

### 8. Jupyter Notebook para a visualização dos gráficos
Os dados salvos no Amazon S3 serão consumidos em um notebook que apresenta todas os gráficos e análises produzidas na aplicação.

## ✍🏼 Aprendizados
> Criação de conta e utilização de serviços AWS.

> Apresentar dados com plotly através da requisição do usuário na API.

> Adicionar timeouts nas queries da AWS Athena.

> Lidar com erros em Python.

> Utilização de Next Token para novas requisições a APIs externas.

> Desafios e limitações do uso de `scatter_geo` em Plotly para grandes quantidades de dados.

> Uso eficiente de funções de janela em consultas SQL para reduzir o armazenamento temporário.

> Implementação de escalas contínuas de cores em visualizações.

> Tipagem de payloads como objetos em Python.

## 💻 Tecnologias Utilizadas
- AWS Athena
- AWS CloudFormation
- AWS S3
- Flask
- SQL
- Python
- Plotly
- HTML