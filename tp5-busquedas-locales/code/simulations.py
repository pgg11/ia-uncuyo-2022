from hill_climbing import HillClimbingAgent
from genetic import GeneticAgent
from simulated_annealing import SimulatedAnnealingAgent

from random import randint
from time import time

import pandas

queen_n = [4,8,10]
max_time = 30

t = 100 #simulated annealing

hillClimbingResults_4Q = list()
simulatedAnnealingResults_4Q = list()
geneticResults_4Q = list()

hillClimbingResults_8Q = list()
simulatedAnnealingResults_8Q = list()
geneticResults_8Q = list()

hillClimbingResults_10Q = list()
simulatedAnnealingResults_10Q = list()
geneticResults_10Q = list()

## Simulaciones para 4 reinas

results_4Q = pandas.DataFrame(columns = ['algorithm_name', 'h', 'n_states', 'time_elapsed'])
results_4Q = results_4Q.append(pandas.Series(['algorithm_name', 'h', 'n_states', 'time_elapsed'], index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)


for iter in range(30):
    env = list()
    for i in range(4):
        rand_num = randint(0,3)
        env.append(rand_num)

    hillClimbingAgent = HillClimbingAgent(env.copy())
    simulatedAnnealingAgent = SimulatedAnnealingAgent(env.copy())
    geneticAgent = GeneticAgent(4)

    hillClimbingResults_4Q.append(hillClimbingAgent.hillClimbing(max_time))
    simulatedAnnealingResults_4Q.append(simulatedAnnealingAgent.simulated_annealing(t,max_time))
    geneticResults_4Q.append(geneticAgent.genetic_algorithm(max_time))

    results_4Q = results_4Q.append(pandas.Series((['hillClimbing']+hillClimbingResults_4Q[iter][1:4]), index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)
    results_4Q = results_4Q.append(pandas.Series((['simulatedAnnealing']+simulatedAnnealingResults_4Q[iter][1:4]), index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)
    results_4Q = results_4Q.append(pandas.Series((['genetic']+geneticResults_4Q[iter][1:4]), index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)




results_4Q.to_csv('tp5-busquedas-locales/4Q-results.csv', index=False, header=False, sep=',',decimal='.')

## Simulaciones para 8 reinas

results_8Q = pandas.DataFrame(columns = ['algorithm_name', 'h', 'n_states', 'time_elapsed'])
results_8Q = results_8Q.append(pandas.Series(['algorithm_name', 'h', 'n_states', 'time_elapsed'], index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)

for iter in range(30):
    env = list()
    for i in range(8):
        rand_num = randint(0,7)
        env.append(rand_num)
    
    hillClimbingAgent = HillClimbingAgent(env.copy())
    simulatedAnnealingAgent = SimulatedAnnealingAgent(env.copy())
    geneticAgent = GeneticAgent(env.copy())

    hillClimbingResults_8Q.append(hillClimbingAgent.hillClimbing(max_time))
    simulatedAnnealingResults_8Q.append(hillClimbingAgent.hillClimbing(max_time))
    geneticResults_8Q.append(hillClimbingAgent.hillClimbing(max_time))
    
    results_8Q = results_8Q.append(pandas.Series((['hillClimbing']+hillClimbingResults_8Q[iter][1:4]), index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)
    results_8Q = results_8Q.append(pandas.Series((['simulatedAnnealing']+simulatedAnnealingResults_8Q[iter][1:4]), index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)
    results_8Q = results_8Q.append(pandas.Series((['genetic']+geneticResults_8Q[iter][1:4]), index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)

    results_8Q.to_csv('tp5-busquedas-locales/8Q-results.csv', index=False, header=False, sep=',',decimal='.')

## Simulaciones para 10 reinas

results_10Q = pandas.DataFrame(columns = ['algorithm_name', 'h', 'n_states', 'time_elapsed'])
results_10Q = results_10Q.append(pandas.Series(['algorithm_name', 'h', 'n_states', 'time_elapsed'], index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)

for iter in range(30):
    env = list()
    for i in range(10):
        rand_num = randint(0,9)
        env.append(rand_num)

    hillClimbingAgent = HillClimbingAgent(env.copy())
    simulatedAnnealingAgent = SimulatedAnnealingAgent(env.copy())
    geneticAgent = GeneticAgent(env.copy())

    hillClimbingResults_10Q.append(hillClimbingAgent.hillClimbing(max_time))
    simulatedAnnealingResults_10Q.append(hillClimbingAgent.hillClimbing(max_time))
    geneticResults_10Q.append(hillClimbingAgent.hillClimbing(max_time))

    results_10Q = results_10Q.append(pandas.Series((['hillClimbing']+hillClimbingResults_10Q[iter][1:4]), index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)
    results_10Q = results_10Q.append(pandas.Series((['simulatedAnnealing']+simulatedAnnealingResults_10Q[iter][1:4]), index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)
    results_10Q = results_10Q.append(pandas.Series((['genetic']+geneticResults_10Q[iter][1:4]), index=['algorithm_name', 'h', 'n_states', 'time_elapsed']), ignore_index=True)

    results_10Q.to_csv('tp5-busquedas-locales/10Q-results.csv', index=False, header=False, sep=',',decimal='.')