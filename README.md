SIMPLEX
Implementação do algoritmo Simplex baseado no livro Algorithms, de Christos Papadimitriou et all.
Criado por Anna Carolina, Fernando Menucci e Sérgio Rodrigues, com trabalho da disciplina Estrutura de Dados e Algoritmos, no curso de Mestrado em Modelagem Matemática da Informação da Fundação Getúlio Vargas, Rio de Janeiro, 2013.

Arquivos:
 - SimplexAFS.py: Classe SimplexAFS que resolver o sistema descrito um arquivo texto.
 - simplex.py: Módulo para execução em linha de comando.
 
 Utilização:
 Para executar o Simplex utilize o seguinte comando:
 python simplex.py <nome_do_arquivo>
 
 Caso o nome do arquivo contenha espaços, colocá-lo entre aspas.
 Caso o arquivo não exista ou seja mal formatadao, um erro será emitido.
 
 O arquivo é do tipo texto e deve conter a seguinte estrutura de exemplo:
 
 1.a linha Começa com o caractere de comentário "#", seguido por 'MIN', ou 'MAX', que determina se o problema é de minimização ou maximização.
 2.a linha Coeficientes da função objetivo, seguido pelo valor 0.
 3.a linha em diante, coeficientes das restrições, seguido pelo valor  das restrições.
 
 Comentários no arquivo são aceitos desde que iniciados com o caracter "#".
 
 Veja um exemplo abaixo:
 
# MAX
2 5	0	#Funcao objetivo. Determina as variaveis. Completar 0.
2 -1 4	#1.a inequacao
1 2 9	#2.a inequacao
-1 1 3 	#3.a inequacao

Fim do exemplo. 