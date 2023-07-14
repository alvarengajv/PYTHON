import re

# Expressões regulares para os tokens
numero = re.compile(r"\b\d+\b")
nome = re.compile(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b")
operador = re.compile(r"\+\+|--|\+=|-=|\*=|/=|//=|%=|==|!=|<=|>=|<|>|=|\+|-|\*|/|//|%")
simbolo = re.compile(r"[()\[\]{},.:;]")
quebra_linha = re.compile(r"\n")
espaco = re.compile(r"\s+")
comentario = re.compile(r"#.*")
string_aspas_simples = re.compile(r"'(\\.|[^\\'])*'")
string_aspas_duplas = re.compile(r'"(\\.|[^\\"])*"')
raw_string_aspas_simples = re.compile(r"r'[^']*'")
raw_string_aspas_duplas = re.compile(r'r"[^"]*"')

palavras_chave = {
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del",
    "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
    "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"
}

with open("lexer.py", "r") as arquivo:
    for linha in arquivo:
        i = 0
        while i < len(linha):
            m = numero.match(linha, i)
            if m:
                print("NUMERO", m.group(0))
                i = m.end()
                continue

            m = nome.match(linha, i)
            if m:
                if m.group(0) in palavras_chave:
                    print("RESERVADA", m.group(0))
                else:
                    print("NOME", m.group(0))
                i = m.end()
                continue

            m = operador.match(linha, i)
            if m:
                print("OPERADOR", m.group(0))
                i = m.end()
                continue

            m = simbolo.match(linha, i)
            if m:
                print("SIMBOLO", m.group(0))
                i = m.end()
                continue

            m = quebra_linha.match(linha, i)
            if m:
                print("QUEBRA DE LINHA")
                i = m.end()
                continue

            m = espaco.match(linha, i)
            if m:
                print("ESPAÇO", m.group(0))
                i = m.end()
                continue

            m = comentario.match(linha, i)
            if m:
                print("COMENTARIO", m.group(0))
                i = m.end()
                continue

            m = string_aspas_simples.match(linha, i)
            if m:
                print("STRING", m.group(0))
                i = m.end()
                continue

            m = string_aspas_duplas.match(linha, i)
            if m:
                print("STRING", m.group(0))
                i = m.end()
                continue

            m = raw_string_aspas_simples.match(linha, i)
            if m:
                print("STRING", m.group(0))
                i = m.end()
                continue

            m = raw_string_aspas_duplas.match(linha, i)
            if m:
                print("STRING", m.group(0))
                i = m.end()
                continue

            # Se nenhum padrão corresponder, significa que encontramos um caractere inválido
            else:
                print("ERRO: CARACTERE INVÁLIDO", linha[i])
                i += 1
