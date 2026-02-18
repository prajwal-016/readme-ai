<<<<<<< HEAD
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCPpHC7lFr_aSYmv-PsaI34WxSEyayTAhM"
genai.configure(api_key=GEMINI_API_KEY)

with open('models_list.txt', 'w') as f:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            f.write(m.name + '\n')
=======
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCPpHC7lFr_aSYmv-PsaI34WxSEyayTAhM"
genai.configure(api_key=GEMINI_API_KEY)

with open('models_list.txt', 'w') as f:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            f.write(m.name + '\n')
>>>>>>> f61a8b6371167df94a75b2d6fa77172f56c97333
