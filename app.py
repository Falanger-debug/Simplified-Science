from flask import Flask, render_template, request, jsonify

import appAPI

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        link = request.form.get('link')  # Użyj get() dla bezpieczeństwa
        knowledge = request.form.get('poziom-wiedzy')
        title = "Sztywny tytuł artykułu"
        test_object = "Sztywny test_object"
        experiment_goal = "Sztywny cel eksperymentu"
        experiment_group_kind = "Sztywny rodzaj grupy eksperymentalnej"
        experiment_environment = "Sztywne środowisko eksperymentu"
        experiment_method = "Sztywna metoda eksperymentu"
        object_effect = "Sztywny efekt obiektu"
        experiment_result = "Sztywny wynik eksperymentu"
        experiment_conclusions = "Sztywne wnioski z eksperymentu"

        #title = appAPI.getTitle(link)
        #test_object = appAPI.getTestObject(link)
        #experiment_goal = appAPI.getExperimentGoal(link)
        #experiment_group_kind = appAPI.getExperimentGroupKind(link)
        #experiment_goal = appAPI.getExperimentGoal(link)
        #experiment_environment = appAPI.getExperimentEnvironment(link)

        # Zwracamy szablon streszczenie.html, przekazując zmienne
        return render_template('1.html')
        return render_template('streszczenie.html', link=link, knowledge=knowledge, title=title,
                               test_object=test_object, experiment_goal=experiment_goal,
                               experiment_group_kind=experiment_group_kind,
                               experiment_environment=experiment_environment,
                               experiment_method=experiment_method,
                               object_effect=object_effect,
                               experiment_result=experiment_result,
                               experiment_conclusions=experiment_conclusions)

    # Przy metodzie GET wyświetlaj index.html
    return render_template('index.html')

@app.route('/streszczenie', methods=['POST'])
def about():
    return render_template('1.html')

@app.route('/example1', methods=['POST'])
def example1():
    return render_template('1.html')

@app.route('/chat_message', methods=['POST'])
def chat_message():
    #message = request.form['message']
    #response = appAPI.askChat(message)
    #return jsonify({'response': response})
    return jsonify({'response': 'ERROR 500: API DOWN'})

if __name__ == '__main__':
    app.run(debug=True)
