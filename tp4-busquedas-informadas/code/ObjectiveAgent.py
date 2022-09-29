
class ObjectiveAgent:

    def __init__(self,env):
        self.env = env
        self.graph = {}
        self.frontier = []
        self.explored = []

    def reset_agent(self):
        self.graph = {}
        self.frontier = []
        self.explored = []

    def update_env(self,env):
        self.env = env

    def get_path(self,graph,start,goal):
        result = []
        node = goal
        while node != start:
            for key in graph:
                if node in graph[key]:
                    result.insert(0,node)
                    node = key
                    break
        return result