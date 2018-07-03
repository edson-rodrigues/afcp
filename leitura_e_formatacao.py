import re
from functions import *

palavra = str(input("\nDigite uma palavra para ser processada pelo automato: "))
arquivo = open('afcp1.txt', 'r')
automato = arquivo.readline();

alfabeto = re.findall(r'[a-e]', automato)
estados = RemoveRepetidosLista(re.findall(r'q\w', automato))
alfabeto_pilha = re.findall(r'[A-C]|[E-Z]', automato)

regras_de_producao = []

linha = arquivo.readline()
while linha != '':
    regras_de_producao.append(re.findall(r'q\w|[a-z]|[A-Z]*[A-Z]*[A-Z]|_|\?', linha))

    linha = arquivo.readline()

estado_inicial = regras_de_producao[0][0]
estado_final = regras_de_producao[-1][3]

verifica_alfabeto(converter_para_string(palavra), alfabeto)
#processamento(regras_de_producao, estado_inicial, estado_final, palavra)
#print(alfabeto)

