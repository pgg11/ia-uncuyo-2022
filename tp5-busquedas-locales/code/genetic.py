from random import randint

class GeneticAgent():


    def __init__(self,queens):
        self.queens = queens


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
    
    def generate_population(self,population_qnty):

        board_len = self.queens
        population = list()
        for i in range(population_qnty):
            indivildual = list()
            for j in range(board_len):
                rand_line = randint(0,board_len-1)
                indivildual.append(rand_line)
            population.append(indivildual)
        
        return population
    
    def select_best_solutions(self,population):

        best_solutions = list()
        max_h_permited = self.queens - 2

        for solution in population:
            h = self.calculate_h(solution)

            if h<max_h_permited:
                best_solutions.append(solution)
        
        return best_solutions
    
    def reproduce(self,individual_x,individual_y):

        individuals_len = len(individual_x)

        mix = randint(0,1)

        if mix == 0:
            offspring = individual_x[0:individuals_len//3]
            offspring += individual_y[individuals_len//3:]
        else:
            offspring = individual_y[0:individuals_len//3]
            offspring += individual_x[individuals_len//3:]

        mutation_p = 0.5
        rand_prob = randint(0,100)/100

        if rand_prob <= mutation_p:
            self.mutate(offspring)

        return offspring
    
    def mutate(self,individual):

        individual_len = len(individual)
        rand_column = randint(0,individual_len-1)
        rand_line = randint(0,individual_len-1)
        individual[rand_column] = rand_line
    
    def genetic_algorithm(self):

        population_qnty = 100
        population = self.generate_population(population_qnty)
        population = self.select_best_solutions(population)

        iter = 0
        best_h = None
        childs = 0
        best_child = list()

        while best_h != 0 and iter < 500:

            new_population = list()
            for i in range(len(population)):
                x = randint(0,len(population)-1)
                y = randint(0,len(population)-1)

                offspring = self.reproduce(population[x],population[y])
                offspring_h = self.calculate_h(offspring)

                childs += 1

                if best_h == None:
                    best_h = offspring_h
                elif offspring_h < best_h:
                    best_h = offspring_h
                    best_child = offspring.copy()
                
                if best_h == 0:
                    break
                
                new_population.append(offspring)
            
            iter += 1
        
        return best_child,best_h,childs

if __name__ == '__main__':
    
    queen_n = [4,8,10]

    for n in queen_n:
        print(f"Cantidad de reinas: {n}")

        a = GeneticAgent(n)

        final_state,final_h,childs = a.genetic_algorithm()
        print(f"Estado final: {final_state}")
        print(f"h = {final_h}")
        print(f"Cantidad de hijos hasta la solución: {childs}")
        print("--------------------------------------------------")