import streamlit as st
import pandas as pd

st.title("Quantas saias de filó a barata tem?")

st.image("https://ofuxico.com.br/wp-content/uploads/2023/05/barata-MET-GALA.jpg",
         width=None,
    use_column_width=None,
    clamp=False,
    channels="RGB",
    output_format="auto",
    use_container_width=False)
  
st.text_input = (label == "Digite aqui quantas saias de filó a barata tem", value=None, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", icon=None)


if st.text_input == "1":
  st.write("Acertou, ela tem é uma só")
  st.video(data, format="video/mp4", start_time=0, *, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)
else: 
  st.write("Errou, era mentira da barata")
