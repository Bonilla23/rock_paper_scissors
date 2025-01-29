import turtle
import time

# Configurar la ventana
wn = turtle.Screen()
wn.setup(width=600, height=600)  # Tamaño correcto
wn.bgcolor("grey")

# Crear el texto
texto = turtle.Turtle()
texto.penup()
texto.goto(0,0)

# Bucle del juego
while True:
    action = wn.textinput("Input", "Introduce qué quieres hacer: ")  # Pedir entrada al usuario
    if action:  # Si el usuario introduce algo
        texto.write(f"Has introducido: {action}")
    
    time.sleep(1)  # Pequeña pausa para evitar saturación
