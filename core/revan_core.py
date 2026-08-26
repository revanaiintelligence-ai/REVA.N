"""
REVA.N Core v0.1
Reasoning Engine for Vision and Analysis Networking

First functional core:
Input → Observation → Evidence → Knowledge
→ Analysis → Reasoning → Evaluation → Decision Support
"""


class REVANCore:

    def __init__(self):
        self.observation = None
        self.evidence = []
        self.knowledge = []
        self.analysis = None
        self.reasoning = None
        self.evaluation = None
        self.decision_support = None

    def observe(self, observation):
        self.observation = observation

    def add_evidence(self, evidence):
        self.evidence.append(evidence)

    def add_knowledge(self, knowledge):
        self.knowledge.append(knowledge)

    def analyze(self):
        if self.observation is None:
            return "No hay una observación para analizar."

        self.analysis = {
            "problem": self.observation,
            "evidence_count": len(self.evidence),
            "knowledge_count": len(self.knowledge),
        }

        return self.analysis

    def reason(self):
        if self.analysis is None:
            self.analyze()

        self.reasoning = (
            "REVA.N ha estructurado el problema "
            "a partir de la observación, la evidencia "
            "y el conocimiento disponible."
        )

        return self.reasoning

    def evaluate(self):
        if self.reasoning is None:
            self.reason()

        self.evaluation = {
            "status": "evaluated",
            "evidence_available": len(self.evidence) > 0,
            "knowledge_available": len(self.knowledge) > 0,
        }

        return self.evaluation

    def support_decision(self):
        if self.evaluation is None:
            self.evaluate()

        self.decision_support = {
            "problem": self.observation,
            "analysis": self.analysis,
            "reasoning": self.reasoning,
            "evaluation": self.evaluation,
        }

        return self.decision_support

    def run(self, problem):
        """
        Ejecuta el flujo básico completo de REVA.N.
        """

        self.observe(problem)
        self.analyze()
        self.reason()
        self.evaluate()

        return self.support_decision()


if __name__ == "__main__":

    revan = REVANCore()

    result = revan.run(
        "Ejemplo de problema para analizar."
    )

    print("REVA.N Core v0.1")
    print(result)