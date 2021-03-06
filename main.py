import matrix_handler as mh
from math import sqrt

def Sigma(a,i,n):
    if i>n:
        return 0
    w = 0
    for j in range(i,n+1):
        w += a(j)
    return w

def LU(a): #LU decomposition
    n = len(a)
    l = mh.MatrixMake(n,n) #MatrixMake(a,b) creates empty Matrix axb
    u = mh.MatrixMake(n,n)
    for i in range(n): #Doolittle's way of computing
        l[i][i] = 1
        for j in range(i,n):
            u[i][j] =  a[i][j] - Sigma(lambda k: l[i][k]*u[k][j],0,i-1)
        for j in range(i+1,n):
            l[j][i] = (a[j][i] - Sigma(lambda k: l[j][k]*u[k][i],0,i-1))/u[i][i]
    return l, u

def symet(a): #check for symmetricity
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i][j]!=a[j][i]:
                return False
    return True

def posDef(a): #Sylvester's way of checking for positive-definite squared matrix
    if len(a)==0:
        return True
    elif mh.MatrixDet(a)>0:
        return posDef(mh.MatrixMinor(a,len(a)-1,len(a)-1)) #MatrixMinor(A,n,m) returns matrix A without n-th row and m-th collumn
    else:
        return False

def LLt(a): #Cholesky
    n = len(a)
    l = mh.MatrixMake(n,n)
    for i in range(n):
        l[i][i] = mh.math.sqrt(a[i][i] - Sigma(lambda k: l[i][k]**2,0,i-1))
        for j in range(i,n):
            l[j][i] = (a[j][i] - Sigma(lambda k: l[j][k]*l[i][k],0,i-1))/l[i][i]
    return l

def dotProd(v,u): #dot product
    return Sigma(lambda k: v[k]*u[k],0,len(v)-1)

def ortProj(u,v): #ortogonal projection v on u
    w = u.copy()
    for i in range(len(w)):
        w[i]*=(dotProd(v,u)/dotProd(u,u))
    return w
    
def magn(v): #magnitude
    return dotProd(v,v)**0.5

def vecSum(v,u): #sum of vectors
    return list(map(lambda k: v[k]+u[k],range(len(v))))

def vecSub(v,u): #difrence of vectors
    return list(map(lambda k: v[k]-u[k],range(len(v))))

def vecSigma(a,i,n):
    w = list(a(i))
    for j in range(i+1,n+1):
        w = vecSum(w,a(j))
    return w

def QR(a): #Gram-Schmidt's proccess
    c = mh.MatrixTrans(a) #easy acces to columns
    u = [c[0].copy()] #first iteration eliminates problem of none return of vecSigma
    e = [list(map(lambda k: k/magn(u[0]),u[0]))]
    for i in range(1,len(a[0])):
        #print(vecSigma( lambda k: ortProj(u[k],c[i]),0,i-1 ))
        u.append( vecSub(c[i], vecSigma( lambda k: ortProj(u[k],c[i]),0,i-1 ) ) )
        e.append(list(map(lambda k: k/magn(u[i]),u[i])))
    q = mh.MatrixTrans(e)
    r = mh.MatrixMulti(e,a) #QR = A => (Q^-1)QR = (Q^-1)A => R = (Qt)A
    return q, r

def HausholderRef(a): #funtion for returning matrics that makes hauholder refletion based on a vector
    v = a.copy()
    v[0] -= magn(a)
    I = mh.MatrixIdentity(len(a))
    return mh.MatrixAdd(I,mh.MatrixScale(mh.MatrixMulti(mh.MatrixTrans([v]),[v]),-2/dotProd(v,v)))

def fill(c,hp): #fill fills hp matrix with identity matrix and two zeroed matrices
    h = mh.MatrixMake(c,c)
    for i in range(c-len(hp)):
        h[i][i]=1
    for i in range(len(hp)):
        for j in range(len(hp)):
            h[i+c-len(hp)][j+c-len(hp)] = hp[i][j]
    return h

def HausQR(a): #another qr decomposition, but now using Hausholder reflections
    c = mh.MatrixTrans(a)
    q = HausholderRef(c[0])
    c = mh.MatrixTrans(mh.MatrixMinor(mh.MatrixMulti(q,a),0,0))
    for _ in range(1,min(len(a)-1,len(a[0]))):
        t = fill(len(a),HausholderRef(c[0]))
        q = mh.MatrixMulti(t,q)
        c = mh.MatrixTrans(mh.MatrixMinor(mh.MatrixMulti(q,a),0,0))
    r = mh.MatrixMulti(q,a)
    q = mh.MatrixTrans(q)
    return q, r

def triU(a,bl): #triU checks for triangular upper matrix
    for k in range(len(a)):
        for w in range(k+1,len(a[k])):
            if (a[w][k])**2 > bl: #cost 
                return False
    return True

def Francis(a,bl=0.00000000001,c=1000):
    '''
    Francis algorithm of finding eigenvalues using Hausholder reflections.

    bl = computational squared error, 
    c = abort counter - after c iterations func just returns currently computed values
    '''
    i=0
    while not(triU(a,bl)|triU(mh.MatrixTrans(a),bl)|(i==c)):
        #print("i =",i)
        q, r = HausQR(a)
        i += 1
        a = mh.MatrixMulti(r,q)
        #mh.MatrixPrint(a)
    #print("end of algorithm after",i,"iterations")
    return list(map(lambda x: a[x][x], range(len(a)))) 

def SVD(a):
    aat = mh.MatrixMulti(a,mh.MatrixTrans(a))
    ata = mh.MatrixMulti(mh.MatrixTrans(a),a)
    mh.MatrixPrint(aat,"aat")
    mh.MatrixPrint(ata,"ata")
    eigenvalues_aat = list(map(lambda x: round(x,ndigits=6), Francis(aat)))
    singularvalues_aat = list(map(sqrt,eigenvalues_aat))
    mh.MatrixPrint([eigenvalues_aat],"eigen aat")
    mh.MatrixPrint([singularvalues_aat],"singular aat")
    eigenvalues_ata = list(map(lambda x: round(x,ndigits=6), Francis(ata)))
    singularvalues_ata = list(map(sqrt,eigenvalues_ata))
    mh.MatrixPrint([eigenvalues_ata],"eigen ata")
    mh.MatrixPrint([singularvalues_ata],"singular ata")
    S = mh.MatrixMake(len(a),len(a[0]))
    for i in range(min(len(a),len(a[0]))):
        S[i][i] = singularvalues_aat[i]
    mh.MatrixPrint(S, msg="Σ")



A = [
    [3, 2, 2],
    [2, 3, -2]
]
C = [
    [2, 4],
    [1, 3],
    [0, 0],
    [0, 0]
]

cU = [
    [0.82, -0.58, 0, 0],
    [0.58, 0.82, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
cS = [
    [5.47, 0],
    [0, 0.37],
    [0, 0],
    [0, 0]
]
cV = [
    [0.40, -0.91],
    [0.91, 0.40]
]


mh.MatrixPrint(mh.MatrixMulti(C,mh.MatrixTrans(C)))
mh.MatrixPrint(mh.MatrixMulti(mh.MatrixTrans(C),C))

SVD(A)

mh.MatrixPrint(
    mh.MatrixMulti(
        mh.MatrixMulti(cU,cS),
        mh.MatrixTrans(cV)
    ),
    msg="USVt"
)
