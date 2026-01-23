from flask import Flask
from flask import Flask, jsonify


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/funcionando")
def home():
    return "<h3>Flask está funcionando!</h3>"

@app.route("/api/saudacao")
def saudacao():
    return jsonify(mensagem="Olá, Patrícia! Sua API está funcionando")


if __name__ == "__main__":
    app.run(debug=True)
