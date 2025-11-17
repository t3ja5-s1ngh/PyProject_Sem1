import board 

b = board.Board().grid

# EMPTY = 0 --> Means cell is empty
# WHITE = 2 --> Means cell is filled with white
# BLACK = 1 --> Means cell is filled with black


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

# It reeturns the coins to be flipped in a particular direction.  
def check_direc(b, r, c, player,vector): #b --> state of board
                                              #r, c -->  co-ord of proposed new move
                                              #player --> current player
                                              #(dr, dc) --> direction vector
    pieces_to_flip = []
    curr_r = r + vector[0]
    curr_c = c + vector[1]
    while (is_on_board(curr_r, curr_c)):
        if b[curr_r][curr_c] == 0:
            return []
        elif b[curr_r][curr_c] == player:
            return pieces_to_flip
        elif b[curr_r][curr_c] != player and b[curr_r][curr_c] != 0:
            pieces_to_flip.append(list(curr_r, curr_c))
            curr_r+=vector[0]
            curr_c+=vector[1]
        # return pieces_to_flip

def count(b):
    for i in b:
        for j in i:
            if j == 2:
                count_w+=1
            elif j == 1:
                count_b+=1
    return [count_w,count_b]


def legal_move(b,vector,r,c,player):
    curr_r= r + vector[0]
    curr_c= c + vector[1]
    while(is_on_board(curr_r,curr_c) is True):
        if b[curr_r][curr_c]== 0:
            return False
        elif b[curr_r][curr_c]==player:
            return True
        elif b[curr_r][curr_c]!=player and b[curr_r][curr_c]!= 0:
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

def has_legal_moves(b,player):
    for r in range(8):
        for c in range(8):
            if b[r][c] == 0:
                for vector in DIRECTIONS:
                    if legal_move(b,vector,r,c,player) is True:
                        return True
    return False

def make_move(b,r,c,player):
    b[r][c] = player
    for vector in DIRECTIONS:
        if legal_move(b,vector,r,c,player) is True:
            pieces_to_flip = check_direc(b,r,c,player,vector)
            for pos in pieces_to_flip:
                b[pos[0]][pos[1]] = player

def switch_player(player):
    if player == 1: return 2
    else: return 1


def get_next_player(b, current_player):
    opponent = switch_player(current_player) #find opponent

    if has_legal_moves(b, opponent):#opponent gets to play only if they have legal moves
        return opponent

    elif has_legal_moves(b, current_player):
        return current_player

    return b
    