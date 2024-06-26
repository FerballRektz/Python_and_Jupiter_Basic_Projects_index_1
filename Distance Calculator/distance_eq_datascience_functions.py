def euc_dist(a,b):
    result = 0
    for g in range(len(b)):
        result += (a[g]-b[g])**2
    result**=(1/2)
    return print(result)

def minnk_dist(a,b,e):
    result = 0
    for g in range(len(b)):
        result += (a[g]-b[g])**(e)
    result**=(1/e)
    return print(result)

def mann_dist(a,b):
     result = 0
     for g in range(len(b)):
        result += abs(a[g]-b[g])
        print(result)
     return print(result)


def cheb_dist(a,b):
    result = []
    for g in range(len(b)):
       result.append((a[g]-b[g]))
    return print(max(result))
    

# excecute code here 
cheb_dist([2.5,1.75,3.0,2.75,1.75],[1.5,2.75,2.25,1.5,2.25])
euc_dist([2.5,1.75,3.0,2.75,1.75],[1.5,2.75,2.25,1.5,2.25])
minnk_dist([2.5,1.75,3.0,2.75,1.75],[1.5,2.75,2.25,1.5,2.25],3)
mann_dist([2.5,1.75,3.0,2.75,1.75],[1.5,2.75,2.25,1.5,2.25])