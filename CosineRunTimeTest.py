def main():

    # number of vectors
    n = 100
    # number of features
    m = 1000
    # sample size interval
    si = 10
    # max samples
    ms = 200
    # test rounds
    TR = 1

    from random import random
    from random import normalvariate
    from random import randint
    from math import log

    time_ints = [0.0 for i in range(ms//si)]
    for rr in range(TR):
        # init the n vectors
        print ('Initializing...')
        dict = {}
        V = []
        n = 0
        f = open('Email-Enron.txt','r')
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
        n//=100
        m=n
        VV = []
        for i in range(n):
            v = [0.0 for kk in range(m)]
            for item in V[i]:
                if item<m:
                    v[item] = 1.0
            v[i] = 1.0
            VV.append(v)
        V = VV

        from time import time
        start_time = time()
        # sampling and error analysis
        S = {}
        maxProd = 20.0
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
                        #if maxProd < V[ii][s] * V[jj][s]:
                        #    maxProd = V[ii][s] * V[jj][s]
                        fs2[ii][jj] += (V[ii][s] * V[jj][s])**2
                        if fs2[ii][jj] > ell:
                            ell = fs2[ii][jj]
            ell = ell**0.5

            time_ints[i] =time()- start_time

    for i in range(ms//si):
        print((i+1)*si, '\t', time_ints[i]*1000)


# test zone
main()

    
