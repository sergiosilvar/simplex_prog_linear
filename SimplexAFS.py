# -*- coding: iso-8859-15 -*-
'''
Created on 25/05/2013
@author: sergio
'''


from numpy import matlib
import copy
import numpy as np
class SimplexAFS():
    '''
    Implementa��o do algoritmo Simplex conforme livro "Algorithms" de Christos 
    Papadimitriou et all.
    '''
    
    INTEIRO_MIN = -99999
    INTEIRO_MAX = 99999
    APROX_ZERO = 0.01
    

    
    def __init__(self, nome_arquivo):
        '''
        Inicializa��o da inst�ncia.
        @param nome_arquivo: arquivo que cont�m o sistema em forma de matriz.
        '''
        
        # Carrea a matriz inteira do arquivo.
        tableau = np.loadtxt(nome_arquivo)
        
        # Determina o n�mero de vari�veis.
        qtd_variaveis = len(tableau[0]) - 1
        
        # Identifica a fun��o objetivo.
        self.funcao_objetivo = tableau[0][:qtd_variaveis]
        
        # Identifica as restri��es.
        self.restricoes = tableau[1:, :qtd_variaveis]
        
        # Identifica os valores das restri��es.
        self.valores = tableau[1:, len(tableau[0]) - 1]
        

    def __monta_expressao(self, expr, coef, indice):
        sinal = ''
        if coef >= 0: sinal = '+'
        return expr + sinal + str(coef) + '*x_' + str(indice)

    def __imprimir_sistema(self, simplex_obj,titulo=None):
        '''
        Imprime em texto a fun��o objetivo e restri��es.
        '''
    
        qtd_var = simplex_obj.qtd_variaveis() 
        qtd_restr = simplex_obj.qtd_restricoes()
        
        if titulo != None:
            print titulo.upper()
        expressao =  ''
        for i in range(qtd_var):
            expressao = simplex_obj.__monta_expressao(expressao, simplex_obj.funcao_objetivo[i], i)
        print 'Funcao Objetivo:\n\t' + expressao 
        
        print 'Restricoes'
        ''' As restri��es s�o inequa��es definidas a partir da segunda linha.'''
        for i in range(qtd_restr): 
            expressao = ''
            for j in range(qtd_var):
                expressao = simplex_obj.__monta_expressao(expressao, simplex_obj.restricoes[i, j], j)
            expressao = expressao + ' <= ' + str(simplex_obj.valores[i])
            print '\t[' + str(i) + ']: ' + expressao 
        print '\n'


        

    def qtd_variaveis(self):
        '''
        Quantidade de vari�veis "x_i" do sistema.
        Nesta implementa��o � o tamanho do array unidimensional 
        "self.funcao_objetivo".
        '''
        return len(self.funcao_objetivo)

    def __montar_matriz_transformacao(self):
        ''' A Matriz de Transforma��o � a Matriz Identidade de dimenss�o igual 
        ao n�mero de var�aveis, trocando-se a linha correspondente � vari�vel 
        ativa pelo sim�trico dos coeficientes da restri��o ativa divididos pelo 
        valor da restri��o ativa . 
        '''
        
        i_restr_ativ = self.__indice_restr_ativa()
        i_var_ativ = self.__indice_var_ativa()
        
        # Cria a matriz identidade.
        matriz_T = matlib.identity(self.qtd_variaveis())
        
        #Coeficiente da vari�vel ativa na restri��o ativa.
        valor = self.restricoes[i_restr_ativ, i_var_ativ]
        
        matriz_T[i_var_ativ] = np.dot(self.restricoes[i_restr_ativ], (-1.0 / valor))
       
        return matriz_T

    def __indice_var_ativa(self):
        '''
        Determina a vari�vel de maior impacto.
        @return: Posi��o, come�ando em 0, da vari�vel com maior coeficiente na
        lista "self.funcao_objetivo".
        '''
        indice = self.INTEIRO_MIN
        maior = self.INTEIRO_MIN
        for i in range(len(self.funcao_objetivo)):
            if self.funcao_objetivo[i] > maior:
                maior = self.funcao_objetivo[i]
                indice = i
        return indice
    
    def __pode_parar(self):
        '''
        Determina se o crit�rio de parada foi atingido.
        @return: 
            True - todos os coeficientes da fun��o objetivo for menor ou 
                igual a ZERO.
            False - Algum coeficiente da fun��o objetivo � maior que ZERO.
        '''
        
        for v in self.funcao_objetivo:
            if v > 0: 
                return False
        return True
        
    def __copiar(self):
        '''
        Cria uma c�pia desta inst�ncia.
        '''
        return copy.deepcopy(self)
    

    def __indice_restr_ativa(self):
        '''
        A restri��o ativa � a restri��o de menor valor no array "self.valores".
        @return: �ndice da restri��o ativa na lista "self.restricoes".
        '''

        x_i = self.restricoes[:, self.__indice_var_ativa()]
        minq = self.INTEIRO_MAX
        i_min = self.INTEIRO_MAX
        for i in range(len(x_i)):
            if x_i[i] != 0:
                q = self.valores[i]/x_i[i]
                if q > 0 and q < minq:
                    minq = q
                    i_min = i
        return i_min



    def qtd_restricoes(self):
        '''
        @return Qantidade de inequa��es que s�o as restri��es do sistema.
        Nesta implementa��o, � o n�mero de linhas do array bidimensional 
        "self.restricoes".
        '''
        return len(self.restricoes)
    
    
    
    
    def __resolve_sitema_original(self):
        '''
        Reolve o sistema de equa��es do problema original. As equa��es s�o
            selecionadas se seu valor � ZERO no fim da execu��o do Simplex. 
        @return: Tupla (x_0, x_1, ..., x_n) com os valores solu��o das vari�veis do problema.
        '''
        
        # �ndice dos valores iguais a ZERO no fim do Simplex.
        indices = np.where(self.valores == 0)
        
        # Seleciona as equa��es originais conforme os �ndices.
        equacoes = self.copia.restricoes[indices]
        
        # Seleciona os valores originais das equa��es selecionadas.
        valores = self.copia.valores[indices]
        
        # Resolve e retorna tupla com solu��es.
        self.solucao =  np.linalg.solve(equacoes, valores)
    
    
    def imprimir_solucao(self):
        print 'SOLUCAO:'
        expressao = ''
        for i in range(self.qtd_variaveis()):
            expressao = self.__monta_expressao(expressao, self.solucao[i], i)
        print 'Funcao Objetivo:\n\t' + expressao 
        
        valor = 0
        for i in range(len(self.copia.funcao_objetivo)):
            x = self.copia.funcao_objetivo[i]
            coef = self.solucao[i]
            valor += coef * x
        print 'Valor: ' + str(valor)


    def __transformar_valores(self):
            i_var_ativa = self.__indice_var_ativa() #O(v)
            i_restr_ativa = self.__indice_restr_ativa() #O(r)
            vetor = [0 for i in range(self.qtd_variaveis())]#O(v)
            vetor[i_var_ativa] = self.valores[i_restr_ativa] \
                / self.restricoes[i_restr_ativa, i_var_ativa]
            valores_T = self.valores - np.dot(self.restricoes, vetor) #O(multiplica��o de matrizes)
            self.valores = valores_T[0:len(valores_T)]
            for index, value in np.ndenumerate(self.valores):
                if value < self.APROX_ZERO:
                    self.valores[index] = 0
    

    def __transformar_restricoes(self, matriz_T):
        restricoes_T = np.dot(self.restricoes, matriz_T) #O(multiplica��o de matrizes)
        self.restricoes = restricoes_T.getA()


    def __transformar_funcao_objetivo(self, matriz_T):
        funcao_obj_T = np.dot(self.funcao_objetivo, matriz_T) #O(multiplica��o de matrizes)
        self.funcao_objetivo = funcao_obj_T.getA()[0]


    def imprimir_sistema_original(self):
        return self.__imprimir_sistema(self.copia, 'SISTEMA ORIGINAL')


    def imprimir_sistema_final(self):
        return self.__imprimir_sistema(self, 'SISTEMA FINAL')

    def resolver(self):
        '''
        Executa o algoritmo Simplex.
        
        '''

        
        # Armazena sistema original para uso ap�s la�o principal.
        self.copia = self.__copiar()
        
        
        # La�o principal.
        while not self.__pode_parar(): #O(v).
           
            # Monta a matriz de transforma��o.
            matriz_T = self.__montar_matriz_transformacao()#O(multiplica��o de matrizes)
            
            # Transofrma��o dos Valores das Restri��es.
            self.__transformar_valores()
            
            # Transforma��o das Restri��es.
            self.__transformar_restricoes(matriz_T)
                        
            # Transforma��o da Fun��o Objetivo.
            self.__transformar_funcao_objetivo(matriz_T)
        
        
        # Resolver sistema original.
        self.__resolve_sitema_original()

class SimplexAFSErro(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
            

    
