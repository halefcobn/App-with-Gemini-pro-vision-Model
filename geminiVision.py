from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv() # load env variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro-vision")
#gemini pro model
def get_response(input, image):
    if input!="":
        response = model.generate_content([input, image])
    else: response = model.generate_content(image)
    
    return response.text

#Streamlit Config
st.set_page_config(page_title='Gemini Image Demo App')

st.header('Gemini Pro LLM Application')

input = st.text_input("Input Prompt: ", key="input") 

uploaded_file = st.file_uploader("Choose an image...", type:=["jpg", "jpeg","png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    

sumbit = st.button("Tell about the image")

#when question is submitted

if sumbit:
    response= get_response(input, image)
    st.subheader("The Response is")
    st.write(response)
    
    
