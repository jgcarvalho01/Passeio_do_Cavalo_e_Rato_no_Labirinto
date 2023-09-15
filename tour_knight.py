def isSafe(x, y, board, n):
    '''
		Uma função utilitária para verificar se i,j são índices válidos
		para um tabuleiro de xadrez N*N
	'''

    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False

def printSolution(n, board):
    '''
		Uma função utilitária para imprimir a matriz do tabuleiro de xadrez
	'''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solveKT(n):
    '''
		Esta função resolve o problema do Passeio do Cavaleiro usando
		Backtracking. Essa função usa principalmente solveKTUtil()
		para resolver o problema. Ela retorna falso se nenhum passeio completo
		for possível, caso contrário, retorna verdadeiro e imprime o
		passeio.
		Por favor, note que pode haver mais de uma solução possível,
		esta função imprime uma das soluções viáveis.
	'''

    # Inicializa o tabuleiro com -1 (indicando que nenhuma casa foi visitada)
    board = [[-1 for i in range(n)] for i in range(n)]

    # move_x e move_y definem o próximo movimento do Cavaleiro.
	# move_x é para o próximo valor da coordenada x
	# move_y é para o próximo valor da coordenada y
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Define a posição inicial do cavaleiro
    board[0][0] = 0

    # Contador de passos para a posição do Cavaleiro
    pos = 1

    # Verifica se a solução é possível e imprime a solução ou informa que não existe solução
    if (not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
        print("Solução não existe para o tabuleiro de tamanho", n)
    else:
        printSolution(n, board)

def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    '''
		Uma função utilitária recursiva para resolver o problema do Passeio do Cavaleiro
	'''
    if (pos == n ** 2):
        return True

    # Tenta todos os próximos movimentos a partir das coordenadas x, y atuais
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (isSafe(new_x, new_y, board, n)):
            board[new_x][new_y] = pos
            if (solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos + 1)):
                return True
            board[new_x][new_y] = -1
    return False

if __name__ == "__main__":
    # Solicita ao usuário o tamanho do tabuleiro
    n = int(input("Informe o tamanho do tabuleiro (por exemplo, 8 para um tabuleiro 8x8): "))
    
    # Verifica se o tamanho do tabuleiro é adequado para a solução do problema
    if n < 5:
        print("O tabuleiro é muito pequeno para ser resolvido pelo Problema do Passeio do Cavaleiro.")
    else:
        # Chama a função principal para resolver o problema
        solveKT(n)
