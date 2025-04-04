import os
import csv
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Create an instance of the GenAI client
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)  # Fetch the API key from the environment variable

# Function to generate structured prompts
def generate_prompt(case, prompt_type):
    base_prompt = f"""
    **Patient Profile:**
    - Age: {case['age']}
    - Gender: {case['gender']}
    - Medical History: {case['medical_history']}
    
    **Presenting Symptoms:**
    - Primary Complaint: {case['primary_complaint']}
    - Duration: {case['duration']}
    - Associated Symptoms: {case['associated_symptoms']}
    
    **Additional Information:**
    - Recent Exposures: {case['recent_exposures']}
    - Medications: {case['medications']}
    - Lifestyle Factors: {case['lifestyle']}
    """

    prompt_templates = {
        "symptom_inquiry": "Based on the provided patient profile, what is the most likely diagnosis? Please include:\n"
                           "1. Most likely diagnosis\n"
                           "2. Other possible conditions to consider\n"
                           "3. Recommended diagnostic tests\n"
                           "4. Confidence level (1-10 scale).",

        "triage_inquiry": "Based on this patient's condition, what are the next best steps for medical evaluation? Please provide:\n"
                          "1. A potential diagnosis\n"
                          "2. Justifications for each recommended action\n"
                          "3. Urgency level (Low, Moderate, High, Emergency).",

        "follow_up_inquiry": f"The patient has been diagnosed with {case.get('correct_diagnosis', 'unknown')}. What structured follow-up care plan do you recommend?\n"
                             "Please provide a structured response including:\n"
                             "1. Necessary follow-up tests\n"
                             "2. Medication adjustments (if any)\n"
                             "3. Lifestyle recommendations\n"
                             "4. Long-term management strategy.",

        "physician_support": "What differential diagnoses should be considered, and what diagnostic tests would you recommend?"
    }

    return base_prompt + "\n\n" + prompt_templates[prompt_type]

# Function to query Gemini (Gemini-2.0-Flash)
def query_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text  # Return the generated text from Gemini
    except Exception as e:
        return f"Error querying Gemini: {e}"

# Load cases from CSV and run tests
results = []

# Specify encoding when opening the CSV file
with open("patient_cases.csv", "r", encoding='ISO-8859-1') as file:
    reader = csv.DictReader(file)
    for row in reader:
        case_id = row["case_id"]

        for prompt_type in ["symptom_inquiry", "triage_inquiry", "follow_up_inquiry", "physician_support"]:
            prompt = generate_prompt(row, prompt_type)

            # Query Gemini
            response = query_gemini(prompt)

            results.append({
                "case_id": case_id,
                "prompt_type": prompt_type,
                "Gemini": response
            })

# Save results as CSV
with open("llm_responses_gemini.csv", "w", newline='') as outfile:
    fieldnames = ["case_id", "prompt_type", "Gemini"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for result in results:
        writer.writerow(result)

print("Batch testing completed. Results saved to llm_responses_gemini.csv.")
