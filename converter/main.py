#!/usr/bin/env python3

import json 
import lexer 
import parser 
import argparse
from pathlib import Path

data = """#N canvas 385 22 722 696 10;
#X obj 71 276 osc 440;
#X obj 27 301 mbut;
#X obj 255 98 text define \$2;
#X msg 15 245 supercazzola prematurata;
#X connect 1 0 7 0;
#X connect 1 1 8 1;
"""

parsearg = argparse.ArgumentParser(description='Process some integers.')
parsearg.add_argument('pdfile', type=str, help='pd file path to convert')

filepath = parsearg.parse_args()
#print(filepath.pdfile)
filepath = Path(filepath.pdfile)

with open(filepath, 'r') as f:
    data = f.read()

data = data.replace(r" \\;",r"\,")

lex = lexer.PdLexer()
par = parser.PdParser()

whole = []
order = 0
line = 1
groups = []

for tokenized in lex.tokenize(data):
    print(tokenized)
    if tokenized.lineno != line:
        res = par.parse(iter(groups))
        print(res)
        if res['type'] == 'obj' or res['type'] =='msg':
            res['order'] = order
            order += 1
        whole.append(res)
        groups = []
        groups.append(tokenized)
        line = tokenized.lineno
    else: 
        groups.append(tokenized)

if groups:
    res = par.parse(iter(groups))
    print(res)
    if res['type'] == 'obj' or res['type'] =='msg':
        res['order'] = order
        order += 1
    whole.append(res)

print(json.dumps(whole, sort_keys=True, indent=4, ensure_ascii=False))