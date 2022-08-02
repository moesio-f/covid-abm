# Calibração de Modelos baseados em Agentes com Algoritmos Evolucionários

Esse projeto aplica diferentes algoritmos evolucionários para calibração de parâmetros do [OpenABM-Covid19](https://github.com/BDI-pathogens/OpenABM-Covid19) para os dados brasileiros acerca da COVID-19.

## Objetivo

O intuito é compreender qual conjunto de parâmetros do modelo melhor descreve o cenário brasileiro e como políticas públicas não-farmacológicas poderiam ter influenciado esse cenário. Em especial, o objetivo é calibrar o modelo para os dados de COVID-19 apresentados pela cidade do **Recife/PE** no mês de **Janeiro de 2022** (01/01 a 31/01).

## Agent-Based Modelling (ABM)

Agent-based Modelling (ABM), em tradução livre "Modelagem baseada em Agentes", é um paradigma amplamente explorado pela literatura para construção de modelos que operam utilizando um conjunto de entidades autônomas chamadas de *agentes*. Tal paradigma permite que simulações complexas do mundo real sejam realizadas através das interações de múltiplos agentes artificiais com comportamentos distintos.

## Calibração de ABMs

Uma etapa crucial na aplicação e uso de tais modelos é a **calibração** de seus parâmetros. Nessa etapa, diferentes estratégias são aplicadas para buscar parâmetros que melhor capturem o mundo real. 

Uma abordagem recente na literatura para a etapa de calibração consistem em utilizar algoritmos evolucionários no lugar da calibração manual.

# OpenABM-Covid19

O OpenABM-Covid19 é um modelo baseado em agentes desenvolvido para simular a transmissão e contágio de COVID-19 em uma cidade. O principal objetivo é permitir a análise dos efeitos de medidas ativas e passivas para o controle da doença. O modelo possui uma série de parâmetros que podem ser alterados para melhor descrever a situação de uma cidade.

# Algoritmos Escolhidos

1. Standard Particle Swarm Optimization (**SPSO**)
2. Restart Covariance Matrix Adaptation Evolution Strategy With Increasing Population Size (**IPOP-CMA-ES**)
3. Success-History Based Parameter Adaptation for Differential Evolution (**SHADE**)

# Parâmetros e Representação

O OpenABM-Covid19 possui um total de 217 parâmetros de entrada, uma descrição desses parâmetros pode ser encontrada no [repositório oficial](https://github.com/BDI-pathogens/OpenABM-Covid19/blob/master/documentation/parameters/parameter_dictionary.md). Para tornar o problema factível aos recursos disponíveis, os seguintes parâmetros (15) serão considerados para calibração automática:

| Nome | Descrição | 
|  ---- | ---- |
| `mean_work_interactions_child` | Média de interações na escola (0-19 anos). |
| `mean_work_interactions_adult` | Média de interações na escola/trabalho (20-69 anos). | 
| `mean_work_interactions_elderly` | Média de interações na escola/trabalho (70+ anos). |
| `infectious_rate` | Quantidade média de indivíduos infectados por um indivíduo positivo sintomático. |
| `quarantine_length_self` | Número máximo de dias para indivíduos sintomáticos (análise própria). |
| `quarantine_length_traced_symptoms`| Número máximo de dias para indivíduos contactes com casos suspeitos. |
| `quarantine_length_traced_positive` | Número máximo de dias para indivíduos contactantes com casos confirmados. |
| `quarantine_length_positive` | Número máximo de dias para indivíduos positivados. |
| `lockdown_time_on`| Tempo (dias) do início do lockdown. |
| `lockdown_elderly_time_on` | Tempo (dias) do início do lockdown para idosos. |
| `lockdown_time_off`| Tempo (dias) do término do lockdown. |
| `lockdown_elderly_time_off` | Tempo (dias) do término do lockdown para idosos. |
| `successive_lockdown_duration` | Duração de lockdowns sucessivos (dias)
| `successive_lockdown_gap` | Intervalo entre lockdowns sucessivos (dias)
| `successive_lockdown_time_on` | Quantidade de dias quando lockdown sucessivos são ativados

Os seguintes parâmetros foram calibrados manualmente:

| Nome | Descrição | 
|  ---- | ---- |
| `n_total` | População total simulada |
| `end_time` | Total de dias simulados |
| `n_seed_infection` | Quantidade de infectados no início do experimento |
| `household_size_1` | Número de "casas" com 1 pessoa (mil) |
| `household_size_2` | Número de "casas" com 2 pessoas (mil) |
| `household_size_3` | Número de "casas" com 3 pessoas (mil) |
| `household_size_4` | Número de "casas" com 4 pessoas (mil) |
| `household_size_5` | Número de "casas" com 5 pessoas (mil) |
| `household_size_6` | Número de "casas" com 6 pessoas (mil) |
| `population_0_9`| População com idade entre 0 e 9 anos |
| `population_10_19` | População com idade entre 10 e 19 anos |
| `population_20_29`| População com idade entre 20 e 29 anos |
| `population_30_39` | População com idade entre 30 e 39 anos |
| `population_40_49` | População com idade entre 40 e 49 anos |
| `population_50_59` | População com idade entre 50 e 59 anos |
| `population_60_69` | População com idade entre 60 e 69 anos |
| `population_70_79` | População com idade entre 70 e 79 anos |
| `population_80` | População com idade maior ou igual a 80 anos |

Demais parâmetros são mantidos os valores padrão do simulador.

## Representação

Para utilizar os algoritmos evolucionários selecionados, faz-se necessário modelar o problema de calibração como um problema de otimização. Nesse sentido, precisamos definir a **função objetiva** e a representação das **soluções**.

As soluções (ou *candidatos*) serão representadas como um vetor $\bm{\mathrm{x}} \in \mathbb{R}^{15}$ de números reais, onde cada uma das componentes representa um dos parâmetros a serem calibrados. Entretanto, um função de mapeamento $\phi: \mathbb{R}^{15} \to D$ é utilizada para mapear o vetor de número reais ao conjunto $D = \mathbb{R}^4 \times \mathbb{N}^{11}$ de possíveis combinação entre os parâmetros.

A função objetiva $f: \mathbb{R}^{15} \to \mathbb{R}$ é definida da seguinte forma:

$f(\bm{\mathrm{x}}) = \left((g\circ \phi)(\bm{\mathrm{x}}) - \hat{Y}\right)^2$, onde $\phi$ é a função de mapeamento, $g: D \to \mathbb{N}$ produz a quantidade cumulativa de infectados usando os parâmetros $\phi(\bm{\mathrm{x}})$ no simulador, e $\hat{Y}$ é o valor real da quantidade de infectados.

# Conjunto de Dados

O conjunto de dados utilizados nesse trabalho incluem os seguintes:

- Dados da COVID-19 no Estado de Pernambuco **(SEPLAG/PE)**: https://dados.seplag.pe.gov.br/apps/corona.html
  - Usados para definição da função objetiva.
- Dados Demográficos do Recife **(IBGE)**: https://cidades.ibge.gov.br/brasil/pe/recife/panorama
  - Usado para calibração manual dos parâmetros.
- Distribuição da População do Recife **(IBGE, CENSO 2010)**: https://censo2010.ibge.gov.br/sinopse/webservice/frm_piramide.php?codigo=261160
  - Usado para calibração manual dos parâmetros.

# Como utilizar

TODO

# Referências

- ***OpenABM-Covid19**: an agent-based model for modelling the spread of SARS-CoV-2 (coronavirus) and control interventions for the Covid-19 epidemic*: https://github.com/BDI-pathogens/OpenABM-Covid19
- ***jMetal**, a framework for multi-objective optimization with metaheuristics*: https://github.com/jMetal/jMetal