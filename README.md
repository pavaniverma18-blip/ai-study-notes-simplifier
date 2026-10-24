# AI Study Notes Simplifier

A beginner-friendly prototype for the Hacktoberfest Week 3 “Slow and Steady” theme.

## What it does
- Explains pasted notes in simpler language
- Creates a short summary
- Produces revision points
- Generates quiz questions with answers

## Open-source AI
The project uses `google/flan-t5-small` through Hugging Face Transformers. Check the model card and license before redistribution or deployment:
https://huggingface.co/google/flan-t5-small

## Run locally (Windows)
1. Install Python 3.10 or newer.
2. Extract this folder.
3. Open Command Prompt in this folder.
4. Create a virtual environment:
   `py -m venv .venv`
5. Activate it:
   `.venv\Scripts\activate`
6. Install dependencies:
   `python -m pip install -r requirements.txt`
7. Start the app:
   `python -m streamlit run app.py`

The first run downloads model files and needs internet access. Later runs may work offline if the model files remain cached. Performance depends on your laptop.

## Limitations
- This is a prototype, not a verified tutoring system.
- AI output may be wrong or incomplete; verify important facts.
- Notes are sent to the local model pipeline in this app, not to a paid model API.
- The app truncates long notes to fit the demo prompt.

## Suggested improvements
- Add upload support for TXT/PDF notes
- Add source citations
- Add tests and clearer error handling
- Improve long-document handling
