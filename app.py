import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image

from api_calling import debug_code

load_dotenv()

st.title ("AI Code Debugger App")
st.markdown("Upload a screenshot of your code")
st.divider()


uploaded_file = st.file_uploader(
    "Upload your error screenshot",
    type = ["jpg", "jpeg", "png"]
)

mode = st.selectbox(
    "Choose an option",
    ["Hints", "Solution with code"],
    index = None
)

if st.button("Debug Code"):
    if uploaded_file is None:
        st.error("Please upload an image")

    elif mode is None:
        st.error("Please select a debugging option")

    else:
        api_key = os.getenv("GEMINI_API_KEY")

        try:
            image = Image.open(uploaded_file).convert("RGB")

            with st.spinner("AI is debugging your code...."):
                result = debug_code(image, mode, api_key)

            with st.container (border = True):
                st.subheader("Debuggin Result")
                st.markdown(result)

        except Exception as e:
            st.error("Something went wrong")
            st.write(str(e))