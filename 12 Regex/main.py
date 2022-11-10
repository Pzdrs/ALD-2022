import sys
import re

with open('vstup.html', mode='r') as file:
    data = file.read()
    # sosni jenom data z tela tabulky
    tbody = re.findall(r'<tbody>([\S\s]*)</table>', data)
    tr_people = re.findall(r'', tbody[0])
    print(tr_people)
