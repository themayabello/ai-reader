import streamlit as st
from gtts import gTTS

st.title("📜 AI Reader")
st.write(
    "Upload a document below and have it read out loud to you."
)

# Let the user upload a file via `st.file_uploader`.
uploaded_file = st.file_uploader(
    "Upload a document (.txt)", type=("txt")
)

if uploaded_file:
    text = uploaded_file.read().decode(errors="ignore")
    st.text_area("Uploaded Text:", value=text, height=300)

    if st.button("Convert to Speech"):
        tts = gTTS(text)
        tts.save("output.mp3")
        st.audio("output.mp3", format="audio/mp3")