import random

class EntornoQuoridor:
    def __init__(self, size=9):
        self.size = size
        self.reset()

    def reset(self):
        self.peones = [(0, self.size // 2), (self.size - 1, self.size // 2)]  # Inicializar peones
        self.vallas_horizontales = set()
        self.vallas_verticales = set()

    def estado_actual(self):
        return {
            'peones': self.peones,
            'vallas_horizontales': self.vallas_horizontales,
            'vallas_verticales': self.vallas_verticales
        }

    def es_movimiento_valido(self, pos_actual, nueva_pos):
        if 0 <= nueva_pos[0] < self.size and 0 <= nueva_pos[1] < self.size:
            if not self.hay_valla_entre(pos_actual, nueva_pos):
                return True
        return False

    def es_valla_valida(self, pos_valla, tipo):
        # Verifica que la posición de la valla horizontal sea válida
        if tipo == 'horizontal':
            if pos_valla[0] < (self.size - 1):
                if pos_valla not in self.vallas_horizontales:
                    if (pos_valla[0]-1,pos_valla[1]) not in self.vallas_horizontales:
                        if (pos_valla[0]+1,pos_valla[1]) not in self.vallas_horizontales:
                            if pos_valla not in self.vallas_verticales:
                                return True
        # Verifica que la posición de la valla vertical sea válida
        if tipo == 'vertical':
            if pos_valla[1] < (self.size - 1):
                if pos_valla not in self.vallas_verticales:
                    if (pos_valla[0],pos_valla[1]-1) not in self.vallas_verticales:
                        if (pos_valla[0],pos_valla[1]+1) not in self.vallas_verticales:
                            if pos_valla not in self.vallas_horizontales:
                                return True
        return False
                    
         

    def hay_valla_entre(self, pos_actual, nueva_pos):
        if pos_actual[0] == nueva_pos[0]:  # Movimiento horizontal
            if pos_actual[1] < nueva_pos[1]:  # Movimiento a la derecha
                return (pos_actual[0], pos_actual[1]) in self.vallas_verticales
            else:  # Movimiento a la izquierda
                return (pos_actual[0], pos_actual[1] - 1) in self.vallas_verticales
        elif pos_actual[1] == nueva_pos[1]:  # Movimiento vertical
            if pos_actual[0] < nueva_pos[0]:  # Movimiento hacia abajo
                return (pos_actual[0], pos_actual[1]) in self.vallas_horizontales
            else:  # Movimiento hacia arriba
                return (pos_actual[0] - 1, pos_actual[1]) in self.vallas_horizontales
        return False

    def mover_peon(self, indice_peon, nueva_pos):
        self.peones[indice_peon] = nueva_pos
        # Verificar si el peón oponente está delante
        if indice_peon == 0 and nueva_pos == self.peones[1]:
            self.peones[indice_peon] = (nueva_pos[0] + 1, self.peones[indice_peon][1])
        elif indice_peon == 1 and nueva_pos == self.peones[0]:
            self.peones[indice_peon] = (nueva_pos[0] - 1, self.peones[indice_peon][1])
        # Verificar si el peón ha llegado a la meta
        if indice_peon == 0 and nueva_pos[0] >= self.size - 1:
            self.peones[indice_peon] = (0, random.randint(0, 8))
        elif indice_peon == 1 and nueva_pos[0] <= 0:
            self.peones[indice_peon] = (self.size - 1, random.randint(0, 8))
        

    def colocar_valla(self, tipo, pos):
        if tipo == 'horizontal':
            self.vallas_horizontales.add(pos)
        elif tipo == 'vertical':
            self.vallas_verticales.add(pos)
    
    def paso(self, accion, indice_peon):
        recompensa = 0
        tipo_accion, *params = accion

        nueva_pos = None

        if tipo_accion == "mover":
            direccion = params[0]
            if direccion == "izquierda":
                nueva_pos = (self.peones[indice_peon][0], self.peones[indice_peon][1] - 1)
            elif direccion == "derecha":
                nueva_pos = (self.peones[indice_peon][0], self.peones[indice_peon][1] + 1)
            elif direccion == "arriba":
                nueva_pos = (self.peones[indice_peon][0] - 1, self.peones[indice_peon][1])
            elif direccion == "abajo":
                nueva_pos = (self.peones[indice_peon][0] + 1, self.peones[indice_peon][1])
            if nueva_pos and self.es_movimiento_valido(self.peones[indice_peon], nueva_pos):
                self.mover_peon(indice_peon, nueva_pos)
                recompensa = 1
            else:
                recompensa = -1
        elif tipo_accion == "colocar_valla":
            pos, tipo_valla = params
            if self.es_valla_valida(pos, tipo_valla):
                self.colocar_valla(tipo_valla, pos)
                recompensa = 1
            else:
                recompensa = -1

        return self.estado_actual(), recompensa