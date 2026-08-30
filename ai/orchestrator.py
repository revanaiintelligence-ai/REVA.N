"""
REVA.N AI Orchestrator v0.2

Coordinates:
REVA.N Core → structured context → AI provider → response
"""


REVA_N_SYSTEM_CONTEXT = """
You are the AI provider operating inside REVA.N.

REVA.N means:
Reasoning Engine for Vision and Analysis Networking.

REVA.N is a proprietary reasoning architecture designed to
structure information, variables, relationships and context
in order to support analysis and human decision-making.

IMPORTANT:

- REVA.N is the name of the system you are operating inside.
- Do not confuse REVA.N with external companies, financial
  tickers, applications, universities, vehicles or unrelated
  entities.
- The AI provider is a component of REVA.N.
- The AI provider itself is NOT REVA.N.
- REVA.N does not make decisions for humans.
- REVA.N structures analysis and supports human decision-making.
- If the REVA.N Core provides context, that context has priority
  when interpreting the user's question.
- Do not replace REVA.N's identity with unrelated external
  meanings unless the user explicitly asks about those meanings.
- If information is unavailable, say so instead of inventing it.
- Answer in the language used by the user.
"""


class AIOrchestrator:

    def __init__(self, ai_provider, revan_core):

        self.ai_provider = ai_provider
        self.revan_core = revan_core

    def process(self, question: str):
        """
        Executes:

        1. REVA.N Core analysis
        2. Context extraction
        3. AI reasoning
        4. Final structured result
        """

        # -------------------------------------------------
        # STEP 1 — REVA.N CORE
        # -------------------------------------------------

        core_result = self.revan_core.run(question)

        context = core_result.get(
            "context",
            {}
        )

        reasoning = core_result.get(
            "reasoning",
            ""
        )

        evaluation = core_result.get(
            "evaluation",
            {}
        )

        # -------------------------------------------------
        # STEP 2 — BUILD CONTROLLED PROMPT
        # -------------------------------------------------

        prompt = f"""
{REVA_N_SYSTEM_CONTEXT}

REVA.N CORE ANALYSIS
====================

User question:
{question}

Detected domain:
{context.get("domain")}

Detected subject:
{context.get("subject")}

Is this a REVA.N question?
{context.get("is_revan_question")}

Core reasoning:
{reasoning}

Core evaluation:
{evaluation}


INSTRUCTION

Use the REVA.N Core analysis above as the primary context
for interpreting the user's question.

If the Core identifies the subject as REVA.N, answer about
the REVA.N system described in this prompt.

Do NOT answer about REVA Medical, NYSE tickers, Mahindra REVA,
REVA University, REVA apps, or other external entities unless
the user explicitly asks about one of them.

Now answer the user's question clearly and directly.
"""

        # -------------------------------------------------
        # STEP 3 — AI PROVIDER
        # -------------------------------------------------

        ai_response = self.ai_provider.generate(
            prompt
        )

        # -------------------------------------------------
        # STEP 4 — FINAL RESULT
        # -------------------------------------------------

        return {
            "question": question,
            "ai_response": ai_response,
            "core_result": core_result,
        }