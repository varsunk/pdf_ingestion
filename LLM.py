from google import genai

class LLM():
    def __init__(self, api_key, model_id):
        self._client = genai.Client(api_key=api_key)
        self._model_id = model_id
        self._uploaded_files = []

    def upload(self, file: str, config: dict[str, str]):
        file = self._client.files.upload(file=file, config=file)
        self._uploaded_files.append(file)

        return file
    
    def _prompt_text(self, prompt: str) -> genai.types.GenerateContentResponse:
        response = self._client.models.generate_content(
            model=self._model_id,
            contents=[prompt]
        )

        return response
    
    

