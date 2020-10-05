#!/usr/bin/env python3

import json 
import lexer 
import parser 
import argparse
from pathlib import Path

data = """#N canvas 385 22 722 696 10;
#X msg 42 242 mbuto;
#X obj 71 276 + 1;
#X obj 27 301 % 10;
#X obj 200 457 -;
#X obj 27 329 t f f;
#X obj 445 329 -;
#X obj 445 304 swap 1;
#X obj 48 203 + 1;
#X obj 221 109 t b f;
#X obj 27 21 inlet bang;
#X obj 221 22 inlet min;
#X obj 321 21 inlet max;
#X obj 445 19 inlet direction;
#X obj 599 20 inlet resetmin;
#X obj 221 143 - \$1;
#X obj 27 498 + \$1;
#X obj 321 97 f \$2;
#X obj 371 57 loadbang;
#X obj 27 662 outlet count;
#X obj 27 276 f 0;
#X obj 200 432 swap;
#X obj 27 403 spigot 1;
#X obj 200 403 spigot 0;
#X obj 445 181 f \$3;
#X obj 445 237 == 0;
#X obj 27 520 t f f f;
#X obj 297 599 sel 0;
#X obj 372 597 sel 1;
#X obj 372 573 ==;
#X obj 297 621 f 0;
#X obj 372 619 f 1;
#X obj 297 644 outlet;
#X text 543 640 f.bianchi;
#X connect 0 0 19 1;
#X connect 1 0 19 1;
#X connect 2 0 4 0;
#X connect 2 0 26 0;
#X connect 2 0 28 0;
#X connect 3 0 15 0;
#X connect 4 0 21 0;
#X connect 4 1 22 0;
#X connect 5 0 22 1;
#X connect 6 0 5 0;
#X connect 6 1 5 1;
#X connect 7 0 2 1;
#X connect 8 0 14 0;
#X connect 8 1 14 1;
#X connect 9 0 19 0;
#X connect 10 0 8 0;
#X connect 10 0 15 1;
#X connect 11 0 16 0;
#X connect 12 0 23 0;
#X connect 13 0 0 0;
#X connect 14 0 7 0;
#X connect 14 0 20 1;
#X connect 14 0 28 1;
#X connect 15 0 25 0;
#X connect 16 0 14 0;
#X connect 17 0 16 0;
#X connect 17 0 23 0;
#X connect 19 0 1 0;
#X connect 19 0 2 0;
#X connect 20 0 3 0;
#X connect 20 1 3 1;
#X connect 21 0 15 0;
#X connect 22 0 20 0;
#X connect 23 0 24 0;
#X connect 24 0 6 0;
#X connect 24 0 21 1;
#X connect 25 0 18 0;
#X connect 26 0 29 0;
#X connect 27 0 30 0;
#X connect 28 0 27 0;
#X connect 29 0 31 0;
#X connect 30 0 31 0;
"""

parsearg = argparse.ArgumentParser(description='Process some integers.')
parsearg.add_argument('pdfile', type=str, help='pd file path to convert')

filepath = parsearg.parse_args()
#print(filepath.pdfile)
filepath = Path(filepath.pdfile)

with open(filepath, 'r') as f:
    data = f.read()

lex = lexer.PdLexer()
par = parser.PdParser()

whole = []
order = 0
line = 1
groups = []

for tokenized in lex.tokenize(data):
    if tokenized.lineno == line:
        groups.append(tokenized)
    else:
        res = par.parse(iter(groups))
        #print(res)
        if res['type'] == 'obj' or res['type'] =='msg':
            res['order'] = order
            order += 1
        whole.append(res)
        groups = []
        groups.append(tokenized)
        line = tokenized.lineno

print(json.dumps(whole, sort_keys=True, indent=4, ensure_ascii=False))