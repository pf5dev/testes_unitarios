import os

os.system('cls')

'''

função: verificar_qualificacao_empregado()

entrada: idade e tempo_de_servico

saída: 'Requerer aposentadoria' ou 'Não requerer'

Critérios para verificar se o funcionário está 

qualificado para aposentadoria:

 - Ter no mínimo 65 anos de idade.

 - Ter trabalhado no mínimo 30 anos.

 - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos. 

Restrição: os parâmetros de entrada, idade e tempo_de_servico, devem, necessariamente, ser números inteiros e maiores que zero.

'''

REQUERER = 'Requerer aposentadoria'
NAO_REQUERER = 'Não requerer'

def verificar_qualificacao_empregado(idade, tempo_de_servico):
    
    if type(idade) == int and type(tempo_de_servico) == int:
        pass
    else:
        raise TypeError(f'exceção: TypeError') 
    if idade == 0 or tempo_de_servico == 0:
        raise ValueError(f'exceção: ValueError') 
    if idade >= 65:
        return REQUERER
    elif tempo_de_servico >= 30:
        return REQUERER
    elif idade >= 60 and tempo_de_servico >= 25:
        return REQUERER
    return NAO_REQUERER

if __name__ == '__main__':    
    l=[(65,20),(59,30),(60,25),(59,24)]
    for j in range(len(l)):
        idade,tempo_de_servico=l[j]
        print(verificar_qualificacao_empregado(idade,tempo_de_servico))