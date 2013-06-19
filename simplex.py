# -*- coding: iso-8859-15 -*-

'''
Exemplo de utilização da classe SimplexAFS.
'''
from SimplexAFS import SimplexAFS
import sys
from numpy.linalg.linalg import LinAlgError

if __name__ == '__main__':
    n = len(sys.argv)
    if n != 2:
        print 'Comando invalido!'
        print 'Use: python simplex.py <nome do arquivo>'
    else:
        nome_arquivo = sys.argv[1]
        print '\n================================================================================'
        print '\n                   SIMPLEX - Arquivo: ' + nome_arquivo
        print '\n--------------------------------------------------------------------------------\n'
        
        try:
            s = SimplexAFS(nome_arquivo)
            s.resolver()
            s.imprimir_sistema_original()
            s.imprimir_solucao()
        except IOError:
            print 'ERRO: Nome do arquivo invalido: \"' + nome_arquivo + '\"'
        except LinAlgError: 
            print 'ERRO: Nao foi possivel encontrar uma solucao. Verifique conteudo do arquivo.'
        print '\n================================================================================'
