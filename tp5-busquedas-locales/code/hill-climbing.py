from random import randint


class HillClimbingAgent():

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
    
    
    

    def hillClimbing(self,max_states):
        states_explored = len(self.states)
        state = self.env.copy()
        h = self.calculate_h(state)

        while states_explored < max_states and h!=0:

            board = self.clac_heuristic(state)
            line,column = self.find_min_cost_indexes(board)

            new_state = state.copy()
            if not new_state in self.states:
                self.states.append(new_state)
            
            state[column] = line
            h = self.calculate_h(state)

            states_explored = len(self.states)
        
        return (state,h)

    def find_min_cost_indexes(self,board):
        minimum_value = None
        for line in board:
            if minimum_value == None:
                minimum_value = min(line)
            elif min(line) < minimum_value:
                minimum_value = min(line)
        min_value_positions = []
        iter = 0
        for line in board:
            min_value_positions += self.find_indexes(line,minimum_value,iter)
            iter += 1
        
        next_state = randint(0,len(min_value_positions)-1)
        line,column = min_value_positions[next_state]

        return((line,column))

    def find_indexes(self,cost_list,value,line):
        indexes = list()
        list_len = len(cost_list)
        for i in range(list_len):
            if cost_list[i] == value:
                indexes.append((line,i))
        
        return indexes

    



if __name__ == '__main__':
    
    queen_n = [4,8,10]
    max_states = 30
    for n in queen_n:
        print(f"Cantidad de reinas: {n}")
        env = list()
        for i in range(n):
            rand_num = randint(0,n-1)
            env.append(rand_num)

        a = HillClimbingAgent(env)

        final_state,final_h = a.hillClimbing(max_states)
        print(f"Estado final: {final_state}")
        print(f"h = {final_h}")
        print(f"Cantidad de estados alcanzados: {len(a.states)}")

