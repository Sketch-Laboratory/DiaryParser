import os
os.chdir(os.path.dirname(__file__))

import re
p = re.compile('\d+년\s*\d+월\s*\d+일')

def extract(data):
    # print(data)
    m1 = p.search(data)
    title = m1.group()
    m2 = p.search(data[m1.end():])
    if m2 == None : return title, data, -1
    body = data[:m1.end() + m2.start()]
    return title, body, m1.end() + m2.start()

dir = './parsed'
if not os.path.isdir(dir): os.mkdir(dir)

def export(title, body):
    f = open(f'{dir}/{title}.txt', 'w')
    f.write(body)
    f.close()

with open('output.txt', 'r', encoding='UTF8') as file:
    data = file.read()
    print(len(p.findall(data)))
    index = 0
    while(True):
        data = data[index:]
        title, body, index = extract(data)
        export(title, body)
        if index == -1: break