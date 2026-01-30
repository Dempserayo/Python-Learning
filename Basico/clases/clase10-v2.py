#piezas: P para peón, R para torre, N para caballo (knight), B para alfil, Q para reina y K para rey. Las piezas
#Para distinguir entres las fichas blancas y negras sera por minusculas(negras) y mayusculas(blancas).

chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

chess_board[7][1] = 0
chess_board[5][2] = 'N'
print(chess_board)
print(len(chess_board))

# Moveria el caballo a este lugar.
#    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
#    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, "ACA", 0, 0, 0, 0, 0],
#    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
#    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
#]