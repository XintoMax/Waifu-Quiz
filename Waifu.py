from flask import *

app = Flask(__name__)
Albedo = 0
Asuna = 0
Aqua = 0
Raphtalia = 0
Sizilien = 0


def score():
    print("Albedo:", Albedo)
    print("Asuna:", Asuna)
    print("Aqua:", Aqua)
    print("Raphtalia:", Raphtalia)
    print("Sizilien:", Sizilien)
    print("--------------------")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/question=1')
def question1():
    return render_template("question1.html")


@app.route('/question=2')
def question2():
    q1_Input = request.args.get("group1")
    global Albedo
    global Asuna
    global Aqua
    global Raphtalia
    global Sizilien
    if q1_Input == 'input1':
        Albedo += 1
    elif q1_Input == 'input2':
        Asuna += 1
    elif q1_Input == 'input3':
        Aqua += 1
    elif q1_Input == 'input4':
        Sizilien += 1
    elif q1_Input == 'input5':
        Raphtalia += 1
    print(score())
    return render_template("question2.html")


@app.route('/question=3')
def question3():
    q2_Input = request.args.get("group2")
    global Albedo
    global Asuna
    global Aqua
    global Raphtalia
    global Sizilien
    if q2_Input == 'input1':
        Albedo += 1
    elif q2_Input == 'input2':
        Sizilien += 1
    elif q2_Input == 'input3':
        Raphtalia += 1
    elif q2_Input == 'input4':
        Aqua += 1
    elif q2_Input == 'input5':
        Asuna += 1
    print(score())
    return render_template("question3.html")


@app.route('/question=4')
def question4():
    q3_Input = request.args.get("group3")
    global Albedo
    global Asuna
    global Aqua
    global Raphtalia
    global Sizilien
    if q3_Input == 'input1':
        Raphtalia += 1
    elif q3_Input == 'input2':
        Albedo += 1
    elif q3_Input == 'input3':
        Asuna += 1
    elif q3_Input == 'input4':
        Aqua += 1
    elif q3_Input == 'input5':
        Sizilien += 1
    print(score())
    return render_template("question4.html")


if __name__ == "__main__":
    app.run()
