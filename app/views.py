from app import app, request, jsonify
from app.core.nlp import NLP

nlp = NLP()

@app.route("/api/v1/question", methods=["POST"])
def command():
        # Proccess question 
        data = request.json
        answer = nlp.get_answer(data['input']["question"])
        error_code = 0
        error_message = "Successful."

        if not answer:
            error_code = 500
            error_message = "Internal server error."

        data = {
            "error_code":error_code,
            "error_message":error_message,
            "data":{
                "answer": answer
            }
        }
        return jsonify(data)

