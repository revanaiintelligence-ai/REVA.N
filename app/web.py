import sys
from pathlib import Path

# Añadir la raíz de REVA.N al PATH de Python
ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

from core.revan_core import REVANCore
from ai.mock_provider import MockAIProvider
from ai.orchestrator import AIOrchestrator


# Configuración
st.set_page_config(
    page_title="REVA.N",
    page_icon="🧠",
    layout="centered"
)


# Identidad
st.title("REVA.N")

st.subheader(
    "Reasoning Engine for Vision and Analysis Networking"
)

st.write(
    "REVA.N estructura información, variables y contexto "
    "para producir un análisis razonado y estructurado."
)


# Entrada
question = st.text_area(
    "Escribe tu pregunta",
    placeholder="Ejemplo: ¿Qué es REVA.N?"
)


# Análisis
if st.button("ANALIZAR"):

    if not question.strip():

        st.warning("Escribe una pregunta antes de analizar.")

    else:

        # Componentes de REVA.N
        provider = MockAIProvider()
        core = REVANCore()

        orchestrator = AIOrchestrator(
            provider,
            core
        )

        # Ejecutar
        result = orchestrator.process(question)


        # Resultado
        st.divider()

        st.subheader("Resultado REVA.N")


        # Mostrar respuesta de IA
        if isinstance(result, dict):

            ai_response = result.get("ai_response")

            if ai_response:
                st.markdown("### Respuesta")
                st.write(ai_response)


            # Mostrar análisis del Core
            core_result = result.get("core_result")

            if core_result:

                st.markdown("### Análisis del Core")

                reasoning = core_result.get("reasoning")

                if reasoning:
                    st.write(reasoning)


                evaluation = core_result.get("evaluation")

                if evaluation:

                    st.markdown("### Evaluación")

                    status = evaluation.get("status")
                    evidence = evaluation.get("evidence_available")
                    knowledge = evaluation.get("knowledge_available")

                    st.write(
                        f"Estado: {status}"
                    )

                    st.write(
                        f"Evidencia disponible: {'Sí' if evidence else 'No'}"
                    )

                    st.write(
                        f"Conocimiento disponible: {'Sí' if knowledge else 'No'}"
                    )


        else:

            st.write(result)