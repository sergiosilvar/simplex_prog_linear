# -*- coding: iso-8859-15 -*-

'''
Created on 27/05/2013

@author: sergio
'''
from SimplexAFS import SimplexAFS
import sys

if __name__ == '__main__':
    n = len(sys.argv)
    if n != 2:
        print 'Comando invalido!'
        print 'Use: python simplex.py <nome do arquivo>'
    else:
        nome_arquivo = sys.argv[1]
        print '\n\nSIMPLEX - Arquivo: ' + nome_arquivo
        
        try:
            s = SimplexAFS(nome_arquivo)
            s.resolver()
            s.imprimir_sistema_original()
            s.imprimir_solucao()
        except IOError:
            print 'ERRO: Nome do arquivo invalido: \"' + nome_arquivo + '\"'