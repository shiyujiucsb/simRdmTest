def random_walks(V,ii,jj,T,c):
    from random import randint
    a = ii
    b = jj
    for i in range(T):
        if a == b:
            return c**i
        if len(V[a])==0 or len(V[b])==0:
            return 0.0
        a = V[a][randint(0,len(V[a])-1)]
        b = V[b][randint(0,len(V[b])-1)]
    return 0.0

def RW_samples(V,ii,jj,S1,S2,c):
    a = ii
    b = jj
    for i in range(len(S1)):
        if a == b:
            return c**i
        if len(V[a])==0 or len(V[b])==0:
            return 0.0
        a = V[a][int(S1[i]*len(V[a]))]
        b = V[b][int(S2[i]*len(V[b]))]
    return 0.0

def main():

    # number of nodes
    n = 10
    # probability of an edge
    p = .1
    # simrank constant
    c = .7
    # sample size interval
    si = 50
    # max samples
    ms = 1000
    # max samples for exact solution
    MS = 1000
    # longest walk
    T = 20
    # test rounds
    TR = 100

    from random import random
    from random import randint
    from math import log

    max_error_array = [0.0 for i in range(ms//si)]
    Delta_array = [0.0 for i in range(ms//si)]
    for rr in range(TR):
        # init the n nodes
        #print ('Initializing...')
        d = 0#3  # small world param
        V = []
        for i in range(n):
            v = []
            for j in range(n):
                if random() < p or (abs(i-j)<d and i != j):
                    v.append(j)
            V.append(v)

        # exact solution
        #print ('Computing the exact solution...')
        
        ExactSim = [[0.0 for i in range(n)] for j in range(n)]
        for ii in range(n):
            for jj in range(ii+1, n):
                for k in range(MS):
                    ExactSim[ii][jj] += random_walks(V,ii,jj,T,c)
                ExactSim[ii][jj] /= MS
        

        # sampling and error analysis
        Sim = [[0.0 for i in range(n)] for j in range(n)]
        fs2 = [[0.0 for i in range(n)] for j in range(n)]
        for i in range(ms//si):
            #print('Sampling', (i+1)*si, 'samples...')
            ell = 0.0
            j=0
            while j<si:
                S1 = [random() for mm in range(T)]
                S2 = [random() for mm in range(T)]
                j += 1
                for ii in range(n):
                    for jj in range(ii+1, n):
                        rw= RW_samples(V,ii,jj,S1,S2,c)
                        Sim[ii][jj]+=rw
                        fs2[ii][jj] += rw**2
                        if fs2[ii][jj] > ell:
                            ell = fs2[ii][jj]
            ell = ell**0.5

            # theory error bound
            delta = 0.0001
            MR = 4*ell/((i+1)*si)*(log(n))**0.5
            Delta = min([c*(((2*log(n)+log(1/delta))/(2*(i+1)*si))**0.5), MR+ c*(1+ (8/((i+1)*si)*log(2/delta))**0.5+(8/((i+1)*si)*log(2/delta)+8*MR/c)**0.5)*((log(8/delta)/(2*(i+1)*si))**0.5)])
            
            
            # error
            max_error = 0.0
            for ii in range(n):
                for jj in range(ii+1, n):
                    if abs(Sim[ii][jj] - ExactSim[ii][jj]) > max_error:
                        max_error = abs(Sim[ii][jj]/((i+1)*si) - ExactSim[ii][jj])
            #print('Max Error: ', max_error)
            max_error_array[i]+=max_error
            #print('Delta / #features: ', Delta/m)
            Delta_array[i]+=Delta

    for i in range(ms//si):
        print((i+1)*si, '\t', max_error_array[i]/TR, '\t', Delta_array[i]/TR)

        
    
# test zone
main()
