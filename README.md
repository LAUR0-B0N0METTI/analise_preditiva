# Análise Preditiva de Vendas - README

Este repositório contém um algoritmo para análise preditiva de vendas, utilizando técnicas de ciência de dados. Esse algoritmo é complementar ao programa "cria_tabela.py", responsável por gerar um conjunto de dados sintético para fins de estudo.

## Funcionalidades

- **Exploração de Dados:** O código realiza a leitura de dados de vendas de uma loja a partir de um arquivo Excel. A etapa inicial envolve a exploração e preparação dos dados, incluindo a extração de informações temporais.

- **Engenharia de Recursos:** São adicionadas colunas 'Ano', 'Mês' e 'Dia' à tabela, derivadas da coluna de data, aprimorando a capacidade preditiva do modelo.

- **Modelagem Preditiva:** Utilizando um modelo RandomForestRegressor, o algoritmo visa prever a quantidade de itens vendidos com base em características como ano, mês, dia, loja e tamanho.

- **Avaliação de Modelo:** A qualidade do modelo é avaliada através do cálculo do Mean Squared Error (Erro Quadrático Médio) utilizando dados de teste.

- **Divisão de Dados:** O conjunto de dados é dividido em conjuntos de treino e teste para avaliação robusta.

## Pré-requisitos

- Python 3
- Bibliotecas Python: pandas, scikit-learn, matplotlib

## Como Usar

1. **Instalação das Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Execução do Algoritmo:**
   ```bash
   python analise_preditiva.py
   ```

3. **Resultado:**
   O algoritmo exibirá o Mean Squared Error (Erro Quadrático Médio) como métrica de avaliação do modelo.

## Complemento do Programa "cria_tabela.py"

Este algoritmo é complementar ao programa "cria_tabela.py", o qual é responsável por gerar dados sintéticos de vendas para fornecer um conjunto de dados realista para análise.
<br>
<br>
## Autor

[ Lauro Bonometti ]
<br>
<br>
## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

**Nota:** Este projeto é desenvolvido apenas para fins educacionais e de estudo em ciência de dados. Os dados gerados são fictícios e não representam informações reais.