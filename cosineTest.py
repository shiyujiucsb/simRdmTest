def main():

    # number of vectors
    n = 100
    # number of features
    m = 1000
    # sample size interval
    si = 10
    # max samples
    ms = 100

    from random import random
    from random import normalvariate
    from random import randint
    from math import log

    # init the n vectors
    print ('Initializing...')
    V = []
    for i in range(n):
        v = [abs(normalvariate(0,1)) for kk in range(m)]
        #v = [random() for kk in range(m)]
        V.append(v)

    # normalize
    print ('Normalizing...')
    for i in range(n):
        norm = sum([item**2 for item in V[i]])**0.5
        ratio = m**0.5 / norm
        v_prime = [item*ratio for item in V[i]]
        V[i] = v_prime

    # exact solution
    print ('Computing the exact solution...')
    maxProd = 0.0
    ExactSim = [[0.0 for i in range(n)] for j in range(n)]
    for ii in range(n):
        for jj in range(ii+1, n):
            for k in range(m):
                ExactSim[ii][jj] += V[ii][k] * V[jj][k]
                #if maxProd < V[ii][k] * V[jj][k]:
                #    maxProd = V[ii][k] * V[jj][k]
            ExactSim[ii][jj] /= m
    #print('Max fi: ', maxProd)
    

    # sampling and error analysis
    S = {}
    maxProd = 0.0
    Sim = [[0.0 for i in range(n)] for j in range(n)]
    fs2 = [[0.0 for i in range(n)] for j in range(n)]
    for i in range(ms//si):
        print('Sampling', (i+1)*si, 'samples...')
        ell = 0.0
        j=0
        while j<si:
            s = randint(0,m-1)
            #if s in S:
            #    continue
            #S[s] = 1
            j += 1
            for ii in range(n):
                for jj in range(ii+1, n):
                    Sim[ii][jj] += V[ii][s] * V[jj][s]
                    if maxProd < V[ii][s] * V[jj][s]:
                        maxProd = V[ii][s] * V[jj][s]
                    fs2[ii][jj] += Sim[ii][jj]**2
                    if fs2[ii][jj] > ell:
                        ell = fs2[ii][jj]
        ell = ell**0.5

        # theory error bound
        delta = 0.0001
        #ss = ((log(n))**0.5)/ell
        #kk = ((i+1)*si)
        #MR = 2/ss/kk*log(n)+2*ss*ell*ell/kk
        MR = 4*ell/((i+1)*si)*(log(n))**0.5
        Delta = MR
        M = maxProd
        Delta += M*(1+ (8/((i+1)*si)*log(2/delta))**0.5+(8/((i+1)*si)*log(2/delta)+8*MR/M)**0.5)*((log(8/delta)/(2*(i+1)*si))**0.5)
        
        # error
        max_error = 0.0
        for ii in range(n):
            for jj in range(ii+1, n):
                if abs(Sim[ii][jj] - ExactSim[ii][jj]) > max_error:
                    max_error = abs(Sim[ii][jj]/((i+1)*si) - ExactSim[ii][jj])
        print('Max Error: ', max_error)
        print('Delta / #features: ', Delta/m)
    
