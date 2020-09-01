no_voters=int(input())				                        #INPUT NO OF VOTERS
que_voters=list(map(str,input()))	                        #INPUT THE VOTERS
que_voters.insert(0,-1)
que_voters.append(-1)
vot=1
temp=1
while vot<(len(que_voters)-1):		                        #LOOP FOR ITERATING THE VOTERS
    last=vot
    if que_voters[vot]=='-':		                        #CHECKING IF VOTER IS NEUTRAL OR NOT
        for nxt in range(vot+1,(len(que_voters)-1)):		#CHECKING FOR NEXT NEUTRAL VOTERS IN THE QUEUE
            if que_voters[nxt]=='-':
                pass
            else:
                temp=nxt
                last=nxt-1
                break
        else:
            temp+=1
        while vot<=last:
            if vot==last and que_voters[vot-1]=='B' and que_voters[last+1]=='A':
                vot+=1
                last-=1
            if que_voters[vot - 1] == 'B' or que_voters[last + 1] == 'A':
                if que_voters[vot-1]=='B':				    #MAKING THE NEUTRAL VOTERS
                    que_voters[vot]='B'				        #SUPPORTER OF B
                    vot+=1
                if que_voters[last+1]=='A':				    #OR SUPPORTER OF A
                    que_voters[last]='A'
                    last-=1
            else:
                if que_voters[vot-1]!='B':
                    vot+=1
                if que_voters[last+1]!='A':
                    last-=1
        vot=temp
    else:
        vot+=1
vot_a=que_voters.count('A')						           #COUNT VOTES OF A
vot_b=que_voters.count('B')						           #COUNT VOTES OF A

if vot_a>vot_b:
    print("A", end='')							           #PRINTING THE CANDIDATE WITH MAXIMUM NO OF VOTES
elif vot_a<vot_b:
    print("B", end='')
else:
    print("Coalition government", end='')
