from flask import Flask, app, redirect, render_template, request, url_for
import plotly.graph_objects as go
import json
import plotly
import pandas as pd
import numpy as np
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

@app.route("/display", methods=['get','post'])
def display():
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    z = z_data.values
    sh_0, sh_1 = z.shape
    x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                    width=500, height=500,
                    margin=dict(l=65, r=50, b=65, t=90))
    graphJson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('display.html', graphJson=graphJson)


@app.route("/input", methods=['get','post'])
def input():
    error = None
    return render_template('input.html', error=error)







if __name__ == "__main__":
    app.run(debug=True)