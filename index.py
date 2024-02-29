from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/')
def principal():
    return "Bienvenido al sitio web de Aaron / Suscribete"

@app.route('/contacto')
def contacto():
    return "Aquí podemos ponernos en contacto"
    
    python .\index.py
    
"""
@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes = ("Fortnite", "Halo", "Minecraft", "Terraria",
                    "Left 4 dead 2", "Geometry Dash", "Age Of Empire ll", "Apex Legends")
    return render_template('lenguajes.html', lenguajes=misLenguajes)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True, port=5017)
    
    
    
    
    
    