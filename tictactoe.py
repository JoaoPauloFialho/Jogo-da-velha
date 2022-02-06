def velha(jogo): #checa se já deu velha
    for c in range(0, 3):
        if jogo[c][0] == 'X' and jogo[c][1] == 'X' and jogo[c][2] == 'X':
            return True
        if jogo[c][0] == 'O' and jogo[c][1] == 'O' and jogo[c][2] == 'O':
            return True
        if jogo[0][c] == 'X' and jogo[1][c] == 'X' and jogo[2][c] == 'X':
            return True
        if jogo[0][c] == 'O' and jogo[1][c] == 'O' and jogo[2][c] == 'O':
            return True
        if jogo[c][c] == 'X' and jogo[c+1][c+1] == 'X' and jogo[c+2][c+2] == 'X':
            return True
        if jogo[c][c] == 'O' and jogo[c+1][c+1] == 'O' and jogo[c+2][c+2] == 'O':
            return True
    
def jogo(jogo): #  escreve o jogo pro usuário saber qual linha falta colocar X ou O
    for e in range(0, 3):
        for x in range(0, 3):
            if jogo[e][x] != '':
                print(f'[ {jogo[e][x]} ]', end=' ')
            else:
                print(f'[ \033[36m{x}\033[m ]', end=' ')
        print()


jogo_da_velha = [[] ,[] ,[]]
for x in range (0, 3):
    for c in range (0, 3): #  cria uma matriz vazia bonita
        jogo_da_velha[x].insert(c,'')

print('\033[033m=\033[m'*30)
print('\033[34mJOGO DA VELHA\033[m')
print('\033[033m=\033[m'*30)
print('             colunas')
print('linha 0 -> [0] [1] [2]')
print('linha 1 -> [0] [1] [2]')
print('linha 2 -> [0] [1] [2]')
print('\033[033m=\033[m'*30)

while True:
    try:
        linha = int(input('Digite a linha (0, 1, 2) -> '))

        coluna = int(input('Digite a coluna (0, 1, 2) -> '))

        x_ou_o = str(input('O ou X -> ')).upper().strip()

        del jogo_da_velha[linha][coluna]
        jogo_da_velha[linha].insert(coluna, x_ou_o)
        jogo(jogo_da_velha[:])
        if velha(jogo_da_velha):
            break
    except:
        print('\033[31mINSIRA DADOS VÁLIDOS\033[m')
print('DEU VELHA')
    

