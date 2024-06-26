import streamlit as st
import pandas as pd
import plotly.express as px
import google.generativeai as genai
from key import key

st.set_page_config(
    page_title="Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carregar os dados no início
data = pd.read_csv("sales_data.csv")
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values('Date')
data['Month'] = data['Date'].apply(lambda x: str(x.year) + "-" + str(x.month))

# Layout da página
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6, col7 = st.columns(3)

# Opção de filtro por mês na barra lateral
all_months = ['Sem Filtros'] + list(data['Month'].unique())
option = st.sidebar.selectbox('Selecione um Mês', all_months)

# Verifica se a opção selecionada não é "Sem Filtro"
if option != 'Sem Filtros':
    # Filtrar os dados pelo mês selecionado
    data = data_filtered = data[data['Month'] == option]
else:
    # Utiliza todos os dados
    data_filtered = data

# Calcular métricas gerais com base nos dados filtrados
total = sum(data_filtered['Total Revenue'])
quantidade_produtos = sum(data_filtered['Units Sold'])


# Mostrar métricas gerais
col1.metric('Total Faturado', f'{total:,.2f}')
col2.metric('Quantidade de Produtos Vendidos', quantidade_produtos)

# Gráficos
fig_date = px.bar(data_filtered, x='Date', y='Total Revenue', title='Faturamento por Dia', color='Region')
col3.plotly_chart(fig_date)

fig_type = px.bar(data_filtered, x='Date', y='Product Category', title='Faturamento por Categoria', color='Region')
col4.plotly_chart(fig_type)

regions = data_filtered.groupby('Region')['Total Revenue'].sum().reset_index().drop_duplicates()
fig_regions = px.bar(regions, x='Region', y='Total Revenue', title='Regiões')
col5.plotly_chart(fig_regions)

fig_kid = px.pie(data_filtered, values='Total Revenue', names='Payment Method', title='Método de Pagamento')
col6.plotly_chart(fig_kid)

products = data_filtered.groupby('Product Name')['Units Sold'].sum().reset_index()
products = products.sort_values(by='Units Sold', ascending=False)
products = products.head(10)
fig_products = px.bar(products, x='Product Name', y='Units Sold', title='Os 10 Produtos Mais Vendidos')
col7.plotly_chart(fig_products)

# Geração de insights com a inteligência artificial Gemini
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-flash')
prompt = f"O dataset a seguir corresponde a dados de um e-commerce. Me informe 5 insights sobre este dataset {data} em português."
response = model.generate_content(prompt)

st.markdown(response.text)
