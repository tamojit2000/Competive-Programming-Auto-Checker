import subprocess

Input='''
3
2
5
8
'''

Output='''
0
1
0
'''

Input=Input.strip('\n')
Output=Output.strip('\n')

################################################# CODE REGION ############################################################

checker=1

import sys

def In():
    return sys.stdin.readline()

def Out(x):
    return sys.stdout.write(str(x)+'\n')


CODE='''
for i in range(int(input())):
    x=int(input())
    if x%2!=0: print(1)
    else: print(0)
    

'''





################################################## CODE REGION ############################################################
if checker:
    result = subprocess.run(
        [sys.executable, "-c", CODE], capture_output=True, text=True, timeout=5, input=Input
    )

    

    ans=result.stdout.strip('\n').split('\n')
    error=result.stderr

    Output=Output.split('\n')

    i,j=0,0
    flag=True
    
    while i<len(Output) and j<len(ans):
        exp=Output[i]
        act=ans[i]
        ver='FAILED'
        if exp==act:
            ver='PASSED'
        else: flag=False
        i+=1
        j+=1
        
        print('Actual:',exp)
        print("Your's:",act)
        print('Verdict:',ver)
        print('\n\n')


    
    if len(Output)<len(ans):
        print('Actual:','NIL')
        print("Your's:",ans[j])
        print('Verdict:','FAILED')
        print('\n\n')
        flag=False


    if error: print('\n\nERROR:',error)
    

    if flag: print('\nALL TESTCASES PASSED')
    else: print('\nTESTCASE FAILED')

















        
