# 86400 Daniel dos Santos Fernandes

from math import sqrt
from math import ceil

#1.1.1 Geracao das Chaves
def gera_chave1(letras):    
    return (letras[0:5], letras[5:10], letras[10:15], letras[15:20], letras[20:])

#1.1.2 Encriptacao de Mensagens
def obtem_codigo1(car, chave):
    for i in range(0, 5):
        for j in range(0, 5):
            if car==chave[i][j]:
                return str(i)+str(j)
   
def codifica1(cad, chave):
    codigo=''
    for k in range(0, len(cad)):
        codigo=codigo + obtem_codigo1(cad[k], chave)
    return codigo

#1.1.3 Desencriptacao de Mensagens
def obtem_car1(cod, chave):
    c=chave[eval(cod[0])][eval(cod[1])]
    return c

def descodifica1(cad_codificada, chave):
    b=''
    for l in range(0, len(cad_codificada)-1, 2):
        b=b + obtem_car1(cad_codificada[l]+cad_codificada[l+1], chave)
    return b

#1.2.1 Geracao das Chaves
def gera_chave2(letras):
    chave=()
    if ceil(sqrt(len(letras)-(ceil(sqrt(len(letras)))-1)))>ceil(sqrt(len(letras)))-1:
        for i in range(0, len(letras), ceil(sqrt(len(letras)))):
            chave=chave+((letras[i:i+ceil(sqrt(len(letras)))]),)
    else:
        for i in range(0, len(letras), ceil(sqrt(len(letras)))-1):
            chave=chave+((letras[i:i+ceil(sqrt(len(letras)))-1]),)        
    return chave

#1.2.2 Encriptcao de Mensagens
def obtem_codigo2(car, chave):
    test=False
    for i in range(0, len(chave)):
        for j in range(0, len(chave[i])):
            if car==chave[i][j]:
                cod=str(i)+str(j)
                test=True
    if test==True:    
        return cod
    else:
        return 'XX'
            
def codifica2(cad, chave):
    codigo=''
    for k in range(0, len(cad)):
        codigo=codigo + obtem_codigo2(cad[k], chave)
    return codigo

#1.2.3 Desencriptacao de Mensagens
def obtem_car2(cod, chave):
    if cod=='XX':
        return '?'
    else:
        c=chave[eval(cod[0])][eval(cod[1])]
        return c

def descodifica2(cad_codificada, chave):
    b=''
    for l in range(0, len(cad_codificada)-1, 2):
        b=b + obtem_car2(cad_codificada[l]+cad_codificada[l+1], chave)
    return b    

        
    