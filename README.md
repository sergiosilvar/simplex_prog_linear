## SIMPLEX

Este repositório contém uma implementação do [algoritmo Simplex](http://pt.wikipedia.org/wiki/Algoritmo_simplex) baseado na técnica de programação linear apresentada no livro [Algorithms, de Christos Papadimitriou, Sanvoy Dasgupta e Umesh Vazirani](http://amzn.com/0073523402).


Esta implementação foi desenvolvida por Anna Carolina, Fernando Menucci e Sérgio Rodrigues, como trabalho da disciplina [Estrutura de Dados e Algoritmos] (https://github.com/arademaker/ED-2013-1), do curso de [Mestrado em Modelagem Matemática da Informação](http://emap.fgv.br) da Fundação Getúlio Vargas, Rio de Janeiro, 2013.


O algoritmo está preparado para maximização, portanto para usá-lo em minimização é necessário converter a função objetivo pelo simétrico.

### ARQUIVOS


- **SimplexAFS.py**: Classe SimplexAFS que implementa o algoritmo tomando como entrada o sistema a ser maximizado como uma matriz descrita em um arquivo texto a ser passado como parâmetro.
- **simplex.py**: Módulo para execução em linha de comando, caso queira utilizar o algoritmo diretamente no comando do sistema operacional.
 
### Pré-requisitos

Para utilizar o algorimto é necessário os seguintes softwares:

- [Interpretador Python versão 2.7;] (http://www.python.org)
- [Biblioteca Numpy;] (http://www.numpy.org)
- Editor de texto de sua preferência.

### Como usar em linha de comando

 Para executar o algoritmo Simplex, abra o prompt de comando de seu sistema operacional, navegue até a pasta onde estão os arquivos *.py e digite o seguinte comando:
 
 **python simplex.py arquivo_de_entrada**
 
 O algoritmo será executado e se houver uma solução uma saída como a abaixo será exibida:

<pre><code>
===============================================================

             SIMPLEX - Arquivo: exemplo.txt

---------------------------------------------------------------

SISTEMA ORIGINAL
Funcao Objetivo:
        +2.0*x_0+5.0*x_1
Restricoes
        [0]: +2.0*x_0-1.0*x_1 <= 4.0
        [1]: +1.0*x_0+2.0*x_1 <= 9.0
        [2]: -1.0*x_0+1.0*x_1 <= 3.0


SOLUCAO:
Funcao Objetivo:
        +1.0*x_0+4.0*x_1
Valor: 22.0
================================================================
</code></pre>

Caso o arquivo esteja mal formatado ou o sistema não tenha solução possível, será exibida a saída:


<pre>
================================================================

                   SIMPLEX - Arquivo: pag_204.txt

----------------------------------------------------------------

ERRO: Nao foi possivel encontrar uma solucao. 
Verifique conteudo do arquivo.

================================================================
</pre>



### Formato do Arquivo de Entrada
- O conteúdo do aqruivo é uma matriz onde os elementos são separados por um ou mais espaços;
- O sistema no arquivo deve representar um sistema para maximização;
- É aceito qualquer ou nenhuma extensão, desde que o arquivo seja do tipo texto puro.
- Caso o nome do arquivo contenha espaços, colocá-lo entre aspas.
- Os elementos na matriz são os coeficientes da função objetivo, coeficientes das restrições, e valores das restrições.
  + 1.a linha: Coeficientes da função objetivo, seguido pelo valor 0.
  + 2.a linha em diante: Coeficientes das restrições, seguido pelo valor  das restrições.
- Em qualquer linha ou posição, comentários são aceitos desde que iniciados com o caracter "#".
- Caso a função objetivo ou uma restrição não possua determinada variável, sua posição na matriz deve assumir como coeficiente o valor 0.

#### Exemplo de um arquivo de entrada

<pre>
2 5  0 #Funcao objetivo com duas variáveis. Necessário colocar um '0' ao final.
2 -1 4	#1.a inequacao
1 2 9	#2.a inequacao
-1 1 3 	#3.a inequacao
</pre>
