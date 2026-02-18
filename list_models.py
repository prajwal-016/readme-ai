<<<<<<< HEAD
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCPpHC7lFr_aSYmv-PsaI34WxSEyayTAhM"
genai.configure(api_key=GEMINI_API_KEY)

print("Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
=======
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCPpHC7lFr_aSYmv-PsaI34WxSEyayTAhM"
genai.configure(api_key=GEMINI_API_KEY)

print("Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
>>>>>>> f61a8b6371167df94a75b2d6fa77172f56c97333
