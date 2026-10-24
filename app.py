import streamlit as st
from google import genai

# Explicitly load the API key from Streamlit Secrets
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("Agri-Pest Diagnostic Assistant")
st.write("Diagnose crop issues and get local treatment plans for Pakistani farmers.")

symptom = st.text_input("Describe the crop damage or symptoms (e.g., yellowing leaves, white powdery spots):")

if st.button("Diagnose"):
    if not symptom:
        st.error("Please enter a symptom description.")
    else:
        system_prompt = f"""You are an agricultural expert in Punjab, Pakistan. 
        The user has provided a crop symptom in either English or Urdu: '{symptom}'. 
        Analyze the symptom and identify the most likely local pest. 
        Provide a concise, 3-bullet treatment plan including non-chemical methods and local chemical controls. 
        Add one brief recommendation for a general recovery fertilizer to help the plant survive the pest stress. Do not provide specific mathematical quantities or land-size ratios.
        Structure your output into two strict sections:
        First, the complete response in English.
        Second, the complete response translated into proper Urdu script (اردو). You must not include any English words, Latin characters, or brackets in the Urdu section. Translate pest names and chemicals directly into Urdu script."""
        
        with st.spinner("Analyzing with Google Gemini API..."):
            try:
                # Must use a valid Gemini model string, not a local Gemma filename
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=system_prompt,
                )
                st.success("Diagnosis Complete")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error calling API: Verify your Streamlit Secrets. Details: {e}")
