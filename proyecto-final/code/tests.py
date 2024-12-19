from Env import Env
from DeterministicAgent import DeterministicAgent
from RLAgent import RLAgent, train_agent

# Prueba inicial de los agentes y el entorno
def test():
    env = Env(5,3)
    agent1 = DeterministicAgent(1)
    agent2 = RLAgent(2,0.1,0.995,0.2)

    train_agent(env,agent2,agent1)

    env.reset()

    while env.turn < env.max_turns:

        print(f"Turno: {env.turn}")
        env.display_board()
        if env.turn % 2 == 0:
            action = agent1.choose_action(env)
            print("Player 1: ",end="")
            print(f"Score: {env.players[1]['score']}", end="")
            print(action)
            env.player_move(1, action)
        else:
            action = agent2.choose_action(env)
            print("Player 2: ",end="")
            print(f"Score: {env.players[2]['score']}", end="")
            print(action)
            env.player_move(2, action)

        env.turn += 1
        print("-----------------------------------------------------------")
    
    print(f"Player 1 - score: {env.players[1]['score']}")
    print(f"Player 2 - score: {env.players[2]['score']}")

if __name__ == '__main__':
    test()