import random

palabras = ['pelota', 'futbol', 'computadora', 'celular', 'cuaderno', 'libro', 'dormitorio', 'cielo', 'estrella', 'estadio']
secreta = random.choice(palabras)
cadena = "-" * len(secreta)
print("Bienvenidos al Juego del Ahorcado")
intentos = 0