#!/usr/bin/env python3
import random,time, subprocess
output='Hello, World!' #Place output here
seed=0          #Starting seed. Modify if running multiple in parallel

chars=''.join(map(chr,range(32,127)))+'\n'
prog,n='',-1

print("Brute-forcing seed...")

seconds=time.clock()
while True:
    n+=1
    print(n)
    random.seed(n)
    prog = ''
    t = 0
    while len(prog) < 500: # maximum length of program; can be changed
        t += 1
        prog += chars[int(random.random()*96)]
        if ',' not in prog or any([x in prog for x in '.&~'+''.join(map(chr,range(65,65+26)))]):
            continue
        print(prog)
        try:
            with open('seed.bf98','w') as f:
                f.write(prog)
            res = subprocess.check_output(['pyfunge','-v','98','-F','seed.bf98'], timeout=1, universal_newlines=True)
            if len(res) > 0 and not output.startswith(res):
                break
            else:
                done()
        except:
            continue

def done():
    print()
    seconds=time.clock()-seconds
    print('Found seed for "{0}"!\nSeed program:\n{1} {2}'.format(prog,length,seed))
    print("Time elapsed: {0} seconds. Tries per second:{1}".format(seconds,int(n/seconds)))
    exit()
