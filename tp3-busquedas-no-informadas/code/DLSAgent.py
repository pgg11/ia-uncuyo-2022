from environment import Environment as env
from random import randint

from ObjectiveAgent import ObjectiveAgent

class DLSAgent(ObjectiveAgent):

    def __init__(self,env,limit):
        super().__init__(env)
        self.limit = limit

    
    def explore(self,posX,posY,level):

        if (posY,posX) in self.explored:
            return 0

        self.explored.insert(0,(posY,posX))

        self.graph[(posY,posX)] = []
       

        if self.env.accept_action('up',posX,posY):
            if not (posY-1,posX) in self.frontier:
                self.frontier.append((posY-1,posX,level+1))
            if not (posY-1,posX) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY-1,posX))

        if self.env.accept_action('right',posX,posY):
            if not (posY,posX+1) in self.frontier:
                self.frontier.append((posY,posX+1,level+1))
            if not (posY,posX+1) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY,posX+1))

        if self.env.accept_action('down',posX,posY):
            if not (posY+1,posX) in self.frontier:
                self.frontier.append((posY+1,posX,level+1))
            if not (posY+1,posX) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY+1,posX))

        if self.env.accept_action('left',posX,posY):
            if not (posY,posX-1) in self.frontier:
                self.frontier.append((posY,posX-1,level+1))
            if not (posY,posX-1) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY,posX-1))

    def think(self):
        start = (self.env.posY,self.env.posX)
        goal = (self.env.objectivePosY,self.env.objectivePosX)
        self.explore(self.env.posX,self.env.posY,0)

        while len(self.frontier)>0:
            y,x,depth = self.frontier.pop()
            if not (y,x) in self.frontier or not (y,x) in self.explored:
                if depth < self.limit:
                    self.explore(x,y,depth)
                if x==self.env.objectivePosX and y==self.env.objectivePosY:
                    return (self.get_path(self.graph,start,goal))

        if len(self.frontier) == 0:
                return []
