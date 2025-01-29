import turtle
import time
import random

# Screen configuration
wn = turtle.Screen()
wn.setup(width=600, height=600) 
wn.bgcolor("grey")

# Text configuration
texto = turtle.Turtle()
texto.penup()
texto.goto(0,0)
texto.hideturtle()

# Bucle 
while True:
    action = wn.textinput("Input", "Introduce qué quieres hacer: ")  #
    if action:  
        texto.write(f"Has introducido: {action}")
        # We need a random number to select a rock,scissors and papaer
        
    else:
        break # Exit the game if you say Cancel
    
    time.sleep(1) # Stop one second
