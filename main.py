import matrix_handler as mh

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

def symet(a): #check symetric
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i][j]!=a[j][i]:
                return False
    return True

def posDef(a): #Sylvester's way of checking for positive-definite squared matrix
    if len(a)==0:
        return True
    elif mh.MatrixDet(a)>0:
        return posDef(mh.MatrixMinor(a,len(a)-1,len(a)-1)) #MatrixMinor(A,n,m) returns matrix A without nth row and mth collumn
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
    #return mh.MatrixMulti(mh.MatrixTrans([v]),[u])[0][0]

def ortProj(u,v): #ortogonal projection v on u
    w = u.copy()
    for i in range(len(w)):
        w[i]*=(dotProd(v,u)/dotProd(u,u))
    return w
    
def magn(v): #magnatude
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
        print(vecSigma( lambda k: ortProj(u[k],c[i]),0,i-1 ))
        u.append( vecSub(c[i], vecSigma( lambda k: ortProj(u[k],c[i]),0,i-1 ) ) )
        e.append(list(map(lambda k: k/magn(u[i]),u[i])))
    q = mh.MatrixTrans(e)
    mh.MatrixPrint(e)
    mh.MatrixPrint(a)
    r = mh.MatrixMulti(e,a) #QR = A => (Q^-1)QR = (Q^-1)A => R = (Qt)A
    return q, r
