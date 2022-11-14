import pandas
import seaborn as sns
import matplotlib.pyplot as plt

from hill_climbing import HillClimbingAgent
from genetic import GeneticAgent
from simulated_annealing import SimulatedAnnealingAgent


from random import randint


def calculate_stadistics(dataframe,algorithm,n_queens):

    #Carga los datos del archivo csv filtrando por algoritmo

    algorithm_data=dataframe[dataframe.algorithm_name==algorithm]

    #Calcula porcentaje de estados óptimos alcanzados
    optimal_states = 0

    for h in algorithm_data['h']:
        if h==0:
            optimal_states+=1
    
    optimal_states_percentage = round(optimal_states / 30 * 100 , 2)

    #Calcula media y desviación estándar de estados recorridos y tiempos de ejecución
    
    algorithm_means = round(algorithm_data[['n_states','time_elapsed']].mean(),5)
    algorithm_std = round(algorithm_data[['n_states','time_elapsed']].std(),5)
    
    print(f'Datos del algoritmo \'{algorithm}\' para {n_queens} reinas:')
    print(f'   Porcentaje de estados óptimos alcanzados: {optimal_states_percentage}')
    print(f'   Media de estados recorridos: {algorithm_means[0]}\n   Media de tiempos de ejecución: {algorithm_means[1]}')
    print(f'   Desviación estándar de estados recorridos: {algorithm_std[0]}\n   Desviación estándar de tiempos de ejecución: {algorithm_std[1]}')


def time_bloxplot(dataframe):
    
    data = pandas.DataFrame(data=dataframe, columns=['algorithm_name','time_elapsed'])

    hillClimbing_data = data[data.algorithm_name=='hillClimbing']
    simulatedAnnealing_data = data[data.algorithm_name=='simulatedAnnealing']
    genetic_data = data[data.algorithm_name=='genetic']

    fig,axes = plt.subplots(2,2)

    fig.suptitle('Distribución de tiempos de ejecución')

    sns.boxplot(ax=axes[0, 0], data=hillClimbing_data, x='algorithm_name', y='time_elapsed')
    sns.boxplot(ax=axes[0, 1], data=simulatedAnnealing_data, x='algorithm_name', y='time_elapsed')
    sns.boxplot(ax=axes[1, 0], data=genetic_data, x='algorithm_name', y='time_elapsed')
    sns.boxplot(ax=axes[1, 1], data=data, x='algorithm_name', y='time_elapsed')
    
    plt.show()

def plot_h_variaton(n_queens):

    max_time = 20
    t = 100 #simulated annealing

    env = list()
    for i in range(n_queens):
        rand_num = randint(0,n_queens-1)
        env.append(rand_num)

    hillClimbingAgent = HillClimbingAgent(env.copy())
    simulatedAnnealingAgent = SimulatedAnnealingAgent(env.copy())
    geneticAgent = GeneticAgent(n_queens)

    
    
    hillClimbingResults = hillClimbingAgent.hillClimbing(max_time)
    simulatedAnnealingResults = simulatedAnnealingAgent.simulated_annealing(t,max_time)
    geneticAgentResults = geneticAgent.genetic_algorithm(max_time)

    results = pandas.DataFrame(columns = ['algorithm_name','variation','h'])
    #results = results.append(pandas.Series(['algorithm_name', 'variation', 'h'], index=['algorithm_name', 'variation','h']), ignore_index=True)

    iter = 0
    for h in hillClimbingResults[4]:
        results = results.append(pandas.Series((['hillClimbing']+[str(iter)]+[str(h)]), index=['algorithm_name','variation','h']), ignore_index=True)
        iter += 1
    iter = 0
    for h in simulatedAnnealingResults[4]:
        results = results.append(pandas.Series((['simulatedAnnealing']+[str(iter)]+[str(h)]), index=['algorithm_name','variation','h']), ignore_index=True)
        iter += 1
    iter = 0
    for h in geneticAgentResults[4]:
        results = results.append(pandas.Series((['genetic']+[str(iter)]+[str(h)]), index=['algorithm_name','variation','h']), ignore_index=True)
        iter += 1

    hillClimbing_data = results[results.algorithm_name=='hillClimbing']
    simulatedAnnealing_data = results[results.algorithm_name=='simulatedAnnealing']
    genetic_data = results[results.algorithm_name=='genetic']

    fig,axes = plt.subplots(3,1)

    fig.suptitle('H variation')

    fig1=sns.lineplot(ax=axes[0], data=hillClimbing_data, x='variation', y='h', hue='algorithm_name')
    fig2=sns.lineplot(ax=axes[1], data=simulatedAnnealing_data, x='variation', y='h',hue='algorithm_name')
    fig3=sns.lineplot(ax=axes[2], data=genetic_data, x='variation', y='h',hue='algorithm_name')

    plt.show()