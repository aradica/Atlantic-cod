from stockfish import Stockfish

def nextTurn(player):
    if player == "white":
        return "black"
    else:
        return "white"
sf = Stockfish("stockfish-win/stockfish_10_x64.exe", 10)
player = "white"
moves = []
i = 0
move = None
while True:
    move = sf.get_best_move()
    if move == False: #check mate
        print(player, "lost!")
        break
    else:
        moves.append(move)
        #print(i, player, move)
        sf.set_position(moves)
        player = nextTurn(player)
        i += 1
player = nextTurn(player)
print("Player", player, "wins after", i, "turns!\n")

print(moves)
