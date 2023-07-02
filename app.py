import os
import json
import openai
from flask import Flask, request, render_template
from answers_functionality import answers


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

f = open('myfile.json', encoding='UTF-8')
data = json.load(f)


@app.route("/", methods=["GET", "POST"])
def home():
    """Main module"""
    answers_str = ''
    paragraph = data['paragraph']
    if request.method == "POST":
        question = request.form["question"]
        response = answers(
                        examples = data['examples'],
                        question = question,
                        examples_context = data['examples_context'],
                        documents = data['documents'],
                        model = "davinci",
                        search_model = "ada",
                        alternative_question = "different test",
                        max_tokens=16,
                        stop=["\n\n"],
                    )
        answers_str = response['answers'][0]
    return render_template("index.html",
                           title="Hello",
                           paragraph=paragraph,
                           answers_str=answers_str)


if __name__ == "__main__":
    app.run()