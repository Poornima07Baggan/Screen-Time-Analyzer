from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def create_graph(mobile, laptop, tv):

    devices = ["Mobile", "Laptop", "TV"]
    hours = [mobile, laptop, tv]

    plt.bar(devices, hours)

    plt.title("Daily Screen Time")
    plt.xlabel("Device")
    plt.ylabel("Hours")

    if not os.path.exists("static"):
        os.makedirs("static")

    plt.savefig("static/graph.png")
    plt.close()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    mobile = int(request.form['mobile'])
    laptop = int(request.form['laptop'])
    tv = int(request.form['tv'])

    total = mobile + laptop + tv

    create_graph(mobile, laptop, tv)

    if total > 8:
        result = "High Screen Time ⚠️"
    else:
        result = "Normal Screen Time ✅"

    return render_template("result.html", total=total, result=result)


if __name__ == "__main__":
    app.run(debug=True)