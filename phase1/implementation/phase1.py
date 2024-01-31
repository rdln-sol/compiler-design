# اردلان سلطانزاده ۴۰۰۴۰۷۰۱۴ - سپهر بزمی ۴۰۰۴۰۵۰۱۹

operators = ['=', '/', '-', '*', '+', '==', '!=', '<=', '<', '>=', '>']
single_char = ['=', '/', '\\', '-', '*', '+', '.', '"', '_', '>', '<', '!']
keywords = ['int', 'float', 'scan', 'print', 'if', 'else', 'while']
separators = ['(', ')', '{', '}', ';']
alphabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
accepted_chars = alphabet+ [chr(95)]
fin_check = alphabet + single_char + separators

token_class = {
    '(':'OPENPARENTHESIS',
    ')':'CLOSEPARENTHESIS',
    '{':'OPENCURLYBRACE',
    '}':'CLOSECURLYBRACE',
    ';':'SEMI-COLON',
    'float':'FLOAT',
    'int':'INT',
    'scan':'SCAN',
    'print':'PRINT',
    'if':'IF',
    'else':'ELSE',
    'while':'WHILE'
}

def lex(input):
    tokens = []
    i = 0

    while i < len(input):
        #POINTER TO THE CURRENT CHARACTER
        char = input[i]

        #SINGLE-LINE COMMENT
        if char == '/' and input[i+1] == '/':
            j = i + 2
            while j < len(input) and input[j] != '\n':
                j += 1
            i = j
            continue
        
        #MULTI-LINE COMMENT
        if char == '\\' and input[i+1] == '*':
            j = i + 1
            while j < len(input) and not (input[j] == '*' and input[j+1] == '\\'):
                j += 1
            i = j + 2
            continue

        #WHITE SPACEs
        if char.isspace():
            i += 1
            continue

        #OPERATORs
        if char in operators:
            if i+1 < len(input) and input[i+1] == '=' and char + '=' in operators:
                tokens.append((char+'=', 'OPERATOR'))
                i += 2
            else:
                tokens.append((char, 'OPERATOR'))
                i += 1
            continue

        #SEPERATORs
        if char in separators:
            tokens.append((char, token_class[char]))
            i += 1
            continue

        #IDs and KEYWORD
        if char.isalpha() or char == '_':
            j = i + 1
            while j < len(input) and input[j] in accepted_chars:
                j += 1

            word = input[i:j]

            if word in keywords:
                tokens.append((word, token_class[word]))
            elif word[0] == '_' or word[0].isalpha():
                if '_' in word[1:]:
                    tokens.clear()
                    tokens.append(('invalid ID', 'ERROR'))
                    return tokens
                tokens.append((word, 'IDENTIFIER'))
            else:
                tokens.clear()
                tokens.append(('ID or KEYWORD was expected', 'ERROR'))
                return tokens
            i = j
            continue

        #INTs and FLOATs
        if char.isdigit() or ((char == '+' and input[i+1].isdigit()) or (char == '-' and input[i+1].isdigit())):
            j = i + 1
        
            has_dot = False
            while j < len(input) and (input[j].isdigit() or input[j] == '.'):
                if input[j] == '.':
                    has_dot=True
                j += 1
            
            if has_dot:
                if input[j-1] == '.':
                    tokens.clear()
                    tokens.append(('number after dot was expected', 'ERROR'))
                    return tokens
                tokens.append((input[i:j], 'FLOAT'))
            else:
                tokens.append((input[i:j], 'INT'))
            i = j
            continue
            
        #STRINGs
        if char == '"':
            j = i + 1
            while j < len(input) and input[j] != '"' and input[j] != '\n':
                j += 1
            if j < len(input) and input[j] == '"':
                tokens.append((input[i:j+1], 'STRING'))
                i = j + 1
            else:
                tokens.clear()
                tokens.append(('string was not closed', 'ERROR'))
                return tokens
            continue
        
        else:
            tokens.clear()
            tokens.append(('not an accepted character', 'ERROR'))
            return tokens
    return tokens

with open('phase1/implementation/input.txt', 'r') as file:
    input = file.read()

tokens = lex(input)

with open('phase1/implementation/output.txt', 'w') as file:
    for token in tokens:
        file.write(f'<{token[1]}, "{token[0]}">\n')