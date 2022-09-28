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

dls_limit = 70 # limite para el algoritmo DLS


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
sheet = client.open("results-tp3").sheet1  #Abrir spreadhseet

insertRow = ['data','bfs-agent','dfs-agent','dls-agent','ucs-agent']
sheet.append_row(insertRow)

for simulation in simulations:
    insertRow1 = ['states_explored',bfs_results[simulation]['states_explored'],dfs_results[simulation]['states_explored'],dls_results[simulation]['states_explored'],ucs_results[simulation]['states_explored']] #Preparando lista a insertar
    insertRow2 = ['path_lenght',bfs_results[simulation]['path_lenght'],dfs_results[simulation]['path_lenght'],dls_results[simulation]['path_lenght'],ucs_results[simulation]['path_lenght']] #Preparando lista a insertar

    sheet.append_row(insertRow1)
    sheet.append_row(insertRow1)