import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from core.revan_core import REVANCore
from ai.mock_provider import MockAIProvider
from ai.orchestrator import AIOrchestrator
from ai.mock_provider import MockAIProvider
from ai.orchestrator import AIOrchestrator


st.set_page_config(
    page_title="REVA.N",
    page_icon="🧠"
)

st.title("REVA.N")
st.write("Reasoning Engine for Vision and Analysis Networking")

question = st.text_area(
    "Escribe tu pregunta",
    placeholder="Ejemplo: ¿Esta propiedad representa una buena oportunidad?"
)

if st.button("ANALIZAR"):
    if not question.strip():
        st.warning("Escribe una pregunta.")
    else:
        provider = MockAIProvider()
        core = REVANCore()
        orchestrator = AIOrchestrator(provider, core)

        result = orchestrator.process(question)

        st.subheader("Resultado REVA.N")
        st.write(result)