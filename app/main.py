from core.revan_core import REVANCore
from ai.mock_provider import MockAIProvider
from ai.orchestrator import AIOrchestrator


def main():
    question = input("Escribe tu pregunta para REVA.N: ")

    provider = MockAIProvider()
    core = REVANCore()
    orchestrator = AIOrchestrator(provider, core)

    result = orchestrator.process(question)

    print("\n=== REVA.N ===")
    print(result)


if __name__ == "__main__":
    main()