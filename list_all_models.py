<<<<<<< HEAD
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyAdGv1nGUuUfpBH13uHTfN57vOKyqY-EtQ"
genai.configure(api_key=GEMINI_API_KEY)

print("Listing all available models for this specific API key:")
try:
    for m in genai.list_models():
        print(f"Name: {m.name}, Methods: {m.supported_generation_methods}")
except Exception as e:
    print(f"Error listing models: {e}")
=======
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyAdGv1nGUuUfpBH13uHTfN57vOKyqY-EtQ"
genai.configure(api_key=GEMINI_API_KEY)

print("Listing all available models for this specific API key:")
try:
    for m in genai.list_models():
        print(f"Name: {m.name}, Methods: {m.supported_generation_methods}")
except Exception as e:
    print(f"Error listing models: {e}")
>>>>>>> f61a8b6371167df94a75b2d6fa77172f56c97333
