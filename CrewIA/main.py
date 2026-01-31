from agentes import construir_entrevista_messi
from dotenv import load_dotenv
load_dotenv()

def main():
    """
      Programa principal: construir y ejecutar la entrevista al Jugador Argentino Messi
    """

    crew=construir_entrevista_messi()
    resultado=crew.kickoff() # poner en marcha los agentes

    print("\n--- Resultado Final ---\n")
    print(resultado)
    # Guardar salida para evidencias en el tutorial
    with open("resultados_ejemplo.txt", "w", encoding="utf-8") as f:
        f.write(str(resultado))

if __name__ == "__main__":
    main()