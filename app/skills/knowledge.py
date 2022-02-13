import sys
import os
import path
sys.path.append(str(path.Path(os.getcwd()).parent))
from app.utils.text import TextUtils
from app.settings import HUNGGINGFACE_API
import json
import requests

class KnowledgeSkills:
    
    @classmethod
    def get_anwser(cls, question):
        try:
            headers = {"Authorization": HUNGGINGFACE_API["key"]}
            qs = {
                    "inputs": {
                    "question": question,
                    "context": TextUtils.query_to_text(question),
                    }
                }
            data = json.dumps(qs)
            response = requests.request("POST", "https://api-inference.huggingface.co/models/nvkha/bert-qa-vi", headers=headers, data=data)
            answer = json.loads(response.content.decode("utf-8"))
            print(answer)
        
            if "answer" in answer:
                return answer['answer']
            elif "error" in answer:
                return "Model đang tải"
        except:
            return "Xin lỗi bạn mình không thể trả lời câu hỏi này"
