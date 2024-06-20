# Dashboard de Análise de Vendas

Este é um dashboard interativo construído utilizando Streamlit, uma plataforma para criação de aplicativos web em Python. O código carrega dados de vendas de um arquivo CSV e oferece visualizações e métricas para análise.

#### Funcionalidades Principais:

1. **Configuração da Página:**
   - O dashboard é configurado para ter um título personalizado ("Dashboard"), um ícone (🧊), layout amplo e a barra lateral expandida por padrão.

2. **Carregamento e Pré-processamento dos Dados:**
   - Os dados de vendas são carregados de um arquivo CSV.
   - A coluna de data é convertida para o formato datetime e os dados são ordenados por data.
   - É criada uma nova coluna 'Month' para facilitar a agregação por mês.

3. **Filtragem Interativa:**
   - Uma opção na barra lateral permite filtrar os dados por mês.
   - Opções disponíveis incluem todos os meses presentes nos dados, além da opção "Sem Filtros" para visualizar todos os dados sem restrições.

4. **Métricas Gerais:**
   - Calcula e exibe o total faturado e a quantidade total de produtos vendidos com base nos dados filtrados.

5. **Visualizações Gráficas:**
   - **Faturamento por Dia:** Um gráfico de barras que mostra o faturamento ao longo do tempo, colorido por região.
   - **Faturamento por Categoria:** Um gráfico de barras que exibe o faturamento por categoria de produto, também colorido por região.
   - **Vendas por Região:** Um gráfico de barras que mostra a quantidade total de produtos vendidos por região.
   - **Método de Pagamento:** Um gráfico de pizza que ilustra a distribuição do faturamento por métodos de pagamento.
   - **Os 10 Produtos Mais Vendidos:** Um gráfico de barras que apresenta os produtos mais vendidos, baseado na quantidade de unidades vendidas.

#### Como Executar:

Para executar o dashboard localmente:

1. Certifique-se de ter as bibliotecas necessárias instaladas (`streamlit`, `pandas`, `plotly`).
2. Faça o download do arquivo `sales_data.csv` e ajuste o caminho de carregamento no código para refletir seu diretório local.
3. Utilize o comando `streamlit run nome_do_arquivo.py` no terminal, onde `nome_do_arquivo.py` é o nome do arquivo Python que contém o código do dashboard.

#### Observações:

- Este dashboard oferece uma análise básica e interativa dos dados de vendas.
- As visualizações são geradas utilizando a biblioteca Plotly Express, permitindo interação e personalização diretas no aplicativo web.


