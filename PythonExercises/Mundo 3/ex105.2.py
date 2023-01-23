# Solução realizada pelo professor Guanabara

def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = (sum(n)/len(n))

    return r

# programa principal
resp = notas(5.5, 2.5, 8.5)
print(resp)
