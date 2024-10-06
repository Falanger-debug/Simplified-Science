from flask import Flask, render_template, request, jsonify

import seleniumm as sele
import appAPI
import keywords as keyW
most_common_words = []

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        link = request.form.get('link')  # Użyj get() dla bezpieczeństwa
        knowledge = request.form.get('poziom-wiedzy')

        title = "Tytuł na sztywno"
        test_object = "Objekt testowy na sztywno"
        experiment_goal = "Experimental goal na sztywno"
        experiment_group_kind = "Experiment group kind"
        experiment_environment = "Experiment Environment"
        experiment_method = "Experiment method"
        object_effect = "Object effect"
        experiment_result = "Experiment result"
        experiment_conclusions = "Experiment conclusions"

        title = appAPI.getTitle(link)
        test_object = appAPI.getTestObject(link)
        most_common_words = keyW.analyze_text_frequency(sele.unique_text)
        #experiment_goal = appAPI.getExperimentGoal(link)
        #experiment_group_kind = appAPI.getExperimentalGroupKind(link)
        #experiment_environment = appAPI.ExperimentEnvironment(link)
        #experiment_method = appAPI.getExperimentMethod(link)
        #object_effect = appAPI.getObjectEffect(link)
        #experiment_result = appAPI.getExperimentResult(link)
        #experiment_conclusions = appAPI.getExperimentConclucions(link)

        # Zwracamy szablon streszczenie.html, przekazując zmienne
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
    return render_template('streszczenie.html')

@app.route('/chat_message', methods=['POST'])
def chat_message():
    message = request.form['message']
    response = appAPI.askChat(message)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
