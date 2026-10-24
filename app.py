import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Study Notes Simplifier", page_icon="📚", layout="centered")

st.title("📚 AI Study Notes Simplifier")
st.write(
    "Turn difficult study notes into simpler explanations, short summaries, "
    "and revision points using an open-source AI model."
)
st.info(
    "This demo uses the open-source FLAN-T5 model from Hugging Face. "
    "The first run downloads the model, so an internet connection is needed initially."
)

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small")

notes = st.text_area(
    "Paste your study notes here",
    height=220,
    placeholder="Example: Photosynthesis is the process by which green plants convert light energy..."
)
task = st.selectbox(
    "Choose what you want the AI to do",
    ["Explain in simple language", "Make a short summary", "Create revision points", "Generate quiz questions"]
)

if st.button("Simplify my notes", type="primary"):
    if not notes.strip():
        st.warning("Please paste some notes first.")
    else:
        prompt_map = {
            "Explain in simple language": "Explain the following study notes in simple language for a student: ",
            "Make a short summary": "Write a short, clear summary of these study notes: ",
            "Create revision points": "Create 5 concise revision points from these study notes: ",
            "Generate quiz questions": "Create 5 simple quiz questions with answers based on these study notes: "
        }
        try:
            with st.spinner("Loading the open-source AI model and processing your notes..."):
                model = load_model()
                result = model(
                    prompt_map[task] + notes[:2500],
                    max_new_tokens=180,
                    do_sample=False,
                    truncation=True
                )[0]["generated_text"]
            st.subheader("AI result")
            st.write(result)
            st.caption("Review AI-generated content for accuracy before using it for exams.")
        except Exception as exc:
            st.error("The model could not run. Check your internet connection and try again.")
            st.caption(f"Technical detail: {exc}")

st.divider()
st.subheader("Why open-source AI?")
st.write(
    "- You can inspect and reuse the model under its published license.\n"
    "- The model can be run on your own computer after it has been downloaded.\n"
    "- You are not required to send notes to a paid hosted AI API.\n"
    "- Small models are useful for learning, though their answers can be imperfect."
)
st.caption("Student project prototype • Built with Streamlit and Hugging Face Transformers")
