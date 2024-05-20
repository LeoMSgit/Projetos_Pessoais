Distância Hamming<br />
Na teoria da informação, a distância de Hamming entre duas cordas de igual comprimento é o número de posições nas quais os símbolos correspondentes são diferentes. De outra forma, mede o número mínimo de substituições necessárias para transformar uma string em outra, ou o número mínimo de erros que poderiam ter transformado uma string em outra.<br />
<br />
A distância de Hamming recebeu o nome de Richard Hamming, que a introduziu em seu artigo fundamental sobre códigos de Hamming, códigos de detecção e correção de erros em 1950.<br />
<br />
É usado em telecomunicações para contar o número de bits invertidos em uma palavra binária de comprimento fixo como uma estimativa de erro e, portanto, às vezes é chamado de distância do sinal. A análise de peso de bits de Hamming é usada em diversas disciplinas, incluindo teoria da informação, teoria da codificação e criptografia.<br />
<br />
Por exemplo, a representação binária do número 9 é 1001 e do número 10 é 1010, portanto a distância Hamming entre eles é 2 porque você só precisa trocar os dois últimos bits 1001 para transformar 1010.<br />
<br /><br />
Entrada<br />
A entrada consiste em uma linha composta por dois inteiros positivos em base decimal X e Y (0 ≤ X, Y < 264).<br />
<br />
Saida<br />
A saída possui uma linha contendo a distância de Hamming das representações binárias de X e Y.<br />
<br />
Exemplo 1<br />
Entrada: 9 10<br />
<br />
Saida: 2<br />
<br />
Exemplo 2<br />
Entrada: 6 9<br />
<br />
Saida: 4<br />
<br />
Exemplo 3<br />
Entrada: 7 15<br />
<br />
Saida: 1<br />
