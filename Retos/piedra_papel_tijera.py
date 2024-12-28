player1 = input('Elige: piedra, papel o tijera: ')
player2 = input('Elige: piedra, papel o tijera: ')

if player1 == player2:
    print('Hay un empate')
elif player1 == 'piedra' and player2 == 'tijera':
    print('La piedra gana a la tijera, jugador 1 gana')
elif player1 == 'papel' and player2 == 'piedra':
    print('El papel gana a la piedra, jugador 1 gana')
elif player1 == 'tijera' and player2 == 'papel':
    print('La tijera gana al papel, jugador 1 gana')
else:
    print(f'{player2} gana a {player1} Jugador 2 gana')