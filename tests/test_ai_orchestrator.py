from core.revan_core import REVANCore
from ai.mock_provider import MockAIProvider
from ai.orchestrator import AIOrchestrator


def test_ai_orchestrator():
    provider = MockAIProvider()
    core = REVANCore()
    orchestrator = AIOrchestrator(provider, core)

    question = "¿Esta propiedad representa una buena oportunidad?"

    result = orchestrator.process(question)

    assert result["question"] == question
    assert "REVA.N Mock AI Response" in result["ai_response"]
    assert result["core_result"] is not None