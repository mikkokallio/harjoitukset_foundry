########################################################################
# Azure AI Foundry - Harjoitus 1 - Foundry Inference Endpoint          #
########################################################################


# 1. Lue artikkeli https://learn.microsoft.com/fi-fi/azure/ai-foundry/foundry-models/concepts/endpoints?tabs=python
# 2. Kopioi tähän tiedostoon Python-esimerkkikoodi kohdasta Azure AI inference endpoint
# 3. Muuta koodia siten, että se toimii.
#    - Vinkki: Tarvitset kolme asiaa. Yksi näistä on AZURE_INFERENCE_CREDENTIAL.
#      - Tämän ja muut arvot voi laittaa .env -tiedostoon.
#      - Alla oleva dotenv mahdollistaa arvojen lukemisen sieltä.
#      - Esim. os.environ["MODEL_DEPLOYMENT_NAME"] sijasta käytä tällöin os.getenv("MODEL_DEPLOYMENT_NAME")
# 4. Suorita koodi ja varmista, että saat vastauksen.
# 5. Muokkaa koodia siten, että se käyttää avaimetonta tunnistautumista (ks. kohta Keyless authentication).
# 6. Suorita koodi uudestaan ja varmista, että saat vastauksen.


from dotenv import load_dotenv
load_dotenv()

# xxx = os.getenv('XXX') # Esimerkki ympäristömuuttujan XXX lukemisesta


### Kopioi esimerkkikoodi tähän ja muokkaa sitä ###

import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

client = ChatCompletionsClient(
    endpoint=os.getenv("AZURE_INFERENCE_ENDPOINT"),
    credential=AzureKeyCredential(os.getenv("AZURE_INFERENCE_CREDENTIAL")),
)

from azure.ai.inference.models import SystemMessage, UserMessage

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="Explain Riemann's conjecture in 1 paragraph"),
    ],
    model=os.getenv("AZURE_INFERENCE_MODEL")
)

print(response.choices[0].message.content)