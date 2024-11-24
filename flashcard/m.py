%pip install --upgrade --quiet google-cloud-text-to-speech langchain-community

from google.cloud import texttospeech
from langchain_community.llms import GoogleVertexAI

llm = GoogleVertexAI(model_name="gemini-1.5-flash-latest")



