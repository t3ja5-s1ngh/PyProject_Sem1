
'''Directions is a list which includes the fundamental directions that is up, up-right, right, down-right, down, down-left, left, up-left.'''

Directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
            #   N    N-E    E     S-E     S     S-W      W     N-W 


'''While going through all the squares on the board this function ensures that we don't exceed the board.'''
def is_on_board(r, c):
    if(0<= r <= 7) and (0<= c <= 7):
        return True
    return False


'''It switches the player and returns the next player'''
def get_opponent(current_player):
    # return switch_player(current_player)
    if current_player == 1: return 2
    else: return 1


'''It returns the list of flipped coins in a particular direction'''
def get_flips_in_direction(b,r,c,player,vector):
    pieces_to_flip = []
    opponent = get_opponent(player)
    curr_r = r + vector[0]
    curr_c = c + vector[1]
    if not is_on_board(curr_r, curr_c) or b[curr_r][curr_c] != opponent:
        return []
    while is_on_board(curr_r,curr_c):
        
        if b[curr_r][curr_c] == 0 : return []
        elif b[curr_r][curr_c] == player: return pieces_to_flip
        else: 
            pieces_to_flip.append([curr_r,curr_c])
            curr_r += vector[0]
            curr_c += vector[1]
    return []


'''It provides all directions one by one to the get_flips_in_direction'''
def get_all_flips(b,r,c,player):
    all_flips = []
    if b[r][c] != 0: return []

    for vector in Directions:
        all_flips.extend(get_flips_in_direction(b,r,c,player,vector))
    return all_flips


'''It checks wheter the player has any legal move or not'''
def has_legal_moves(b,player):
    for r in range(8):
        for c in range(8):
            if b[r][c] == 0:
                if get_all_flips(b, r, c, player):
                    return True
    return False


'''If the next player doesnt have any legal move there turn will skip '''
def determine_next_player_id(b, last_player):
    opponent = get_opponent(last_player)

    if has_legal_moves(b, opponent):
        return opponent

    elif has_legal_moves(b, last_player):
        return last_player 
     
'''next_state is the main function which is called by main and returns the final state of the board with the player who will be playing next'''
def next_state(b,r,c,player):
    board_cpy = [row[:] for row in b]
    all_flips = get_all_flips(b,r,c,player)
    if not all_flips:
        return (b, player) 
            
    board_cpy[r][c] = player

    for coordinate in all_flips:
        board_cpy[coordinate[0]][coordinate[1]] = player

    opponent = get_opponent(player)
    if has_legal_moves(board_cpy,opponent):
        next_player = opponent
    elif has_legal_moves(board_cpy, player):
        next_player = player 
    else:
        next_player = None

    return (board_cpy, next_player)