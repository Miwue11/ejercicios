def make_list_of_free_fields(board):
	free = []	# la lista esta vacía inicialmente
	for row in range(3): # itera a través de las filas
		for col in range(3): # iitera a través de las columnas
			if board[row][col] not in ['O','X']: # ¿Está la celda libre?
				free.append((row,col)) # si, agrega una nueva tupla a la lista
	return free