p_board = board = [".." for _ in range(64)]
i_board = [g for g in range(64)]

for h in range(10):
    i_board[h] = "0" + str(i_board[h])


brow = "RNBQKBNR"
frow = "PPPPPPPP"

for u in [h for h in range(64) if h in range(8) or h in range(56,64)]:
    if u > 8:
        p_board[u] = board[u] = "^" + brow[u%8] 
    else:
        p_board[u] = board[u] = "#" + brow[u%8]

for u in [h for h in range(64) if h in range(8,16) or h in range(48,56)]:
    if u > 16:
        board[u] = "^" + frow[u%8]
    else:
        board[u] = "#" + frow[u%8]

tran = {
    "a8":0,  "b8":1,  "c8":2,  "d8":3,  "e8":4,  "f8":5,  "g8":6,  "h8":7,
    "a7":8,  "b7":9,  "c7":10, "d7":11, "e7":12, "f7":13, "g7":14, "h7":15,
    "a6":16, "b6":17, "c6":18, "d6":19, "e6":20, "f6":21, "g6":22, "h6":23,
    "a5":24, "b5":25, "c5":26, "d5":27, "e5":28, "f5":29, "g5":30, "h5":31,
    "a4":32, "b4":33, "c4":34, "d4":35, "e4":36, "f4":37, "g4":38, "h4":39,
    "a3":40, "b3":41, "c3":42, "d3":43, "e3":44, "f3":45, "g3":46, "h3":47,
    "a2":48, "b2":49, "c2":50, "d2":51, "e2":52, "f2":53, "g2":54, "h2":55,
    "a1":56, "b1":57, "c1":58, "d1":59, "e1":60, "f1":61, "g1":62, "h1":63,
}

keys = tran.keys()
def show(board_style = board):
    for i in range(8):
        for j in range(8):
            print(list(keys)[i*8+j], end=" ")
            #print(["|" for i in range(64)][i*8+j], end="")
            print(board_style[i*8+j], end="\t")
        print()
show()

def index():
    global all_b,all_r,all_p,all_n,all_q,all_k,wB,bB,wR,bR,wP,bP,wN,bN,bK,wK,bQ,wQ
    wB = [index for index, value in enumerate(p_board) if value == "^B"]
    bB = [index for index, value in enumerate(p_board) if value == "#B"]
    wR = [index for index, value in enumerate(p_board) if value == "^R"]
    bR = [index for index, value in enumerate(p_board) if value == "#R"]
    wP = [index for index, value in enumerate(p_board) if value == "^P"]
    bP = [index for index, value in enumerate(p_board) if value == "#P"]
    wN = [index for index, value in enumerate(p_board) if value == "^N"]
    bN = [index for index, value in enumerate(p_board) if value == "#N"]
    bQ = [index for index, value in enumerate(p_board) if value == "#Q"]
    wQ = [index for index, value in enumerate(p_board) if value == "^Q"]
    bK = [index for index, value in enumerate(p_board) if value == "#K"]
    wK = [index for index, value in enumerate(p_board) if value == "^K"]
    all_b = wB + bB
    all_r = wR + bR
    all_p = wP + bP
    all_n = wN + bN
    all_q = wQ + bQ
    all_k = wK + bK

