from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@app.route('/streszczenie', methods=['POST'])
def about():
    return render_template('streszczenie.html')

if __name__ == '__main__':
    app.run(debug=True)
