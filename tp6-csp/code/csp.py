import copy

class CSP:
    def __init__(self, n):
        #Dimension del tablero
        self.n = n
        #Tablero inicial
        self.board = [0] * n

    def backtracking(self):
        states = 0
        currentX = 0
        prevY = [0]
        while (currentX < self.n):
            initY = prevY.pop()
            isOk = False
            for y in range (initY, self.n):
                states += 1
                self.board[currentX] = y
                isOk = self.__checkPrevious(currentX)
                if(isOk):
                    prevY.append(y+1)
                    break
            if(isOk):
                currentX += 1
                prevY.append(0)
            else:
                currentX -= 1
        return states
    def __checkPrevious(self, x):
        value = self.board[x]        
        for i in range (x):
            currentValue = self.board[i]        
            #Si la reina anterior se encuentra en la misma linea, diagonal superior o diagonal inferior
            if (currentValue == value or value + i - x == currentValue or value - i + x == currentValue):
                return False
        return True
    
    
    def forwardChecking(self):
        #Dominio de las variables [0 .. n]
        D = [x for x in range (self.n)]
        #Variables: Variable_n en posicion n
        V = [Variable(D) for _ in range (self.n)]
        
        states = 0
        prevY = [0]
        currentX = 0
        while (currentX < self.n):
            initY = prevY.pop()
            isOk = False
            for y in range (initY, self.n):
                if(V[currentX].isPosible(y)):
                    states += 1
                    #Asigno parcialmente
                    V[currentX].value = y
                    #Actualizo el dominio de los vecinos
                    isOk = self.__updateNeighbors(V, currentX + 1)
                    #Se actualizo correctamente el domino (paso a la siguiente variable)
                    if(isOk):
                        #Guarda la variable y
                        prevY.append(y+1)
                        break
            if(isOk):
                currentX += 1
                prevY.append(0)
            else:
                self.__rollBackVariables(V, currentX, self.n-1)
                currentX -= 1
        result = []
        for v in V:
            result.append(v.value)
        self.board = result
        return states


    def __updateNeighbors(self, V, initX):
        y = V[initX-1].value
        notEmpty = True
        distance = 1
        #Elimina las posiciones en la que se veria amenazada
        for V_n in range (initX, self.n):
            #Misma fila
            notEmpty &= V[V_n].deleteElementToDomain(y, True)

            #Diagonal superior
            if(y - distance > -1):
                notEmpty &= V[V_n].deleteElementToDomain(y - distance)

            #Diagonal inferior
            if(y + distance < self.n):
                notEmpty &= V[V_n].deleteElementToDomain(y + distance)
            
            #Se vacio el dominio (vuelve a la normalidad)
            if(not notEmpty):
                self.__rollBackVariables(V, initX, V_n)
                return False
            distance += 1
        return True
    def __rollBackVariables(self, V, initX, endX):
        while (initX <= endX):
            V[initX].rollBack()
            initX += 1

class Variable:
    def __init__(self, D):
        self.dimension = len(D)
        #Inicializa el dominio
        d = {}
        for i in range(self.dimension):
            d[D[i]] = 0
        #Guarda el dominio
        self.D = d
        #Guarda la cantidad de elementos eliminados
        self.deletes = 0
        #Guarda un backup de los dominios y la cantidad de elementos eliminados anteriormente
        self.backup = []
        #Guarda el valor asignado
        self.value = None        

    def deleteElementToDomain(self, element, isNEVariable = False):
        #Si se esta eliminando un elemento del domino con respecto a la asignacion de otra variable
        if(isNEVariable):
            backup = {
                #Guarda los estados posibles anteriores
                'D': copy.copy(self.D),
                #Guarda la cantidad de elementos eliminados anteriormente
                'deletes': self.deletes,
                #Guarda la asignacion parcial
                'value': self.value
            }
            self.backup.append(backup)
        if(self.D[element] == 0):
            #Elimina el elemento del domino
            self.D[element] = 1
            #Aumenta el contador de eliminados
            self.deletes += 1
        #Si no se han eliminado todos los elementos del dominio
        return self.deletes < self.dimension

    #Si es posible tomar ese valor del dominio
    def isPosible (self, element):
        return self.D[element] == 0

    #Vuelve al dominio anterior
    def rollBack(self):
        backup = self.backup.pop()
        self.D = copy.copy(backup['D'])
        self.deletes = backup['deletes']
        self.value = backup['value']