index()
#Bishop
b_can_move = []
def bishop(list_type = all_b):
    index()
    if len(b_can_move) > 0:
        for _ in range(len(b_can_move)):
            #print(b_can_move)
            #print(board[(tran[move_list[1]])],board[b_can_move[0]])
            if board[b_can_move[0]] != "**":
                #print(b_can_move[0])
                b_can_move.pop(0)
                continue
            board[b_can_move[0]] = ".."
            b_can_move.pop(0)

    #print(b_can_move)
    b_can_move.clear()
    for bishop in list_type:
        var = bishop
        while var%8 < 7 and var//8 > 0:
            var -= 7
            if ".." in board[var] or "**" in board[var]:
                #board[var] = "**"
                b_can_move.append(var)
            elif ("^" in board[var] and "#" in board[tran[move_list[1]]]) or ("#" in board[var] and "^" in board[tran[move_list[1]]]):
                b_can_move.append(var)
                break
            else:
                break
        var = bishop
        while var%8 < 7 and var//8 < 7:
            var += 9
            if ".." in board[var] or "**" in board[var]:
                #board[var] = "**"
                b_can_move.append(var)
            elif ("^" in board[var] and "#" in board[tran[move_list[1]]]) or ("#" in board[var] and "^" in board[tran[move_list[1]]]):
                b_can_move.append(var)
                break
            else:
                break
        var = bishop
        while var%8 > 0 and var//8 < 7:
            var += 7
            if ".." in board[var] or "**" in board[var]:
                #board[var] = "**"
                b_can_move.append(var)
            elif ("^" in board[var] and "#" in board[tran[move_list[1]]]) or ("#" in board[var] and "^" in board[tran[move_list[1]]]):
                b_can_move.append(var)
                break
            else:
                break
        var = bishop
        while var%8 > 0 and var//8 > 0:
            var -= 9
            if ".." in board[var] or "**" in board[var]:
                #board[var] = "**"
                b_can_move.append(var)
            elif ("^" in board[var] and "#" in board[tran[move_list[1]]]) or ("#" in board[var] and "^" in board[tran[move_list[1]]]):
                b_can_move.append(var)
                break
            else:
                break
    #print(b_can_move, "b_can_move")
            

#Rooks
r_can_move = []
r_has_moved = [i for i in range(64) if "R" in board[i]]
def rook(list_type = all_r):
    index()
    global r_has_moved,r_can_castle
    r_can_castle = False
    #print("r_has_moved:",r_has_moved,list_type)
    if list_type[0] in [0,7,56,63]:
        if list_type[0] in r_has_moved:
            r_has_moved.remove(list_type[0])
            r_can_castle = True
        #print("new r_has_moved:",r_has_moved)
    if len(r_can_move) > 0:
        for _ in range(len(r_can_move)):
            #print(r_can_move)
            if board[r_can_move[0]] != "**":
                r_can_move.pop(0)
                continue
            board[r_can_move[0]] = ".."
            r_can_move.pop(0)
    #print(r_can_move)
    if len(move_list) > 1:
        for rook in list_type:
            var = rook
            while var//8 > 0:
                var -= 8
                #print(rook,board[rook][0],var,board[var][0])
                if ".." in board[var] or "**" in board[var]:
                    #board[var] = "**"
                    r_can_move.append(var)
                elif ("^" in board[var] and "#" in board[tran[move_list[1]]]) or ("#" in board[var] and "^" in board[tran[move_list[1]]]):
                    r_can_move.append(var)
                    break
                else:
                    break
            var = rook
            while var//8 < 7:
                var += 8
                #print(rook,board[rook][0],var,board[var][0])
                if ".." in board[var] or "**" in board[var]:
                    #board[var] = "**"
                    r_can_move.append(var)
                elif ("^" in board[var] and "#" in board[tran[move_list[1]]]) or ("#" in board[var] and "^" in board[tran[move_list[1]]]):
                    r_can_move.append(var)
                    break
                else:
                    break
            var = rook
            while var%8 > 0:
                var -= 1
                if ".." in board[var] or "**" in board[var]:
                    #board[var] = "**"
                    r_can_move.append(var)
                elif ("^" in board[var] and "#" in board[tran[move_list[1]]]) or ("#" in board[var] and "^" in board[tran[move_list[1]]]):
                    r_can_move.append(var)
                    break
                else:
                    break
            var = rook
            while var%8 < 7:
                var += 1
                if ".." in board[var] or "**" in board[var]:
                    #board[var] = "**"
                    r_can_move.append(var)
                elif ("^" in board[var] and "#" in board[tran[move_list[1]]]) or ("#" in board[var] and "^" in board[tran[move_list[1]]]):
                    r_can_move.append(var)
                    break
                else:
                    break
        #print(r_can_move,"r_can_move")

