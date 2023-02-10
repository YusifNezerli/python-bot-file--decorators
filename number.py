
# number duzelme

l = []
l.append(input("Mobil number:"))

def decor(fn):
    def inner(l):
        fn("+994" +" "+ c[1]+ c[2] +" " + c[3]+ c[4] + c[5]  +" "+c[6]+c[7] +" "+c[-2:] for c in l)
    return inner

@decor
def number(l):
    print(*(l))

number(l)