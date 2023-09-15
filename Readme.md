# Algoritmos de Passeio do Cavaleiro e Rato no Labirinto

Este repositório contém dois algoritmos: um para o Problema do Passeio do Cavalo e outro para o Problema do Rato no Labirinto.

## Passeio do Cavaleiro (tour_knight.py)

O algoritmo `tour_knight.py` resolve o Problema do Passeio do Cavalo, onde o objetivo é encontrar um caminho para que um cavaleiro em um tabuleiro de xadrez visite todas as células sem repetições e seguindo as regras de movimento de um cavalo de xadrez.

### Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.

2. Baixe o arquivo `tour_knight.py` deste repositório.

3. Abra um terminal e navegue até o diretório onde você salvou o arquivo.

4. Execute o seguinte comando:
`python3 tour_knight.py`

5. O programa solicitará que você insira o tamanho do tabuleiro (por exemplo, "8" para um tabuleiro 8x8).

### Entrada

- O programa solicitará que você insira o tamanho do tabuleiro (um número inteiro maior que zero).
```
Informe o tamanho do tabuleiro (por exemplo, 8 para um tabuleiro 8x8): 8 
```

### Saída

- O programa imprimirá um possível caminho de passeio do cavalo no tabuleiro, se existir, ou informará que não há solução.
```
0 59 38 33 30 17 8 63 
37 34 31 60 9 62 29 16 
58 1 36 39 32 27 18 7 
35 48 41 26 61 10 15 28 
42 57 2 49 40 23 6 19 
47 50 45 54 25 20 11 14 
56 43 52 3 22 13 24 5 
51 46 55 44 53 4 21 12
```

## Rato no Labirinto (rat-in-a-maze.py)

O algoritmo `rat-in-a-maze.py` resolve o Problema do Rato no Labirinto, onde um rato precisa encontrar um caminho do ponto de partida até o ponto de destino em um labirinto, evitando obstáculos.

### Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.

2. Baixe o arquivo `rat-in-a-maze.py` deste repositório.

3. Abra um terminal e navegue até o diretório onde você salvou o arquivo.

4. Execute o seguinte comando:
`python3 rat-in-a-maze.py`

5. O programa executará a resolução do problema do rato no labirinto.

### Entrada

- O programa pode ter entradas diferentes, dependendo do labirinto definido dentro do código. Você pode personalizar o labirinto diretamente no código-fonte.
```
# Inicializando o labirinto
	maze = [[1, 0, 0, 0],
			[1, 1, 0, 1],
			[0, 1, 0, 0],
			[1, 1, 1, 1]]

```

### Saída

- O programa imprimirá o labirinto resolvido ou informará que não há solução.
```
1 0 0 0 
1 1 0 0 
0 1 0 0 
0 1 1 1
```