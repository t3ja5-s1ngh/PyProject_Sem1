import board 

b = board.Board().grid

EMPTY = 'e' #Means cell is empty
WHITE = 'w' #Means cell is filled with white
BLACK = 'b' #Means cell is filled with black 


DIRECTIONS = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1,0),   # Up
    (1, 1),   # Down-Right
    (-1, -1), # Up-Left
    (1, -1),  # Down-Left
    (-1, 1)   # Up-Right
]

def is_on_board(r, c):
    if(0<= r <= 7) and (0<= c <= 7):
        return True
    return False

def check_direc(b, r, c, player,vector): #board --> state of board
                                              #r, c -->  co-ord of proposed new move
                                              #player --> current player
                                              #(dr, dc) --> DIRECn vector
    pieces_to_flip = []
    curr_r = r + vector[0]
    curr_c = c + vector[1]
    while (is_on_board(curr_r, curr_c)):
        if b[curr_r][curr_c] == 'e':
            return []
        elif b[curr_r][curr_c] == player:
            return pieces_to_flip
        elif b[curr_r][curr_c] != player and b[curr_r][curr_c] != 0:
            pieces_to_flip.append(list(curr_r, curr_c))
            curr_r+=vector[0]
            curr_c+=vector[1]
        return pieces_to_flip

def count(b):
    count_w=0
    count_b=0
    for i in b:
        for j in i:
            if j==W:
                count_w+=1
            elif j==B:
                count_b+=1
    return [count_w,count_b]


def legal_move(b,vector,r,c,player):
    curr_r= r + vector[0]
    curr_c= c + vector[1]
    while(is_on_board(curr_r,curr_c) is True):
        if b[curr_r][curr_c]== 0
            return False
        elif b[curr_r][curr_c]==player
            return True
        elif b[curr_r][curr_c]!=player and b[curr_r][curr_c]!= 0
            curr_r+=vector[0]
            curr_c+=vector[1]
            continue

def new_state(b,r,c,player):
    new_board = [row[:] for row in b]
    new_board[r][c] = player
    for vector in DIRECTIONS:
        if legal_move(new_board,vector,r,c,player) is True:
            pieces_to_flip = check_direc(new_board,r,c,player,vector)
            for pos in pieces_to_flip:
                b[pos[0]][pos[1]] = player
            
    return b







        
