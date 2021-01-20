import os
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def get_links(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    print(f'Requests for {url}')
    page = requests.get(url,headers=headers)
    if(page.status_code != 200):
        print(f'Return code from {url} is {page.status_code}')
        return None
    
    soup = BeautifulSoup(page.content, 'html.parser') 
    all_refs = []
    for a in soup.find_all('a', href=True):
        if len(a.contents) >= 1:
            lower_text = str(a.contents[0]).lower()
            if 'print' in lower_text and 'recipe' in lower_text:
                print("Found the URL:", a['href'])
                all_refs.append(a['href'])
    return all_refs

@app.route('/', methods=['GET', 'POST'])
@app.route('/<name>/', methods=['GET', 'POST'])
def index(name=None):
    print(f'Name is {name}')
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            url = request.form['url']
            results = get_links(url)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
    return render_template('index.html', errors=errors, results=results, name=name)


if __name__ == '__main__':
    app.run()