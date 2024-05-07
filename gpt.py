'''
Utility class for interacting with ChatGPT API
'''
from db_util import DbUtil
import openai

class GptUtil:
    def __init__(self, key: str) -> None:
        self.dbu = DbUtil()
        openai.api_key = key

    def ask_question(self, question: str) -> str:
        self.dbu.connect()

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Choose the model you prefer
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        answer = response['choices'][0]['message']['content']
        # maybe query inside here?

        self.dbu.disconnect()
        return answer
    


