# Torre de Hanoi
## Alunos: 
- Akles Pires Camoleze 
- João Felipe Silva Lamounier

## Algoritmo
A Torre de Hanói é um quebra-cabeça com três pinos e discos de tamanhos diferentes. O objetivo é mover todos os discos da origem para o destino, usando um pino auxiliar e seguindo duas regras simples: um disco por vez e discos maiores nunca sobre discos menores.
O algoritmo pode ser resumido da seguinte forma:
1. Se tivermos apenas um disco (caso base), movemos diretamente da origem para o destino.
2. Caso contrário, movemos n-1 discos da origem para o pino auxiliar usando o destino como apoio (chamada recursiva).
Movemos o maior disco da origem para o destino.
3. Finalmente, movemos os n-1 discos do pino auxiliar para o destino usando a origem como apoio (outra chamada recursiva).

O algoritmo continua a se chamar recursivamente até que todos os discos sejam movidos. Essa abordagem eficiente quebra o problema em subproblemas menores e resolve-o de forma ordenada.