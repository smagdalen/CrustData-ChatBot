from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

static_answers = {
    "How do I search for people given their current title, current company \
    and location?": "You can use api.crustdata.com/screener/person/search "
    "endpoint. Here's an example: ...", "What is the standard for region values?":
    "You can refer to this list: https://crustdata-docs-region-json.s3.us-east \
    -2.amazon.aws.com/updated_regions.json"
}

@app.route("/")

def index():
    return render_template('chatbot.html')

@app.route("/get", methods=["POST"])

def chat():
    user_msg = request.form.get["msg"].strip()
    response = static_answers.get(user_msg, "I'm sorry, I don't have an answer for this question.")
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)