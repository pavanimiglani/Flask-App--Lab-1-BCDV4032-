from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif')
    cat_gif_url = response.json()[0]['url'] if response.status_code == 200 else None
    return render_template('index.html', cat_gif_url=cat_gif_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
