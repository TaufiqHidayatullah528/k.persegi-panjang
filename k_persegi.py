import streamlit as st
 
st.title('Hitung Luas Persegi Panjang')


panjang = st.number_input ('masukan nilai panjang',0)
lebar = st.number_input ('masukan nilai lebar', 0)
hitung = st.button('hitung luas')

if hitung :
    luas = panjang * lebar
    st.write('luas persegi panjang adalah = ', luas)