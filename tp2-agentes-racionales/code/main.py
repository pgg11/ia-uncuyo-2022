from agent import RandomAgent, SimpleReflectiveAgent
from environment import Environment
from random import randint  
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from time import sleep


#   Funcion que corre cada simulación

def run_simulation(size,dirt_rate,iterations):



    agent1_performances = list()
    agent2_performances = list()
    for i in range(iterations):
        init_posX = randint(0,size-1)
        init_posY = randint(0,size-1)

        env1 = Environment(size,size,init_posX,init_posY,dirt_rate)
        env1.generate_dirt()
        agent1 = SimpleReflectiveAgent(env1,action_moves)

        env2 = Environment(size,size,init_posX,init_posY,dirt_rate)
        env2.generate_dirt()
        agent2 = RandomAgent(env2,action_moves)

        while agent2.remaining_actions > 0:
            agent1.think()
            agent2.think()
        agent1_performances.append(agent1.env.get_performance())
        agent2_performances.append(agent2.env.get_performance())

    agent1_avg = sum(agent1_performances) / iterations
    agent2_avg = sum(agent2_performances) / iterations

    return {'size':size,'dirt_rate':dirt_rate,'simple_agent_performances':agent1_performances,'random_agent_performances':agent2_performances,
    'simple_agent_avg':agent1_avg,'random_agent_avg':agent2_avg}


#   Constantes de analisis

iterations = 10
action_moves = 1000
sizes = [2,4,8,16,32,64,128]
dirt_rates = [0.1,0.2,0.4,0.8]


##  Entornos
#Lista con los resultados de todas las simulaciones, inicialmente vacío
results = list()
#   Entornos de 2x2
results.append(run_simulation(sizes[0],dirt_rates[0],iterations))
results.append(run_simulation(sizes[0],dirt_rates[1],iterations))
results.append(run_simulation(sizes[0],dirt_rates[2],iterations))
results.append(run_simulation(sizes[0],dirt_rates[3],iterations))

#   Entornos de 4x4
results.append(run_simulation(sizes[1],dirt_rates[0],iterations))
results.append(run_simulation(sizes[1],dirt_rates[1],iterations))
results.append(run_simulation(sizes[1],dirt_rates[2],iterations))
results.append(run_simulation(sizes[1],dirt_rates[3],iterations))

#   Entornos de 8x8
results.append(run_simulation(sizes[2],dirt_rates[0],iterations))
results.append(run_simulation(sizes[2],dirt_rates[1],iterations))
results.append(run_simulation(sizes[2],dirt_rates[2],iterations))
results.append(run_simulation(sizes[2],dirt_rates[3],iterations))

#   Entornos de 16x16
results.append(run_simulation(sizes[3],dirt_rates[0],iterations))
results.append(run_simulation(sizes[3],dirt_rates[1],iterations))
results.append(run_simulation(sizes[3],dirt_rates[2],iterations))
results.append(run_simulation(sizes[3],dirt_rates[3],iterations))

#   Entornos de 32x32
results.append(run_simulation(sizes[4],dirt_rates[0],iterations))
results.append(run_simulation(sizes[4],dirt_rates[1],iterations))
results.append(run_simulation(sizes[4],dirt_rates[2],iterations))
results.append(run_simulation(sizes[4],dirt_rates[3],iterations))

#   Entornos de 64x64
results.append(run_simulation(sizes[5],dirt_rates[0],iterations))
results.append(run_simulation(sizes[5],dirt_rates[1],iterations))
results.append(run_simulation(sizes[5],dirt_rates[2],iterations))
results.append(run_simulation(sizes[5],dirt_rates[3],iterations))

#   Entornos de 128x128
results.append(run_simulation(sizes[6],dirt_rates[0],iterations))
results.append(run_simulation(sizes[6],dirt_rates[1],iterations))
results.append(run_simulation(sizes[6],dirt_rates[2],iterations))
results.append(run_simulation(sizes[6],dirt_rates[3],iterations))

#   Recopilación de los resultados en una hoja de calculo de google

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("tp2-agentes-racionales/code/tp2-agentes-racionales-86fcc92c5d7a.json", scope)
client = gspread.authorize(creds)
sheet = client.open("results").sheet1  #Abrir spreadhseet

insertRow = ['agent','dirt_rate','performance']
sheet.append_row(insertRow)
sizes = ['2x2','4x4','8x8','16x16','32x32','64x64','128x128']
size = 0

for result in results:
    insertRow = [result['size']]
    sheet.append_row(insertRow)
    for i in range(10):
        insertRow1 = ['simple_reflective',result['dirt_rate'],result['simple_agent_performances'][i]] #Preparando lista a insertar
        insertRow2 = ['random',result['dirt_rate'],result['random_agent_performances'][i]] #Preparando lista a insertar
        sheet.append_row(insertRow1)
        sheet.append_row(insertRow2)
    sleep(60)