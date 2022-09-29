from environment import Environment as env
from random import randint

from ObjectiveAgent import ObjectiveAgent

class DFSAgent(ObjectiveAgent):

    def __init__(self,env):
        super().__init__(env)

    
    def explore(self,posX,posY):

        if (posY,posX) in self.explored:
            return 0
        self.explored.insert(0,(posY,posX))

        self.graph[(posY,posX)] = []
       

        if self.env.accept_action('up',posX,posY):
            self.frontier.append((posY-1,posX))
            if not (posY-1,posX) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY-1,posX))

        if self.env.accept_action('right',posX,posY):
            self.frontier.append((posY,posX+1))
            if not (posY,posX+1) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY,posX+1))

        if self.env.accept_action('down',posX,posY):
            self.frontier.append((posY+1,posX))
            if not (posY+1,posX) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY+1,posX))

        if self.env.accept_action('left',posX,posY):
            self.frontier.append((posY,posX-1))
            if not (posY,posX-1) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY,posX-1))

    def think(self):
        start = (self.env.posY,self.env.posX)
        goal = (self.env.objectivePosY,self.env.objectivePosX)
        self.explore(self.env.posX,self.env.posY)
        while len(self.frontier)>0:
            y,x = self.frontier.pop()
            if not (y,x) in self.frontier or not (y,x) in self.explored:
                self.explore(x,y)
                if x==self.env.objectivePosX and y==self.env.objectivePosY:
                    return (self.get_path(self.graph,start,goal))
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
    a = DFSAgent(e)
    
    e.print_environment()
    res = a.think()
    
    print(res)