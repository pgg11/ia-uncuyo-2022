from Env import Env
from DeterministicAgent import DeterministicAgent
from RLAgent import RLAgent, train_agent

import os
import pandas as pd

def tune():

    env_size = 9 # Tamaño del entorno
    alpha_values = [0.1, 0.5]
    gamma_values = [0.9]
    epsilon_values = [1.0]
    epsilon_decay_values = [0.99]
    episodes_values = [50, 100, 250, 500, 750, 1000]

    simulations = 3
    
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

    current_simulation = 0
    
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
                            current_simulation += simulations
                            continue
                        ##
                        score = 0
                        for simulation in range(simulations):
                            current_simulation += 1
                            print(f"Current simulation: {current_simulation}")
                            score += run_simulation(env_size, alpha, gamma, epsilon, epsilon_decay, episodes_num)
                        avg_score = score / simulations
                        
                        # Guardar inmediatamente después de completar 5 simulaciones
                        df = pd.DataFrame([[alpha, gamma, epsilon, epsilon_decay, episodes_num, simulations, avg_score]], 
                                          columns=['Alpha', 'Gamma', 'Epsilon', 'Epsilon_Decay', 'Episodes', 'Simulations', 'Avg_Score'])
                        df.to_csv(file_path, mode='a', index=False, header=write_header)
                        write_header = False  # Asegurar que la cabecera solo se escriba una vez


def run_simulation(env_size,alpha,gamma,epsilon,epsilon_decay,episodes):

    barriers = 10

    if env_size == 5:
        barriers = 3

    env = Env(env_size,barriers)
    agent1 = DeterministicAgent(1)
    agent2 = RLAgent(2,alpha,gamma,epsilon,epsilon_decay)

    train_agent(env,agent2,agent1, episodes, 45) # 45 turnos

    env.reset()


    while env.turn < env.max_turns:

        if env.turn % 2 == 0:
            action = agent1.choose_action(env)
            env.player_move(1, action)
        else:
            action = agent2.choose_action(env)
            env.player_move(2, action)

        env.turn += 1

    return(env.players[2]['score'] - env.players[1]['score'])

if __name__ == '__main__':
    tune()