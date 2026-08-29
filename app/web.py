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


# Configuración de la aplicación
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


# Entrada del usuario
question = st.text_area(
    "Escribe tu pregunta",
    placeholder="Ejemplo: ¿Esta propiedad representa una buena oportunidad?"
)


# Ejecutar análisis
if st.button("ANALIZAR"):

    if not question.strip():

        st.warning("Escribe una pregunta antes de analizar.")

    else:

        # Proveedor de IA de prueba
        provider = MockAIProvider()

        # Núcleo de REVA.N
        core = REVANCore()

        # Orquestador
        orchestrator = AIOrchestrator(
            provider,
            core
        )

        # Procesamiento
        result = orchestrator.process(question)

        # Resultado
        st.subheader("Resultado REVA.N")

        st.write(result)