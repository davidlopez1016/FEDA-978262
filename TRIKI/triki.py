# Combinaciones de juego 
# X = Movimientos jugador uno
# O = Movimientos jugador dos
# _ = Masilla en blanco, no hay movimientos.

board_no_winner = [["X", "O", "X"], ["O", "O", "X"], ["X", "X", "O"]]
board_winner_rows = [["X", "X", "X"], ["O", "O", "_"], ["_", "_", "_"]]
board_winner_columns = [["O", "X", "_"], ["O", "X", "_"], ["O", "X", "_"]]
board_winner_diagonal = [["X", "O", "_"], ["_", "X", "O"], ["_", "_", "X"]]
board_tie = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
board_in_progress = [["X", "O", "X"], ["_", "O", "_"], ["O", "X", "_"]]



def verify_winner(table):
    if table is None:
        return "table"
    
    #filas
    for fila in table:
        if fila[0] == fila[1] == fila[2] != "_":
            return f"Ganador: {fila[0]}"

    # columnas
    for col in range(3):
        if table[0][col] == table[1][col] == table[2][col] != "_":
            return f"Ganador: {table[0][col]}"

    # diagonales
    if table[0][0] == table[1][1] == table[2][2] != "_":
        return f"Ganador: {table[0][0]}"
    if table[0][2] == table[1][1] == [2][0] != "_":
        return f"Ganador: {table[0][2]}"
    
    
    for fila in table:
        if "_" in fila:
            return " juego en proceso "
    
   
    return "Empate"




print(verify_winner(board_no_winner))
print(verify_winner(board_winner_rows))
print(verify_winner(board_winner_columns))
print(verify_winner(board_winner_diagonal))


print(verify_winner(None))

