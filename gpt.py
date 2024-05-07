'''
Utility class for interacting with ChatGPT API
'''
from db_util import DbUtil
import openai

class GptUtil:
    def __init__(self, key: str) -> None:
        self.dbu = DbUtil()
        openai.api_key = key

    def ask_question(self, type: int, question: str) -> str:
        self.dbu.connect()

        content: str = None

        match type:
            # Fun fact
            case 0:
                content = ''
            # Cars table 
            case 1:
                content = self.dbu.query('cars')
            # Manufacturers table
            case 2:
                content = self.dbu.query('manufacturers')

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Choose the model you prefer
            messages=[
                {"role": "system", "content": "You are a helpful assistant. You will either be asked to generate a fun fact, or if provided SQL tables you will need to answer a question in the context of the provided data."},
                {"role": "user", "content": question + 'Content (if blank ignore and just give fun fact): ' + str(content)}
            ]
        )
        answer = response['choices'][0]['message']['content']

        self.dbu.disconnect()
        return answer
    


