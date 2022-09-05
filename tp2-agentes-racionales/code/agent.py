from environment import Environment as env
from random import randint


class Agent:

    def __init__(self,env,remaining_actions):
        self.env = env
        self.remaining_actions = remaining_actions

    def up(self):
        self.env.posY -= 1
        self.remaining_actions -= 1
    
    def down(self):
        self.env.posY += 1
        self.remaining_actions -= 1
    
    def left(self):
        self.env.posX -= 1
        self.remaining_actions -= 1
    
    def right(self):
        self.env.posX +=1
        self.remaining_actions -= 1
    
    def suck(self):
        if(self.env.board[self.env.posY][self.env.posX]):
            self.env.performance += 1
            self.env.board[self.env.posY][self.env.posX] = False
        self.remaining_actions -= 1
    
    def idle(self):
        self.remaining_actions -= 1
    
    def perspective(self,env):
        pass
    
    def think(self):
        pass


class SimpleReflectiveAgent(Agent):

    def __init__(self,env,remaining_actions):
        super().__init__(env, remaining_actions)
    
    def think(self):
        if self.env.is_dirty():
            self.suck()
        elif self.env.posY%2 == 0 and self.env.accept_action('right'):
            self.right() 
        elif self.env.posY%2 == 1 and self.env.accept_action('left'):
            self.left()  
        elif self.env.accept_action('down'):
            self.down()
        else:
            self.idle()


class RandomAgent(Agent):

    def __init__(self, env, remaining_actions):
        super().__init__(env, remaining_actions)

    def think(self):
        
        random_action = randint(0,5)

        if random_action == 0 and self.env.accept_action('up'):
            self.up()
        if random_action == 1 and self.env.accept_action('down'):
            self.down()
        if random_action == 2 and self.env.accept_action('right'):
            self.right()
        if random_action == 3 and self.env.accept_action('left'):
            self.left()
        if random_action == 4:
            self.suck()
        if random_action == 5:
            self.idle() 