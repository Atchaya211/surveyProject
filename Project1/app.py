from flask import Flask, render_template, redirect, url_for, request
from flask import app
app = Flask(__name__)


# Route for handling the login page logic
@app.route('/login', methods=['get', 'post'])
def login():
    error = None
    if request.method == 'post':
        if request.form['mailId'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            return redirect(url_for('home'))
        else:
            return redirect(url_for("/Project1/templates/home"))
    return render_template('index.html', error=error)



if __name__ == "__main__":
    app.run(debug=True)