print("                                      Bienvenido a nuestro juego de piedra papel y tijera                   ")
print("                                         En esta versiñon jugaras 5 rodas contra la PC💻                   ")
print("                                              Necesitas 150 puntos o mas para ganar                       ")
print("                                                          Suerte 😉                                  ")

import random
def obtener_numero_rondas():
    return 5 #se estable el numero de rondas 

def obtener_nivel_dificultad():
    while True:
        nivel = input("         Seleccione el nivel de dificultad 😏 (1 para facil😁, 2 para intermedio😨, 3 para difícil☠️): ").lower()
        if nivel in ["1", "2", "3"]:
            return nivel
        else:
            print("por favor, seleccione un vivel de dificultad válido")

def obtener_nombre_jugador():
    nombre = input("ingrese su nombre ")
    return nombre

def jugar_ronda_():
    opciones = {1: "piedra", 2: "papel", 3: "tijeras"}

    eleccion_jugador = obtener_eleccion_jugador(opciones)
    eleccion_computadora = obtener_eleccion_computadora(opciones)

    resultado = determinar_ganador(eleccion_jugador, eleccion_computadora)

    print(f"\nTú eliste: {eleccion_jugador}")
    print(f"La computadora eligio: {eleccion_computadora}")
    print(f"Resultado: {resultado}")

    return resultado 

def obtener_eleccion_jugador(opciones):
    print("Elije 1 para piedra, 2 para papel, 3 para tijeras")

    for key, value in opciones.items():
        print(f"{key}: {value}")

    while True:
        try:
            eleccion_numero = int(input())
            if eleccion_numero in opciones:
                return opciones[eleccion_numero]
            else:
                print("Numero no válido. Intenta nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido")

def obtener_eleccion_computadora(opciones):
    return opciones[random.randint(1, 3)]

def determinar_ganador(eleccion_jugador, eleccion_computadora):
    if eleccion_jugador == eleccion_computadora:
        return "Esto es un empate 🤝"
    elif (
         (eleccion_jugador ==  "piedra" and eleccion_computadora == "tijera") or
         (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or
         (eleccion_jugador == "tijeras" and eleccion_computadora == "papel")
    ):
        return "¡Felicidades, Ganaste😎"
    else:
        return "La computadora gana.🥲"

def actulizar_puntaje(resultado, puntaje):
    if resultado == "¡Felicidades, Ganaste😎":
        return puntaje + 100
    elif resultado == "Esto es un empate 🤝":
        return puntaje + 50
    elif resultado == "La computadora gana.🥲":
        return puntaje - 15
    
    else:
        return puntaje

def main():
    num_rondas = obtener_numero_rondas()
    nivel_dificultad = obtener_nivel_dificultad()
    nombre_jugador = obtener_nombre_jugador()

    puntaje = 0
    historial_puntaje = []

    for _ in range(num_rondas):
        print(f"\nRonda {_ + 1}")
        resultado_ronda = jugar_ronda_()

        puntaje = actulizar_puntaje(resultado_ronda, puntaje)
        historial_puntaje.append(puntaje)

    print("\n--- Resultado Final ---")
    print(f"{nombre_jugador}, tu puntaje es: {puntaje}")
    print(f"Historial de puntajes: {historial_puntaje}" )

if __name__ == "__main__":
    main()