from random import randint

from environment import Environment as env
from ObjectiveAgent import ObjectiveAgent

class AstarAgent(ObjectiveAgent):

    def __init__(self,env):
        super().__init__(env)

    
    def explore(self,posX,posY,current_cost):

        goal_posX = self.env.objectivePosX
        goal_posY = self.env.objectivePosY

        if (posY,posX) in self.explored:
            return 0
        self.explored.insert(0,(posY,posX))

        self.graph[(posY,posX)] = []
       

        if self.env.accept_action('up',posX,posY):
            
            if not (posY-1,posX) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY-1,posX))
            if not (posY-1,posX) in self.frontier:
                h = ((posX - goal_posX )**2 + (posY-1 - goal_posY)**2)**(1/2)  # se utiliza de heurística la distancia de la diagonal del casilero al objetivo
                self.frontier.insert(0,[posY-1,posX,current_cost+1+h])

        if self.env.accept_action('right',posX,posY):
            
            if not (posY,posX+1) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY,posX+1))
            if not (posY,posX+1) in self.frontier:
                h = ((posX+1 - goal_posX )**2 + (posY - goal_posY)**2)**(1/2)
                self.frontier.insert(0,[posY,posX+1,current_cost+1+h])

        if self.env.accept_action('down',posX,posY):
            
            if not (posY+1,posX) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY+1,posX))
            if not (posY+1,posX) in self.frontier:
                h = ((posX - goal_posX )**2 + (posY+1 - goal_posY)**2)**(1/2)
                self.frontier.insert(0,[posY+1,posX,current_cost+1+h])

        if self.env.accept_action('left',posX,posY):
            if not (posY,posX-1) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY,posX-1))
            if not (posY,posX-1) in self.frontier:
                h = ((posX-1 - goal_posX )**2 + (posY - goal_posY)**2)**(1/2)
                self.frontier.insert(0,[posY,posX-1,current_cost+1+h])

    def sort_frontier(self):
        self.frontier.sort(key=lambda x:x[2], reverse=True)
            

    def think(self):
        start = (self.env.posY,self.env.posX)
        goal = (self.env.objectivePosY,self.env.objectivePosX)
        self.explore(self.env.posX,self.env.posY,0)
        while len(self.frontier)>0:
            self.sort_frontier()
            y,x,cost = self.frontier.pop()
            if not (y,x) in self.frontier or not (y,x) in self.explored:
                if x==self.env.objectivePosX and y==self.env.objectivePosY:
                    return self.get_path(self.graph,start,goal)
                self.explore(x,y,cost)     
                
        if len(self.frontier) == 0:
                return []



if __name__ == '__main__':

    size = 100
    init_posX = randint(0,99)
    init_posY = randint(0,99)
    goal_posX = randint(0,99)
    goal_posY = randint(0,99)
    obstacles_rate = 0.08
    e = env(size,init_posX,init_posY,goal_posX,goal_posY,obstacles_rate)
    e.generate_obstacles()
    a = AstarAgent(e)
    
    e.print_environment()
    res = a.think()
    
    print(res)