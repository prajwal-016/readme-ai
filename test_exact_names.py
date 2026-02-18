<<<<<<< HEAD
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyAdGv1nGUuUfpBH13uHTfN57vOKyqY-EtQ"
genai.configure(api_key=GEMINI_API_KEY)

# Try models exactly as listed in your account list
models_to_test = [
    'gemini-flash-latest',
    'gemini-pro-latest',
    'gemini-1.5-flash-lite-latest',
    'gemini-2.0-flash', # Even if it gave quota error before, maybe 1.5 versions work?
]

for m in models_to_test:
    print(f"Testing Exact Match: {m}")
    try:
        model = genai.GenerativeModel(m)
        response = model.generate_content("Say hello")
        print(f"SUCCESS with {m}: {response.text}")
        break
    except Exception as e:
        print(f"FAILED with {m}: {e}")
=======
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyAdGv1nGUuUfpBH13uHTfN57vOKyqY-EtQ"
genai.configure(api_key=GEMINI_API_KEY)

# Try models exactly as listed in your account list
models_to_test = [
    'gemini-flash-latest',
    'gemini-pro-latest',
    'gemini-1.5-flash-lite-latest',
    'gemini-2.0-flash', # Even if it gave quota error before, maybe 1.5 versions work?
]

for m in models_to_test:
    print(f"Testing Exact Match: {m}")
    try:
        model = genai.GenerativeModel(m)
        response = model.generate_content("Say hello")
        print(f"SUCCESS with {m}: {response.text}")
        break
    except Exception as e:
        print(f"FAILED with {m}: {e}")
>>>>>>> f61a8b6371167df94a75b2d6fa77172f56c97333
