# 🦠 Análise AWS COVID-19 

## 👓 Visão Geral
Este projeto visa construir rotas web interativa usando Flask que se conecta ao AWS COVID-19 data lake para visualizar dados atualizados sobre a pandemia. As rotas oferecem gráficos e mapas para explorar tendências de casos, disponibilidade de leitos hospitalares e dados de vacinação, facilitando a compreensão dos diversos aspectos da pandemia.

## 🏗️ Etapas do Projeto
### 1. Configuração Inicial
Utilização do Amazon CloudFormation para configurar o Data Catalog no AWS Athena, garantindo acesso fácil aos datasets relevantes do COVID-19 data lake.

### 2. Exploração de Dados
Identificação e seleção dos conjuntos de dados mais relevantes, como números de casos, dados de leitos hospitalares e informações sobre vacinação.

### 3. Desenvolvimento de Consultas SQL
Elaboração de consultas SQL para extrair os dados necessários do AWS Athena para as visualizações planejadas.

### 4. Criação da Aplicação Flask
Desenvolvimento de uma aplicação Flask que serve como a base, gerenciando conexões e execuções de consultas ao Athena.

### 5. Visualização de Dados
Criação de gráficos e mapas interativos usando bibliotecas como Plotly para representar visualmente os dados.

### 6. Implementação
Integração das visualizações na aplicação Flask, assegurando uma interface interativa para os usuários.

## ✍🏼 Aprendizados
Utilização de Next Token para novas requisições a APIs externas.

Desafios e limitações do uso de `scatter_geo` em Plotly para grandes quantidades de dados.

Aplicação de logaritmo para normalização de dados.

Uso eficiente de funções de janela em consultas SQL para reduzir o armazenamento temporário.

Implementação de escalas contínuas de cores em visualizações.

Navegação entre diretórios em Python.

Criação de dicionários de cores para mapeamento em dataframes.

Tipagem de payloads como objetos em Python.

## 💻 Tecnologias Utilizadas
- AWS Athena
- AWS CloudFormation
- Flask
- SQL
- Python
- Plotly

## 📖 Documentação e Compartilhamento
O projeto está documentado detalhadamente, incluindo as decisões de design, consultas SQL e arquitetura da aplicação Flask. Todo o código e documentação estão disponíveis no GitHub, e pode ser acessada e compartilhada através do perfil no LinkedIn.

