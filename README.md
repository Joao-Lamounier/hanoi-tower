# Documentação do Projeto

## Descrição
Este projeto implementa um algoritmo recursivo para resolver o famoso problema das Torres de Hanói. O problema consiste em mover uma torre de discos de um pino de origem para um pino de destino, utilizando um pino auxiliar, seguindo algumas regras específicas.

## Função Solver
A função `solver` é a peça central do algoritmo. Ela recebe quatro parâmetros:
- `n`: o número de discos a serem movidos.
- `source`: o pino de origem.
- `aux`: o pino auxiliar.
- `target`: o pino de destino.

A função utiliza o paradigma da indução para resolver o problema. A base da indução é quando `n` é igual a zero, onde a função simplesmente retorna, já que não há discos para serem movidos. A etapa de indução é realizada recursivamente da seguinte maneira:
1. Mover os `n-1` discos superiores do pino de origem para o pino auxiliar, utilizando o pino de destino como pino auxiliar.
2. Imprimir a ação de mover o disco `n` do pino de origem para o pino de destino.
3. Mover os `n-1` discos do pino auxiliar para o pino de destino, utilizando o pino de origem como pino auxiliar.

Esta abordagem divide o problema maior em subproblemas menores, resolvendo cada um deles de forma recursiva.

## Execução Principal
No bloco `if __name__ == "__main__":`, o código inicializa os argumentos do programa através da função `init_args()` (que não está fornecida no código fornecido) e, em seguida, chama a função `solver` com o número absoluto de discos especificado nos argumentos, e os pinos A, B e C como origem, auxiliar e destino, respectivamente.

## Paradigma da Indução
O paradigma da indução é fundamental nesta implementação. Ele parte do caso base, quando `n` é zero, e assume que o algoritmo é capaz de resolver o problema para `n-1`. Dessa forma, a solução para `n` é obtida combinando as soluções dos casos menores. Isso é demonstrado na chamada recursiva da função `solver`.

## Conclusão
O código implementa uma solução eficiente e elegante para o problema das Torres de Hanói, utilizando o paradigma da indução para dividir o problema em subproblemas menores e resolvê-los recursivamente. A modularidade da função `solver` permite fácil compreensão e manutenção do código.
