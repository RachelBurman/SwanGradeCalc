# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 20:36:13 2021

@author: mogzy
"""

import matplotlib.pyplot as plt

lf=0
uf=0
l1=0
u1=0
# l2=74.5 #Average marks achieved in remaining Level 5 credits pursued
# u2=87 #Average of the best marks achieved in 40 credits pursued at Level 5

CS200=70
CS210=75
CS255=62
CS275=46
CS205=54
CS230=65
CS250=40
CS270=49

CS200a=70
CS210a=75
CS255a=62
CS275a=46
CS205a=54
CS230a=65
CS250a=40
CS270a=49

CS318=(0.711*20)+10
CS325=(0.8*15)+10+((13.2/15)*15)
CS371=0.572*30
CS345=68
CS348=70
CS368=63
CS344=0
CS354=(0.68*35)+(10)+(0.8*25)+(0.58*30)

est=0.23

CS318a=(0.711*20)+10 + (est*70)
CS325a=(0.8*15)+10+((13.2/15)*15)+(est*60)
CS371a=0.572*30 +(est*70)
CS345a=68
CS348a=70
CS368a=63
CS344a=est*100
CS354a=(0.68*35)+(10)+(0.8*25)+(0.58*30)

g2= [CS200,CS200,CS200,CS210,CS210,CS210,CS255,CS255,CS255,CS275,CS275,CS275,CS205,CS205,CS205,CS230,CS230,CS230,CS250,CS250,CS250,CS270,CS270,CS270]
g2s=g2.sort(reverse=True)
g3= [CS318,CS318,CS318,CS325,CS325,CS325,CS371,CS371,CS371,CS345,CS345,CS345,CS348,CS348,CS348,CS368,CS368,CS368,CS344,CS344,CS344,CS354,CS354,CS354]
g3s=g3.sort(reverse=True)

l2=sum(g2[8:23]) / len(g2[8:23])
u2=sum(g2[0:7]) / len(g2[0:7])
l3=sum(g3[16:23]) / len(g3[16:23])
u3=sum(g3[0:15]) / len(g3[0:15])

g2a= [CS200a,CS200a,CS200a,CS210a,CS210a,CS210a,CS255a,CS255a,CS255a,CS275a,CS275a,CS275a,CS205a,CS205a,CS205a,CS230a,CS230a,CS230a,CS250a,CS250a,CS250a,CS270a,CS270a,CS270a]
g2sa=g2a.sort(reverse=True)
g3a= [CS318a,CS318a,CS318a,CS325a,CS325a,CS325a,CS371a,CS371a,CS371a,CS345a,CS345a,CS345a,CS348a,CS348a,CS348a,CS368a,CS368a,CS368a,CS344a,CS344a,CS344a,CS354a,CS354a,CS354a]
g3sa=g3a.sort(reverse=True)

l2a=sum(g2a[8:23]) / len(g2a[8:23])
u2a=sum(g2a[0:7]) / len(g2a[0:7])
l3a=sum(g3a[16:23]) / len(g3a[16:23])
u3a=sum(g3a[0:15]) / len(g3a[0:15])


current=((l2)+(u2+sum(g3[16:23]) / len(g3[16:23]))+((sum(g3[0:15]) / len(g3[0:15]))*3))/6

currenta=((l2a)+(u2a+sum(g3a[16:23]) / len(g3a[16:23]))+((sum(g3a[0:15]) / len(g3a[0:15]))*3))/6

unweight=((sum(g2) / len(g2))+(sum(g3) / len(g3)))/2

unweighta=((sum(g2a) / len(g2a))+(sum(g3a) / len(g3a)))/2

total=[]
godx=[]
gody=[]
gdx=[]
gdy=[]
ydx=[]
ydy=[]
rdx=[]
rdy=[]
for l in range(0,1001,1):
    for u in range(0,1001,1):

        b1=l2
        b2=u2+(l/10)
        b3=(u/10)*3
        
        total.append((u/10,l/10,((b1+b2+b3)/6)))
        
    
for n in range (0,len(total),1):
    if total[n][2]>=70 and total[n][1]<=total[n][0]:
        godx.append(total[n][0])
        gody.append(total[n][1])    
    
for n in range (0,len(total),1):
    if total[n][2]>=58 and total[n][1]<=total[n][0]:
        gdx.append(total[n][0])
        gdy.append(total[n][1])
        
for n in range (0,len(total),1):
    if total[n][2]>=48 and total[n][1]<=total[n][0]:
        ydx.append(total[n][0])
        ydy.append(total[n][1])
        
for n in range (0,len(total),1):
    if total[n][2]>=38 and total[n][1]<=total[n][0]:
        rdx.append(total[n][0])
        rdy.append(total[n][1])
      
        
plt.xlabel("Average for top 80 credits for 3rd year")
plt.ylabel("Average for bottom 40 credits for 3rd year")
plt.plot(rdx,rdy, 'r')
plt.plot(ydx,ydy, 'orange')
plt.plot(gdx,gdy, 'g')
plt.plot(godx,gody, 'gold')
#plt.plot(uf, lf, 'bo')
#plt.text(uf+1, lf, 'Foundation Year ('+str(round(uf,1))+', '+str(round(lf,1))+ ')')
#plt.plot(u1, l1, 'bo')
#plt.text(u1+1, l1, 'First Year ('+str(round(u1,1))+', '+str(round(l1,1))+ ')')
plt.plot(u2, l2, 'bo')
plt.text(u2+1, l2, 'Second Year ('+str(round(u2,1))+', '+str(round(l2,1))+ ')')
plt.plot(u3,l3, 'bo')
plt.text(u3+1,l3, 'Current Third Year Grade ('+str(round(u3,1))+', '+str(round(l3,1))+ ')')
plt.ylim(-1,80)
plt.xlim(u3-20,100)
plt.title('Current Overall Grade '+str(round(current,1))+'%, '+str(round(currenta,1))+'%')
plt.grid()
plt.locator_params(axis="x", nbins=20)
plt.locator_params(axis="y", nbins=20)
plt.show()





# import matplotlib.pyplot as plt

# l2=74.5 #Average marks achieved in remaining Level 5 credits pursued
# l3=50 #Average remaining marks in 60 Level 6 credits pursued
# u2=87  #Average of the best marks achieved in 30 credits pursued at Level 5
# u3=50 #Average best marks in 60 credits pursued at Level 6

# total=[]
# gdx=[]
# gdy=[]

# for l in range(0,101,1):
#     for u in range(0,101,1):

#         b1=l2
#         b2=((u2*2)+(l3*4))/3
#         b3=(u3*2)+l
#         b4=u*4
        
#         total.append((u,l,((b1+b2+b3+b4)/10)))
        
    
# for n in range (0,len(total),1):
#     if total[n][2]>70 and total[n][1]<=total[n][0]:
#         gdx.append(total[n][0])
#         gdy.append(total[n][1])
        
# plt.xlabel("Average for top 90 credits for 4th year")
# plt.ylabel("Average for bottom 30 credits for 4th year")
# plt.plot(gdx,gdy)
# plt.ylim(0,min(gdx))
# plt.xlim(min(gdx),100)
# plt.grid()

# plt.show()