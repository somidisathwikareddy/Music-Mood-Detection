from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_link', methods=['POST'])
def process_link():
    song_link = request.form['song_link']
    
    # Send the song link to Jupyter Notebook (replace with your logic)
    jupyter_url = 'http://localhost:8100'  # Replace with your Jupyter Notebook URL
    response = requests.post(f'{jupyter_url}/your_endpoint', data={'song_link': song_link})
    
    # Process the response from Jupyter Notebook (replace with your logic)
    result = response.text
    result_dict = json.loads(result)
    
    return render_template('result.html', result=result_dict)

if __name__ == '__main__':
    app.run(debug=True, port=7901)
