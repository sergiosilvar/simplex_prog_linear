# -*- coding: iso-8859-15 -*-
'''
Classe Simplex AFS:

Implementação do algoritmo Simplex como programação linear, objeto de trabalho de 
conclusão da disciplina Estrutura de Dados, do curso de Modelagem Matemática da
Informação, Fundação Getúlio Vargas, 2013.

Desenvolvido pelos alunos Anna Carolina, Fernando Menucci e Sérgio Rodrigues.

Para maiores informações sobre o algoritmo Simplex, consulte 
http://pt.wikipedia.org/wiki/Algoritmo_simplex.
'''


from numpy import matlib
import copy
import numpy as np

class SimplexAFS():
    '''
    Implementação do algoritmo Simplex conforme livro "Algorithms" de Christos 
    Papadimitriou et all.
    '''
    
    INTEIRO_MIN = -99999
    INTEIRO_MAX = 99999
    APROX_ZERO = 0.01
    

    
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

    def __imprimir_sistema(self, simplex_obj,titulo=None):
        '''
        Imprime em texto a função objetivo e restrições.
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
        ''' As restrições são inequações definidas a partir da segunda linha.'''
        for i in range(qtd_restr): 
            expressao = ''
            for j in range(qtd_var):
                expressao = simplex_obj.__monta_expressao(expressao, simplex_obj.restricoes[i, j], j)
            expressao = expressao + ' <= ' + str(simplex_obj.valores[i])
            print '\t[' + str(i) + ']: ' + expressao 
        print '\n'


        

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
        valor da restrição ativa . 
        '''
        
        i_restr_ativ = self.__indice_restr_ativa()
        i_var_ativ = self.__indice_var_ativa()
        
        # Cria a matriz identidade.
        matriz_T = matlib.identity(self.qtd_variaveis())
        
        #Coeficiente da variável ativa na restrição ativa.
        valor = self.restricoes[i_restr_ativ, i_var_ativ]
        
        matriz_T[i_var_ativ] = np.dot(self.restricoes[i_restr_ativ], (-1.0 / valor))
       
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
        
    def __copiar(self):
        '''
        Cria uma cópia desta instância.
        '''
        return copy.deepcopy(self)
    

    def __indice_restr_ativa(self):
        '''
        A restrição ativa é a restrição de menor valor no array "self.valores".
        @return: Índice da restrição ativa na lista "self.restricoes".
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
        @return Qantidade de inequações que são as restrições do sistema.
        Nesta implementação, é o número de linhas do array bidimensional 
        "self.restricoes".
        '''
        return len(self.restricoes)
    
    
    
    
    def __resolve_sitema_original(self):
        '''
        Reolve o sistema de equações do problema original. As equações são
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
        self.solucao =  np.linalg.solve(equacoes, valores)
    
    
    def imprimir_solucao(self):
        '''
        Gera uma saída no prompt de comando formatada para leitura.
        '''
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
        '''
        Aplica a matriz de transformação aos valores das restrições.
        '''
        
        i_var_ativa = self.__indice_var_ativa() 
        i_restr_ativa = self.__indice_restr_ativa() 
        vetor = [0 for i in range(self.qtd_variaveis())]
        vetor[i_var_ativa] = self.valores[i_restr_ativa] \
            / self.restricoes[i_restr_ativa, i_var_ativa]
        valores_T = self.valores - np.dot(self.restricoes, vetor) 
        self.valores = valores_T[0:len(valores_T)]
        
        # Arredonda os valores para zero conforme uma dada aproximação.
        for index, value in np.ndenumerate(self.valores):
            if value < self.APROX_ZERO:
                self.valores[index] = 0


    def __transformar_restricoes(self, matriz_T):
        '''
        Aplica a matriz de transformação às restrições.
        @param matriz_T: Matriz de transformação.
        '''
        restricoes_T = np.dot(self.restricoes, matriz_T) #O(multiplicação de matrizes)
        self.restricoes = restricoes_T.getA()


    def __transformar_funcao_objetivo(self, matriz_T):
        '''
        Aplica a matriz de transformação à função objetivo.
        @param matriz_T: Matriz de transformação.
        '''
        funcao_obj_T = np.dot(self.funcao_objetivo, matriz_T) #O(multiplicação de matrizes)
        self.funcao_objetivo = funcao_obj_T.getA()[0]


    def imprimir_sistema_original(self):
        '''
        Gera uma saída no prompt de comando apresentando o sistema original.
        '''
        return self.__imprimir_sistema(self.copia, 'SISTEMA ORIGINAL')


    def imprimir_sistema_final(self):
        '''
        Gera uma saída no prompt de comando apresentando o sistema final.
        '''
        
        return self.__imprimir_sistema(self, 'SISTEMA FINAL')

    def resolver(self):
        '''
        Executa o algoritmo Simplex para encontrar a solução do problema dado.
        '''

        
        # Armazena sistema original para uso após laço principal.
        self.copia = self.__copiar()
        
        
        # Laço principal.
        while not self.__pode_parar(): #O(v).
           
            # Monta a matriz de transformação.
            matriz_T = self.__montar_matriz_transformacao()#O(multiplicação de matrizes)
            
            # Transofrmação dos Valores das Restrições.
            self.__transformar_valores()
            
            # Transformação das Restrições.
            self.__transformar_restricoes(matriz_T)
                        
            # Transformação da Função Objetivo.
            self.__transformar_funcao_objetivo(matriz_T)
        
        
        # Resolver sistema original.
        self.__resolve_sitema_original()

class SimplexAFSErro(Exception):
    '''
    Classe de implementação do algoritmo Simplex.
    Para mais informações sobre o Simplex, consulte http://pt.wikipedia.org/wiki/Algoritmo_simplex.
    '''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
            
