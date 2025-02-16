import numpy as np
import random
import os
import pandas as pd

class RLAgent:
    def __init__(self, player_id, alpha=0.01, gamma=0.95, epsilon=0.05, epsilon_decay_rate=0.99):
        self.player_id = player_id
        self.alpha = alpha      # Tasa de aprendizaje
        self.gamma = gamma      # Factor de descuento
        self.epsilon = epsilon  # Parámetro de exploración
        self.epsilon_decay_rate = epsilon_decay_rate  # Tasa de descuento para epsilon
        self.q_table = {}       # Diccionario para almacenar la Q-Table

    def get_player_id(self):
        return self.player_id

    def get_q_value(self, state, action):
        # Obtiene el valor Q para un estado y acción específicos
        return self.q_table.get((state, action), 0.0)

    def update_q_value(self, actions, state, action, reward, next_state):
        # Actualiza el valor Q usando la fórmula de Q-learning
        max_next_q = max([self.get_q_value(next_state, a) for a in actions], default=0.0)
        current_q = self.get_q_value(state, action)
        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
        self.q_table[(state, action)] = new_q

    def choose_action(self, env):
        # Selecciona una acción usando una política epsilon-greedy
        actions = env.get_actions(self.get_player_id())
        available_barriers = env.get_available_barriers()
        state = env.get_state()
        #print(actions)
        #env.display_board()
        if random.random() < self.epsilon:  # Exploración
            selected_action = random.choice(actions)
            return selected_action
        else:  # Explotación
            q_values = {action: self.get_q_value(state, action) for action in actions}
            max_q = max(q_values.values())
            best_actions = [action for action, q in q_values.items() if q == max_q]
            selected_action = random.choice(best_actions)
            return selected_action


    def decay_epsilon(self):
        #Reduce el valor de epsilon para explorar menos con el tiempo
        if self.epsilon * self.epsilon_decay_rate < 0.1: #Establece un piso para el epsilon
            self.epsilon = 0.1
        else:
            self.epsilon *= self.epsilon_decay_rate


def train_agent(env, rl_agent, opponent_agent, episodes=1000, save_results = False, file_path = None):

    if save_results:
        results = []  # Lista para almacenar los resultados
    max_turns = 20 * env.size
    total_wins = 0

    for episode in range(episodes):
        env.reset()  # Reinicia el entorno para un nuevo episodio

        # Aleatorizar que jugador empieza
        if random.choice([True, False]):
            first_turn = 1
        else:
            first_turn = 2

        turn = 0
        winner = 0
        score = 0
        match_result = "Lose"
        #print(f"Episodio: {episode}")
        while winner == 0 and turn < max_turns:
            state = env.get_state()  # Estado actual
            #env.display_board()
            if turn % 2 == 0:
                if first_turn == 1:
                    action = opponent_agent.choose_action(env)
                    env.player_move(1, action)
                else:
                    action = rl_agent.choose_action(env)
                    actions = env.get_actions(rl_agent.get_player_id())
                    env.player_move(2, action)
                    reward = calculate_reward(env,action,2,1,turn)
                    score += reward
                    next_state = env.get_state()
                    rl_agent.update_q_value(actions, state, action, reward, next_state)
                
                #print("Player 1: ",end="")
                #print(action)
                
            else:
                if first_turn == 2:
                    action = opponent_agent.choose_action(env)
                    env.player_move(1, action)
                else:
                    action = rl_agent.choose_action(env)
                    actions = env.get_actions(rl_agent.get_player_id())
                    #print("Player 1: ",end="")
                    #print(action)
                    env.player_move(2, action)
                    reward = calculate_reward(env,action,2,1,turn)
                    score += reward
                    next_state = env.get_state()
                    rl_agent.update_q_value(actions, state, action, reward, next_state)

            winner = is_game_finished(env)
            turn += 1
        if winner == rl_agent.player_id:
            match_result = "Win"
        elif turn > max_turns:
            match_result = "Draw"

        if save_results:

            episode_interval = 1 # Número de episodios entre mediciones

            if episode % episode_interval == 0 and episode > 0:
                results.append([episode, rl_agent.epsilon, match_result, score, turn])  # Agrega a la lista

        rl_agent.decay_epsilon()  # Decae epsilon tras cada episodio

    if save_results and results:
        df = pd.DataFrame(results, columns=['Episode', 'Current_Epsilon', 'Win|Lose', 'Score', 'Turns'])
        df.to_csv(file_path, mode='w', index=False, header=True)

    env.reset()  # Reinicia el entorno luego del entrenamiento

def calculate_reward(env,action,rl_agent_id,deterministic_agent_id,turn):
    reward = 0

    if action[0] == "move":
        row_position = env.get_player_position(rl_agent_id)[0]
        goal_row = 0 if rl_agent_id == 2 else env.get_size()-1
        factor = -1 if rl_agent_id == 1 else 1
        if action[1] == "up" or action[1] == "jump up" or action[1] == "jump up left" or action[1] == "jump up right":
            reward = factor * 2 ** (env.size - abs(goal_row - row_position))
        elif action[1] == "left" or action[1] == "jump left" or action[1] == "right" or action[1] == "jump right":
            reward = - 2 * turn
        else:
            reward = -factor * (2 ** (env.size - abs(goal_row - row_position)))
    elif action[0] == "place_barrier" and env.players[rl_agent_id]["barriers_left"] > 0:
        opponent_position = env.players[deterministic_agent_id]["position"]
        orientation, x, y = action[1]
        if orientation == "H" and (y == opponent_position[1] or y == opponent_position[1]+1):
            reward = env.size**2 # Recompensa por bloquear oponente con barrera
        else:
            reward = env.size * -10  # Penalizar si la barrera no bloquea al oponente

    return reward

def is_game_finished(env):
    if env.players[1]['position'][0] >= env.size-1:
        return 1
    elif env.players[2]['position'][0] <= 0:
        return 2
    else:
        return 0