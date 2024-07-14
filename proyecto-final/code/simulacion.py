from entorno_quoridor import EntornoQuoridor
from agente_deterministico import AgenteDeterministico

# Por el momento el agente no va a colocar vallas ya que no es posible que se de la situación
# de que coloquen una valla por la naturaleza de la implementación determinística y que los
# dos agentes en la prueba son determinísticos

def probar_agentes_deterministicos():
    entorno = EntornoQuoridor()
    agente_1 = AgenteDeterministico((0, 4), 8)  # Meta en la fila 8
    agente_2 = AgenteDeterministico((8, 4), 0)  # Meta en la fila 0

    turnos = 0

    while turnos < 100:  # Simular 100 movimientos
        estado = entorno.estado_actual()

        # Turno del Agente 1
        accion_1 = agente_1.decidir_accion(estado, entorno)
        if accion_1:
            if accion_1[0] == "mover":
                entorno.mover_peon(0, accion_1[1])
            elif accion_1[0] == "colocar_valla":
                entorno.colocar_valla(accion_1[2], accion_1[1])
        
        estado = entorno.estado_actual()

        # Turno del Agente 2
        accion_2 = agente_2.decidir_accion(estado, entorno)
        if accion_2:
            if accion_2[0] == "mover":
                entorno.mover_peon(1, accion_2[1])
            elif accion_2[0] == "colocar_valla":
                entorno.colocar_valla(accion_2[2], accion_2[1])

        # Imprimir el estado actual del entorno para ver el progreso
        print(f"Turno {turnos + 1}")
        print(f"Peón Agente 1: {entorno.peones[0]}, Vallas restantes: {agente_1.vallas_restantes}")
        print(f"Peón Agente 2: {entorno.peones[1]}, Vallas restantes: {agente_2.vallas_restantes}")
        print(f"Vallas horizontales: {entorno.vallas_horizontales}")
        print(f"Vallas verticales: {entorno.vallas_verticales}")
        print("-" * 30)

        turnos += 1

probar_agentes_deterministicos()
