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
