import streamlit as st

st.title('CloudSQLWatch Dashboard')

st.write('Bem-vindo ao aplicativo Streamlit do CloudSQLWatch!')

# Um exemplo de gráfico simples
st.line_chart([1, 2, 3, 4, 5])

# Entrada do usuário
nome = st.text_input('Digite seu nome:')
st.write(f'Olá, {nome}!')

