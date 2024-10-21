import streamlit as st
from transformers import pipeline

# Load the translation pipeline from Hugging Face
model_name = "your-username/english-to-roman-urdu"  # Replace with the actual model name
translator = pipeline("translation", model=model_name)

# Streamlit app
st.title("English to Roman Urdu Translator")

# Input prompt
input_text = st.text_area("Enter English text:")

if st.button("Translate"):
    if input_text:
        # Translate the input text
        translation = translator(input_text)
        st.success(f"Translation: {translation[0]['translation_text']}")
    else:
        st.warning("Please enter some text to translate.")

# Note: Run the app using: streamlit run app.py
