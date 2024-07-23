import random

class AgenteDeterministico:
    def __init__(self, pos_inicial, meta_fila):
        self.vallas_restantes = 10
        self.meta_fila = meta_fila  # La fila de la meta
        self.pos_inicial = pos_inicial  # La posición inicial del peón

    def decidir_accion(self, estado, entorno):
        vallas_horizontales, vallas_verticales = estado['vallas_horizontales'], estado['vallas_verticales']

        if self.meta_fila == 0:
            peon_pos = estado['peones'][1]
            peon_oponente_pos = estado['peones'][0]
        else:
            peon_pos = estado['peones'][0]
            peon_oponente_pos = estado['peones'][1]

        # Intentar moverse hacia la meta
        accion_mover = self.mover_hacia_meta(peon_pos, entorno)
        if accion_mover:
            return accion_mover

        # Si no puede moverse hacia la meta, moverse lateralmente
        accion_lateral = self.mover_lateralmente(peon_pos, entorno)
        if accion_lateral:
            return accion_lateral

        # Si no puede moverse lateralmente, intentar bloquear al peón oponente
        if self.vallas_restantes > 0:
            accion_valla = self.bloquear_contrincante(peon_oponente_pos, vallas_horizontales, vallas_verticales, peon_pos, entorno)
            if accion_valla:
                return accion_valla

        return None

    def distancia_a_meta(self, pos):
        return abs(self.meta_fila - pos[0])

    def mover_hacia_meta(self, pos, entorno):

        nueva_pos = (None, None)

        if self.meta_fila == 0:
            nueva_pos = (pos[0] - 1, pos[1])
        elif self.meta_fila > 0:
            nueva_pos = (pos[0] + 1, pos[1])

        if entorno.es_movimiento_valido(pos, nueva_pos):
            return ("mover", nueva_pos)
        return None

    def mover_lateralmente(self, pos, entorno):
        opciones = [(pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]

        random.shuffle(opciones)
        for nueva_pos in opciones:
            if entorno.es_movimiento_valido(pos, nueva_pos):
                return ("mover", nueva_pos)
        return None

    def bloquear_contrincante(self, pos_peon_oponente, vallas_horizontales, vallas_verticales, pos_peon_propio, entorno):
        # Evaluar si es posible bloquear con una valla en forma de U
        if self.distancia_a_meta(pos_peon_oponente) > self.distancia_a_meta(pos_peon_propio) + 2:
            opciones = []
            if pos_peon_oponente[0] < entorno.size - 1:
                opciones.append((pos_peon_oponente, 'horizontal'))
            if pos_peon_oponente[1] < entorno.size - 1 and entorno.es_valla_valida(pos_peon_oponente,'vertical'):
                opciones.append((pos_peon_oponente, 'vertical'))

            random.shuffle(opciones)
            for opcion in opciones:
                if opcion[1] == 'horizontal' and entorno.es_valla_valida(opcion[0],'horizontal'):
                    self.vallas_restantes -= 1
                    return ("colocar_valla", opcion[0], 'horizontal')
                elif opcion[1] == 'vertical' and entorno.es_valla_valida(opcion[0],'vertical'):
                    self.vallas_restantes -= 1
                    return ("colocar_valla", opcion[0], 'vertical')
        return None
