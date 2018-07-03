def RemoveRepetidosLista(l):
    # cria um dicionario em branco
    dict = {}
    # para cada valor na lista l
    for word in l:
        # adiciona ao dicionario: valor:1
        # note que se for repetido o valor somente sobrescreve ele :)
        dict[word] = 1
    # retorna uma copia das 'keys'
    l[:] = dict.keys()
    return l
def processamento(regras_de_producao, estado_inicial, estado_final, palavra):
    print ('hello world')

def converter_para_string(lista):
    retorno = ''
    for i in lista:
        retorno = retorno + lista
    return retorno

def verifica_alfabeto(palavra, alfabeto):
    for i in range(len(palavra)):
            if(alfabeto.find(palavra[i]) == -1):
                print("\nWARNING: voce digitou um ou mais simbolos que nao pertencem ao alfabeto do automato!!!")
                break
    return False




