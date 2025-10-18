def changecar(ch,ca1,ca2,debut=0,fin=None):
    if fin is None:
        fin=len(ch)
        return ch[:debut]+ch[debut:fin].replace(ca1,ca2)+ch[fin:]
phrase="ceci est toute petite phrase"
print(changecar(phrase,"","+"))
print(changecar(phrase,"","+",8,12))