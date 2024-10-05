from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        link = request.form.get('link')  # Użyj get() dla bezpieczeństwa
        knowledge = request.form.get('poziom-wiedzy')
        title= "Sztywny tytuł artykułu"
        # Zwracamy szablon streszczenie.html, przekazując zmienne
        return render_template('streszczenie.html', link=link, knowledge=knowledge, title=title)

    # Przy metodzie GET wyświetlaj index.html
    return render_template('index.html')

@app.route('/streszczenie', methods=['POST'])
def about():
    return render_template('streszczenie.html')

if __name__ == '__main__':
    app.run(debug=True)
