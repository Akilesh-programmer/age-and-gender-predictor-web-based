import requests 
from flask import Flask, render_template

def get_gender(name_):
    name = str(name_)
    url = "https://api.genderize.io?name=" + name
    response = requests.get(url)
    data = response.json()
    return data["gender"]

def get_age(name_):
    name = str(name_)
    url = "https://api.agify.io?name=" + name
    response = requests.get(url)
    data = response.json()
    return data["age"]


app = Flask(__name__)

@app.route("/")
def greet():
    return "<h1>Welcome</h1>"
    
@app.route("/guess/<some_name>")
def age_gender_guess(some_name):
    age = get_age(some_name)
    gender = get_gender(some_name)
    return f"<h1>Hey {some_name},</h1> \
        <h2>I think you are {gender},</h2> \
        <h3>And maybe {age} years old."


if __name__ == "__main__":
    app.run(debug=True)

