from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        link = request.form.get('link')  # Użyj get() dla bezpieczeństwa
        knowledge = request.form.get('poziom-wiedzy')
        title= "Sztywny tytuł artykułu"
        test_object = "Sztywny test_object"
        experiment_goal = "Sztywny cel eksperymentu"
        experiment_group_kind = "Sztywny rodzaj grupy eksperymentalnej"

        # Zwracamy szablon streszczenie.html, przekazując zmienne
        return render_template('streszczenie.html', link=link, knowledge=knowledge, title=title, test_object=test_object, experiment_goal=experiment_goal, experiment_group_kind=experiment_group_kind)

    # Przy metodzie GET wyświetlaj index.html
    return render_template('index.html')

@app.route('/streszczenie', methods=['POST'])
def about():
    return render_template('streszczenie.html')

if __name__ == '__main__':
    app.run(debug=True)
