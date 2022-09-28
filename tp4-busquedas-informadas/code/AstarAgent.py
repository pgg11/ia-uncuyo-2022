from random import randint

from environment import Environment as env
from ObjectiveAgent import ObjectiveAgent

class AstarAgent(ObjectiveAgent):

    def __init__(self,env):
        super().__init__(env)

    
    def explore(self,posX,posY):

        if (posY,posX) in self.explored:
            return 0
        self.explored.insert(0,(posY,posX))

        self.graph[(posY,posX)] = []
       

        if self.env.accept_action('up',posX,posY):
            if not (posY-1,posX) in self.frontier:
                self.frontier.insert(0,(posY-1,posX))
            if not (posY-1,posX) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY-1,posX))

        if self.env.accept_action('right',posX,posY):
            if not (posY,posX+1) in self.frontier:
                self.frontier.insert(0,(posY,posX+1))
            if not (posY,posX+1) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY,posX+1))

        if self.env.accept_action('down',posX,posY):
            if not (posY+1,posX) in self.frontier:
                self.frontier.insert(0,(posY+1,posX))
            if not (posY+1,posX) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY+1,posX))

        if self.env.accept_action('left',posX,posY):
            if not (posY,posX-1) in self.frontier:
                self.frontier.insert(0,(posY,posX-1))
            if not (posY,posX-1) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY,posX-1))

    def calc_cost(self,node):
        start = (self.env.posY,self.env.posX)
        nodeX, nodeY = node
        heuristic_cost = ((nodeX - self.env.objectivePosX)**2 + (nodeY - self.env.objectivePosY)**2)**(1/2)
        return (len(self.get_path(self.graph,start,node))-1 + heuristic_cost)

    def sort_frontier(self):
        self.frontier.sort(key=self.calc_cost)
        self.frontier.reverse()
            

    def think(self):
        start = (self.env.posY,self.env.posX)
        goal = (self.env.objectivePosY,self.env.objectivePosX)
        self.explore(self.env.posX,self.env.posY)
        while len(self.frontier)>0:
            y,x = self.frontier.pop()
            if not (y,x) in self.frontier or not (y,x) in self.explored:
                self.explore(x,y)
                self.sort_frontier()
                if x==self.env.objectivePosX and y==self.env.objectivePosY:
                    return self.get_path(self.graph,start,goal)
        if len(self.frontier) == 0:
                return []

