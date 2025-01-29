import turtle
import time
import random

# Create the function
def ganador(action, maquina):
    if action == maquina:
        return "Empate!"
    elif (action == "rock" and maquina == "scissor") or \
         (action == "scissor" and maquina == "paper") or \
         (action == "paper" and maquina == "rock"):
        return "Ganaste!"
    else:
        return "Perdiste!"

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
    action = wn.textinput("Input", "Action: rock | scissor | paper ")  #
    if action:  
        # Only write if you select rock, scissors or paper
        action = action.lower()
        if action == "rock" or action == "scissor" or action == "paper":
            maquina = random.choice(["rock","scissor","paper"])
            # We need a random number to select a rock,scissors and papaer
            resultado = ganador(action,maquina)
            # Mostrar las elecciones y el resultado
            texto.clear()
            texto.write(f"Tú: {action}\nMáquina: {maquina}\n{resultado}", 
            align="center", font=("Arial", 16, "bold"))

            time.sleep(1) # Stop one second
        else:
            texto.write("Opcion no reconocida",align="center", font=("Arial", 16, "bold"))
            time.sleep(1)
            texto.clear()
  
    else:
        break # Exit the game if you say Cancel
    
    time.sleep(1) # Stop one second
