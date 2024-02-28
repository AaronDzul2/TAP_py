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
def lenguajes():
    return render_template('lenguajes.html')


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

#fdfdfdffdDSDSD

if __name__=='__main__':
    app.run(debug=True)
    
    