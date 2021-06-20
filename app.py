from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)

@app.route('/')                       
def index():                           
    return  render_template('index.html')

@app.route('/quienes-somos')                       
def quienes():                           
    return  render_template('quienes-somos.html')

@app.route('/proyectos/nuestros-proyectos')                       
def exito():                           
    return  render_template('/proyectos/nuestros-proyectos.html')

@app.route('/proyectos/programacion-plc/plc-br')                       
def plc():                           
    return  render_template('/proyectos/programacion-plc/plc-br.html')

@app.route('/proyectos/scada-web/scada-web-formapol')                       
def scada():                           
    return  render_template('/proyectos/scada-web/scada-web-formapol.html')
@app.route('/proyectos/desarrollo-web/paginas-web')                       
def paginas():                           
    return  render_template('/proyectos/desarrollo-web/paginas-web.html')

@app.route('/proyectos/monitoreo/redes-electricas-potencia')                       
def monitoreo():                           
    return  render_template('/proyectos/monitoreo/redes-electricas-potencia.html')

@app.route('/contacto')                       
def formulario():                           
    return  render_template('contacto.html')

@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5100, debug=True)