city=[]				                #array of city
trajectory=[]		                #all coordinates of trajectory
total_pop=0
non_inf_pop=0
for r in range(9):
    cty=list(input())
    total_c=(cty.count('c'))
    total_a=(cty.count('a'))
    total=total_a+total_c
    total_pop+=total				#total population
    city.append(cty)
print('0 0')
row=7
col=1
count=0
aa=-1
b=1
dir='ur'
while count<2:						#check how many times the virus touches the boundry.
    if city[row][col] == '.':		#condition for empty spaces
        print(col, 8-row)
        row+=aa
        col+=b

    elif city[row][col] == 'a':		#condition for anticlockwise turn
        print(col, 8-row)
        city[row][col]='-'
        if dir=='ur':
            aa=aa
            b=-b
            dir='ul'
        elif dir=='ul':
            aa = -aa
            b = -b
            dir = 'bl'
        elif dir=='bl':
            aa = aa
            b = -b
            dir = 'br'
        elif dir=='br':
            aa = -aa
            b = b
            dir = 'ur'
        row += aa
        col += b

    elif city[row][col] == 'c':			#condition for clockwise turn
        print(col, 8 - row)
        city[row][col]='-'
        if dir=='ur':
            aa=-aa
            b=b
            dir='br'
        elif dir=='ul':
            aa = aa
            b = -b
            dir = 'ur'
        elif dir=='bl':
            aa = -aa
            b = b
            dir = 'ul'
        elif dir=='br':
            aa = aa
            b = -b
            dir = 'bl'
        row += aa
        col += b

    elif city[row][col]=="*":			#condition for boundry
        print(col, 8 - row)
        if dir == 'ur':
            if row==0:
                aa = -aa
                b = b
                dir = 'br'
            else:
                aa = aa
                b = -b
                dir = 'ul'
        elif dir == 'ul':
            if row==0:
                aa = -aa
                b = b
                dir = 'bl'
            else:
                aa = aa
                b = -b
                dir = 'ur'
        elif dir == 'bl':
            if row==8:
                aa = -aa
                b = b
                dir = 'ul'
            else:
                aa = aa
                b = -b
                dir = 'br'

        elif dir == 'br':
            if row==8:
                aa = -aa
                b = b
                dir = 'ur'
            else:
                aa = aa
                b = -b
                dir = 'bl'
        count+=1
        row += aa
        col += b

for people in trajectory:				#printing the trajectory
    print(people)
for people in city:						#printing the city array(updated)
    total_c = (people.count('c'))
    total_a = (people.count('a'))
    total = total_a + total_c
    non_inf_pop += total			    #non infected population
    print(''.join(people))

print("safe="+str(non_inf_pop))								#print safe population
print("infected="+str(total_pop-non_inf_pop),end='')		#print infected population




'''

********************
*..................*
*..c...............*
*....c.............*
*.........a........*
*..................*
*.......a......c...*
*..................*
********************

'''
