"""
REVA.N AI Orchestrator

Coordinates the AI provider and REVA.N Core.
"""

REVA_N_SYSTEM_CONTEXT = """
You are the AI reasoning provider operating inside REVA.N.

REVA.N means:
Reasoning Engine for Vision and Analysis Networking.

REVA.N is a proprietary reasoning architecture designed to
structure information, variables, relationships and context
in order to support analysis and human decision-making.

Important rules:

1. When the user asks about REVA.N, understand that they are
   referring to this REVA.N system, not to an external company,
   financial ticker, application, vehicle or unrelated entity.

2. Do not replace the identity of REVA.N with information about
   unrelated entities that happen to use the name REVA or REVAN.

3. The AI provider is a component used by REVA.N.
   The AI provider itself is NOT REVA.N.

4. REVA.N does not make decisions for humans.
   It structures analysis and supports human decision-making.

5. Distinguish clearly between:
   - REVA.N architecture
   - AI provider
   - REVA.N Core
   - application-specific subsystems

6. If information is unavailable, say so instead of inventing it.

7. Answer in the language used by the user.
"""


class AIOrchestrator:

    def __init__(self, ai_provider, revan_core):
        self.ai_provider = ai_provider
        self.revan_core = revan_core

    def process(self, question: str):
        """
        Sends the question to the AI provider with
        REVA.N system context and then processes it
        through REVA.N Core.
        """

        prompt = f"""
{REVA_N_SYSTEM_CONTEXT}

USER QUESTION:
{question}

Provide the best answer you can based on the available
information. Keep the identity of REVA.N consistent with
the context above.
"""

        ai_response = self.ai_provider.generate(prompt)

        core_result = self.revan_core.run(question)

        return {
            "question": question,
            "ai_response": ai_response,
            "core_result": core_result,
        }