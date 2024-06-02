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
from collections import Counter


# Configure sua chave de API

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Função para ler reclamações de um arquivo de texto
def ler_reclamacoes_arquivo(arquivo_entrada):
    with open(arquivo_entrada, 'r', encoding='utf-8', errors='ignore') as f:
        conteudo = f.read()
    reclamacoes = conteudo.split("\n\n")
    reclamacoes_filtradas = [reclamacao.strip() for reclamacao in reclamacoes if reclamacao.startswith("Resposta")]
    return reclamacoes_filtradas

# Função para analisar e classificar as reclamações usando o modelo gpt-3.5-turbo-16k-0613
def analisar_reclamacoes(arquivo_entrada):
    reclamacoes = ler_reclamacoes_arquivo(arquivo_entrada)
    analises = []
    for reclamacao in reclamacoes:
        response = client.chat.completions.create(
            model="gpt-4",
            #model="gpt-3.5-turbo-16k-0613",
            messages=[
                {"role": "system", "content": "Você é um assistente que analisa e classifica reclamações."},
                {"role": "user", "content": f"Reclamação: {reclamacao}"}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        analise = response.choices[0].message.content
        analises.append(analise)
    return reclamacoes, analises

# Função para classificar prioridade das reclamações
def classificar_prioridade(analises):
    prioridades = {'baixa': [], 'media': [], 'alta': []}
    for analise in analises:
        if "baixa" in analise.lower():
            prioridades['baixa'].append(analise)
        elif "média" in analise.lower() or "media" in analise.lower():
            prioridades['media'].append(analise)
        elif "alta" in analise.lower():
            prioridades['alta'].append(analise)
    return prioridades

# Função para classificar por categoria
def classificar_categoria(reclamacoes):
    categorias = {}
    for reclamacao in reclamacoes:
        linhas = reclamacao.split('\n')
        categoria = None
        for linha in linhas:
            if linha.lower().startswith("categoria:"):
                categoria = linha.split(":", 1)[1].strip()
                if categoria not in categorias:
                    categorias[categoria] = []
                categorias[categoria].append(reclamacao)
    return categorias

# Função para salvar os resultados classificados em um arquivo Markdown
def salvar_resultados_markdown(arquivo_saida, reclamacoes, prioridades, categorias):
    with open(arquivo_saida, 'w', encoding='utf-8', errors='ignore') as f:
        f.write("# Análise PLN - Setor Público\n\n")
        f.write(f"Total de reclamações analisadas: {len(reclamacoes)}\n\n")
        f.write("| Prioridade | Quantidade |\n")
        f.write("|------------|------------|\n")
        for prioridade, items in prioridades.items():
            f.write(f"| {prioridade.capitalize()} | {len(items)} |\n")
        f.write("\n")

        for prioridade, items in prioridades.items():
            f.write(f"## Prioridade {prioridade.capitalize()}\n")
            for item in items:
                f.write(f"- {item}\n")
            f.write("\n")

        f.write("## Categorias\n")
        for categoria, items in categorias.items():
            f.write(f"### Categoria {categoria}\n")
            for item in items:
                f.write(f"- {item}\n")
            f.write("\n")

# Função para salvar o resumo dos resultados em um arquivo Markdown
def salvar_resumo_markdown(arquivo_saida, reclamacoes, prioridades, categorias):
    total_reclamacoes = len(reclamacoes)
    total_baixa = len(prioridades['baixa'])
    total_media = len(prioridades['media'])
    total_alta = len(prioridades['alta'])

    # Contar quantas categorias se repetem
    contagem_categorias = Counter([cat for cat in categorias.keys()])
    categorias_repetidas = {k: v for k, v in contagem_categorias.items() if v > 1}

    # Identificar as 3 análises mais prioritárias (media e alta)
    analises_prioritarias = prioridades['media'] + prioridades['alta']
    contagem_prioritarias = Counter(analises_prioritarias)
    top_prioritarias = contagem_prioritarias.most_common(3)

    with open(arquivo_saida, 'w', encoding='utf-8', errors='ignore') as f:
        f.write("# Resumo da Análise PLN - Setor Público\n\n")
        f.write(f"Total de reclamações analisadas: {total_reclamacoes}\n\n")
        f.write(f"Total de reclamações de prioridade baixa: {total_baixa}\n")
        f.write(f"Total de reclamações de prioridade média: {total_media}\n")
        f.write(f"Total de reclamações de prioridade alta: {total_alta}\n\n")

        f.write("## Categorias Repetidas\n")
        for categoria, quantidade in categorias_repetidas.items():
            f.write(f"- {categoria}: {quantidade} vezes\n")
        f.write("\n")

        f.write("## Prioridades Principais\n")
        for prioridade, quantidade in top_prioritarias:
            f.write(f"- {prioridade} (Quantidade: {quantidade})\n")

# Exemplo de uso para análise e classificação de reclamações
arquivo_entrada = "dados_ficticios.txt"
arquivo_saida_resultados = "resultados_classificados.md"
arquivo_saida_resumo = "resumo_analise.md"

reclamacoes, analises = analisar_reclamacoes(arquivo_entrada)
prioridades = classificar_prioridade(analises)
categorias = classificar_categoria(reclamacoes)


# Salvar resultados e resumo
salvar_resultados_markdown(arquivo_saida_resultados, reclamacoes, prioridades, categorias)
salvar_resumo_markdown(arquivo_saida_resumo, reclamacoes, prioridades, categorias)
print(f"Resultados classificados salvos em {arquivo_saida_resultados}")
print(f"Resumo da análise salvo em {arquivo_saida_resumo}")
