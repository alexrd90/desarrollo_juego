from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido"

@app.route('/hola')
def hola():
    alex = {}
    alex['Nombre']='Alex'
    alex['Edad']=25
    alex['Sexo']='Masculino'
    alex['Ocupacion']='Estudiante'
    alex['Hobbies']=['Leer','Cine','Deportes']

    return render_template('hola.html',alex=alex)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)