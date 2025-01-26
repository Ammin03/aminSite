
import random

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

def jugar():
    """
    Función principal del juego. El usuario puede responder preguntas matemáticas hasta que decida salir.
    """
    print("¡Bienvenido al Juego de Operaciones Matemáticas!")
    print("Resuelve las operaciones que se generarán aleatoriamente.")
    print("Escribe 'salir' en cualquier momento para terminar el juego.\n")

    puntuacion = 0
    intentos = 0

    while True:
        # Generar una nueva pregunta
        pregunta, respuesta_correcta = generar_pregunta()

        # Mostrar la pregunta
        print(f"¿Cuánto es {pregunta}?")
        respuesta_usuario = input("Tu respuesta: ")

        # Permitir al usuario salir
        if respuesta_usuario.lower() == 'salir':
            print("\n¡Gracias por jugar!")
            print(f"Tu puntuación final: {puntuacion}/{intentos}")
            break

        try:
            # Convertir la respuesta a número
            respuesta_usuario = float(respuesta_usuario)
        except ValueError:
            print("Por favor, ingresa un número válido.\n")
            continue

        # Comparar la respuesta con la correcta
        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto! 🎉\n")
            puntuacion += 1
        else:
            print(f"Incorrecto. La respuesta era {respuesta_correcta}.\n")

        intentos += 1

if __name__ == "__main__":
    jugar()
