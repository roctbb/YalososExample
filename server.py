import random
import vk
from config import vk_token
from flask import Flask, render_template, request

app = Flask(__name__)
session = vk.Session(access_token=vk_token)
api = vk.API(session)


@app.route('/search')
def search():
    query = request.args.get('query', '')
    if query == '':
        results = []
    else:
        posts = api.wall.search(domain='baneks', v=5.74, query=query, owners_only=1, count=100)
        results = posts['items']
    return render_template('results.html', results=results)


@app.route('/')
def index():
    return render_template('index.html')




app.run(debug=True, port=8081, host='0.0.0.0')