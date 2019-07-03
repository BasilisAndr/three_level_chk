import re, os

patterns = {
    re.compile(':(@U.V..v@)([^ ]*)([иу])([^ ]*)э'): ':\\1\\2\\3\\4%{Æ%}',
    re.compile(':(@U.V..v@)([^ ]*)э([^ ]*)([иу])'): ':\\1\\2%{Æ%}\\3\\4'
}
files = [
    'preverbs.lexc',
    'verbv.lexc'
]

def main():
    for fil in files:
        with open(os.path.join('../lexicons', fil)) as f:
            text = f.read()
        for pat in patterns:
            text = re.sub(pat, patterns[pat], text)
        with open(os.path.join('../lexicons', '{}_repl.lexc'.format(fil[:-5])), 'w') as f:
            f.write(text)

if __name__ == '__main__':
    main()
