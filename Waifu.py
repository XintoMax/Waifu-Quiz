from flask import *

app = Flask(__name__)
Albedo = 0
Asuna = 0
Aqua = 0
Raphtalia = 0
Sizilien = 0
waifu_name = dict()


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
        Aqua += 2
    elif q1_Input == 'input4':
        Sizilien += 1
    elif q1_Input == 'input5':
        Raphtalia += 1
        Albedo += 1
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
        Albedo += 1
    elif q2_Input == 'input3':
        Raphtalia += 2
    elif q2_Input == 'input4':
        Aqua += 1
    elif q2_Input == 'input5':
        Asuna += 1
        Raphtalia += 1
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
        Aqua += 1
    elif q3_Input == 'input4':
        Asuna += 1
    elif q3_Input == 'input5':
        Sizilien += 1
    print(score())
    return render_template("question4.html")


@app.route('/question=5')
def question5():
    q4_Input = request.args.get("group4")
    global Albedo
    global Asuna
    global Aqua
    global Raphtalia
    global Sizilien
    if q4_Input == 'input1':
        Aqua += 1
    elif q4_Input == 'input2':
        Asuna += 1
        Sizilien += 1
        Raphtalia += 1
    elif q4_Input == 'input3':
        Sizilien += 2
    elif q4_Input == 'input4':
        Raphtalia += 2
    elif q4_Input == 'input5':
        Albedo += 1
    print(score())
    return render_template("question5.html")


@app.route('/question=6')
def question6():
    q5_Input = request.args.get("group5")
    global Albedo
    global Asuna
    global Aqua
    global Raphtalia
    global Sizilien
    if q5_Input == 'input1':
        Asuna += 1
    elif q5_Input == 'input2':
        Albedo += 1
    elif q5_Input == 'input3':
        Raphtalia += 1
    elif q5_Input == 'input4':
        Aqua += 1
    elif q5_Input == 'input5':
        Sizilien += 1
    print(score())
    return render_template("question6.html")


@app.route('/question=7')
def question7():
    q6_Input = request.args.get("group6")
    global Albedo
    global Asuna
    global Aqua
    global Raphtalia
    global Sizilien
    if q6_Input == 'input1':
        Aqua += 1
    elif q6_Input == 'input2':
        Albedo += 2
    elif q6_Input == 'input3':
        Asuna += 1
    elif q6_Input == 'input4':
        Sizilien += 1
        Albedo += 1
    elif q6_Input == 'input5':
        Raphtalia += 1
    print(score())
    return render_template("question7.html")


@app.route('/result')
def result():
    q7_Input = request.args.get("group7")
    global Albedo
    global Asuna
    global Aqua
    global Raphtalia
    global Sizilien
    if q7_Input == 'input1':
        Aqua += 1
    elif q7_Input == 'input2':
        Raphtalia += 1
    elif q7_Input == 'input3':
        Sizilien += 1
    elif q7_Input == 'input4':
        Albedo += 1
    elif q7_Input == 'input5':
        Asuna += 1
    print(score())
    waifu_name["Albedo"] = Albedo
    waifu_name["Asuna"] = Asuna
    waifu_name["Aqua"] = Aqua
    waifu_name["Raphtalia"] = Raphtalia
    waifu_name["Sizilien"] = Sizilien
    max_name = (max(waifu_name, key=waifu_name.get))
    return render_template("result.html", waifu=max_name)


if __name__ == "__main__":
    app.run(debug=True, port=1337)
