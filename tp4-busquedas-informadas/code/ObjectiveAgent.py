
class ObjectiveAgent:

    def __init__(self,env):
        self.env = env
        self.graph = {}
        self.frontier = []
        self.explored = []

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