import numpy as np

class Env:
    def __init__(self, size=9, barriers_per_player=10):
        self.size = size
        self.board = np.zeros((size, size), dtype=int)  # 0: casilla libre, 1: jugador 1, 2: jugador 2
        self.barriers = set({})  # conjunto donde se guarda la posicion de las barreras. ej: ("H", x, y) {('V', 0, 0), ('V', 2, 3), ('H', 1, 1), ('H', 4, 0), ('V', 0, 1), ('V', 1, 2)}
        self.players = {
            1: {"position": (0,size // 2), "barriers_left": barriers_per_player, "score": 0},
            2: {"position": (size-1,size // 2), "barriers_left": barriers_per_player, "score": 0}
        }
        self.turn = 0
        self.max_turns = 50  # limite de turnos
    
    def reset(self):

        self.barriers = set()
        x1, y1 = self.players[1]["position"]
        x2, y2 = self.players[2]["position"]

        self.board[x1][y1] = 0
        self.board[x2][y2] = 0

        self.players[1]["position"] = (0, self.size//2)
        self.players[1]["barriers_left"] = 10 if self.size == 9 else 3
        self.players[1]["score"] = 0

        self.players[2]["position"] = (self.size-1 , self.size//2)
        self.players[2]["barriers_left"] = 10 if self.size == 9 else 3
        self.players[2]["score"] = 0

    def get_state(self):

        sorted_barriers = tuple(sorted(self.barriers))
        state = (self.players[2]["position"], sorted_barriers)

        return state
    
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
            if position[0] >= self.size-1:
                self.players[player]["position"] = (0 , self.size // 2)
        else:
            if position[0] <= 0:
                self.players[player]["position"] = (self.size-1 , self.size // 2)

    def display_board(self):

        x,y = self.players[1]["position"]
        x2,y2 = self.players[2]["position"]

        self.board[x][y] = 1
        self.board[x2][y2] = 2
        #print("Barriers:", self.barriers)
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
            if ("H", x - 1, y) not in self.barriers and ("H", x - 1 , y - 1) not in self.barriers:
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
        elif move == "jump down right" and (x < self.size - 1 and y < self.size - 1) and self.is_opponent_adjacent(self.players[player],self.players[opponent],"down"):
            if ("H", x, y) not in self.barriers and ("H", x, y - 1) not in self.barriers:
                if ("H", x+1, y) in self.barriers or ("H", x+1, y-1) in self.barriers:
                    if ("V", x, y) not in self.barriers and ("V", x+1, y) not in self.barriers:
                        return True
        elif move == "jump down left" and (x < self.size - 1 and y > 0) and self.is_opponent_adjacent(self.players[player],self.players[opponent],"down"):
            if ("H", x, y) not in self.barriers and ("H", x, y - 1) not in self.barriers:
                if ("H", x+1, y) in self.barriers or ("H", x+1, y-1) in self.barriers:
                    if ("V", x, y-1) not in self.barriers and ("V", x+1, y-1) not in self.barriers:
                        return True
        elif move == "jump up" and x > 0 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"up"):
            if ("H", x - 1, y) not in self.barriers and ("H", x - 1 , y - 1) not in self.barriers:
                if ("H", x-2, y) not in self.barriers and ("H", x-2, y - 1) not in self.barriers:
                    return True
        elif move == "jump up right" and (x > 0 and y < self.size-1) and self.is_opponent_adjacent(self.players[player],self.players[opponent],"up"):
            if ("H", x - 1, y) not in self.barriers and ("H", x - 1 , y + 1) not in self.barriers:
                if ("H", x-2, y) in self.barriers or ("H", x-2, y-1) in self.barriers:
                    if ("V", x-1, y) not in self.barriers and ("V", x-2, y) not in self.barriers:
                        return True
        elif move == "jump up left" and (x > 0 and y > 0) and self.is_opponent_adjacent(self.players[player],self.players[opponent],"up"):
            if ("H", x - 1, y) not in self.barriers and ("H", x - 1 , y + 1) not in self.barriers:
                if ("H", x-2, y) in self.barriers or ("H", x-2, y-1) in self.barriers:
                    if ("V", x-1, y-1) not in self.barriers and ("V", x-2, y-1) not in self.barriers:
                        return True
        elif move == "jump left" and y > 1 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"left"):
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
        elif move == "jump right" and y < self.size-2 and self.is_opponent_adjacent(self.players[player],self.players[opponent],"right"):
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
                actions.append(("move",move))
        
        available_barriers = self.get_available_barriers()

        if self.players[player]["barriers_left"] > 0:
            for barrier in available_barriers:
                actions.append(("place_barrier", barrier))

        return actions
    
    def is_valid_barrier(self, barrier):
        orientation, row, col = barrier
        if barrier in self.barriers:  # Si ya existe, no es válida
            return False
        # Verifica límites del tablero y superposiciones
        if orientation == "H" and (row < self.size - 1 and col < self.size - 1):
            if ("H", row, col-1) in self.barriers or ("H", row, col+1) in self.barriers:
                return False
            if ("V", row, col) in self.barriers:
                return False
        elif orientation == "V" and (row < self.size - 1 and col < self.size - 1):
            if ("V", row - 1, col) in self.barriers or ("V", row + 1, col) in self.barriers:
                return False
            if("H", row, col) in self.barriers:
                return False
        else:
            return False
        
        # Verifica que colocar la barrera no bloquee el camino de ningún jugador
        self.barriers.add(barrier)  # Simula agregar la barrera temporalmente
        initial_position_1 = (0, self.size // 2)
        initial_position_2 = (self.size-1, self.size // 2)
        goal_row_player_1 = self.size - 1
        goal_row_player_2 = 0

        if not self.is_path_to_goal(self.players[1]["position"], goal_row_player_1) or not self.is_path_to_goal(self.players[2]["position"], goal_row_player_2) or not self.is_path_to_goal(initial_position_1, goal_row_player_1) or not self.is_path_to_goal(initial_position_2,goal_row_player_2):
            self.barriers.remove(barrier)  # Revierte el cambio si no es válido
            return False

        self.barriers.remove(barrier)  # Revierte el cambio tras validación
        return True
    
    def is_path_to_goal(self, position, goal_row):
        # Verifica si hay un camino desde la posición actual del jugador hasta la fila objetivo
        from collections import deque

        start = position
        visited = set()
        queue = deque([start])

        while queue:
            x, y = queue.popleft()

            if x == goal_row:  # Si alcanza la fila objetivo, hay camino
                return True

            if (x, y) in visited:
                continue

            visited.add((x, y))

            # Genera movimientos posibles y verifica barreras
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Arriba, abajo, izquierda, derecha
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.size and 0 <= ny < self.size:  # Dentro del tablero
                    if dx == -1 and ("H", x - 1, y) not in self.barriers and ("H", x - 1, y - 1) not in self.barriers:
                        queue.append((nx, ny))
                    elif dx == 1 and ("H", x, y) not in self.barriers and ("H", x, y - 1) not in self.barriers:
                        queue.append((nx, ny))
                    elif dy == -1 and ("V", x - 1, y - 1) not in self.barriers and ("V", x, y - 1) not in self.barriers:
                        queue.append((nx, ny))
                    elif dy == 1 and ("V", x, y) not in self.barriers and ("V", x - 1, y) not in self.barriers:
                        queue.append((nx, ny))

        return False  # No encontró camino

    def get_available_barriers(self):
        possible_barriers = []  # Lista de barreras posibles en formato (orientación, fila, columna)
        orientations = ["H", "V"]  # "H" para horizontal, "V" para vertical

        for row in range(self.size - 1):  # Considera barreras entre filas
            for col in range(self.size - 1):  # Considera barreras entre columnas
                for orientation in orientations:
                    barrier = (orientation, row, col)
                    if self.is_valid_barrier(barrier):  # Verifica si la barrera es válida
                        possible_barriers.append(barrier)

        return possible_barriers
    
    def player_move(self,player,action):

        player_pos = self.get_player_position(player)

        if action[0] == "move":
            move = action[1]
            self.set_player_position(player,self.calculate_new_position(player_pos, action))

            row_position = self.get_player_position(player)[0]
            goal_row = 0 if player == 2 else self.size-1
            factor = -1 if player == 1 else 1
            if move in ["up", "jump up", "jump up left", "jump up right"]:
                self.players[player]["score"] += factor * 2 ** (self.size - abs(goal_row - row_position))
            elif move in ["left", "jump left", "right", "jump right"]:
                self.players[player]["score"] += 0
            else:
                self.players[player]["score"] += -factor * (2 ** (self.size - abs(goal_row - row_position)))

        elif action[0] == "place_barrier":
            barrier = action[1]
            self.barriers.add(barrier)
            self.players[player]["barriers_left"] -= 1
            self.players[player]["score"] += 10
    
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