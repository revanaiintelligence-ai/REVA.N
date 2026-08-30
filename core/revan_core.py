"""
REVA.N Core v0.2
Reasoning Engine for Vision and Analysis Networking

Flujo:
Input → Observation → Context → Evidence → Knowledge
→ Analysis → Reasoning → Evaluation → Decision Support
"""


class REVANCore:

    def __init__(self):
        self.observation = None
        self.context = {}
        self.evidence = []
        self.knowledge = []
        self.analysis = None
        self.reasoning = None
        self.evaluation = None
        self.decision_support = None

    def observe(self, observation):
        self.observation = observation

    def identify_context(self):
        """
        Identifica el contexto básico de la consulta.
        """

        if not self.observation:
            self.context = {
                "domain": "unknown",
                "subject": None,
                "is_revan_question": False,
            }
            return self.context

        text = self.observation.lower()

        is_revan_question = (
            "reva.n" in text
            or "revan" in text
        )

        if is_revan_question:
            domain = "REVA.N"
            subject = "REVA.N"
        else:
            domain = "general"
            subject = self.observation

        self.context = {
            "domain": domain,
            "subject": subject,
            "is_revan_question": is_revan_question,
        }

        return self.context

    def add_evidence(self, evidence):
        self.evidence.append(evidence)

    def add_knowledge(self, knowledge):
        self.knowledge.append(knowledge)

    def analyze(self):

        if self.observation is None:
            return "No hay una observación para analizar."

        if not self.context:
            self.identify_context()

        self.analysis = {
            "problem": self.observation,
            "context": self.context,
            "evidence_count": len(self.evidence),
            "knowledge_count": len(self.knowledge),
        }

        return self.analysis

    def reason(self):

        if self.analysis is None:
            self.analyze()

        if self.context.get("is_revan_question"):

            self.reasoning = (
                "La consulta se refiere al sistema REVA.N. "
                "Debe analizarse utilizando la identidad y "
                "arquitectura propias de REVA.N, evitando "
                "confundirla con entidades externas."
            )

        else:

            self.reasoning = (
                "REVA.N ha estructurado el problema "
                "a partir de la observación, el contexto, "
                "la evidencia y el conocimiento disponible."
            )

        return self.reasoning

    def evaluate(self):

        if self.reasoning is None:
            self.reason()

        self.evaluation = {
            "status": "evaluated",
            "evidence_available": len(self.evidence) > 0,
            "knowledge_available": len(self.knowledge) > 0,
            "context_identified": bool(self.context),
        }

        return self.evaluation

    def support_decision(self):

        if self.evaluation is None:
            self.evaluate()

        self.decision_support = {
            "problem": self.observation,
            "context": self.context,
            "analysis": self.analysis,
            "reasoning": self.reasoning,
            "evaluation": self.evaluation,
        }

        return self.decision_support

    def run(self, problem):
        """
        Ejecuta el flujo completo de REVA.N Core v0.2.
        """

        self.observe(problem)
        self.identify_context()
        self.analyze()
        self.reason()
        self.evaluate()

        return self.support_decision()


if __name__ == "__main__":

    revan = REVANCore()

    result = revan.run(
        "Ejemplo de problema para analizar."
    )

    print("REVA.N Core v0.2")
    print(result)