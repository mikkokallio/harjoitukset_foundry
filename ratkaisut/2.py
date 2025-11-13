########################################################################
# Azure AI Foundry - Harjoitus 2 - OpenAI Service                      #
########################################################################


# 1. Lisää tänne koodi edellisen harjoituksen artikkelista kohdasta OpenAI Service.
# 2. Edellisen harjoituksen tapaan muuta koodia siten, että se toimii.
#    - Vinkki: Tälläkin kertaa tarvitset kolme asiaa.
#      Mutta mitä edellisistä ympäristömuuttujista voit käyttää uudestaan?
# 3. Testaa koodi - kokeile myös muuttaa system ja user -viestejä haluamallasi tavalla.
# 4. Vertaile koodia edellisen harjoituksen koodiin. Mitä eroja ja yhtäläisyyksiä löydät?


from dotenv import load_dotenv
load_dotenv()

### Kopioi esimerkkikoodi tähän ja muokkaa sitä ###

import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint=os.getenv("OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_INFERENCE_CREDENTIAL"),  
    api_version="2024-10-21",
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_INFERENCE_MODEL"),
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain Riemann's conjecture in 1 paragraph"}
    ]
)

print(response.model_dump_json(indent=2))
