from flask import Flask, request, render_template
from scrape import find_links 

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('myform.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    target_url = request.form['url']
    links = find_links(text, target_url)
    # processed_text = text.upper()
    # return processed_text
    return render_template('results.html', links=links, target_url=target_url, text=text)


@app.route('/results.html')
def results():
    return
