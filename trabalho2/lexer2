import re

# Expressões regulares para os tokens
numero = re.compile(r"\b\d+\b")
variavel = re.compile(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b")
operador_soma = re.compile(r"\+")
operador_subtracao = re.compile(r"-")
operador_multiplicacao = re.compile(r"\*")
operador_divisao = re.compile(r"/")
operador_divisao_inteira = re.compile(r"//")
operador_resto_divisao = re.compile(r"%")
simbolo_igual = re.compile(r"=")
simbolo_abre_parenteses = re.compile(r"\(")
simbolo_fecha_parenteses = re.compile(r"\)")
quebra_linha = re.compile(r"\n")
espaco = re.compile(r"\s+")
comentario = re.compile(r"#.*")
reservada = re.compile(r"\b(sqrt|sin|cos|tan)\b")
saida = re.compile("@")

with open("entrada.txt", "r") as arquivo:
    for linha in arquivo:
        i = 0
        while i < len(linha):
            m = numero.match(linha, i)
            if m:
                print("NUMERO:", m.group(0))
                i = m.end()
                continue

            m = variavel.match(linha, i)
            if m:
                if reservada.match(m.group(0)):
                    print("RESERVADA:", m.group(0))
                else:
                    print("VARIAVEL:", m.group(0))
                i = m.end()
                continue

            m = operador_soma.match(linha, i)
            if m:
                print("OPERADOR_SOMA:", m.group(0))
                i = m.end()
                continue

            m = operador_subtracao.match(linha, i)
            if m:
                print("OPERADOR_SUBTRACAO:", m.group(0))
                i = m.end()
                continue

            m = operador_multiplicacao.match(linha, i)
            if m:
                print("OPERADOR_MULTIPLICACAO:", m.group(0))
                i = m.end()
                continue

            m = operador_divisao.match(linha, i)
            if m:
                print("OPERADOR_DIVISAO:", m.group(0))
                i = m.end()
                continue

            m = operador_divisao_inteira.match(linha, i)
            if m:
                print("OPERADOR_DIVISAO_INTEIRA:", m.group(0))
                i = m.end()
                continue

            m = operador_resto_divisao.match(linha, i)
            if m:
                print("OPERADOR_RESTO_DIVISAO:", m.group(0))
                i = m.end()
                continue

            m = simbolo_igual.match(linha, i)
            if m:
                print("SIMBOLO_IGUAL:", m.group(0))
                i = m.end()
                continue

            m = simbolo_abre_parenteses.match(linha, i)
            if m:
                print("SIMBOLO_ABRE_PARENTES:", m.group(0))
                i = m.end()
                continue

            m = simbolo_fecha_parenteses.match(linha, i)
            if m:
                print("SIMBOLO_FECHA_PARENTES:", m.group(0))
                i = m.end()
                continue

            m = quebra_linha.match(linha, i)
            if m:
                print("QUEBRA_DE_LINHA:")
                i = m.end()
                continue

            m = espaco.match(linha, i)
            if m:
                print("ESPACO:", m.group(0))
                i = m.end()
                continue

            m = comentario.match(linha, i)
            if m:
                print("COMENTARIO:", m.group(0))
                i = m.end()
                continue

            m = saida.match(linha, i)
            if m:
                print("SAÍDA:", m.group(0))
                i = m.end()
                continue

            # Se nenhum padrão corresponder, significa que encontramos um caractere inválido
            else:
                print("ERRO: CARACTERE INVÁLIDO:", linha[i])
                i += 1
