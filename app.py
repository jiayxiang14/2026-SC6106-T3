from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    return(render_template("main.html"))

@app.route("/transferMoney",methods=["GET","POST"])
def transferMoney():
    return(render_template("transferMoney.html"))

@app.route("/depositMoney",methods=["GET","POST"])
def depositMoney():
    return(render_template("depositMoney.html"))

@app.route("/storeMessage", methods=["GET","POST"])
def storeMessage():
    return render_template("storeMsg.html")

@app.route("/logs", methods=["GET","POST"])
def logs():
    return render_template("logs.html")

@app.route("/deleteLogs", methods=["POST"])
def deleteLogs():
    return render_template("deletelogs.html")

if __name__ == "__main__":
        app.run()