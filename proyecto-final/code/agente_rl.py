import random
import numpy as np

class AgenteRL:
    def __init__(self, acciones, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.acciones = acciones
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def inicializar_q_table(self, estado):
        estado_str = str(estado)
        if estado_str not in self.q_table:
            self.q_table[estado_str] = {}
            for accion in self.acciones:
                if accion[0] == "colocar_valla":
                    for i in range(9):
                        for j in range(9):
                            self.q_table[estado_str][("colocar_valla", (i, j), accion[2])] = 0
                else:
                    self.q_table[estado_str][accion] = 0

    def seleccionar_accion(self, estado):
        estado_str = str(estado)
        self.inicializar_q_table(estado)
        
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.acciones)
        else:
            return max(self.q_table[estado_str], key=self.q_table[estado_str].get)

    def actualizar_q_table(self, estado, accion, recompensa, nuevo_estado):
        estado_str = str(estado)
        nuevo_estado_str = str(nuevo_estado)
        
        self.inicializar_q_table(estado)
        self.inicializar_q_table(nuevo_estado)

        max_q_nuevo_estado = max(self.q_table[nuevo_estado_str].values())
        self.q_table[estado_str][accion] += self.alpha * (
            recompensa + self.gamma * max_q_nuevo_estado - self.q_table[estado_str][accion]
        )