<<<<<<< HEAD
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyAdGv1nGUuUfpBH13uHTfN57vOKyqY-EtQ"
genai.configure(api_key=GEMINI_API_KEY)

models_to_test = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-1.0-pro']

for model_name in models_to_test:
    print(f"Testing model: {model_name}")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Say hello")
        print(f"Success with {model_name}: {response.text}")
        break
    except Exception as e:
        print(f"Failed with {model_name}: {e}")
=======
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyAdGv1nGUuUfpBH13uHTfN57vOKyqY-EtQ"
genai.configure(api_key=GEMINI_API_KEY)

models_to_test = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-1.0-pro']

for model_name in models_to_test:
    print(f"Testing model: {model_name}")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Say hello")
        print(f"Success with {model_name}: {response.text}")
        break
    except Exception as e:
        print(f"Failed with {model_name}: {e}")
>>>>>>> f61a8b6371167df94a75b2d6fa77172f56c97333
