from Env import Env
from DeterministicAgent import DeterministicAgent
from RLAgent import RLAgent, train_agent

# Prueba del entrenamiento y evaluación del RLAgent
def test_score_progression():
    # Inicializar el entorno y los agentes
    env = Env(9, 10)
    agent1 = DeterministicAgent(1)
    agent2 = RLAgent(2, alpha=0.1, gamma=0.95, epsilon=1.0, epsilon_decay_rate=0.995)

    # Entrenar el agente RL y guardar datos en CSV
    print("Iniciando entrenamiento...")
    train_agent(env, agent2, agent1, episodes=1000, max_turns=45, save_results=True)
    print("Entrenamiento finalizado.\n")

    # Reiniciar el entorno para la prueba después del entrenamiento
    env.reset()

    print("Iniciando prueba después del entrenamiento...")
    while env.turn < env.max_turns:
        if env.turn % 2 == 0:
            action = agent1.choose_action(env)  # Acción del agente determinístico
            env.player_move(1, action)
        else:
            action = agent2.choose_action(env)  # Acción del agente RL entrenado
            env.player_move(2, action)

        env.turn += 1  # Avanzar el turno

    # Mostrar resultados finales
    print(f"\nResultados finales:")
    print(f"Player 1 - Deterministic - Score: {env.players[1]['score']}")
    print(f"Player 2 - RL - Score: {env.players[2]['score']}")

if __name__ == '__main__':
    test_score_progression()