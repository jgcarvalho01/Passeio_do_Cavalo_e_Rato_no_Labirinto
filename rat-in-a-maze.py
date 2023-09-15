# Programa em Python3 para resolver o problema do Rato em um Labirinto
# usando backtracking (retrocesso).

# Tamanho do labirinto
n = 4

# Uma função de utilidade para verificar se x, y é um índice válido
# para o labirinto N * N.
def isValid(n, maze, x, y, res):
	if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and res[x][y] == 0:
		return True
	return False

# Uma função recursiva de utilidade para resolver o problema do labirinto.
def RatMaze(n, maze, move_x, move_y, x, y, res):
	# Se (x, y) é o objetivo, retorne Verdadeiro (True)
	if x == n-1 and y == n-1:
		return True
	for i in range(4):
		# Gerar o novo valor de x
		x_new = x + move_x[i]

		# Gerar o novo valor de y
		y_new = y + move_y[i]

		# Verificar se maze[x][y] é válido
		if isValid(n, maze, x_new, y_new, res):

			# Marcar x, y como parte do caminho da solução
			res[x_new][y_new] = 1
			if RatMaze(n, maze, move_x, move_y, x_new, y_new, res):
				return True
			res[x_new][y_new] = 0
	return False

def solveMaze(maze):
	# Criar uma lista 2-D de tamanho 4 * 4
	res = [[0 for i in range(n)] for i in range(n)]
	res[0][0] = 1

	# Matriz x para cada direção
	move_x = [-1, 1, 0, 0]

	# Matriz y para cada direção
	move_y = [0, 0, -1, 1]

	if RatMaze(n, maze, move_x, move_y, 0, 0, res):
		for i in range(n):
			for j in range(n):
				print(res[i][j], end=' ')
			print()
	else:
		print('Solução não existe')

# Programa principal para testar a função acima
if __name__ == "__main__":
	# Inicializando o labirinto
	maze = [[1, 0, 0, 0],
			[1, 1, 0, 1],
			[0, 1, 0, 0],
			[1, 1, 1, 1]]

	solveMaze(maze)

# Este código foi contribuído por Anvesh Govind Saxena
