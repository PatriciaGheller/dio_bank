from flask import Flask
from flask import Flask
from flask import url_for, request


app = Flask(__name__)

@app.route("/funcionando/<usuario>/<int:idade>/<float:altura>")
def home(usuario, idade, altura):
    return {"Usuário": usuario, 
            "Idade": idade, 
            "Altura": altura, 
            }

@app.route("/api/saudacao")
def saudacao():
    return {"mensagem": "Olá, Patrícia! Sua API está funcionando"}

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
    
    
 
    
    
