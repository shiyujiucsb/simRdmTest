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
    si = 500
    # max samples
    ms = 10000
    # max samples for exact solution
    MS = 1000
    # longest walk
    T = 20
    # test rounds
    TR = 1
    from time import time

    from random import random
    from random import randint
    from math import log
    

    time_ints = [0.0 for i in range(ms//si)]
    for rr in range(TR):
        # init the n nodes
        #print ('Initializing...')
        dict = {}
        V = []
        n = 0
        f = open('egoGplus.edges','r')
        for line in f:
            A = line.split()[0]
            B = line.split()[1]
            if A not in dict:
                V.append([])
                dict[A] = n
                n += 1
            if B not in dict:
                V.append([])
                dict[B] = n
                n += 1
            V[dict[A]].append(dict[B])
        f.close()
        print(n)
        
        start_time = time()
        # sampling and error analysis
        Sim = [[0.0 for i in range(n)] for j in range(n)]
        fs2 = [[0.0 for i in range(n)] for j in range(n)]
        for i in range(ms//si):
            print('Sampling', (i+1)*si, 'samples...')
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

            time_ints[i] = time()-start_time

    for i in range(ms//si):
        print((i+1)*si, '\t', time_ints[i])
    
# test zone
main()
