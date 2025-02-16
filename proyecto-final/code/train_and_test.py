from Env import Env
from DeterministicAgent import DeterministicAgent
from RLAgent import RLAgent, train_agent, calculate_reward, is_game_finished

import random

# Prueba del entrenamiento y evaluación del RLAgent
def test_score_progression():
    # Inicializar el entorno y los agentes
    env_size = 9
    barriers = 3 if env_size == 5 else 10

    env = Env(env_size, barriers)

    deterministic_agent = DeterministicAgent(1)
    rl_agent = RLAgent(2, alpha=0.2, gamma=0.9, epsilon=1.0, epsilon_decay_rate=0.999)

    # Entrenar el agente RL y guardar datos en CSV
    file_path = 'score_progression_9x9_5000.csv'
    print("Iniciando entrenamiento...")
    train_agent(env, rl_agent, deterministic_agent, episodes=5000, save_results=True, file_path=file_path)
    print("Entrenamiento finalizado.\n")

    # Reiniciar el entorno para la prueba después del entrenamiento
    env.reset()

    print("Iniciando prueba después del entrenamiento...")
    tests_num = 100
    total_wins = 0
    for tests in range(tests_num):
        env.reset()
        winner = 0
        score = 0
        turn = 0

        # Aleatorizar que jugador empieza
        if random.choice([True, False]):
            first_turn = 1
        else:
            first_turn = 2

        while winner == 0:
            state = env.get_state()  # Estado actual
            #env.display_board()
            if turn % 2 == 0:
                if first_turn == 1:
                    action = deterministic_agent.choose_action(env)
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
                    action = deterministic_agent.choose_action(env)
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

        total_wins += 1 if winner == 2 else 0
    
    win_rate = total_wins / tests_num * 100
    print(win_rate)

if __name__ == '__main__':
    test_score_progression()