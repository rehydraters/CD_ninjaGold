from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.yourgold = 0

def generate_gold(loc):
    newgold = 0
    winlose = 0
    import random
    import datetime
    if loc == "farm":
        newgold = random.randrange(10,21)
        session['yourgold'] = session['yourgold'] + newgold
        session['activity'].append('Earned ' + str(newgold) + ' golds from the farm! (' + datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p)"))
    elif loc == "cave":
        newgold = random.randrange(5,11)
        session['yourgold'] = session['yourgold'] + newgold
        session['activity'].append('Earned ' + str(newgold) + ' golds from the cave! (' + datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p)"))
    elif loc == "house":
        newgold = random.randrange(2,6)
        session['yourgold'] = session['yourgold'] + newgold
        session['activity'].append('Earned ' + str(newgold) + ' golds from the house! (' + datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p)"))
    elif loc == "casino":
        winlose = random.randrange(1,3)
        if winlose == 1:
            newgold = random.randrange(0,51)
            session['yourgold'] = session['yourgold'] + newgold
            session['activity'].append('Earned ' + str(newgold) + ' golds from the casino! (' + datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p)"))
        else:
            newgold = random.randrange(10,21)
            session['yourgold'] = session['yourgold'] - newgold
            session['activity'].append('Entered a casino and lost ' + str(newgold) + ' golds.. Ouch.. (' + datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p)"))

@app.route('/')
def index():
    if app.yourgold == 0:
        session['yourgold'] = 0
        session['activity'] = []
        app.yourgold = -1

    yourgold = session['yourgold']
    activity = session['activity']
    return render_template('index.html', yourgold = yourgold, activity = activity)

@app.route('/process_money', methods = ['POST'])
def process_money():
    your_location = request.form.get('building')
    yourgold = session['yourgold']
    generate_gold(your_location)

    return redirect('/')

app.run(debug=True)