from flask import Flask,request
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/chatgpt')
def chatgpt():
    args = request.args
    message =args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']


@app.route('/generate_code')
def generate_code():
    # get user input
    language = request.args.get('language')
    content = request.args.get('content')
    
    # create code using OpenAI
    completion = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Generate {language} code: {content}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # return generated code
    return completion.choices[0].text
