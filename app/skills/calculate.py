import sys
import os
import path
sys.path.append(str(path.Path(os.getcwd()).parent))
import wolframalpha
from app.settings import WOLFRAMALPHA_API

class CalculateSkills:
    
    @classmethod
    def calculate(cls, question):
        try: 
            question = cls.__question_reprocess(question)
            client = wolframalpha.Client(WOLFRAMALPHA_API["key"])
            print(question)
            res = client.query(question)
            answer = next(res.results).text
            return answer
            
        
        except Exception as e:
            print(e)
            return None

    def __question_reprocess(question):
        question.replace("bằng mấy", "") \
                .replace("bằng bao nhiêu", "") \
                .replace("=", "") \
                .replace("tính", "") \
                .replace("bao nhiêu", "") \
                .replace("bằng", "") 
        return question

