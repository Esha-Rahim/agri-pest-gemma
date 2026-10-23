# Agri-Pest Diagnostic Assistant

Our app helps Pakistani farmers diagnose crop pests from symptom descriptions and get local treatment options using Gemma.

## Tech Stack
* UI: Streamlit
* Model: `gemma-4-26b-a4b-it` (Released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0))
* Integration: Google GenAI SDK via Gemini API

## How to Run Locally
1. Clone the repository.
2. Create a `.env` file in the root directory and add your key: `GEMINI_API_KEY=your_key_here`
3. Install dependencies: `pip install google-genai python-dotenv streamlit`
4. Run the application: `streamlit run app.py`
## How It Works

1. **User Input:** The user enters a description of crop damage or symptoms via the Streamlit frontend.
2. **Context Injection:** The app wraps the raw input into a strict system prompt. This prompt applies safety guardrails (restricting specific chemical ratios) and sets the persona as a localized agricultural expert in Punjab, Pakistan.
3. **LLM Processing (API):** The structured prompt is sent to the Google Gemini API, which serves as the backend reasoning engine to bypass the hardware compute limits required for local open-weight models. 
4. **Bilingual Output:** The model generates a concise, 3-bullet treatment plan (covering non-chemical and local chemical controls) and provides a localized Urdu translation. The Streamlit app then renders both versions for the user.
