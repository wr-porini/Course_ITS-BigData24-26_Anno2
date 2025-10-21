import pickle
import streamlit as st

st.set_page_config("App di prova per ML", layout='wide')

st.title("Benvenuti nella mia app di prova per Machine Learning!")

st.write("""
         Questa è una semplice applicazione web creata con Streamlit per dimostrare le funzionalità di base.

         Fornisci:
         - Tempo in secondi
         - Latitudine
         - Longitudine

         Riceverai in output una previsione basata sui dati inseriti.
         """)


col1, col2, col3, _,_,_ = st.columns(6)

with col1:
    time = st.number_input("Inserisci il tempo in secondi:", min_value=60.0, value=1000.0)

with col2:
    lat = st.number_input("Inserisci la latitudine:", min_value=-90.0, max_value=90.0, value=45.0)

with col3:
    lon = st.number_input("Inserisci la longitudine:", min_value=-180.0, max_value=180.0, value=9.0)

if st.button("Prevedi"):
    with open("../data/ufo_model.pkl", "rb") as f:
        model = pickle.load(f)
        prediction = model.predict([[time, lat, lon]])
    st.write(f"Previsione: {prediction[0]}")
    

