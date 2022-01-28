# Procure por linhas que comecem com 'X' seguido por qualquer não
# caracteres de espaço em branco e ':'
# seguido por um espaço e qualquer número.
# O número pode incluir um decimal.
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)
