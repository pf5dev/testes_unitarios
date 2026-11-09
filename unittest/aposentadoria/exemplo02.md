## **Exemplo 02**

Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito:

- Ter no mínimo 65 anos de idade.
- Ter trabalhado no mínimo 30 anos.
- Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.

*Restrição: os parâmetros de entrada, idade e tempo_de_servico, devem, necessariamente, ser números inteiros e maiores que zero*.

Escreva testes unitários para a função do módulo:

$$
verificarqualificacaoempregado(idade, tempodeservico): ..
$$

- entrada: idade e tempodeservico
- saída: 'Requerer aposentadoria' ou 'Não requerer'

Utilize os valores abaixo como parâmetros de entrada e saída da função:
$$
verificarqualificacaoempregado(idade, tempodeservico): ..
$$

|Entrada|Saída|
|:-----:|:---:|
|idade = 0|exceção: ValueError|
|tempo_de_servico = 10|"|
|idade = 20|"|
|tempo_de_servico = 0|"|
|idade = '65'|exceção: TypeError|
|tempo_de_servico = 30|"|
|idade = 65|exceção: TypeError|
|tempo_de_servico = '30'|"|
|idade = 65|'Requerer aposentadoria'|
|tempo_de_servico = 20|"|
|idade = 59|"|
|tempo_de_servico = 30|"|
|idade = 60|"|
|tempo_de_servico = 25|"|
|idade = 59|'Não requerer'|
|tempo_de_servico = 24|"|