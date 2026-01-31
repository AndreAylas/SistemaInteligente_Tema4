from crewai import Agent, Task, Crew

def construir_entrevista_messi(tema="Mundial 2026"):
    """
        Sistema multi-agente: entrevista breve a Messi sobre el Mundial 2026
    """

    messi = Agent(
        role="Lionel Messi",
        goal=f"Responder como futbolista profesional sobre el {tema}",
        backstory=(
            "Eres Lionel Messi, futbolista argentino campeón del mundo. "
            "Respondes de forma reflexiva, breve y realista, desde tu experiencia personal."
        ),
        verbose=True,
        allow_delegation=False,
    )

    reportero = Agent(
        role="Reportero deportivo",
        goal=f"Redactar una entrevista periodística breve sobre el {tema}",
        backstory=(
            "Eres un periodista deportivo. Transformas respuestas en una entrevista clara, "
            "natural y bien redactada."
        ),
        verbose=True,
        allow_delegation=False,
    )

    tarea_entrevista = Task(
        description=(
            f"Responde como Lionel Messi a una pregunta sobre el {tema}. "
            "Habla sobre expectativas, importancia del torneo y tu visión personal. "
            "Limita la respuesta a 3-4 frases."
        ),
        expected_output="Respuesta breve en primera persona como Messi.",
        agent=messi,
    )

    tarea_redaccion = Task(
        description=(
            "Usa la respuesta anterior para redactar una entrevista periodística "
            "de exactamente 5 líneas, con formato pregunta-respuesta."
        ),
        expected_output="Entrevista deportiva breve (5 líneas).",
        agent=reportero,
        context=[tarea_entrevista],
    )

    crew = Crew(
        agents=[messi, reportero],
        tasks=[tarea_entrevista, tarea_redaccion],
        verbose=True,
    ) #construir el sistema multi-agente

    return crew
