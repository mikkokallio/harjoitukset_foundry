########################################################################
# Azure AI Foundry - Harjoitus 3 - Responses API                      #
########################################################################


# 1. Lue https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses?tabs=python-secure
# 2. Mitä eroja edelliseen huomaat kohdissa Generate a text response, Retrieve a response?
# 3. Kokeillaan työkalun antamista AI:lle! Toteuta kohdan Function calling esimerkki edellisten tehtävien tapaan.
#    - Vinkki: Malli on määritelty koodissa kahteen kertaan, huomaa tämä.
# 4. Mitä koodissa tapahtuu?


from dotenv import load_dotenv
load_dotenv()

### Kopioi esimerkkikoodi tähän ja muokkaa sitä ###

import os
from openai import OpenAI

client = OpenAI(  
  base_url = f"{os.getenv('OPENAI_ENDPOINT')}/openai/v1/",
  api_key=os.getenv("AZURE_OPENAI_API_KEY")  
)

response = client.responses.create(  
    model=os.getenv("AZURE_INFERENCE_MODEL"),
    tools=[  
        {  
            "type": "function",  
            "name": "get_weather",  
            "description": "Get the weather for a location",  
            "parameters": {  
                "type": "object",  
                "properties": {  
                    "location": {"type": "string"},  
                },  
                "required": ["location"],  
            },  
        }  
    ],  
    input=[{"role": "user", "content": "What's the weather in San Francisco?"}],  
)  

print(response.model_dump_json(indent=2))  
  
# To provide output to tools, add a response for each tool call to an array passed  
# to the next response as `input`  
input = []  
for output in response.output:  
    if output.type == "function_call":  
        match output.name:  
            case "get_weather":  
                input.append(  
                    {  
                        "type": "function_call_output",  
                        "call_id": output.call_id,  
                        "output": '{"temperature": "70 degrees"}',  
                    }  
                )  
            case _:  
                raise ValueError(f"Unknown function call: {output.name}")  
  
second_response = client.responses.create(  
    model=os.getenv("AZURE_INFERENCE_MODEL"),  
    previous_response_id=response.id,  
    input=input  
)  

print(second_response.model_dump_json(indent=2))