from random import randint

class Environment:

    def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = init_posX
        self.posY = init_posY
        self.dirt_rate = dirt_rate
        self.performance = 0
        self.board = [[False for x in range(sizeX)] for y in range(sizeY)]

    def generate_dirt(self):
        dirt_qty = int(self.sizeX*self.sizeY*self.dirt_rate)

        while dirt_qty > 0:
            x = randint(0,self.sizeX-1)
            y = randint(0,self.sizeY-1)
            if not self.board[x][y]:
                self.board[x][y] = True
                dirt_qty-=1

    def accept_action(self,action):
        if action == 'up' and self.posY > 0:
            return True
        if action == 'down' and self.posY < self.sizeY-1 :
            return True
        if action == 'right' and self.posX < self.sizeX-1:
            return True
        if action == 'left' and self.posX > 0:
            return True

        return False
    

    def is_dirty(self):
        if(self.board[self.posY][self.posX]):
            self.board[self.posY][self.posX] = False
            self.performance += 1
            return True
        return False
    
    def get_posX(self):
        return self.posX
    
    def get_posY(self):
        return self.posY

    def get_performance(self):
        return self.performance
    
    def print_environment(self):
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if self.posX==j and self.posY==i:
                    print("^",end="")
                elif(self.board[i][j]):
                    print("*",end="")
                else:
                    print(".",end="")
            print("")
        print("---------------------------")