from flask import Flask, render_template, request, jsonify

import appAPI

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        link = request.form.get('link')  # Użyj get() dla bezpieczeństwa
        knowledge = request.form.get('poziom-wiedzy')
        title = "Profilowanie transkrypcyjne wątroby myszy biorących udział w misji Rodent Research Reference Mission-1 (RRRM-1)"
        test_object = "Obiektem badań w eksperymencie Rodent Research Reference Mission (RRRM-1) były myszy, w tym 40 samic BALB/cAnNTac w dwóch grupach wiekowych: 20 młodych myszy w wieku 10-12 tygodni oraz 20 starszych myszy w wieku 32 tygodni."
        experiment_goal = "Celem eksperymentu Rodent Research Reference Mission (RRRM-1) było zbadanie wpływu lotu kosmicznego na organizmy myszy, w szczególności w odniesieniu do różnic wynikających z wieku. W tym celu porównywano efekty lotu kosmicznego u młodych (10-12 tygodni) i starszych (32 tygodnie) myszy."
        experiment_group_kind = "Sztywny rodzaj grupy eksperymentalnej"


        title = appAPI.getTitle(link)
        test_object = appAPI.getTestObject(link)
        experiment_goal = appAPI.getExperimentGoal(link)
        #experiment_group_kind = appAPI.getExperimentGroupKind(link)
        #experiment_goal = appAPI.getExperimentGoal(link)
        #experiment_environment = appAPI.getExperimentEnvironment(link)

        # Zwracamy szablon streszczenie.html, przekazując zmienne
        return render_template('streszczenie.html', link=link, knowledge=knowledge, title=title,
                               test_object=test_object, experiment_goal=experiment_goal,
                               #experiment_group_kind=experiment_group_kind,
                               experiment_environment=experiment_environment,
                               experiment_method=experiment_method,
                               object_effect=object_effect,
                               experiment_result=experiment_result,
                               experiment_conclusions=experiment_conclusions)

    # Przy metodzie GET wyświetlaj index.html
    return render_template('index.html')

@app.route('/streszczenie', methods=['POST'])
def about():
    return render_template('streszczenie.html')

@app.route('/chat_message', methods=['POST'])
def chat_message():
    message = request.form['message']
    response = appAPI.askChat(message)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
