from cmath import e
from math import pow
from random import randint
import time


class SimulatedAnnealingAgent:

    def __init__(self,env):
        self.env = env
        self.states = [self.env]


    def calculate_h(self,state):
        h = 0
        board_len = len(state)
        threats = dict()
        for column in range(board_len):

            queens = list()
            line_queens,line_threats = self.queen_line_threat_count(state,column)
            h += line_queens
            diagonal_queens,diagonal_threats = self.queen_diagonal_threat_count(state,column)
            h += diagonal_queens

            queens += line_threats
            queens += diagonal_threats

            threats[column] = queens
        
        self.delete_repeted_queens(threats)
            
        return(self.count_threats(threats))

    def delete_repeted_queens(self,queens_threats):
        for column in queens_threats:
            for queen in queens_threats[column]:
                if column in queens_threats[queen]:
                    queens_threats[queen].remove(column)
        
        return queens_threats
    
    def count_threats(self,queens_threats):
        total = 0
        for queen in queens_threats:
            total += len(queens_threats[queen])
        return total

    def queen_line_threat_count(self,state,column):
        line = state[column]
        queens_thretening_index = []
        count = 0
        board_len = len(state)
        for i in range(board_len):
            if i == column:
                continue
            elif state[i] == line:
                queens_thretening_index.append(i)
                count += 1
        return (count,queens_thretening_index)
    
    def queen_diagonal_threat_count(self,state,column):
        line = state[column]
        queens_thretening_index = []
        count = 0
        board_len = len(state)
        for i in range(board_len):
            if i < column:
                if (column-i == line-state[i]) or (column-i == state[i]-line):
                    queens_thretening_index.append(i)
                    count += 1

            if i>column and i<=(board_len-column):
                if (i-column == line - state[i]) or (i-column == state[i]-line):
                    queens_thretening_index.append(i)
                    count += 1
        return (count,queens_thretening_index)
    
    def clac_heuristic(self,state):
        
        board_len = len(self.env)
        board = [[0 for _ in range(board_len)] for _ in range(board_len)]
        for i in range(board_len):
            new_state = state.copy()
            line = new_state[i]
            for j in range(board_len):
                if j == line:
                    board[j][i] = self.calculate_h(new_state)#'R'
                    continue
                
                new_state[i] = j
                board[j][i] = self.calculate_h(new_state)
        
        return board

    def simulated_annealing(self,t,max_time):
        h_variation = list()
        init_time = time.time()
        board_len = len(self.env)
        current_state = self.env.copy()
        current_h = self.calculate_h(current_state)
        h_variation.append(current_h)

        time_elapsed = round(time.time() - init_time , 4)

        while time_elapsed < max_time and current_h !=0:

            rand_column = randint(0,board_len-1)
            rand_line = randint(0,board_len-1)

            posible_state = current_state.copy()
            posible_state[rand_column] = rand_line
            posible_h = self.calculate_h(posible_state)

            if posible_h < current_h:
                current_state = posible_state
                current_h = posible_h
                self.states.append(current_state)
                h_variation.append(current_h)
            elif posible_h > current_h:
                cost_increase = posible_h - current_h
                p = pow(e,(-cost_increase/t)) * 100
                decision = randint(0,100)

                if decision <= p:
                    current_state = posible_state
                    current_h = posible_h
                    h_variation.append(current_h)
                    self.states.append(current_state)
                
                t = t*0.60
            

            time_elapsed = round(time.time() - init_time , 4)
        time_elapsed = str(time_elapsed)
        
        states_explored = len(self.states)
            


        
        return ([current_state,current_h,states_explored,time_elapsed,h_variation])
    
if __name__ == '__main__':
    
    queen_n = [4,8,10]
    max_time = 30
    t = 100
    for n in queen_n:
        print(f"Cantidad de reinas: {n}")
        env = list()
        for i in range(n):
            rand_num = randint(0,n-1)
            env.append(rand_num)

        a = SimulatedAnnealingAgent(env)

        final_state,final_h,states,time_elapsed,h_variation = a.simulated_annealing(t,max_time)
        print(f"Estado final: {final_state}")
        print(f"h = {final_h}")
        print(f"Cantidad de estados alcanzados: {states}")
        print((f"Tiempo transcurrido hasta la solución: {time_elapsed} segundos"))
        print("----------------------------------------------------")
