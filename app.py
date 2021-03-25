from flask import Flask, render_template,redirect,url_for,jsonify,json
app = Flask(__name__)
@app.route('/')                       
def index():                           
    return  render_template('index.html')

@app.route('/quienes-somos')                       
def quienes():                           
    return  render_template('quienes-somos.html')

@app.route('/proyectoplc')                       
def plc():                           
    return  render_template('proyectoplc.html')

@app.route('/Scadaweb')                       
def scada():                           
    return  render_template('Scadaweb.html')

@app.route('/contacto')                       
def formulario():                           
    return  render_template('contacto.html')


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5100, debug=True)