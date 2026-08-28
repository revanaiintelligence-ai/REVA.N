"""
REVA.N AI Provider Interface

Defines the common interface that any AI provider must implement.
"""


class AIProvider:

    def generate(self, prompt: str) -> str:
        """
        Generate an AI response from a prompt.

        Every AI provider connected to REVA.N
        must implement this method.
        """

        raise NotImplementedError(
            "AI provider must implement generate()."
        )