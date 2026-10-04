import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="AI Image Analyzer",
    page_icon="🤖",
    layout="wide"
)


# ---------------- WEBPAGE DESIGN ----------------

st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- WEBPAGE CONTENT ----------------

st.markdown(
    '<div class="title">🤖 AI Image Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload an image and ask a question about it.</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- IMAGE UPLOAD ----------------

st.subheader("🖼️ Upload Your Image")

image_path = st.file_uploader(
    "Choose an image",
    type=["png", "jpg", "jpeg"]
)


if image_path is not None:

    image = Image.open(image_path)

    st.image(
        image,
        caption="Uploaded Image",
        width=500
    )


    # ---------------- QUESTION ----------------

    st.subheader("💬 Ask a Question")

    prompt = st.text_input(
        "Ask your question",
        placeholder="Example: What is present in this image?"
    )


    # ---------------- BUTTON ----------------

    if st.button("🔍 Analyze Image",disabled=not prompt):

        Input = [image, prompt]

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=Input
        )

        # ---------------- RESULT ----------------

        st.divider()

        st.subheader("🤖 AI Response")

        st.write(response.text)

