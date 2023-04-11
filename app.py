from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', display_stuff_please="hidden")

@app.route('/summarize', methods=['POST'])
def summarize():
    article = request.form['article']
    print(article)
    api_key = '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'
    # Send a request to ChatGPT's API and get the summarized text
    URL = "https://api.openai.com/v1/chat/completions"

    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f'summarize the following article:{article}'}],
    "temperature" : 1.0,
    "top_p":1.0,
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    }

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    display_stuff_please = "visible"

    response = requests.post(URL, headers=headers, json=payload, stream=False)
    summary = response.json()['choices'][0]['message']['content']
    return render_template('index.html', summary=summary, display_stuff_please=display_stuff_please)


if __name__ == '__main__':
    app.run(debug=True)


