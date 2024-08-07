# Lexer Implementation (Part 1)

This repository contains the first part of a lexer implementation in Python. The lexer is designed to tokenize a simple programming language, identifying various elements such as operators, keywords, separators, identifiers, integers, floats, and strings. This document provides an overview of the code and instructions for running the lexer on an input file.

## Authors
- Sepehr Bazmi
- Ardalan SoltanZadeh

## Overview

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

## Code

The core of the lexer is implemented in the `lex` function, which processes an input string and returns a list of tokens. The function handles various language constructs, including comments, whitespace, operators, separators, keywords, identifiers, numbers, and strings.

### Lexer Function

A lexical analyzer, also known as a scanner or tokenizer, is a component of a compiler that breaks down the source code into a sequence of 
tokens. Its purpose is to recognize and extract the smallest meaningful units of the programming language, such as keywords, identifiers, 
literals, and operators.
The lexical analyzer works by scanning the source code character by character. It uses a set of rules, defined by regular expressions or patterns, 
to identify and classify different tokens. These rules are typically specified through a combination of regular expressions and finite automata.
It also known as a scanner or tokenizer, is a component of a compiler that breaks down the source code into a sequence of tokens. Its purpose 
is to recognize and extract the smallest meaningful units of the programming language, such as keywords, identifiers, literals, and operators.


