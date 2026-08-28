"""
REVA.N AI Orchestrator

Coordinates the AI provider and REVA.N Core.
"""


class AIOrchestrator:

    def __init__(self, ai_provider, revan_core):
        self.ai_provider = ai_provider
        self.revan_core = revan_core

    def process(self, question: str):
        """
        Send a question to the AI provider and
        pass the result through REVA.N Core.
        """

        ai_response = self.ai_provider.generate(question)

        core_result = self.revan_core.run(question)

        return {
            "question": question,
            "ai_response": ai_response,
            "core_result": core_result,
        }