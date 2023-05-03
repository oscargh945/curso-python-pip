import random

print('Bienvenido al juego clasico de piedra, papel o tijera')
print('Creo que no tendria por que recordarte las reglas del juego, ya que alguna vez todos hemos jugado este juego, solo te dire que te vas a enfrentar con la computadora.')
print('Sin mas que decir te deseo mucha suerte.')

def choose_optiones():
    optiones = ("piedra", "papel", "tijera")
    jugador = input(("¿piedra, papel o tijera? => "))
    jugador = jugador.lower()

    if not jugador in optiones:
        print("ingresa una opcion valida por favor!")
        #continue
        return None, None

    pc = random.choice(optiones)

    print("El jugador eligio ", jugador)
    print("La pc eligio ", pc)
    return jugador, pc

def check_rules(jugador, pc, jugador_wins, pc_wins):
    if jugador == pc:
        print("Empate!")

    elif (
        (jugador == "piedra" and pc == "tijera")
        or (jugador == "papel" and pc == "piedra")
        or (jugador == "tijera" and pc == "papel")
    ):
        print("Ganaste!")
        jugador_wins += 1

    else:
        print("Perdiste!")
        pc_wins += 1
    return jugador_wins, pc_wins    

def run_game():
    jugador_wins = 0
    pc_wins = 0
    rounds = 1

    while True:
        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)

        rounds += 1

        jugador, pc = choose_optiones()
        jugador_wins, pc_wins = check_rules(jugador, pc, jugador_wins, pc_wins)

        if jugador_wins == 3:
            print('El ganador es el jugador y gano con ', jugador_wins, ' puntos')
            break
        print('el jugador lleva = ', jugador_wins, ' puntos')

        if pc_wins == 3:
            print('El ganador es la pc y gano con ', pc_wins, ' puntos')
            break
        print('la pc lleva = ', pc_wins, ' puntos')

run_game()