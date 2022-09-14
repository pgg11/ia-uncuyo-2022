from environment import Environment as env
from random import randint


class BFSAgent:

    def __init__(self,env):
        self.env = env
        self.graph = {}
        self.frontier = []
        self.explored = []

    
    def explore(self,posX,posY):

        if (posY,posX) in self.explored:
            return 0
        self.explored.insert(0,(posY,posX))

        self.graph[(posY,posX)] = []
       

        if self.env.accept_action('up',posX,posY):
            self.frontier.insert(0,(posY-1,posX))
            if not (posY-1,posX) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY-1,posX))

        if self.env.accept_action('right',posX,posY):
            self.frontier.insert(0,(posY,posX+1))
            if not (posY,posX+1) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY,posX+1))

        if self.env.accept_action('down',posX,posY):
            self.frontier.insert(0,(posY+1,posX))
            if not (posY+1,posX) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY+1,posX))

        if self.env.accept_action('left',posX,posY):
            self.frontier.insert(0,(posY,posX-1))
            if not (posY,posX-1) in self.explored:
                self.graph[(posY,posX)].insert(0,(posY,posX-1))

        
    
    def get_path(self,graph,start,goal):
        result = []
        node = goal
        while node != start:
            for key in graph:
                if node in graph[key]:
                    result.insert(0,node)
                    node = key
                    break
        result.insert(0,start)
        return result

    def think(self):
        start = (self.env.posY,self.env.posX)
        goal = (self.env.objectivePosY,self.env.objectivePosX)
        self.explore(self.env.posX,self.env.posY)
        while len(self.frontier)>0:
            y,x = self.frontier.pop()
            if not (y,x) in self.frontier or not (y,x) in self.explored:
                self.explore(x,y)
                if x==self.env.objectivePosX and y==self.env.objectivePosY:
                    return self.get_path(self.graph,start,goal)
        if len(self.frontier) == 0:
                return False



initPosX= randint(0,9)
initPosY= randint(0,9)
objectivePosX= randint(0,9)
objectivePosY= randint(0,9)
obstacles_rate = 0.08
e = env(10,initPosX,initPosY,objectivePosX,objectivePosY,obstacles_rate)
e.generate_obstacles()
e.print_environment()
a = BFSAgent(e)
print('inicio')
print((a.env.posY,a.env.posX))
print('objetivo')
print((objectivePosY,objectivePosX))
res = a.think()


print(res)