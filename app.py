from flask import Flask, request, render_template
from scrape import find_links, retrieve_text
from markupsafe import Markup, escape


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('myform.html')

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    links_to_check = []
    text = request.form['text']
    target_url = request.form['url']
    links = find_links(text, target_url)
    for link in links:
        links_to_check.append((link.get('href')))
    art_text = retrieve_text(links_to_check)
    
    return render_template('results.html', links=links, art_text=art_text)


@app.route('/results.html')
def results():
    return
