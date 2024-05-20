Rainha<br />
O jogo de Xadrez possui diversas peças com movimentos curiosos. Uma delas é a Rainha, que pode se mover qualquer número de casas em qualquer direção: na mesma linha, na mesma coluna ou em qualquer uma das diagonais, conforme ilustrado na figura abaixo (os pontos pretos representam as posições que a rainha pode alcançar):<br />

![alt text](https://456c997f.widgets.sphere-engine.com/files/problems/TECHFELLOW_24_Q3/uoj-1087.webp)<br /><br />
O grande mestre de xadrez Gary Carakov inventou um novo tipo de problema de xadrez: dada a posição de uma rainha em um tabuleiro de xadrez padrão vazio (ou seja, um tabuleiro de 8 x 8), quantos movimentos são necessários para que ela chegue a outra casa dada no quadro?<br />
<br />
Gary encontrou a solução para alguns desses problemas, mas está tendo dificuldades para resolver alguns outros e, portanto, pediu que você escrevesse um programa para resolver esse tipo de problema.<br />
<br /><br />
Entrada<br />
A entrada contém um caso de teste, que contém quatro inteiros X1, Y1, X2 e Y2 (1 ≤ X1, Y1, X2, Y2 ≤ 8). A rainha começa na casa com coordenadas (X1, Y1), e deve terminar na casa com coordenadas (X2, Y2). No tabuleiro de xadrez, as colunas são numeradas de 1 a 8, da esquerda para a direita; as linhas também são numeradas de 1 a 8, de cima para baixo. As coordenadas de um quadrado na linha X e na coluna Y são (X, Y).<br />
<br />
Saida<br />
Seu programa deve imprimir uma única linha, contendo um inteiro, indicando o menor número de movimentos necessários para a rainha alcançar a nova posição.<br />
<br />
Exemplo 1<br />
Entrada: 4 4 6 2<br />
<br />
Saida: 1<br />
<br />
Exemplo 2<br />
Entrada: 3 5 3 5<br />
<br />
Saida: 0<br />
<br />
Exemplo 3<br />
Entrada: 5 5 4 3<br />
<br />
Saida: 2<br />
