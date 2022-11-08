def automato1():
    alfabeto = ['0', '1']  # Alfabeto aceito pelo autômato
    estados = ['q0', 'q1', 'q2']  # Estados pertecentes ao autômato
    estado_inicial = 'q0'  # Estado inicial do autômato
    estado_final = ['q0']  # Estados finais do autômato
    dfa = {'q0': {'0': 'q0', '1': 'q1'},  # Conjunto de estados e transições que o dfa segue
           'q1': {'0': 'q2', '1': 'q0'},
           'q2': {'0': 'q1', '1': 'q2'}}

    return alfabeto, estados, estado_inicial, estado_final, dfa


def trans(estado, char, dfa):
    if char not in dfa[estado]:  # Verifica se char não faz parte do alfabeto
        return ValueError(f"O char {char} não pertence ao alfabeto")  # Retorna um ValueError caso for isso
    next_estado = dfa[estado][
        char]  # Função de transição do autômato, no qual o próximo estado será a verificação do estado que estamos
    # com a leitura do novo char

    return next_estado  # retorna o novo estado


def le_char(palavra, i):
    char = list(palavra)  # Função para pegarmos o caractere na posição i da palavra
    return char[i]  # Retorna esse caractere


def volta_char(palavra):
    palavra = palavra[:-1]  # Função para excluirmos o último caractere da palavra
    return palavra  # Retorna a  nova palavra


def analise_lexico(palavra):
    alfabeto, estados, estado_inicial, estado_final, dfa = automato1()  # Chamada da função automato e guardamos
    estado = estado_inicial  # atribui a variável estado o estado inicial
    lexema = ""  # Lexema começa vazio
    pilha = []  # Pilha começa vazia
    for i in range(len(palavra)):  # Enquanto o tamanho da palavra for < i
        char = le_char(palavra, i)  # Chama a função le_char para pegarmos o char da palavra na posição i
        lexema = lexema + char  # vai acrescentando ao lexema o char lido
        pilha.append(estado)  # Adiciona na pilha o estado
        estado = trans(estado, char, dfa)  # Chama a função de transição para pegar o próximo estado
        estado_fim_palavra = estado  # Salva o último estado da palavra passada como parâmetro

    if estado in estado_final:  # Verifica se o estado faz parte de algum dos estados finais
        print(f"Chegamos no estado final com a palavra {lexema} e o estado final {estado}")
        return estado, lexema  # Returna o estado final e o lexema

    while estado != estado_final and len(
            pilha) != 0:  # Verifica e faz um loop enquanto o estado não é final e a pilha não está vazia
        estado = pilha.pop()  # Retira o estado da pilha
        lexema = volta_char(lexema)  # Chama o volta_char para retirar o último caractere

    if estado == estado_final:  # Verifica se o estado faz parte de algum dos estados finais

        print(
            f"A palavra: {palavra} que termina no estado {estado_fim_palavra} não pertence a linguagem mas passamos "
            f"pelo estado final: {estado} com a palavra: {lexema}")
        return estado, lexema

    else:
        return print(
            f"Não conseguimos encontrar um estado final com essa palavra: {palavra} e paramos no estado {estado_fim_palavra}")


analise_lexico("11111")

analise_lexico("11211")

analise_lexico("10101")


def automato2():
    alfabeto = ['a', 'b']
    estados = ['q0', 'q1', 'q2']
    estado_inicial = 'q0'
    estado_final = ['q2']
    dfa = {'q0': {'a': 'q1', 'b': 'q2'},
           'q1': {'a': 'q1', 'b': 'q2'},
           'q2': {'a': 'q2', 'b': 'q2'}}

    return alfabeto, estados, estado_inicial, estado_final, dfa


def trans(estado, char, dfa):
    if char not in dfa[estado]:  # Verifica se char não faz parte do alfabeto
        return ValueError(f"O char {char} não pertence ao alfabeto")  # Retorna um ValueError caso for isso
    next_estado = dfa[estado][
        char]  # Função de transição do autômato, no qual o próximo estado será a verificação do estado que estamos
    # com a leitura do novo char

    return next_estado  # retorna o novo estado


def le_char(palavra, i):
    char = list(palavra)  # Função para pegarmos o caractere na posição i da palavra
    return char[i]  # Retorna esse caractere


def volta_char(palavra):
    palavra = palavra[:-1]  # Função para excluirmos o último caractere da palavra
    return palavra  # Retorna a  nova palavra


def analise_lexico(palavra):
    alfa, estados, estado_ini, estado_final, dfa = automato2()  # Chamada da função automato e guardamos
    estado = estado_ini  # atribui a variável estado o estado inicial
    lexema = ""  # Lexema começa vazio
    pilha = []  # Pilha começa vazia
    for i in range(len(palavra)):  # Enquanto o tamanho da palavra for < i
        char = le_char(palavra, i)  # Chama a função le_char para pegarmos o char da palavra na posição i
        lexema = lexema + char  # vai acrescentando ao lexema o char lido
        pilha.append(estado)  # Adiciona na pilha o estado
        estado = trans(estado, char, dfa)  # Chama a função de transição para pegar o próximo estado
        estado_fim_palavra = estado  # Salva o último estado da palavra passada como parâmetro

    if estado in estado_final:  # Verifica se o estado faz parte de algum dos estados finais
        print(f"Chegamos no estado final com a palavra {lexema} e o estado final {estado}")
        return estado, lexema  # Returna o estado final e o lexema

    while estado != estado_final and len(
            pilha) != 0:  # Verifica e faz um loop enquanto o estado não é final e a pilha não está vazia
        estado = pilha.pop()  # Retira o estado da pilha
        lexema = volta_char(lexema)  # Chama o volta_char para retirar o último caractere

    if estado == estado_final:  # Verifica se o estado faz parte de algum dos estados finais

        print(
            f"A palavra: {palavra} que termina no estado {estado_fim_palavra} não pertence a linguagem mas passamos "
            f"pelo estado final: {estado} com a palavra: {lexema}")
        return estado, lexema

    else:
        return print(
            f"Não conseguimos encontrar um estado final com essa palavra: {palavra} e paramos no estado {estado_fim_palavra}")


analise_lexico("aaaaa")

analise_lexico("abga")

analise_lexico("aaaab")
