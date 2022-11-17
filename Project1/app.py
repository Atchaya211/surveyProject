from flask import Flask, app, redirect, render_template, request, url_for

app = Flask(__name__)


# Route for handling the login page logic
@app.route('/', methods=['get', 'post'])
def login():
    error = None
    if request.method == 'post':
        if request.form['mailId'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            
        else:
            return redirect("/home")
    return render_template('index.html', error=error)


@app.route("/home", methods=['get','post'])
def home():
    error = None
    return render_template('home.html', error=error)







if __name__ == "__main__":
    app.run(debug=True)