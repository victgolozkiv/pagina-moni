from flask import Flask, render_template

# Creamos la app
app = Flask(__name__)

# Ruta principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Ejecutamos la app
if __name__ == "__main__":
    app.run(debug=True)
