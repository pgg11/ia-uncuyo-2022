import numpy as np
import random

class RLAgent:
    def __init__(self, player_id, alpha=0.1, gamma=0.95, epsilon=0.3):
        self.player_id = player_id
        self.alpha = alpha      # Tasa de aprendizaje
        self.gamma = gamma      # Factor de descuento
        self.epsilon = epsilon  # Parámetro de exploración
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
        print(actions)
        env.display_board()
        if random.random() < self.epsilon:  # Exploración
            selected_action = random.choice(actions)
            if selected_action == 'place_barrier':
                return (selected_action, random.choice(available_barriers))
            else:
                return ("move", selected_action)
        else:  # Explotación
            q_values = {action: self.get_q_value(state, action) for action in actions}
            max_q = max(q_values.values())
            best_actions = [action for action, q in q_values.items() if q == max_q]
            selected_action = random.choice(best_actions)
            if selected_action == 'place_barrier':
                return (selected_action, random.choice(available_barriers))
            else:
                return ("move",selected_action)

    def decay_epsilon(self, decay_rate):
        #Reduce el valor de epsilon para explorar menos con el tiempo
        self.epsilon *= decay_rate


def train_agent(env, rl_agent, opponent_agent, episodes=500, max_turns=64):
    for episode in range(episodes):
        env.reset()  # Reinicia el entorno para un nuevo episodio
        for turn in range(max_turns):
            state = env.get_state()  # Estado actual

            if turn % 2 == 0:
                action = opponent_agent.choose_action(env)
                #print("Player 1: ",end="")
                #print(action)
                env.player_move(1, action)
            else:
                action = rl_agent.choose_action(env)
                actions = env.get_actions(rl_agent.get_player_id())
                #print("Player 2: ",end="")
                #print(action)
                env.player_move(2, action)
                reward = 0

                if action[0] == "move":
                    row_position = env.get_player_position(rl_agent.get_player_id())[0]
                    goal_row = 0 if rl_agent.get_player_id() == 2 else 8
                    if action[1] == "up" or action[1] == "jump up" or action[1] == "jump up left" or action[1] == "jump up right":
                        reward = 2 ** (env.size - abs(goal_row - row_position))
                    elif action[1] == "left" or action[1] == "jump left" or action[1] == "right" or action[1] == "jump right":
                        reward = -(env.size - abs(goal_row - row_position))
                    else:
                        reward = -(2 ** (env.size - abs(goal_row - row_position)))

                elif action[0] == "place_barrier" and env.players[rl_agent.get_player_id()]["barriers_left"] > 0:

                    reward = 5  # Recompensa por colocar una barrera

                next_state = env.get_state()
                rl_agent.update_q_value(actions, state, action, reward, next_state)

                rl_agent.decay_epsilon(0.995)  # Decae epsilon tras cada episodio    
    
    env.reset()  # Reinicia el entorno luego del entrenamiento