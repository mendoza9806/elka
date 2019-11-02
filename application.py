from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods= ['GET', 'POST'])

def principal():

 return render_template("index.html")

@app.route("/electronica")

def electronica():
    return render_template("electronica.html")

@app.route("/digital")

def digital():
    return render_template("digital.html")

@app.route("/potencia")

def potencia():
    return render_template("potencia.html")

@app.route("/analogica")

def analogica():
    return render_template("analogica.html")

@app.route("/electricidad")

def electricidad():
    return render_template("electricidad.html")

@app.route("/instalaciones")

def instalaciones():
    return render_template("instalaciones.html")

@app.route("/maquinas")

def maquinas():
    return render_template("maquinas.html")

@app.route("/automatismo")

def automatismo():
    return render_template("automatismo.html")

@app.route("/medicion")

def medicion():
    return render_template("medicion.html")

@app.route("/luminotecnia")

def luminotecnia():
    return render_template("luminotecnia.html")

@app.route("/electrotecnia")

def electrotecnia():
    return render_template("electrotecnia.html")

@app.route("/nosotros")

def nosotros():
    return render_template("nosotros.html")



if __name__ == "__main__":
  app.run(debug=True)