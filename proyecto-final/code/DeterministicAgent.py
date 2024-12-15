import random

class DeterministicAgent:
    
    def __init__(self, player_id):
        self.player_id = player_id

    def get_player_id(self):
        return self.player_id

    def choose_action(self, env):
        opponent_id = 2 if self.player_id == 1 else 1
        player_pos = env.players[self.player_id]["position"]
        opponent_pos = env.players[opponent_id]["position"]
        player_barriers_left = env.players[self.player_id]["barriers_left"]
        opponent_goal_row = 0 if opponent_id == 2 else env.size - 1
        player_goal_row = 0 if self.player_id == 2 else env.size - 1
        barriers = env.get_barriers()
        size = env.get_size()

        # 1. Avance hacia la meta
        actions = env.get_actions(self.player_id)
        print(f"player 1: {actions}")
        
        if self.player_id == 1:
            if "down" in actions:
                return ("move","down")
            elif "jump down" in actions:
                return ("move","jump down")

        elif self.player_id == 2:
            if "up" in actions:
                return ("move","up")
            elif "jump up" in actions:
                return ("move","jump up")

        # 2. Colocación de paredes
        available_barriers = env.get_available_barriers()
        if player_barriers_left > 0:

            if self.player_id == 1:
                if abs(opponent_pos[0] - opponent_goal_row) > 3 and ("H", opponent_pos[0] - 2, opponent_pos[1]) not in barriers and ("H", opponent_pos[0] - 1, opponent_pos[1]) not in barriers:
                    if ("H", opponent_pos[0]-3, opponent_pos[1]) in available_barriers:
                        return ("place_barrier", ("H", opponent_pos[0]-3, opponent_pos[1]))

                elif abs(opponent_pos[0] - opponent_goal_row) > 2 and ("V", opponent_pos[0], opponent_pos[1] - 1) not in barriers:
                    if ("V", opponent_pos[0]-1, opponent_pos[1]-1) in available_barriers:
                        return ("place_barrier", ("V", opponent_pos[0]-1, opponent_pos[1]-1))

                elif abs(opponent_pos[0] - opponent_goal_row) > 1:
                    if ("V", opponent_pos[0], opponent_pos[1]) in available_barriers:
                        return ("place_barrier", ("V", opponent_pos[0], opponent_pos[1]))
            
            else:
                if abs(opponent_pos[0] - opponent_goal_row) > 3 and ("H", opponent_pos[0] + 1, opponent_pos[1]) not in barriers and ("H", opponent_pos[0], opponent_pos[1]) not in barriers:
                    if ("H", opponent_pos[0]+2, opponent_pos[1]) in available_barriers:
                        return ("place_barrier", ("H", opponent_pos[0]+2, opponent_pos[1]))

                elif abs(opponent_pos[0] - opponent_goal_row) > 2 and ("V", opponent_pos[0] - 1, opponent_pos[1] - 1) not in barriers:
                    if ("V", opponent_pos[0], opponent_pos[1]-1) in available_barriers:
                        return ("place_barrier", ("V", opponent_pos[0], opponent_pos[1]-1))

                elif abs(opponent_pos[0] - opponent_goal_row) > 1:
                    if ("V", opponent_pos[0], opponent_pos[1]) in available_barriers:
                        return ("place_barrier", ("V", opponent_pos[0]-1, opponent_pos[1]))

        # 3. Movimiento lateral
        lateral_moves = [move for move in ["left", "right", "jump left", "jump right"] if move in actions]
        if lateral_moves:
            return ("move",random.choice(lateral_moves))

        # 4. Retroceso
        if self.player_id == 1 and ("up" in actions or "jump up" in actions):
            return ("move","up")
        elif self.player_id == 2 and ("down" in actions or "jump down" in actions):
            return ("move","down")
            
    # def is_col_blocked(self, pos, barriers, size):
    #     player_id = self.get_player_id()
    #     goal_row = 0 if player_id == 2 else size - 1
        
    #     if player_id == 1:
    #         for i in range(pos[0],goal_row):
    #             if ("H", i, pos[1]) in barriers or ("H", i, pos[1]-1) in barriers:
    #                 return True
    #     else:
    #         for i in range(pos[0],goal_row,-1):
    #             if ("H", i-1, pos[1]) in barriers or ("H", i-1, pos[1]-1) in barriers:
    #                 return True
        
    #     return False