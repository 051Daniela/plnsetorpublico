# Análise de Reclamações do Transporte Público com Processamento de Linguagem Natural



## Introdução

- **Problema:** Grande volume de reclamações sobre transporte público que precisam ser analisadas e categorizadas para melhorar o serviço.
- **Solução:** Utilização de técnicas de Processamento de Linguagem Natural (PLN) para automatizar a análise e classificação das reclamações.

## Objetivos

- **Objetivo Geral:** Desenvolver um sistema automatizado utilizando PLN para análise e classificação de reclamações do transporte público.
- Objetivos Específicos:
  - Gerar dados fictícios de reclamações para testes usando modelos de PLN.
  - Analisar e classificar as reclamações utilizando a API da OpenAI.
  - Categorizar as reclamações por prioridade e categoria.
  - Gerar relatórios detalhados e resumos da análise.

## Metodologia

1. **Geração de Dados Fictícios com PLN:**
   - Utilizar a API da OpenAI para gerar reclamações fictícias sobre problemas no transporte público.
   - Prompt: "Gere uma reclamação fictícia sobre problemas no transporte público, incluindo detalhes específicos como tipo de problema, localização, categoria e impacto no usuário."
   - **Técnica:** Utilização do modelo GPT-4, um modelo avançado de PLN que compreende e gera texto com alta precisão.
2. **Leitura e Análise das Reclamações com PLN:**
   - **Leitura:** Ler reclamações de um arquivo de texto.
   - **Análise:** Utilizar a API da OpenAI (modelo GPT-4) para analisar e classificar cada reclamação.
   - **Técnica:** Aplicação de modelos de PLN para entender o contexto e o conteúdo das reclamações, extraindo informações relevantes.
3. **Classificação das Reclamações:**
   - **Prioridade:** Classificar por prioridade (baixa, média, alta) utilizando análise de texto com PLN.
   - **Categoria:** Agrupar por categoria com base no conteúdo da reclamação.
   - **Técnica:** Uso de modelos de PLN para identificar e categorizar temas e níveis de urgência nas reclamações.
4. **Geração de Relatórios:**
   - **Detalhados:** Salvar os resultados classificados em um arquivo Markdown detalhado.
   - **Resumidos:** Criar um resumo dos resultados em outro arquivo Markdown, destacando as categorias repetidas e as prioridades principais.
   - **Técnica:** Automação da geração de relatórios utilizando scripts Python e modelos de PLN.

## Resultados Esperados

- **Relatórios Detalhados:** Arquivos Markdown com a classificação das reclamações por prioridade e categoria, gerados automaticamente.
- **Resumo da Análise:** Arquivo Markdown resumido com estatísticas importantes e prioridades principais.
- **Insights:** Identificação das áreas que necessitam de maior atenção e possíveis melhorias no transporte público, baseados na análise de PLN.



## Explicação técnica do projeto



Projeto utilizando API do OpenAI para gerar dados fictícios de reclamações de Usuários e aplicar PLN avançado para analisar e classificar os dados



O projeto é divido em 2  parte:

- Gerar dados fictícios
- Analisar dados, classificar  e gerar resultado



## Gerar dados fictícios



1. **Chamada da API da OpenAI:**
   - O código utiliza `openai.ChatCompletion.create` para gerar respostas fictícias baseadas no prompt fornecido.
   - O modelo `gpt-4` é chamado com um prompt que orienta o modelo a gerar dados fictícios. Este modelo é treinado para compreender e gerar texto de alta qualidade.
2. **PLN Interno:**
   - A OpenAI usa modelos de PLN que são redes neurais treinadas em grandes corpora de texto. Esses modelos podem compreender o contexto, gerar texto coerente e responder a perguntas de maneira semelhante a um humano.



Código utilizado para geração de dados : [criarDados.py]()

Saída do código: [dados_ficticios.txt]()



## Analisar dados, classificar  e gerar resultado



1. **Leitura das Reclamações:**
   - A função `ler_reclamacoes_arquivo` lê as reclamações de um arquivo de texto e as filtra com base na presença de "Resposta".
2. **Análise das Reclamações:**
   - A função `analisar_reclamacoes` faz chamadas para a API da OpenAI, que usa modelos de PLN para analisar e classificar cada reclamação.
   - A OpenAI aplica técnicas avançadas de PLN para entender o contexto e o conteúdo de cada reclamação.
3. **Classificação por Prioridade:**
   - A função `classificar_prioridade` classifica as análises em categorias de prioridade (baixa, média, alta) com base no texto da análise.
4. **Classificação por Categoria:**
   - A função `classificar_categoria` agrupa as reclamações por categoria, extraindo a categoria de cada reclamação.
5. **Salvamento dos Resultados em Markdown:**
   - As funções `salvar_resultados_markdown` e `salvar_resumo_markdown` escrevem os resultados classificados e o resumo em arquivos Markdown, garantindo que a codificação UTF-8 seja usada para suportar acentuações e caracteres especiais.

Este código utiliza a API da OpenAI para aplicar técnicas de PLN na análise e classificação das reclamações, sem a necessidade de implementar diretamente modelos de redes neurais.

Código utilizado para geração de dados : [analisarReclamacoes.py]()

Saída do código: 

[resultados_classificados.md]()

[resumo_analise.md](resumo_analise.md)



## Conclusão

- **Automatização da Análise com PLN:** Redução do tempo e esforço necessários para analisar reclamações de transporte público utilizando modelos avançados de PLN.
- **Melhoria do Serviço:** Fornecimento de insights valiosos para melhorar a qualidade do transporte público com base nas reclamações dos usuários.
- **Escalabilidade:** A metodologia pode ser aplicada a outros setores que necessitam de análise de grandes volumes de texto, demonstrando a versatilidade das técnicas de PLN.

