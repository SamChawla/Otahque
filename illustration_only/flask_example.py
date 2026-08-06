# illustration_only/flask_example.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/events/")
def event_list():
    # You bring the ORM, auth, forms, and admin
    return render_template("events/list.html")
