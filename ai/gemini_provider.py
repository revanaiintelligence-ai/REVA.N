"""
REVA.N Gemini AI Provider

Connects REVA.N to Google Gemini API
using the GEMINI_API_KEY stored in Streamlit Secrets.
"""

import streamlit as st
from google import genai


class GeminiAIProvider:

    def __init__(self):

        self.name = "Google Gemini"

        api_key = st.secrets.get("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY no está configurada en Streamlit Secrets."
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text