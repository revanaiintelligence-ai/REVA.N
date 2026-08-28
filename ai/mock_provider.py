"""
REVA.N Mock AI Provider

Simulated AI provider used for testing.
No API key, internet connection, or payment required.
"""


class MockAIProvider:

    def __init__(self):
        self.name = "Mock AI"

    def generate(self, prompt: str) -> str:
        """
        Generate a simulated AI response.
        """

        return (
            "REVA.N Mock AI Response\n\n"
            f"Pregunta recibida: {prompt}\n\n"
            "Respuesta de prueba: "
            "La pregunta fue recibida correctamente por "
            "el proveedor de IA de prueba."
        )