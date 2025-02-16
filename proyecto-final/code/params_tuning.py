from Env import Env
from DeterministicAgent import DeterministicAgent
from RLAgent import RLAgent, train_agent, calculate_reward, is_game_finished

import os
import pandas as pd
import random

def tune():

    env_size = 9 # Tamaño del entorno
    alpha_values = [0.1, 0.2]
    gamma_values = [0.9]
    epsilon_values = [1.0]
    epsilon_decay_values = [0.999]
    episodes_values = [1000, 2500, 5000]

    tests = 100
    
    results = []  # Lista para almacenar los resultados

    file_path = 'q_learning_tuning_results_9x9.csv'
    ##
    # Cargar el CSV existente para ver qué configuraciones ya se probaron
    completed_configs = set()
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            config = (row['Alpha'], row['Gamma'], row['Epsilon'], row['Epsilon_Decay'], row['Episodes'])
            completed_configs.add(config)
    ##
    write_header = not os.path.exists(file_path)  # Solo escribir la cabecera si el archivo no existe

    current_test = 0
    
    for alpha in alpha_values:
        for gamma in gamma_values:
            for epsilon in epsilon_values:
                for epsilon_decay in epsilon_decay_values:
                    for episodes_num in episodes_values:
                        ##
                        config = (alpha, gamma, epsilon, epsilon_decay, episodes_num)
                        
                        # Si esta configuración ya está en el CSV, saltarla
                        if config in completed_configs:
                            print(f"Skipping completed configuration: {config}")
                            current_test += tests
                            continue
                        ##
                        barriers = 10

                        if env_size == 5:
                            barriers = 3

                        env = Env(env_size,barriers)

                        agent1 = DeterministicAgent(1)
                        agent2 = RLAgent(2,alpha,gamma,epsilon,epsilon_decay)

                        train_agent(env,agent2,agent1, episodes_num)

                        total_wins = 0
                        total_score = 0
                        total_barriers_placed = 0
                        for test in range(tests):
                            current_test += 1
                            print(f"Current test: {current_test}")
                            rl_agent_win,score,barriers_placed= run_test(env,agent2,agent1, alpha, gamma, epsilon, epsilon_decay, episodes_num)
                            total_wins += rl_agent_win
                            total_score += score
                            total_barriers_placed += barriers_placed

                        win_rate = (total_wins / tests) * 100
                        avg_score = total_score / tests
                        avg_barriers_placed = total_barriers_placed / tests

                        # Guardar inmediatamente después de completar los test de cada configuracion
                        df = pd.DataFrame([[alpha, gamma, epsilon, epsilon_decay, episodes_num, tests, win_rate, avg_score, avg_barriers_placed]], 
                                          columns=['Alpha', 'Gamma', 'Epsilon', 'Epsilon_Decay', 'Episodes', 'Tests_qty','Win_Rate','Avg_Score','Avg_Barriers_Placed'])
                        df.to_csv(file_path, mode='a', index=False, header=write_header)
                        write_header = False  # Asegurar que la cabecera solo se escriba una vez


def run_test(env,rl_agent,opponent_agent,alpha,gamma,epsilon,epsilon_decay,episodes):

    env.reset()

    barriers = 10 if env.size == 9 else 3

    winner = 0
    score = 0
    max_turns = 20 * env.size
    turn = 0

    # Aleatorizar que jugador empieza
    if random.choice([True, False]):
        first_turn = 1
    else:
        first_turn = 2

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
                env.player_move(2, action)
                reward = calculate_reward(env,action,2,1,turn)
                score += reward
                next_state = env.get_state()
                rl_agent.update_q_value(actions, state, action, reward, next_state)

            #print("Player 2: ",end="")
            #print(action)

        winner = is_game_finished(env)
        turn += 1

    barriers_placed = abs(env.players[rl_agent.player_id]["barriers_left"] - barriers)
    rl_agent_win = 1 if rl_agent.get_player_id() == winner else 0

    return(rl_agent_win,score,barriers_placed)

if __name__ == '__main__':
    tune()