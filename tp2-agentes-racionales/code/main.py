from agent import RandomAgent, SimpleReflectiveAgent
from environment import Environment
from random import randint

init_posX = randint(0,9)
init_posY = randint(0,9)
sizeX = 32
sizeY = 32
dirt_rate = 0.8
moves = 20

env1 = Environment(sizeX,sizeY,init_posX,init_posY,dirt_rate)
env1.generate_dirt()

agent1 = SimpleReflectiveAgent(env1,moves)


while agent1.remaining_actions > 0:
    posY = agent1.env.get_posY()
    posX = agent1.env.get_posX()
    #print(f"Fila: {posY} | Columna:{posX}")
    #print(agent1.env.board[posY][posX])
    #agent1.env.print_environment()
    agent1.think()




env2 = Environment(sizeX,sizeY,init_posX,init_posY,dirt_rate)
env2.generate_dirt()

agent2 = RandomAgent(env2, moves)

while agent2.remaining_actions > 0:
    posY = agent2.env.get_posY()
    posX = agent2.env.get_posX()
    #print(f"Fila: {posY} | Columna:{posX}")
    #print(agent2.env.board[posY][posX])
    #agent2.env.print_environment()
    agent2.think()

print(f"Entorno {sizeX}x{sizeY}   |   dirt_rate: {dirt_rate}  |   cantidad_de_movimientos: {moves}" )
print(f"Performance agente reflexivo simple: {agent1.env.get_performance()}")
print(f"Performance agente aleatorio: {agent2.env.get_performance()}")
