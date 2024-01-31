# اردلان سلطانزاده ۴۰۰۴۰۷۰۱۴ - سپهر بزمی ۴۰۰۴۰۵۰۱۹

def token(input):
    tokens = []
    i = 0
    while i < len(input):
        char = input[i]

        if char.isspace():
            i += 1
            continue

        if char == 'i':
            if i+2 < len(input) and input[i+1] == 'n' and input[i+2]:
                tokens.append('int')
                i += 3
            else:
                tokens.clear()
                tokens.append('ERROR, unknown token')
                return tokens
            continue

        if char == '(':
            tokens.append('(')
            i += 1
            continue
        
        if char == ')':
            tokens.append(')')
            i += 1
            continue

        if char == '+':
            tokens.append('+')
            i += 1
            continue

        if char == '*':
            tokens.append('*')
            i += 1
            continue

        else:
            tokens.clear()
            tokens.append('ERROR, unknown token')
            return tokens
    tokens.append('$')
    return tokens

GRAMMAR = {
    '0':['S', ['S','+','E']],
    '1':['S', ['E']],
    '2':['E', ['E','*','T']],
    '3':['E', ['T']],
    '4':['T', ['(','S',')']],
    '5':['T', ['int']]
}

ACTION = {
    '0,int': 'S,17', '0,(': 'S,6',
    '1,+': 'S,2', '1,$': '-,Accept',
    '2,int': 'S,17', '2,(': 'S,6',
    '3,+': 'R,0', '3,*': 'S,4', '3,$': 'R,0',
    '4,int': 'S,17', '4,(': 'S,6',
    '5,+': 'R,2', '5,*': 'R,2', '5,$': 'R,2',
    '6,int': 'S,16', '6,(': 'S,11',
    '7,+': 'S,9', '7,)': 'S,19',
    '8,+': 'R,1', '8,*': 'S,15', '8,)': 'R,1',
    '9,int': 'S,16', '9,(': 'S,11',
    '10,+': 'R,3', '10,*': 'R,3', '10,)': 'R,3',
    '11,int': 'S,16', '11,(': 'S,11',
    '12,+': 'S,9', '12,)': 'S,13',
    '13,+': 'R,4', '13,*': 'R,4', '13,)': 'R,4',
    '14,+': 'R,0', '14,*': 'S,15', '14,)': 'R,0',
    '15,int': 'S,16', '15,(': 'S,11',
    '16,+': 'R,5', '16,*': 'R,5', '16,)': 'R,5',
    '17,+': 'R,5', '17,*': 'R,5', '17,$': 'R,5',
    '18,+': 'R,3', '18,*': 'R,3', '18,$': 'R,3',
    '19,+': 'R,4', '19,*': 'R,4', '19,$': 'R,4',
    '20,+': 'R,1', '20,*': 'S,4', '20,$': 'R,1',
    '21,+': 'R,2', '21,*': 'R,2', '21,)': 'R,2'
}


GOTO = {'0,S': 1, '0,E': 20, '0,T':  18,
        '2,E': 3, '2,T': 18,
        '4,T': 5,
        '6,S': 7, '6,E': 8, '6,T': 10,
        '9,E': 14, '9,T': 10,
        '11,S': 12, '11,E': 8, '11,T': 10,
        '15,T':21
}


def parse(input):
    answer = ""
    tokens = token(input)
    stack = list()
    curr_state = list()
    curr_state.append(0)

    while True:
        
        if f'{curr_state[-1]},{tokens[0]}' in ACTION:
            action = ACTION[f'{curr_state[-1]},{tokens[0]}']
            if action.split(',')[1] == 'Accept':
                answer = "YES"
                return answer
            #shift
            if action.split(',')[0] == 'S':
                curr_state.append(int(action.split(',')[1]))
                stack.append(tokens.pop(0))
                
            #reduce
            elif action.split(',')[0] == 'R':
                index = action.split(',')[1]
                grammar = GRAMMAR.get(index)
                j = len(grammar[1])
                while j > 0:
                    stack.pop()
                    curr_state.pop()
                    j -= 1
                stack.append(grammar[0])
                #goto
                goto_index = f'{curr_state[-1]},{stack[-1]}'
                curr_state.append(GOTO.get(goto_index))

        else:
            answer = "NO"
            return answer

while True:
    inp = input('enter the input string : ')
    if inp == 'quit':
        break
    print(parse(inp))