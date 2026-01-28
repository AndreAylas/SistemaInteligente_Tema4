from crewai import Agent, Task, Crew
import os

def construir_two_agen(tema="Sistemas Multi-Agentes"):
    """
     Crear un sistmea de dos agentes (investigador y redactor)
    
    """
    investigador= Agent(
        role="Investigador",
        goal=f"Reunir puntos clave y precisos sobre {tema}",
        backstory=(
            "Eres un asistente técnico. Tu trabajo es sintetizar información "
            "en bullets claros y correctos, sin relleno."
        ),
        verbose=True,
        allow_delegation=False,
    )

    redactor = Agent(
        role="Redactor",
        goal=f"Redactar un mini-informe claro y estructurado sobre {tema}",
        backstory=(
            "Eres un redactor técnico. Transformas bullets en un texto breve, "
            "coherente y fácil de leer."
        ),
        verbose=True,
        allow_delegation=False,
    )

    tarea_investigacion = Task(
        description=(
            f"Genera una lista de 6-8 bullets sobre {tema} que incluya: "
            "definición breve, 3 características, 1 caso de uso y 1 limitación. "
            "Evita exageraciones."
        ),
        expected_output="Lista de bullets con los puntos clave.",
        agent=investigador,
    )

    tarea_redaccion = Task(
        description=(
            "Usa la lista de bullets anterior para redactar un mini-informe de 8 a 12 líneas. "
            "Estructura: 1) Definición, 2) Características, 3) Caso de uso, 4) Limitación."
        ),
        expected_output="Mini-informe final (8-12 líneas) bien estructurado.",
        agent=redactor,
        context=[tarea_investigacion],
    )

    crew = Crew(
        agents=[investigador, redactor],
        tasks=[tarea_investigacion, tarea_redaccion],
        verbose=True,
    )

    return crew