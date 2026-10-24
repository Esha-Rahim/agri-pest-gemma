# Agri-Pest Diagnostic Assistant

An MVP agricultural diagnostic tool designed to help Pakistani farmers identify crop diseases and receive localized treatment plans in English and Urdu.

## Tech Stack
* **Frontend:** Streamlit
* **Backend Reasoning:** Google Gemini API 
* *Note: The Gemini API is utilized as a cloud-based MVP substitute for a local open-weights pipeline to bypass the GPU compute limits of free-tier cloud hosting.*

## How It Works
1. **User Input:** The farmer enters a description of crop damage or symptoms via the Streamlit interface.
2. **Context Injection:** The app wraps the raw input into a strict system prompt. This applies safety guardrails (restricting exact chemical ratios) and sets the persona as an agricultural expert in Punjab, Pakistan.
3. **LLM Processing:** The structured prompt is routed to the Google Gemini API, avoiding the heavy hardware requirements of hosting local LLMs.
4. **Bilingual Output:** The model generates a concise, 3-bullet treatment plan covering non-chemical and local chemical controls, translated into Urdu for field accessibility.

## How to Run Locally

1. Clone the repository:
```bash
git clone [https://github.com/Esha-Rahim/agri-pest-gemma.git](https://github.com/Esha-Rahim/agri-pest-gemma.git)
cd agri-pest-gemma

## How It Works

1. **User Input:** The user enters a description of crop damage or symptoms via the Streamlit frontend.
2. **Context Injection:** The app wraps the raw input into a strict system prompt. This prompt applies safety guardrails (restricting specific chemical ratios) and sets the persona as a localized agricultural expert in Punjab, Pakistan.
3. **LLM Processing (API):** The structured prompt is sent to the Google Gemini API, which serves as the backend reasoning engine to bypass the hardware compute limits required for local open-weight models. 
4. **Bilingual Output:** The model generates a concise, 3-bullet treatment plan (covering non-chemical and local chemical controls) and provides a localized Urdu translation. The Streamlit app then renders both versions for the user.
