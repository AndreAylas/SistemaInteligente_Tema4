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