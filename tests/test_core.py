from core.revan_core import REVANCore


def test_revan_core_runs():
    revan = REVANCore()

    result = revan.run(
        "¿Esta propiedad representa una buena oportunidad?"
    )

    assert result is not None
    assert result["problem"] == "¿Esta propiedad representa una buena oportunidad?"
    assert result["analysis"] is not None
    assert result["reasoning"] is not None
    assert result["evaluation"] is not None
    assert result["evaluation"]["status"] == "evaluated"