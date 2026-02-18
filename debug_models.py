<<<<<<< HEAD
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCPpHC7lFr_aSYmv-PsaI34WxSEyayTAhM"
genai.configure(api_key=GEMINI_API_KEY)

try:
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    print("START_MODELS")
    for m in available_models:
        print(m)
    print("END_MODELS")
except Exception as e:
    print(f"ERROR: {e}")
=======
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCPpHC7lFr_aSYmv-PsaI34WxSEyayTAhM"
genai.configure(api_key=GEMINI_API_KEY)

try:
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    print("START_MODELS")
    for m in available_models:
        print(m)
    print("END_MODELS")
except Exception as e:
    print(f"ERROR: {e}")
>>>>>>> f61a8b6371167df94a75b2d6fa77172f56c97333
