from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/juego1')
def juego1():
    return render_template('juego1.html')

@app.route('/juego2')
def juego2():
    return render_template('juego2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)