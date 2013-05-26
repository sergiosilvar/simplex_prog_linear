# -*- coding: iso-8859-15 -*-
'''
Created on 25/05/2013
@author: sergio




'''


from numpy import matlib
import copy
import numpy as np

def exemplo_hardcoded():
    A = np.array([[2, -1],
                  [1, 2],
                  [-1, 1],
                  [-1, 0],
                  [0, -1]])
    M = np.array([[1, 0],
                  [1, -1]])
    b = np.array([4, 9, 3, 0, 0])
    f = np.array([2, 5])

    A2 = np.dot(A, M)
    f2 = np.dot(f, M)  # - np.dot(f,[0,3])
    b2 = b - np.dot(A, [0, 3])
    print 'func obj 2:'
    print f2
    print 'A2: '
    print A2
    print 'b2:'
    print b2
    
    
    M2 = np.array([[-1.0 / 3, 2.0 / 3],
                   [0, 1]])
    
    A3 = np.dot(A2, M2)
    f3 = np.dot(f2, M2)
    b3 = b2 - np.dot(A2, [1, 0])
    
    print 'func obj 3:'
    print f3
    print 'A3: '
    print A3
    print 'b3:'
    print b3

 
 

    


class SimplexAFS():
    '''
    Implementação do algoritmo Simplex conforme livro "Algorithms" de Christos 
    Papadimitriou et all.
    '''
    
    
    INTEIRO_MIN = -99999
    INTEIRO_MAX = 99999
    
    def __init__(self, nome_arquivo):
        '''
        Inicialização da instância.
        @param nome_arquivo: arquivo que contém o sistema em forma de matriz.
        '''
        # Carrea a matriz inteira do arquivo.
        tableau = np.loadtxt(nome_arquivo)
        
        # Determina o número de variáveis.
        qtd_variaveis = len(tableau[0]) - 1
        
        # Identifica a função objetivo.
        self.funcao_objetivo = tableau[0][:qtd_variaveis]
        
        # Identifica as restrições.
        self.restricoes = tableau[1:, :qtd_variaveis]
        
        # Identifica os valores das restrições.
        self.valores = tableau[1:, len(tableau[0]) - 1]
        

    def __monta_expressao(self, expr, coef, indice):
        sinal = ''
        if coef >= 0: sinal = '+'
        return expr + sinal + str(coef) + '*x_' + str(indice)
    
    def imprimir_sistema(self):
        '''
        Imprime em texto a função objetivo e restrições.
        '''
    
        qtd_var = self.qtd_variaveis() 
        qtd_restr = self.qtd_restricoes()
    
        expressao = 'max '
        for i in range(qtd_var):
            expressao = self.__monta_expressao(expressao, self.funcao_objetivo[i], i)
        print 'Função Objetivo:\n\t' + expressao 
        
        print 'Restrições'
        ''' As restrições são inequações definidas a partir da segunda linha.'''
        for i in range(qtd_restr): 
            expressao = ''
            for j in range(qtd_var):
                expressao = self.__monta_expressao(expressao, self.restricoes[i, j], j)
            expressao = expressao + ' <= ' + str(self.valores[i])
            print '\t[' + str(i) + ']: ' + expressao 


        

    def qtd_variaveis(self):
        '''
        Quantidade de variáveis "x_i" do sistema.
        Nesta implementação é o tamanho do array unidimensional 
        "self.funcao_objetivo".
        '''
        return len(self.funcao_objetivo)

    def __montar_matriz_transformacao(self):
        ''' A Matriz de Transformação é a Matriz Identidade de dimenssão igual 
        ao número de varíaveis, trocando-se a linha correspondente à variável 
        ativa pelo simétrico dos coeficientes da restrição ativa divididos pelo 
        coeficiente da variável ativa na restrição ativa . 
        '''
        
        i_restr_ativ = self.__indice_restr_ativa()
        i_var_ativ = self.__indice_var_ativa()
        
        # Cria a matriz identidade.
        matriz_T = matlib.identity(self.qtd_variaveis())
        
        #Coeficiente da variável ativa na restrição ativa.
        coef_ativo = self.restricoes[i_restr_ativ, i_var_ativ]
        
        
        matriz_T[i_var_ativ] = np.dot(self.restricoes[i_restr_ativ], -1.0 / coef_ativo)
        matriz_T[i_var_ativ, i_var_ativ] = -1.0 / coef_ativo
       
        return matriz_T

    def __indice_var_ativa(self):
        '''
        Determina a variável de maior impacto.
        @return: Posição, começando em 0, da variável com maior coeficiente na
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
        Determina se o critério de parada foi atingido.
        @return: 
            True - todos os coeficientes da função objetivo for menor ou 
                igual a ZERO.
            False - Algum coeficiente da função objetivo é maior que ZERO.
        '''
        
        for v in self.funcao_objetivo:
            if v > 0: 
                return False
        return True
        
    def copiar(self):
        '''
        Cria uma cópia desta instância.
        '''
        return copy.deepcopy(self)
    

    def __indice_restr_ativa(self):
        '''
        A restrição ativa é a restrição de menor valor no array "self.valores".
        @return: Índice da restrição ativa na lista "self.restricoes".
        '''
        valor = self.INTEIRO_MAX
        i_min = self.INTEIRO_MAX
        for i in range(self.qtd_restricoes()):
            if self.restricoes[i, self.__indice_var_ativa()] != 0 :
                if self.valores[i] > 0:
                    if self.valores[i] < valor:
                        valor = self.valores[i]
                        i_min = i
        return i_min
    
    def qtd_restricoes(self):
        '''
        @return Qantidade de inequações que são as restrições do sistema.
        Nesta implementação, é o número de linhas do array bidimensional 
        "self.restricoes".
        '''
        return len(self.restricoes)
    
    
    
    
    def __resolve_sitema_original(self):
        '''
        Reolve um sistema de equações do problema original. As equações são
            selecionadas se seu valor é ZERO no fim da execução do Simplex. 
        @return: Tupla (x_0, x_1, ..., x_n) com os valores solução das variáveis do problema.
        '''
        
        # Índice dos valores iguais a ZERO no fim do Simplex.
        indices = np.where(self.valores == 0)
        
        # Seleciona as equações originais conforme os índices.
        equacoes = self.copia.restricoes[indices]
        
        # Seleciona os valores originais das equações selecionadas.
        valores = self.copia.valores[indices]
        
        # Resolve e retorna tupla com soluções.
        return  np.linalg.solve(equacoes, valores)
    
    
    def __imprimir_solucao(self):
        print 'SOLUCAO:'
        expressao = ''
        for i in range(self.qtd_variaveis()):
            expressao = self.__monta_expressao(expressao, self.solucao[i], i)
        print 'Função Objetivo:\n\t' + expressao 
        
        valor = 0
        for i in range(len(self.copia.funcao_objetivo)):
            x = self.copia.funcao_objetivo[i]
            coef = self.solucao[i]
            valor += coef * x
        print 'Valor: ' + str(valor)
    
    
    def resolver(self):
        '''
        Resolve o Simplex.
        Complexidade: 
        '''

        
        # Armazena valores originais para uso no final.
        self.copia = self.copiar()
        
        
        # Executa o laço enquanto a condição de parada não for atingida.
        while not self.__pode_parar(): #O(v).
            
            i_var_ativa = self.__indice_var_ativa() #O(v)
            i_restr_ativa = self.__indice_restr_ativa() #O(r)
            
            # Monta a matriz de transformação.
            matriz_T = self.__montar_matriz_transformacao()#O(multiplicação de matrizes)
            
            # Transofrmação dos Valores das Restrições.
            vetor = [0 for i in range(self.qtd_variaveis())]#O(v)
            vetor[i_var_ativa] = self.valores[i_restr_ativa] \
                / self.restricoes[i_restr_ativa, i_var_ativa]
            valores_T = self.valores - np.dot(self.restricoes, vetor) #O(multiplicação de matrizes)
            self.valores = valores_T[0:len(valores_T)]
            
            # Transformação das Restrições.
            restricoes_T = np.dot(self.restricoes, matriz_T) #O(multiplicação de matrizes)
            self.restricoes = restricoes_T.getA()
                        
            # Transformação da Função Objetivo.
            funcao_obj_T = np.dot(self.funcao_objetivo, matriz_T) #O(multiplicação de matrizes)
            self.funcao_objetivo = funcao_obj_T.getA()[0]
        
        self.imprimir_sistema() 
        
        self.solucao = self.__resolve_sitema_original()
        
        self.__imprimir_solucao()
        
        return self.solucao
        
            
if __name__ == '__main__':
#    exemplo_hardcoded()
    SimplexAFS('exemplo.txt').resolver()
#    SimplexAFS('pag_204.txt').resolver()

    
