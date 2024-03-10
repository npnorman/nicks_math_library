# Nick's Math Interpreter

## 3 stages of interpreting

* Lexing (Lexer)
* Parsing (Parser)
* Evaluating (Evaluator)

The lexer is used to break down a mathematical statement into tokens to pass to the parser. The parser then takes these tokens and creates a tree to represent the math statment in order (PEMDAS). Then the evaluator evaluates the tree and returns the correct answer to the math statement.

### Lexer

* Goal: convert a string to a list of mathematical tokens
* input: a string
* output: a list of tokens

#### Types of Tokens

Tokens | Desc | Example
-------|------|--------
Number | float | 10.03
Variable | unknown number  that will be passed later, represented by a symbol such as 'x' or 'y' | x
Plus | addition between two tokens | 5 + 3
Sub | subtraction between two tokens | 5 - 3
Multi | multiplication between two tokens | 5 * 3
Div | Division between two tokens | 5 / 3
PAR | Start or End  parenthesis | (5)
//Pow | Some base to the power of an exponent | 5^3

#### Token Class

* var data
* string type
* get/set data


### Parser

* Goal: convert a list of tokens into a math tree in order of operations
* input: a list of tokens
* output: a binary tree made up of tokens

### Evaluator

* Goal: evaluate a binary token tree
* input: binary token tree
* output: correct answer as float