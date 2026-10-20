from google import genai

def debug_code(image, mode, api_key):
    if mode == "Hints":
        prompt = """You are a Python debugging assitant.
        Analyze the uploaded code image.

        Explain:
        - What the error is.
        - Why the error happens.
        - Give simple hints to fix it.

        Do not provide the complete corrected code.
        """
    else:
        prompt = """You are an exert Python debugging assistant.
        Analyze the uploaded code screenshot.

        Explain:
        - What the error is.
        - Why it happens.
        - Provide the corrected code.
        - Explain how the correction works.

        Display the corrected code using Markdown code blocks/
        """

    client = genai.Client(api_key = api_key)    
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents= [image, prompt]
    )

    return response.text or "Gemini returned no response"