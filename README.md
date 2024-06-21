# Dashboard de Vendas - Streamlit

## Visão Geral

Este repositório contém um dashboard interativo criado com Streamlit para visualizar e analisar dados de vendas de um e-commerce. O dashboard oferece gráficos e métricas dinâmicas que permitem explorar o faturamento, a quantidade de produtos vendidos, e outras informações relevantes. Além disso, utiliza a inteligência artificial Gemini para gerar insights automáticos sobre os dados.

## Funcionalidades

- **Filtro por Mês**: Selecione um mês específico para filtrar os dados.
- **Métricas Gerais**: Exibe o total faturado e a quantidade de produtos vendidos.
- **Gráficos Interativos**:
  - Faturamento por Dia
  - Faturamento por Categoria de Produto
  - Faturamento por Região
  - Métodos de Pagamento
  - Os 10 Produtos Mais Vendidos
- **Geração de Insights**: Utiliza a inteligência artificial Gemini para gerar insights sobre os dados.

## Pré-requisitos

Para executar este projeto, você precisará ter os seguintes pacotes Python instalados:

- streamlit
- pandas
- plotly
- google-generativeai

Você pode instalar esses pacotes usando o pip:

```bash
pip install streamlit pandas plotly google-generativeai
```
## Como Executar
1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
````

2. **Configure sua chave de API para a Gemini AI:**
Crie um arquivo key.py no diretório raiz do projeto e adicione sua chave de API da seguinte forma:
```bash
key = 'sua_chave_de_api'
```

3. **Execute o aplicativo Streamlit:**

```bash
streamlit run app.py
```

Substitua app.py pelo nome do arquivo onde o código está salvo.

4. **Visualize o dashboard:**
O aplicativo será aberto no seu navegador padrão. Você poderá interagir com os filtros e visualizar os gráficos e métricas.

## Estrutura do Código
- **Carregamento de Dados:** Os dados são carregados de um arquivo CSV e pré-processados.
- **Layout da Página:** A página é dividida em várias colunas para organizar as métricas e gráficos.
- **Filtragem de Dados:** A filtragem é feita com base na seleção do mês pelo usuário.
- **Cálculo de Métricas:** As métricas gerais são calculadas com base nos dados filtrados.
- **Visualização:** Gráficos interativos são gerados usando Plotly e exibidos no dashboard.
- **Geração de Insights:** Utiliza a API da Gemini AI para gerar insights automáticos sobre os dados.
