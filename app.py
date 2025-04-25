from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<param>')
def list_prof(param):
    professions = [
        "инженер-исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астротеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов"
    ]
    app.logger.info(f"Получен запрос на /list_prof/{param}")
    if param == 'ol':
        return render_template('listl.html', typel='ol', profes=professions)
    elif param == 'ul':
        return render_template('listl.html', typel='ul', profes=professions)
    else:
        return "Ошибка: используйте /list_prof/ol или /list_prof/ul", 404


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/distribution')
def distribution():
    astronauts = ['Иванов', 'Петров', 'Сидоров']
    return render_template('distribution.html', astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=False)