#Pawn
p_can_move = []
first_move = all_p
def pawn(list_style = all_p):
    index()
    if len(p_can_move) > 0:
        for _ in range(len(p_can_move)):
            #print(p_can_move)
            if board[p_can_move[0]] != "**":
                p_can_move.pop(0)
                continue
            board[p_can_move[0]] = ".."
            p_can_move.pop(0)
    #print(p_can_move)
    for pawn in list_style:
        var = pawn
        if board[pawn][0] == "^":
            if var%8 == 0 and "#" in board[var-7]:
                var -= 7
                #board[var] = "**"
                p_can_move.append(var)
            elif var%8 == 7 and "#" in board[var-9]:
                var -= 9
                #board[var] = "**"
                p_can_move.append(var)
            elif "#" in board[var-7] and "#" in board[var-9]:
                var -= 7
                #board[var] = "**"
                p_can_move.append(var)
                #board[var] = "**"
                var -= 2
                p_can_move.append(var)
            elif "#" in board[var-7]:
                var -= 7
                #board[var] = "**"
                p_can_move.append(var)
            elif "#" in board[var-9]:
                var -= 9
                #board[var] = "**"
                p_can_move.append(var)
            var = pawn
            if pawn in first_move:
                var -= 8
                #board[var] = "**"
                p_can_move.append(var)
                var -= 8
                #board[var] = "**"
                p_can_move.append(var)
                first_move.pop(first_move.index(pawn))
            elif pawn not in first_move:
                var -= 8
                #board[var] = "**"
                p_can_move.append(var)
        
        if board[pawn][0] == "#":
            if var%8 == 0 and "^" in board[var+9]:
                var += 9
                #board[var] = "**"
                p_can_move.append(var)
            elif var%8 == 7 and "^" in board[var+7]:
                var += 7
                #board[var] = "**"
                p_can_move.append(var)
            elif "^" in board[var+7] and "^" in board[var+9]:
                var += 7
                #board[var] = "**"
                p_can_move.append(var)
                board[var] = "**"
                var += 2
                p_can_move.append(var)
            elif "^" in board[var+7]:
                var += 7
                #board[var] = "**"
                p_can_move.append(var)
            elif "^" in board[var+9]:
                var += 9
                #board[var] = "**"
                p_can_move.append(var)
            var = pawn
            if pawn in first_move:
                var += 8
                #board[var] = "**"
                p_can_move.append(var)
                var += 8
                p_can_move.append(var)
            elif pawn not in first_move:
                var += 8
                #board[var] = "**"
                p_can_move.append(var)
        #Promotion
        promotion = [i for i in p_can_move if i//8 == 0 or  i//8 == 7] #contains of all pawn moves for that peice that allow for promotion
        if tran[move_list[2]] in promotion: #if their move is in the list above
            while True:
                pro_choice = input("Pawn promotion. Pick a peice to turn the pawn into (N,B,Q,R): ") #lets the user choose
                pro_choice = pro_choice.upper() #changes the users choice uppercase so when its converted to the real board, its uppercase
                if pro_choice == "K" or pro_choice == "P": #if they choose pawn or king, ask again
                    print("You can't promote to a king or pawn")
                    continue
                elif len(pro_choice) > 1: #if they enter more characters than 1, ask again
                    print("Enter a single character to signal the peice (p = pawn, q = queen, etc)")
                    continue
                elif pro_choice not in ["R","B","N","Q"]: #if the character they entered is not a peice, ask again
                    print("You have to pick from the options above.")
                    continue
                
                p_board[tran[move_list[1]]] = turn_list[-1] + pro_choice #if their choice passed all the tests, turn the original pawn to their choice
                break #exit the loop

                


#Knight
n_can_move = []
def knight(list_type = all_n):
    index()
    if len(n_can_move) > 0:
        for _ in range(len(n_can_move)):
            #print(n_can_move)
            if board[n_can_move[0]] != "**":
                #print(n_can_move[0],board[n_can_move[0]])
                n_can_move.pop(0)
                continue
            board[n_can_move[0]] = ".."
            n_can_move.pop(0)
    #print(n_can_move)
    for knight in list_type:
        var = [knight+17,knight-17,knight+15,knight-15,knight+10,knight-10,knight+6,knight-6]
        for knight_move in var:
            #print("in loop: ", knight_move,var)
            if (abs((knight%8)-(knight_move%8)) <= 2 and abs((knight//8)-(knight_move//8)) <= 2) and knight_move in range(64):
                if board[knight_move][0] not in board[knight][0]:
                    #print(board[knight_move])
                    n_can_move.append(knight_move)
                    #board[knight_move] = "**"

#King
k_can_move = []
k_has_moved = [i for i in range(64) if "K" in board[i]]
stalemate = checkmate = False
def king(list_type = all_k):
    global stalemate,checkmate,att,pot_moves,k_has_moved,k_can_castle
    k_can_castle = False
    #print("k_has_moved:",k_has_moved,list_type,)
    if list_type[0] in k_has_moved:
        k_has_moved.remove(list_type[0])
        k_can_castle = True
    #print("new k_has_moved:",k_has_moved)
    op_king = [i for i in range(64) if "K" in board[i] and turn_list[-1] != board[i][0]][0]
    op_king_att = [i for i in [op_king+1,op_king-1,op_king+8,op_king-8,op_king-7,op_king+7,op_king+9,op_king-9] if i in range(64)]
    #print(op_king_att)
    #print(op_king, list_type[0])
    if len(move_list) > 1:
        if turn_list[-1] == "^": 
            bishop(wB)
            knight(wN)
            rook(wR)
            pawn(wP)
            pot_moves = b_can_move + r_can_move + p_can_move + n_can_move
            bishop(bB)
            knight(bN)
            rook(bR)
            pawn(bP)
            att = b_can_move + r_can_move + p_can_move + n_can_move + op_king_att
            
        elif turn_list[-1] == "#":
            bishop(bB)
            knight(bN)
            rook(bR)
            pawn(bP)
            pot_moves = b_can_move + r_can_move + p_can_move + n_can_move
            bishop(wB)
            knight(wN)
            rook(wR)
            pawn(wP)
            att = b_can_move + r_can_move + p_can_move + n_can_move + op_king_att
        k_can_move.clear()
        for king in list_type:
            var = [king+1,king-1,king+8,king-8,king+7,king-7,king+9,king-9]
            #print("var = ",var)
            for king_move in var:
                if king_move not in att and ((abs((king%8)-(king_move%8)) <= 1 and abs((king//8)-(king_move//8)) <= 1) and king_move in range(64)):
                    #print("Stage 1")
                    #print(board[king_move][0],board[king][0])
                    if board[king_move][0] != board[king][0]:
                        """print(king_move)
                        k_can_move.append(king_move)
                        p_board[king_move] = "**" """
                        #print("Stage 2")
                        #print([i for i in [king_move+1,king_move-1,king_move+8,king_move-8,king_move+9,king_move-9,king_move+7,king_move-7] if (i in range(64) and "K" in board[i]) and i != king])
                        if len(["K" for i in [king_move+1,king_move-1,king_move+8,king_move-8,king_move+9,king_move-9,king_move+7,king_move-7] if (i in range(64) and "K" in board[i]) and i != king]) <= 1:
                            #print("Stage 3")
                            #board[king_move] = board[list_type[0]]
                            board[list_type[0]] = ".."
                            #print(r_can_move,"hi")
                            if turn_list[-1] == "^":
                                bishop(bB)
                                knight(bN)
                                rook(bR)
                                pawn(bP)
                                att += b_can_move + r_can_move + p_can_move + n_can_move + op_king_att
                                #print("hi")
                                #print(r_can_move,"- - - -")
                            elif turn_list[-1] == "#":
                                bishop(wB)
                                knight(wN)
                                rook(wR)
                                pawn(wP)
                                att += b_can_move + r_can_move + p_can_move + n_can_move + op_king_att
                                #print(r_can_move,"- - - -")
                            #show()
                            board[list_type[0]] = turn_list[-1] + "K"
                            #board[king_move] = ".."
                            #show()
                            #print(r_can_move)
                            #print("new_att =",att)
                            if king_move not in att:
                                #print(king_move)
                                k_can_move.append(king_move)
                                #p_board[king_move] = "**"
        
        index() #very important for the program to continue acknowledging the kings existence
        #print("k_moves = ",k_can_move,"pot_moves =",pot_moves,"list_type[0] =",list_type[0],"tran[move[2]] =",tran[move_list[1]],all_k)
        if tran[move_list[2]] in att:
            print("You're in check, the king isn't safe.")
        if len(k_can_move) == 0 and len(pot_moves) == 0 and list_type[0] not in att:
            stalemate = True
            print("Stalemate:",stalemate)
        elif len(k_can_move) == 0 and list_type[0] in att:
            checkmate = True
            print("Checkmate:",checkmate)
    
#queen
q_can_move = []
def queen(list_type = all_q):
    global q_can_move
    index()
    bishop(list_type)
    rook(list_type)
    q_can_move = r_can_move + b_can_move
    #print(q_can_move,"Q moves")
    
    
#Implement proper captures[Done], everything about the king(castling) and queen(movement), and pawn promotion. then remove all board[] = "**" or ".." 
def main():
    global move_list,turn_list
    turn_list = ["#"]
    while (('#K' in p_board and '^K' in p_board) and (stalemate == False and checkmate == False)):
        if turn_list[-1] == "^":
            print("\nBlack's turn")
            turn_list.append("#")
        elif turn_list[-1] == "#":
            print("\nWhite's Turn")
            turn_list.append("^")

        while True:
            show(p_board)
            print()
            move_list = []
            move = input("Enter peice, current location, wanted location (eg. P e2 e4): ")
            move_list = move.split(" ")
            if turn_list[-1] == "^" and move == "o-o-o":
                rook([56])
                king(wK)
                if k_can_castle == True and r_can_castle == True and len([0 for i in [57,58,59] if p_board[i] == ".."]) == 3:
                    board[59] = board[56]
                    board[56] = ".."
                    board[58] = board[60]
                    board[60] = ".."
                    break
                else:
                    print("You can't castle")
                    continue
            elif turn_list[-1] == "#" and move == "o-o-o":
                rook([0])
                king(bK)
                if k_can_castle == True and r_can_castle == True and len([0 for i in [1,2,3] if p_board[i] == ".."]) == 3:
                    board[3] = board[0]
                    board[0] = ".."
                    board[2] = board[4]
                    board[4] = ".."
                    break
                else:
                    print("You can't castle")
                    continue
            elif turn_list[-1] == "^" and move == "o-o":
                king(wK)
                rook([63])
                if k_can_castle == True and r_can_castle == True and len([0 for i in [62,61] if p_board[i] == ".."]) == 2:
                    board[62] = board[60]
                    board[60] = ".."
                    board[61] = board[63]
                    board[63] = ".."
                    break
                else:
                    print("You can't castle")
                    continue
            elif turn_list[-1] == "#" and move == "o-o":
                king(bK)
                rook([7])
                if k_can_castle == True and r_can_castle == True and len([0 for i in [5,6] if p_board[i] == ".."]) == 2:
                    board[5] = board[7]
                    board[7] = ".."
                    board[6] = board[4]
                    board[4] = ".."
                    break
                else:
                    print("You can't castle")
                    continue
                
            print(move_list)
            if len(move_list) != 3 and ("o-o-o" not in move_list or "o-o-o"):
                print("You have to enter 3 things or o-o-o / o-o to castle\n")
                continue
            if len(move_list) == 3:
                if move_list[0].lower() not in brow.lower() and move_list[0].lower() not in frow.lower():
                    print("Enter a valid peice (eg. P for pawn, R for rook, N for knight.)\n")
                    continue
                elif move_list[1] not in keys:
                    print(move_list[1],"\n",keys)
                    print("Enter a current location on the board (eg. e7, a3).")
                    continue
                elif move_list[2] not in keys:
                    print(move_list[2],"\n",keys)
                    print("Enter a wanted location on the board. (eg. g6, g2)")
                    continue
                else:
                    pass
            
            if turn_list[-1] not in p_board[tran[move_list[1]]]:
                print("You can only move your own peices", turn_list[-1],p_board[tran[move_list[1]]],"\n")
                continue
        
            if move_list[0].upper() == "P":
                pawn([tran[move_list[1]]])
                if tran[move_list[1]] in all_p and tran[move_list[2]] in p_can_move:
                    break
                else:
                    print("Invalid Pawn Move\n")
                    continue
            elif move_list[0].upper() == "B":
                bishop([tran[move_list[1]]])
                if tran[move_list[1]] in all_b and tran[move_list[2]] in b_can_move:
                    break
                else:
                    print("Invalid Bishop Move\n")
                    continue
            elif move_list[0].upper() == "R":
                rook([tran[move_list[1]]])
                if tran[move_list[1]] in all_r and tran[move_list[2]] in r_can_move:
                    break
                else:
                    print("Invalid Rook Move\n")
                    continue
            elif move_list[0].upper() == "N":
                knight([tran[move_list[1]]])
                if tran[move_list[1]] in all_n and tran[move_list[2]] in n_can_move:
                    break
                else:
                    print("Invalid Knight Move\n")
                    continue
            elif move_list[0].upper() == "Q":
                queen([tran[move_list[1]]])
                if tran[move_list[1]] in all_q and tran[move_list[2]] in q_can_move:
                    break
                else:
                    print("Invalid Queen Move\n")
            elif move_list[0].upper() == "K":
                king([tran[move_list[1]]])
                if tran[move_list[1]] in all_k and (tran[move_list[2]] in k_can_move or (len(k_can_move) == 0 and len(pot_moves) == 0 )):
                    break
                else:
                    print("Invalid King move")
                    continue
        if checkmate == False and stalemate == False and len(move_list) > 1:
            p_board[tran[move_list[2]]] = p_board[tran[move_list[1]]]
            p_board[tran[move_list[1]]] = ".."
    else:
        if stalemate == True:
            print("The game is a draw")
        elif "^" in turn_list[-1] and checkmate == True:
            print("Checkmate... White is the winner")
        elif "#" in turn_list[-1] and checkmate == True:
            print("Checkmate... Black is the winner")
        elif '^' in turn_list[-1]:
            print("The winner is White")
        elif '#' in turn_list[-1]:
            print("The winner is Black")

def menu():
    while True:
        print("---")
        print("Welcome to Chess by Emmanuel Tesfaye (motivated by Haileleul)")
        print("---\n"+"I'm assuming you know the rules of chess and how to play")
        print("If you want help learning this version of chess, type \"help\" \n"+"If you think you're ready: Enter anything")
        player_choice = input()
        player_choice.lower()
        if player_choice == "help":
            print("\nOk I hear you need some help.\n")
            print("To move a peice from 1 place to another enter the letter that represents the peice,\nthen press space, then enter the current location of that peice in chess notation,\nthen the place you want to go. This program checks for legal moves so illigal moves aren't allowed")
            print("\n ---> N for knight, B for bishop, R for rook, K for king, Q for queen, and P for pawn\n")
            print(" ---> ^ means white, # means black")
            print("In order to castle")
            print(" ---> o-o-o for queenside(left) castle, o-o for kingside(right) castle\n")
            print("I wasn't able to code \'En Passant'\ or checks properly like discovered check but the game \nends if its checkmate, stalemate, or one of the kings gets taken. ")
            continue
        else:
            main()
            break
        
menu()