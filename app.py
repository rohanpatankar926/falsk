from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/something",methods=["GET"])
def somethingh():
    return "<h1>Hello world</h1>"

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/something2")
def predict():
    return "something"

@app.route("/predict",methods=["POST"])
def main():
    x=[int(x) for x in request.form.values]

if __name__=="__main__":
    app.run(debug=True,host="192.168.121.124",port=5000)