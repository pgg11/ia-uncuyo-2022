from entorno_quoridor import EntornoQuoridor
from agente_rl import AgenteRL
from agente_deterministico import AgenteDeterministico

import random

def entrenar_agente_rl(episodios=1000):
    entorno = EntornoQuoridor()
    acciones = [
        ("mover", "izquierda"), 
        ("mover", "derecha"), 
        ("mover", "arriba"), 
        ("mover", "abajo"), 
        ("colocar_valla", (0, 0), "horizontal"), 
        ("colocar_valla", (0, 0), "vertical")
    ]
    agente_rl = AgenteRL(acciones)
    agente_deterministico = AgenteDeterministico((8, 4), 0)  # Meta en la fila 0

    for episodio in range(episodios):
        estado = entorno.reset()
        total_recompensa = 0

        for turno in range(100):
            # Agente RL
            accion_rl = agente_rl.seleccionar_accion(estado)
            if accion_rl[0] == "colocar_valla":
                accion_rl = (accion_rl[0], (random.randint(0, entorno.size-1), random.randint(0, entorno.size-1)), accion_rl[2])
            nuevo_estado, recompensa_rl = entorno.paso(accion_rl, 0)
            total_recompensa += recompensa_rl
            agente_rl.actualizar_q_table(estado, accion_rl, recompensa_rl, nuevo_estado)
            estado = nuevo_estado

            # Agente Determinista
            accion_deterministico = agente_deterministico.decidir_accion(estado, entorno)
            if accion_deterministico:
                if accion_deterministico[0] == "mover":
                    tipo_accion, nueva_pos = accion_deterministico
                    entorno.mover_peon(1, nueva_pos)
                elif accion_deterministico[0] == "colocar_valla":
                    tipo_accion, pos, tipo_valla = accion_deterministico
                    entorno.colocar_valla(tipo_valla, pos)

        print(f"Episodio {episodio+1}/{episodios} - Recompensa Total: {total_recompensa}")

if __name__ == "__main__":
    entrenar_agente_rl()
