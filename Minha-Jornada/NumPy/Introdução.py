'''
Criação de Arrays
np.array(): converte listas ou outras estruturas compatíveis em arrays NumPy.

Geração de Sequências

np.arange(): gera uma sequência numérica utilizando início, fim e passo.
Start: valor inicial da sequência.
Stop: valor que define o limite da sequência; normalmente não é incluído.
Step: intervalo entre os elementos consecutivos da sequência.


Matrizes Prontas
np.zeros(): cria arrays preenchidos exclusivamente por zeros.
np.ones(): cria arrays preenchidos exclusivamente por uns.
Shape: representação das dimensões de um array.
Linha: dimensão horizontal de uma matriz.
Coluna: dimensão vertical de uma matriz.
Tupla: estrutura imutável frequentemente utilizada para especificar formatos e dimensões.

Espaçamento Linear

np.linspace(): cria uma quantidade definida de pontos distribuídos uniformemente entre dois valores.
Espaçamento Uniforme: propriedade em que a distância entre elementos consecutivos permanece constante.
Endpoint: valor final do intervalo, normalmente incluído pelo linspace.

Álgebra Linear

Álgebra Linear: ramo da matemática que estuda vetores, matrizes e transformações lineares.
np.eye(): gera uma matriz identidade.
Matriz Identidade: matriz quadrada cuja diagonal principal contém apenas valores iguais a 1 e todas as demais posições contêm 0.
Diagonal Principal: conjunto de posições que vai do canto superior esquerdo ao canto inferior direito da matriz.

Números Aleatórios
Aleatoriedade: processo de geração de valores imprevisíveis dentro de determinadas regras.
np.random: módulo do NumPy dedicado à geração de números aleatórios.
Distribuição: regra matemática que descreve como os valores podem ser gerados.

Distribuição Uniforme
Distribuição Uniforme: distribuição em que todos os valores possuem a mesma probabilidade de ocorrência.
np.random.rand(): gera números reais aleatórios provenientes de uma distribuição uniforme entre 0 e 1.

Distribuição Normal
Distribuição Normal: distribuição estatística em formato de sino, muito comum em fenômenos naturais.
Distribuição Normal Padrão: distribuição normal com média igual a 0 e desvio padrão igual a 1.
np.random.randn(): gera amostras de uma distribuição normal padrão.
Média: valor central esperado da distribuição.
Variância: medida que indica a dispersão dos valores em torno da média.
Desvio Padrão: medida que representa o grau de espalhamento dos dados.

Inteiros Aleatórios
np.random.randint(): gera números inteiros aleatórios dentro de um intervalo especificado.
Limite Inferior: menor valor possível de ser sorteado.
Limite Superior: valor máximo permitido, normalmente não incluído.

Reprodutibilidade
Seed: valor utilizado para definir o estado inicial do gerador de números aleatórios.
np.random.seed(): função utilizada para fixar uma sequência aleatória reproduzível.
Reprodutibilidade: capacidade de executar novamente um experimento e obter exatamente os mesmos resultados.

Manipulação e Estrutura
reshape(): reorganiza a forma de um array preservando todos os seus elementos.
Reformatação (Reshape): mudança estrutural de um array sem alteração dos dados armazenados.
Compatibilidade de Shape: regra que exige que a nova forma possua o mesmo número total de elementos da forma original.

Propriedades de Arrays
shape: atributo que informa as dimensões do array.
dtype: atributo que informa o tipo de dado armazenado.
int64: tipo numérico inteiro armazenado em 64 bits.
float64: tipo numérico decimal armazenado em 64 bits de precisão.

Operações de Consulta
max(): retorna o maior valor presente no array.
min(): retorna o menor valor presente no array.
argmax(): retorna a posição onde o maior valor está localizado.
argmin(): retorna a posição onde o menor valor está localizado.
Índice: posição de um elemento dentro de um array.









'''