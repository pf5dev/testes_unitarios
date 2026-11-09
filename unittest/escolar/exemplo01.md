## **Exemplo 01**

Suponha que você foi contratado para realizar testes automatizados para um sistema escolar. O módulo para avaliar a nota de um aluno recebe como entrada três notas obtidas pelo aluno em provas, e também, a média dos exercícios e calcula a média de aproveitamento de acordo com a fórmula abaixo:

$$
\text{media-aproveitamento}=\frac{n_1+2\cdot n_{2}+3 \cdot n_{3}+ \text{mediaexercicios}}{7}
$$

A atribuição de conceitos obedece a tabela abaixo:

|média de aproveitamento|Conceito|
|:-----------------------:|:--------:|
|>= 9,0|A|
|>= 7,5 e < 9|B|
|>= 6,0 e < 7,5|C|
|< 6,0|D|

Escreva testes unitários para as funções do módulo *escolar.py*:

$$
avaliarnotas(n1, n2, n3, mediaexercicios): ...
$$
$$
\text{mediaaproveitamento((n1+2*n2+3*n3+mediaexercicios)/7): ...}
$$

Utilize os valores abaixo como parâmetros de entrada e saída da função: 
$$avaliarnotas
(n1, n2, n3, mediaexercicios)
$$
|Entrada|Saída|
|:-----:|:---:|
|n1 = -1|exceção: ValueError|
|n2 = 0|"|
|n3 = 0|"|
|media_exercicios = 0|"|
|n1 = 0|"|
|n2 = -1|"|
|n3 = 0|"|
|media_exercicios = 0|"|
|n1 = 0|"|
|n2 = 0|"|
|n3 = -1|"|
|media_exercicios = 0|"|
|n1 = 10|'A'|
|n2 = 10|"|
|n3 = 10|"|
|media_exercicios = 10|"|
|n1 = 9|'A'|
|n2 = 9|"|
|n3 = 9|"|
|media_exercicios = 9|"|
|n1 = 8.9|'B'|
|n2 = 8.9|"|
|n3 = 8.9|"|
|media_exercicios = 8.9|"|
|n1 = 7.5|'B'|
|n2 = 7.5|"|
|n3 = 7.5|"|
|media_exercicios = 7.5|"|
|n1 = 7.4|'C'|
|n2 = 7.4|"|
|n3 = 7.4|"|
|media_exercicios = 7.4|"|
|n1 = 6.0|'C'|
|n2 = 6.0|"|
|n3 = 6.0|"|
|media_exercicios = 6.0|"|
|n1 = 5.9|'D'|
|n2 = 5.9|"|
|n3 = 5.9|"|
|media_exercicios = 5.9|"|
|n1 = 0.0|'D'|
|n2 = 0.0|"|
|n3 = 0.0|"|
|media_exercicios = 0.0|"|