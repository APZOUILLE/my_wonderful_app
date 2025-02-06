import streamlit as st
import plotly.express as px


st.title('Hello World')


df = px.data.iris()

feature_x = st.selectbox("Select features", ['petal_length', 'petal_width'])

feature_y = st.selectbox("Select features", ['sepal_length', 'sepal_width'])




fig = px.scatter(df, x=feature_x, y=feature_y)
st.plotly_chart(fig)

st.dataframe(df.describe())

starter , ender = st.slider('Hello choose intervall', 0, 100, (20, 30))

if starter > 30:
    st.write('hello')