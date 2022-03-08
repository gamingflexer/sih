with open('..//xyx.json', 'r', encoding='utf-8') as istr:
    with open('..//abc.json', 'w', encoding='utf-8') as ostr:
        for line in istr:
            line = line.rstrip('\n') + ','
            print(line, file=ostr)

    istr.close()

with open("..//abc.json", "r+", encoding='utf-8') as file:
    file.write('{"data":[{"id":')
    file.seek(0)
    content = file.read()

buggy_name = open('..//abc.json', 'r', encoding='utf-8')
name = buggy_name.read()
newtext = name[:-2]
newFile = open('..//abc.json', 'w', encoding='utf-8')
newFile.write(newtext)
newFile.close()
print(newtext)


file = open('..//abc.json', 'a', encoding='utf-8')
file.write(']}')
file.close()

