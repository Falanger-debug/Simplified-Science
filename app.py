from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        link = request.form.get('link')  # Użyj get() dla bezpieczeństwa
        return render_template('streszczenie.html', link=link)

    return render_template('index.html')  # Renderuj index.html przy GET


@app.route('/streszczenie', methods=['POST'])
def about():
    return render_template('streszczenie.html')

if __name__ == '__main__':
    app.run(debug=True)
