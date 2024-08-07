## Authors
- Sepehr Bazmi
- Ardalan SoltanZadeh

# Lexer Implementation (Part 1)

The lexer processes an input string and categorizes its components into tokens. The primary elements identified by the lexer include:

- **Operators**: `=`, `/`, `-`, `*`, `+`, `==`, `!=`, `<=`, `<`, `>=`, `>`
- **Single Characters**: `=`, `/`, `\\`, `-`, `*`, `+`, `.`, `"`, `_`, `>`, `<`, `!`
- **Keywords**: `int`, `float`, `scan`, `print`, `if`, `else`, `while`
- **Separators**: `(`, `)`, `{`, `}`, `;`
- **Identifiers**: Combinations of letters, digits, and underscores, starting with a letter or underscore
- **Integers and Floats**: Numeric literals, with or without decimal points
- **Strings**: Sequences of characters enclosed in double quotes

## Token Classes

The lexer assigns a specific class to each token it identifies. These classes include:
- `OPENPARENTHESIS`
- `CLOSEPARENTHESIS`
- `OPENCURLYBRACE`
- `CLOSECURLYBRACE`
- `SEMI-COLON`
- `FLOAT`
- `INT`
- `SCAN`
- `PRINT`
- `IF`
- `ELSE`
- `WHILE`
- `OPERATOR`
- `IDENTIFIER`
- `STRING`
- `ERROR`

## Lexer Function

A lexical analyzer, also known as a scanner or tokenizer, is a component of a compiler that breaks down the source code into a sequence of 
tokens. Its purpose is to recognize and extract the smallest meaningful units of the programming language, such as keywords, identifiers, 
literals, and operators.
The lexical analyzer works by scanning the source code character by character. It uses a set of rules, defined by regular expressions or patterns, 
to identify and classify different tokens. These rules are typically specified through a combination of regular expressions and finite automata.
It also known as a scanner or tokenizer, is a component of a compiler that breaks down the source code into a sequence of tokens. Its purpose 
is to recognize and extract the smallest meaningful units of the programming language, such as keywords, identifiers, literals, and operators.

### Operators

![Sample Image](main/Static/logical-operator)
![Sample Image](main/Static/mathematical-operator)


# Parser Implementation (Part 2)

LR(1) parsing is a bottom-up parsing technique used to analyze and validate the syntax of a programming language or any other context-free 
language. The "LR" stands for "left-to-right" scanning of the input string and "rightmost derivation" of the parse tree, while the "(1)" indicates that 
the parser considers one lookahead symbol to make parsing decisions.
The LR(1) parser builds a deterministic finite automaton (DFA) known as an LR(1) automaton or LR(1) item set. This automaton represents the 
state transitions that occur during the parsing process. The DFA is constructed based on a set of augmented grammar rules and their 
corresponding LR(1) items.
An LR(1) item is a production rule with a dot (.) marker that represents the current position in the production. It also includes a lookahead 
symbol, which is the symbol that immediately follows the dot.
The LR(1) DFA is then used during the parsing process to perform shift and reduce actions. Shift actions correspond to moving to the next state 
based on the current input symbol, while reduce actions involve applying a production rule and replacing a group of symbols with a nonterminal.
Overall, the LR(1) parser uses the LR(1) DFA to determine the appropriate parsing actions based on the current state and the lookahead symbol, 
allowing it to build a valid parse tree for the input string.

## Grammar Rules

The grammar rules used by the parser are defined as follows:


| Rule ID | Non-terminal | Production                            |
|---------|--------------|---------------------------------------|
| 0       | S            | S → S + E                             |
| 1       | S            | S → E                                 |
| 2       | E            | E → E * T                             |
| 3       | E            | E → T                                 |
| 4       | T            | T → ( S )                             |
| 5       | T            | T → int                               |



Converting an LR(1) DFA to a parsing table is an essential step in building an LR(1) parser. The parsing table provides a concise representation of 
the DFA's state transitions and the corresponding parsing actions to be taken based on the current state and lookahead symbol :

## Action Table

The action table defines what action to take based on the current state and the lookahead token. 

| State/Token | int        | (          | )          | +          | *          | $          |
|-------------|------------|------------|------------|------------|------------|------------|
| 0           | S,17       | S,6        |            |            |            |            |
| 1           |            |            |            | S,2        |            | - , Accept |
| 2           | S,17       | S,6        |            |            | S,4        |            |
| 3           |            |            | R,0        | R,0        | S,4        | R,0        |
| 4           | S,17       | S,6        |            |            |            |            |
| 5           |            |            | R,2        | R,2        |            |            |
| 6           | S,16       | S,11       |            |            |            |            |
| 7           |            |            |            | S,9        |            | S,19       |
| 8           |            |            | R,1        |            | S,15       | R,1        |
| 9           | S,16       | S,11       |            |            |            |            |
| 10          |            |            | R,3        | R,3        |            | R,3        |
| 11          | S,16       | S,11       |            |            |            |            |
| 12          |            |            |            | S,9        |            | S,13       |
| 13          |            |            | R,4        | R,4        |            | R,4        |
| 14          |            |            | R,0        | S,15       |            | R,0        |
| 15          | S,16       | S,11       |            |            |            |            |
| 16          |            |            | R,5        | R,5        |            | R,5        |
| 17          |            |            | R,5        | R,5        |            | R,5        |
| 18          |            |            | R,3        | R,3        |            | R,3        |
| 19          |            |            | R,4        | R,4        |            | R,4        |
| 20          |            |            |            | S,4        |            | R,1        |
| 21          |            |            |            |            | R,2        | R,2        |

## Goto Table

The Goto table defines the state transitions based on the current state and the non-terminal being processed.

| State/Non-terminal | S  | E  | T  |
|--------------------|----|----|----|
| 0                  | 1  | 20 | 18 |
| 2                  | 3  | 18 |    |
| 4                  |    |    | 5  |
| 6                  | 7  | 8  | 10 |
| 9                  |    | 14 | 10 |
| 11                 | 12 | 8  | 10 |
| 15                 |    |    | 21 |






