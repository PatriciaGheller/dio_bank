from flask import Flask
from flask import Flask, jsonify
from flask import url_for, request
from flask import jsonify

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/funcionando/<usuario>/<int:idade>/<float:altura>")
def home(usuario, idade, altura):
    print(idade)
    print(f' tipo da variável idade: {type(idade)}')
    print(f' tipo da variável usuário: {type(usuario)}')
    print(f' tipo da variável altura: {type(altura)}')
    return f"<h1>Olá usuário: {usuario.upper()}! O Flask está funcionando!</h1>"

@app.route("/api/saudacao")
def saudacao():
    return jsonify(mensagem="Olá, Patrícia! Sua API está funcionando")

@app.route("/projects/")
def projects():
    return "<h1>Meus projetos</h1>"

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return 'This is a GET request'
    else:
        return 'This is a POST request'
        
@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"

if __name__ == "__main__":
    app.run(debug=True)
    
with app.test_request_context():
    print(url_for("home", usuario="Patrícia", idade=30, altura=1.65))
    print(url_for("saudacao"))
    print(url_for("projects"))
    print(url_for("about", next="/projects/"))
    print(url_for("profile", username="Patrícia"))
    
    
 
    
    
