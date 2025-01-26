from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def generar_pregunta():
    """
    Genera una pregunta matemática aleatoria y devuelve la pregunta como texto y su respuesta correcta.
    """
    operadores = ['+', '-', '*', '/']
    operador = random.choice(operadores)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Asegurarse de que no haya división por cero y que la división sea exacta
    if operador == '/':
        num1 = num1 * num2  # Garantiza una división sin decimales

    # Crear la pregunta y calcular la respuesta correcta
    pregunta = f"{num1} {operador} {num2}"
    respuesta_correcta = round(eval(pregunta), 2)

    return pregunta, respuesta_correcta

@app.route('/')
def index():
    return render_template('index.html')  # HTML file to display the game

@app.route('/pregunta', methods=['GET'])
def pregunta():
    """
    Endpoint para generar una pregunta matemática.
    """
    pregunta, respuesta_correcta = generar_pregunta()
    return jsonify({'pregunta': pregunta, 'respuesta_correcta': respuesta_correcta})

@app.route('/verificar', methods=['POST'])
def verificar():
    """
    Endpoint para verificar la respuesta enviada por el usuario.
    """
    data = request.json
    respuesta_usuario = float(data.get('respuesta_usuario'))
    respuesta_correcta = float(data.get('respuesta_correcta'))

    es_correcta = respuesta_usuario == respuesta_correcta
    return jsonify({'es_correcta': es_correcta})

if __name__ == '__main__':
    app.run(debug=True)
