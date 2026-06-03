from flask import Flask, request, render_template, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "mi_clave_secreta_123"

USUARIO_CORRECTO = "odin"
PASSWORD_CORRECTO = "1234"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    mensaje = ""

    if "intentos" not in session:
        session["intentos"] = 0

    restantes = 3 - session["intentos"]

    if session["intentos"] >= 3:
        return redirect(url_for("bloqueado"))

    if request.method == "POST":

        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTO:

            session["intentos"] = 0
            return redirect(url_for("bienvenida"))

        else:

            session["intentos"] += 1
            restantes = 3 - session["intentos"]
            mensaje = "Usuario o contraseña incorrectos"

            if session["intentos"] >= 3:
                return redirect(url_for("bloqueado"))

    return render_template("login.html", mensaje=mensaje, restantes=restantes)


@app.route("/bienvenida")
def bienvenida():
    return render_template("bienvenida.html")


@app.route("/bloqueado")
def bloqueado():
    return render_template("bloqueado.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)