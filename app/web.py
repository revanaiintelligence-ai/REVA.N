import sys
from pathlib import Path

# Añadir la raíz de REVA.N al PATH de Python
ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

from core.revan_core import REVANCore
from ai.gemini_provider import GeminiAIProvider
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

        try:

            # Proveedor real de IA
            provider = GeminiAIProvider()

            # Core de REVA.N
            core = REVANCore()

            # Orquestador
            orchestrator = AIOrchestrator(
                provider,
                core
            )

            # Ejecutar análisis
            result = orchestrator.process(question)


            # Resultado
            st.divider()
            st.subheader("Resultado REVA.N")


            if isinstance(result, dict):

                # Respuesta de Gemini
                ai_response = result.get("ai_response")

                if ai_response:

                    st.markdown("### Respuesta")

                    st.write(ai_response)


                # Resultado del Core
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
                        evidence = evaluation.get(
                            "evidence_available"
                        )
                        knowledge = evaluation.get(
                            "knowledge_available"
                        )

                        st.write(
                            f"Estado: {status}"
                        )

                        st.write(
                            "Evidencia disponible: "
                            f"{'Sí' if evidence else 'No'}"
                        )

                        st.write(
                            "Conocimiento disponible: "
                            f"{'Sí' if knowledge else 'No'}"
                        )


            else:

                st.write(result)


        except Exception as error:

            st.error(
                "REVA.N encontró un error al procesar "
                "la solicitud."
            )

            st.caption(
                str(error)
            )