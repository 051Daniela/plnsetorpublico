import os
import openai
from openai import OpenAI
from openai.types import ErrorObject, FunctionDefinition, FunctionParameters

from openai.types import Completion, CompletionChoice, CompletionUsage

from openai.types import ChatModel
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionAssistantMessageParam,
    ChatCompletionChunk,
    ChatCompletionFunctionMessageParam,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionMessageToolCall,
    ChatCompletionRole,
    ChatCompletionSystemMessageParam,
    ChatCompletionTokenLogprob,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam
)
from openai.types import Model, ModelDeleted
from openai.types.beta import (
    Assistant,
    AssistantDeleted,
    AssistantStreamEvent,
    AssistantTool,
    CodeInterpreterTool,
    FileSearchTool,
    FunctionTool
)

# Configure sua chave de API

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Função para gerar dados fictícios usando o modelo gpt-3.5-turbo-16k-0613 e GPT-4

def gerar_dados_ficticios(prompt, num_entradas, arquivo_saida):
    dados_ficticios = []
    #for _ in range(num_entradas):
    for i in range(1, num_entradas + 1):        
        response = client.chat.completions.create(
            model="gpt-4",
            #model="gpt-3.5-turbo-16k-0613",
            messages=[
                {"role": "system", "content": "Você é um assistente que gera dados fictícios."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            n=1,
            temperature=0.7,
        )
        
        response_message = response.choices[0].message.content
        dados_ficticios.append(f"Resposta {i}:\n{response_message}\n")

        #dados_ficticios.append(response_message.strip())
         
    # Salvar dados fictícios em um arquivo de texto
    with open(arquivo_saida, 'w', encoding='utf-8', errors='ignore' ) as f:        
        for dado in dados_ficticios:
            f.write(dado + "\n")
         


prompt = "Gere uma reclamação sobre problemas no transporte público, incluindo detalhes específicos como tipo de problema, localização e impacto no usuário. Sempre classificando em uma das seguintes Categorias: 1 - Falta de iluminação , 2 - Bancos Danificados, 3 - Lixo acumulado, 4 - Transporte em más condições"
num_entradas = 20  # Número de entradas fictícias para gerar
arquivo_saida = "dados_ficticios.txt"

   
gerar_dados_ficticios(prompt, num_entradas, arquivo_saida)
print(f"Dados fictícios salvos em {arquivo_saida}")

  



