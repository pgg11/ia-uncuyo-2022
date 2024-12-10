import numpy as np
from DeterministicAgent import DeterministicAgent

class Env:
    def __init__(self, size=9, barriers_per_player=10):
        self.size = size
        self.board = np.zeros((size, size), dtype=int)  # 0: casilla libre, 1: jugador 1, 2: jugador 2
        self.barriers = set({("H", 3, 3)})  # conjunto donde se guarda la posicion de las barreras. ej: ("H", x, y) {('V', 0, 0), ('V', 2, 3), ('H', 1, 1), ('H', 4, 0), ('V', 0, 1), ('V', 1, 2)}
        self.players = {
            1: {"position": (0,size // 2), "barriers_left": barriers_per_player},
            2: {"position": (size-1,size // 2), "barriers_left": barriers_per_player}
        }
        self.turn = 0
        self.max_turns = 30  # limite de turnos
    
    def get_barriers(self):
        return self.barriers
    
    def get_size(self):
        return self.size

    def get_player_position(self, player):
        return self.players[player]["position"]
    
    def set_player_position(self, player, position):
        x, y = self.players[player]["position"]
        self.board[x][y] = 0
        self.players[player]["position"] = position
        if player == 1:
            if position[0] >= 8:
                self.players[player]["position"] = (0 , self.size // 2)
        else:
            if position[0] <= 0:
                self.players[player]["position"] = (self.size-1 , self.size // 2)

    def display_board(self):

        x,y = self.players[1]["position"]
        x2,y2 = self.players[2]["position"]

        self.board[x][y] = 1
        self.board[x2][y2] = 2
        print("Barriers:", self.barriers)
        print("   " + "   ".join(str(i) for i in range(self.size)))
        print("  " + "--" * (2 * self.size - 1))

        for i in range(self.size):
            # Imprimir la fila de celdas
            print(f"{i}| ", end="")
            for j in range(self.size):
                print(self.board[i][j], end=" ")
                # Agregar barreras verticales
                if ("V", i, j) in self.barriers or ("V", i-1, j) in self.barriers:
                    print("|", end=" ")
                else:
                    print("  ", end="")
            print()  # Salto de línea tras la fila

            # Imprimir barreras horizontales
            if i < self.size - 1:  # No imprimir al final del tablero
                print("   ", end="")
                for j in range(self.size):
                    if ("H", i, j) in self.barriers or ("H", i, j-1) in self.barriers:
                        print("---", end="")
                    else:
                        print("    ", end="")
                print()
    
    def is_valid_step(self, player, move):

        if player == 1:
            opponent = 2
        else:
            opponent = 1
        x, y = self.players[player]["position"]

        if move == "up" and x > 0 and not self.is_opponent_adjacent(self.players[player],self.players[opponent],"up"):
            if ("H", x - 1, y) not in self.barriers and ("H", x - 1 , y + 1) not in self.barriers:
                return True
        elif move == "down" and x < self.size - 1 and not self.is_opponent_adjacent(self.players[player],self.players[opponent],"down"):
            if ("H", x, y) not in self.barriers and ("H", x, y - 1) not in self.barriers:
                return True
        elif move == "left" and y > 0 and not self.is_opponent_adjacent(self.players[player],self.players[opponent],"left"):
            if ("V", x, y - 1) not in self.barriers and ("V", x - 1, y - 1) not in self.barriers:
                return True
        elif move == "right" and y < self.size - 1 and not self.is_opponent_adjacent(self.players[player],self.players[opponent],"right"):
            if ("V", x, y) not in self.barriers and ("V", x - 1, y) not in self.barriers:
                return True
        elif move == "jump down" and x < self.size - 1 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"down"):
            if ("H", x, y) not in self.barriers and ("H", x, y - 1) not in self.barriers:
                if ("H", x+1, y) not in self.barriers and ("H", x+1, y - 1) not in self.barriers:
                    return True
        elif move == "jump down right" and x < self.size - 1 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"down"):
            if ("H", x, y) not in self.barriers and ("H", x, y - 1) not in self.barriers:
                if ("H", x+1, y) in self.barriers or ("H", x+1, y-1) in self.barriers:
                    if ("V", x, y) not in self.barriers and ("V", x+1, y) not in self.barriers:
                        return True
        elif move == "jump down left" and x < self.size - 1 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"down"):
            if ("H", x, y) not in self.barriers and ("H", x, y - 1) not in self.barriers:
                if ("H", x+1, y) in self.barriers or ("H", x+1, y-1) in self.barriers:
                    if ("V", x, y-1) not in self.barriers and ("V", x+1, y-1) not in self.barriers:
                        return True
        elif move == "jump up" and x > 0 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"up"):
            if ("H", x - 1, y) not in self.barriers and ("H", x - 1 , y + 1) not in self.barriers:
                if ("H", x-2, y) not in self.barriers and ("H", x-2, y - 1) not in self.barriers:
                    return True
        elif move == "jump up right" and x > 0 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"up"):
            if ("H", x - 1, y) not in self.barriers and ("H", x - 1 , y + 1) not in self.barriers:
                if ("H", x-2, y) in self.barriers or ("H", x-2, y-1) in self.barriers:
                    if ("V", x-1, y) not in self.barriers and ("V", x-2, y) not in self.barriers:
                        return True
        elif move == "jump up left" and x > 0 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"up"):
            if ("H", x - 1, y) not in self.barriers and ("H", x - 1 , y + 1) not in self.barriers:
                if ("H", x-2, y) in self.barriers or ("H", x-2, y-1) in self.barriers:
                    if ("V", x-1, y-1) not in self.barriers and ("V", x-2, y-1) not in self.barriers:
                        return True
        elif move == "jump left" and y > 0 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"left"):
            if ("V", x, y - 1) not in self.barriers and ("V", x - 1, y - 1) not in self.barriers:
                if ("V", x, y-2) not in self.barriers or ("V", x-1, y-2) not in self.barriers:
                    return True
        elif move == "jump left up" and y > 0 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"left"):
            if ("V", x, y - 1) not in self.barriers and ("V", x - 1, y - 1) not in self.barriers:
                if ("V", x, y-2) in self.barriers or ("V", x-1, y-2) in self.barriers:
                    if("H", x-1, y-1) not in self.barriers and ("H", x-1, y-2) not in self.barriers:
                        return True
        elif move == "jump left down" and y > 0 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"left"):
            if ("V", x, y - 1) not in self.barriers and ("V", x - 1, y - 1) not in self.barriers:
                if ("V", x, y-2) in self.barriers or ("V", x-1, y-2) in self.barriers:
                    if("H", x, y-1) not in self.barriers and ("H", x, y-2) not in self.barriers:
                        return True
        elif move == "jump right" and y < self.size-1 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"right"):
            if ("V", x, y) not in self.barriers and ("V", x - 1, y) not in self.barriers:
                if ("V", x, y+1) not in self.barriers or ("V", x-1, y+1) not in self.barriers:
                    return True
        elif move == "jump right up" and y < self.size-1 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"right"):
            if ("V", x, y) not in self.barriers and ("V", x - 1, y) not in self.barriers:
                if ("V", x, y+1) in self.barriers or ("V", x-1, y+1) in self.barriers:
                    if("H", x-1, y) not in self.barriers and ("H", x-1, y+1) not in self.barriers:
                        return True
        elif move == "jump right down" and y < self.size-1 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"right"):
            if ("V", x, y) not in self.barriers and ("V", x - 1, y) not in self.barriers:
                if ("V", x, y+1) in self.barriers or ("V", x-1, y+1) in self.barriers:
                    if("H", x, y) not in self.barriers and ("H", x, y+1) not in self.barriers:
                        return True
        
        return False

    def is_opponent_adjacent(self,player,opponent,direction):
        x1,y1 = player["position"]
        x2,y2 = opponent["position"]
        if direction == "down" and y1 == y2 and x1 == x2-1:
            return True
        if direction == "up" and y1 == y2 and x1 == x2+1:
            return True
        if direction == "right" and y1 == y2-1 and x1 == x2:
            return True
        if direction == "left" and y1 == y2+1 and x1 == x2:
            return True
    
    def get_actions(self, player):
        possible_moves = ["up","jump up","jump up left","jump up right",
                          "right","jump right","jump right up", "jump right down",
                          "left","jump left","jump left up","jump left down",
                          "down","jump down","jump down left", "jump down right"]
        actions = []

        for move in possible_moves:
            if self.is_valid_step(player, move):
                actions.append(move)

        return actions
    
    def player_move(self,player,action):

        player_pos = self.get_player_position(player)

        if action[0] == "move":
            move = action[1]
            self.set_player_position(player,self.calculate_new_position(player_pos, action))
        
        elif action[0] == "place_barrier":
            barrier = action[1]
            self.barriers.add(barrier)
            self.players[player]["barriers_left"] -= 1
    
    def calculate_new_position(self, pos, action):
        
        moves = {
            "up": [-1,0],
            "jump up": [-2,0],
            "jump up left": [-1,-1],
            "jump up right": [-1,1],
            "right": [0,1],
            "jump right": [0, 2],
            "jump right up": [-1,1],
            "jump right down": [1,1],
            "left": [0,-1],
            "jump left": [0,-2],
            "jump left up": [-1,-1],
            "jump left down": [1,-1],            
            "down": [1,0],
            "jump down": [2,0],
            "jump down left": [1,-1],
            "jump down right": [1,1]
        }

        new_pos = (pos[0]+ moves[action[1]][0], pos[1]+ moves[action[1]][1])

        return new_pos





def test():
    env = Env(9,10)
    agent1 = DeterministicAgent(1)
    agent2 = DeterministicAgent(2)

    while env.turn < env.max_turns:

        print(f"Turno: {env.turn}")
        env.display_board()
        if env.turn % 2 == 0:
            action = agent1.choose_action(env)
            print("Player 1: ",end="")
            print(action)
            env.player_move(1, action)
        else:
            action = agent2.choose_action(env)
            print("Player 2: ",end="")
            print(action)
            env.player_move(2, action)

        env.turn += 1
        print("-----------------------------------------------------------")



if __name__ == "__main__":
    test()