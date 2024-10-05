from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    link = None  # Inicjalizujemy link jako None
    if request.method == 'POST':
        link = request.form['link']  # Odbieramy wartość z formularza
        return render_template('streszczenie.html')  # Przekazujemy link do szablonu  
        
    return render_template('index.html')  # Przekazujemy link do szablonu  

@app.route('/streszczenie', methods=['POST'])
def about():
    return render_template('streszczenie.html')

if __name__ == '__main__':
    app.run(debug=True)
