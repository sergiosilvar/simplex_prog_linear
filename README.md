# SIMPLEX

Este repositório contém uma implementação do [algoritmo Simplex](http://pt.wikipedia.org/wiki/Algoritmo_simplex) baseado na técnica de programação linear apresentada no livro [Algorithms, de Christos Papadimitriou, Sanvoy Dasgupta e Umesh Vazirani](http://amzn.com/0073523402). et all.


Esta implementação foi desenvolvida por Anna Carolina, Fernando Menucci e Sérgio Rodrigues, como trabalho da disciplina Estrutura de Dados e Algoritmos, do curso de Mestrado em Modelagem Matemática da Informação da Fundação Getúlio Vargas, Rio de Janeiro, 2013.


O algoritmo está preparado para maximização, portanto para usá-lo em minimização é necessário converter a função objetivo pelo simétrico.

## ARQUIVOS


- <b>SimplexAFS.py</b>: Classe SimplexAFS que implementa o algoritmo tomando como entrada o sistema a ser maximizado como uma matriz descrita em um arquivo texto a ser passado como parâmetro.
- <b>simplex.py</b>: Módulo para execução em linha de comando, caso queira utilizar o algoritmo diretamente no comando do sistema operacional.
 
## Pré-requisitos

Para utilizar o algorimto é necessário os seguintes softwares:

- [Interpretador Python versão 2.7;] (http://www.python.org)
- [Biblioteca Numpy;] (http://www.numpy.org)
- Editor de texto de sua preferência.

## Como usar em linha de comando

 Para executar o algoritmo Simplex, abra o prompt de comando de seu sistema operacional, navegue até a pasta onde estão os arquivos *.py e digite o seguinte comando:
 
 python simplex.py <nome_do_arquivo>
 
 Caso o nome do arquivo contenha espaços, colocá-lo entre aspas.
 Caso o arquivo não exista ou seja mal formatadao, um erro será emitido.
 
 O arquivo é do tipo texto e deve conter o sistema a ser maximizado descrito como uma matriz onde os elementos são os coeficientes da função objetivo e restrições, e valores das restrições, no seguinte formato:
 
 1.a linha: Coeficientes da função objetivo, seguido pelo valor 0.
 2.a linha em diante: Coeficientes das restrições, seguido pelo valor  das restrições.
 
### Observações 
 - Em qualquer linha ou posição, comentários são aceitos desde que iniciados com o caracter "#".
 - Caso a função objetivo ou uma restrição não possua determinada variável, sua posição na matriz deve assumir como coeficiente o valor 0.

## Exemplo


> Início do exemplo.
2 5  0 #Funcao objetivo com duas variáveis. Necessário colocar um '0' ao final para que esta linha contenha o mesmo número de colunas que as restriões seguidas .
2 -1 4	#1.a inequacao
1 2 9	#2.a inequacao
-1 1 3 	#3.a inequacao
> Fim do exemplo.
Fim do exemplo. 
