from random import randint

class Environment:

    def __init__(self,size,init_posX,init_posY,objectivePosX,objectivePosY,obstacles_rate):
        self.size = size
        self.posX = init_posX
        self.posY = init_posY
        self.objectivePosX = objectivePosX 
        self.objectivePosY = objectivePosY
        self.obstacles_rate = obstacles_rate
        self.moves = 0
        self.board = [[True for x in range(size)] for y in range(size)]

    def generate_obstacles(self):
        obstacles_qty = int(self.size*self.size*self.obstacles_rate)

        while obstacles_qty > 0:
            x = randint(0,self.size-1)
            y = randint(0,self.size-1)
            if (self.board[y][x] and not(x==self.posX and y==self.posY) 
            and not(x==self.objectivePosX and y==self.objectivePosY)):
                self.board[y][x] = False
                obstacles_qty-=1

    def accept_action(self,action,x,y):

        if action == 'up' and y > 0:
            return self.board[y-1][x]
        if action == 'down' and y < self.size-1 :
            return self.board[y+1][x]
        if action == 'right' and x < self.size-1:
            return self.board[y][x+1]
        if action == 'left' and x > 0:
            return self.board[y][x-1]

        return False
    
    def get_posX(self):
        return self.posX
    
    def get_posY(self):
        return self.posY

    def get_performance(self):
        return self.performance
    
    def print_environment(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.posX==j and self.posY==i:
                    print("^",end="")
                elif self.objectivePosY==i and self.objectivePosX==j:
                    print("=",end="")
                elif(not self.board[i][j]):
                    print("*",end="")
                else:
                    print(".",end="")
            print("")


#initPosX= randint(0,9)
#initPosY= randint(0,9)
#objectivePosX= randint(0,9)
#objectivePosY= randint(0,9)
#obstacles_rate = 0.08

#env = Environment(10,initPosX,initPosY,objectivePosX,objectivePosY,obstacles_rate)
#env.generate_obstacles()

#env.print_environment()