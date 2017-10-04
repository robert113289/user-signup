from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    
    error = request.args.get("error")

    return render_template('index.html',title="User Sign up",error=error)

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']

    err = "ON" 
    if err == "ON":
        error = "oops the ship has sunk"
        return redirect("/?error=" + error)


    return render_template('welcome.html',title="Welcome",username=username,)


app.run()