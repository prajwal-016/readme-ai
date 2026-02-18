<<<<<<< HEAD
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyAdGv1nGUuUfpBH13uHTfN57vOKyqY-EtQ"
genai.configure(api_key=GEMINI_API_KEY)

model_name = 'gemini-1.5-flash-latest' # This often maps to a stable ID
print(f"Testing specifically: {model_name}")
try:
    model = genai.GenerativeModel(model_name)
    response = model.generate_content("Say hello")
    print(f"SUCCESS: {response.text}")
except Exception as e:
    print(f"FAILED: {e}")
=======
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyAdGv1nGUuUfpBH13uHTfN57vOKyqY-EtQ"
genai.configure(api_key=GEMINI_API_KEY)

model_name = 'gemini-1.5-flash-latest' # This often maps to a stable ID
print(f"Testing specifically: {model_name}")
try:
    model = genai.GenerativeModel(model_name)
    response = model.generate_content("Say hello")
    print(f"SUCCESS: {response.text}")
except Exception as e:
    print(f"FAILED: {e}")
>>>>>>> f61a8b6371167df94a75b2d6fa77172f56c97333
