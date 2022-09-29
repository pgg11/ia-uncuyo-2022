from environment import Environment
from BFSAgent import BFSAgent
from DFSAgent import DFSAgent
from DLSAgent import DLSAgent
from UCSAgent import UCSAgent

from random import randint
import gspread
from oauth2client.service_account import ServiceAccountCredentials


## Constantes

size = 100
simulations = 30

dls_limit = 100 # limite para el algoritmo DLS


## Variables

environments = list()

for i in range(simulations):
    initial_posX = randint(0,99)
    initial_posY = randint(0,99)
    goal_posX = randint(0,99)
    goal_posY = randint(0,99)
    obstacles_rate = randint(5,10) / 100 #Obstaculos en entre un 5% y un 10% de las casillas 
    environments.append(Environment(size,initial_posX,initial_posY,goal_posX,goal_posY,obstacles_rate))


bfs_results = list()
dfs_results = list()
dls_results = list()
ucs_results = list()


# Simulaciones

bfs_agent = BFSAgent(environments[0])
dfs_agent = DFSAgent(environments[0])
dls_agent = DLSAgent(environments[0],dls_limit)
ucs_agent = UCSAgent(environments[0])


for env in environments:
    env.generate_obstacles()

    bfs_agent.reset_agent()
    bfs_agent.update_env(env)
    bfs_path = bfs_agent.think()
    bfs_states_explored = len(bfs_agent.graph)
    
    bfs_results.append({'states_explored':bfs_states_explored,'path_lenght':len(bfs_path)})

    dfs_agent.reset_agent()
    dfs_agent.update_env(env)
    dfs_path = dfs_agent.think()
    dfs_states_explored = len(dfs_agent.graph)
    
    dfs_results.append({'states_explored':dfs_states_explored,'path_lenght':len(dfs_path)})

    dls_agent.reset_agent()
    dls_agent.update_env(env)
    dls_path = dls_agent.think()
    dls_states_explored = len(dls_agent.graph)
    
    dls_results.append({'states_explored':dls_states_explored,'path_lenght':len(dls_path)})

    ucs_agent.reset_agent()
    ucs_agent.update_env(env)
    ucs_path = ucs_agent.think()
    ucs_states_explored = len(ucs_agent.graph)
    
    ucs_results.append({'states_explored':ucs_states_explored,'path_lenght':len(ucs_path)})


# Recopilación de resultados en google sheets

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("tp3-busquedas-no-informadas/code/tp3-busqueda-no-informada-5406f79cbf97.json",scope)
client = gspread.authorize(creds)
sheet = client.open("no-informada-results").sheet1  #Abrir spreadhseet

insertRow = ['algorithm_name','run_n','estate_n','solution_found']
sheet.append_row(insertRow)

for i in range(simulations):

    if bfs_results[i]['path_lenght'] > 0 :
        bfs_path = "True"
    else:
        bfs_path = "False"
    
    if dfs_results[i]['path_lenght'] > 0 :
        dfs_path = "True"
    else:
        dfs_path = "False"
    
    if dls_results[i]['path_lenght'] > 0 :
        dls_path = "True"
    else:
        dls_path = "False"
    
    if ucs_results[i]['path_lenght'] > 0 :
        ucs_path = "True"
    else:
        ucs_path = "False"  

    run = i+18

    insertRow1 = ['bfs',run,bfs_results[i]['states_explored'],bfs_path]
    insertRow2 = ['dfs',run,dfs_results[i]['states_explored'],dfs_path]
    insertRow3 = ['dls',run,dls_results[i]['states_explored'],dls_path]
    insertRow4 = ['ucs',run,ucs_results[i]['states_explored'],ucs_path]

    sheet.append_row(insertRow1)
    sheet.append_row(insertRow2)
    sheet.append_row(insertRow3)
    sheet.append_row(insertRow4)