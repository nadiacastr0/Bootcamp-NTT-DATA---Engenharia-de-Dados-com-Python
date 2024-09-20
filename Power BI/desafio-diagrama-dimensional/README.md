# Desafio de modelagem dimensional

## Star Schema

Fato: A tabela FatoCurso centraliza os dados principais para análise, incluindo o número de inscritos, a duração e o custo dos cursos.
Dimensões:
- Curso: Contém informações detalhadas sobre cada curso, como nome, descrição e categoria.
- Professor: Armazena dados sobre os professores palestrantes, incluindo nome, área de especialização e título acadêmico.
- Disciplina: Inclui informações sobre as disciplinas, como nome, descrição e departamento responsável.
- Data: Permite a análise temporal dos dados, com campos que abrangem diferentes níveis de granularidade, como ano, mês, dia, trimestre e semestre.

![star schema](./image-diagrama-star-schema.png)

## Modelando um Star Schema com DAX
Utilizei a tabela única de Financial Sample para criar as tabelas dimensão e fato do nosso modelo baseado em star schema.

Fato: F_Vendas 
Dimensões:
- D_Produtos: tabela criada por agrupamento das informações, colunas sendo construídas a partir de condicional – Índice de Produtos
- D_Produtos_Detalhes
- D_Descontos 
- D_Detalhes
- D_Calendário - Criada por DAX com calendar()

![star schema dax](./image-diagrama-star-schema-dax.png)