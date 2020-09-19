import pandas as p
from locationiq.geocoder import LocationIQ
from math import radians,sin,cos,acos
import json
geocoder = LocationIQ("e4e5a0627a2ac0")

df=p.read_excel('Indian_capitals.xlsx',names=['src','des','dis'],header=None)

d = {}
for i in df['src'].unique():
    d[i] = [df['des'][j] for j in df[df['src']==i].index]
dr = {}
for i in df['des'].unique():
    dr[i] = [df['src'][j] for j in df[df['des']==i].index]
for key in d: 
    if key in dr: 
        d[key] = d[key] + dr[key]
        
    else: 
        pass
for key in dr: 
    if key not in d: 
        d[key] = dr[key]
    else: 
        pass
di=d 

f= {}
for i in df['src'].unique():
    f[i] = [{df['des'][j]:df['dis'][j]} for j in df[df['src']==i].index]

fr = {}
for i in df['des'].unique():
    fr[i] = [{df['src'][j]:df['dis'][j]} for j in df[df['des']==i].index]

for key in f: 
    if key in fr: 
        f[key] = f[key] + fr[key]
        
    else: 
        pass

for key in fr: 
    if key not in f: 
        f[key] = fr[key]
    else: 
        pass
def isgoal(city,goal):
        if(city==goal):
            return True
        return False
class bfs:
    def __init__(self,name,parent):
        self.name=name
        self.parent=parent
    
    
    
    
    def search(s,de):
           
        
        state=s

        explored=[]
        queue=[]
        node=bfs(s,None)
        parent=node
        if isgoal(s,de)==True:
            print("You are at the goal")
        else:
            while isgoal(state,de)==False:
                explored.append(state)

                neigh=di.get(state)
                if neigh is not None:
                    for city in neigh:

                        if city not in explored and not(ispresent(queue,city)):
                            node=bfs(city,parent)
                            queue.append(node)


                if(len(queue)==0):
                    break
                parent=queue.pop(0)    
                state=parent.name


        li=[]
        if(parent.name==de):
            while(parent!=None):
                li.append(parent.name)

                parent=parent.parent


        else:
            print("There is no path")
        print(Reverse(li))


class dfs:
    def __init__(self,name,parent):
        self.name=name
        self.parent=parent
    
    
    
    
    def search(s,de):
           
        
        state=s

        explored=[]
        queue=[]
        node=dfs(s,None)
        parent=node
        if isgoal(s,de)==True:
            print("You are at the goal")
        else:
            while isgoal(state,de)==False:
                explored.append(state)

                neigh=di.get(state)
                if neigh is not None:
                    for city in neigh:

                        if city not in explored and not(ispresent(queue,city)):
                            node=dfs(city,parent)
                            queue.append(node)


                if(len(queue)==0):
                    break
                parent=queue.pop()    
                state=parent.name


        li=[]
        if(parent.name==de):
            while(parent!=None):
                li.append(parent.name)

                parent=parent.parent


        else:
            print("There is no path")
        print(Reverse(li))


def Enquiry(lis1): 
    if len(lis1) == 0: 
        return 0
    else: 
        return 1
def ispresent(q,city):
        for n in q:
            if(n.name==city):
                return True
        return False
def Reverse(lst): 
    lst.reverse() 
    return lst 
def common_member(a, b): 
        aset = set(a) 
        bset = set(b) 
        if len(aset.intersection(bset)) > 0: 
            return(True)  
        return(False) 
def common_member_name(a, b): 
        a_set = set(a) 
        b_set = set(b) 
        if (a_set & b_set): 
            return(a_set & b_set) 


class bibfs:
    def __init__(self,name,parent):
        self.name=name
        self.parent=parent
    
    
    
    
    def search(s,de):
        
        state1=s
        state2=de
        de1=de
        de2=s

        explored1=[]
        explored2=[]
        store1=[]
        store2=[]
        queue1=[]
        queue2=[]
        q1=[]
        q2=[]
        node1=bibfs(s,None)
        node2=bibfs(de,None)
        parent1=node1
        parent2=node2
        q1.append(s)
        q2.append(de)
        if isgoal(s,de)==True:
            print("You are at the goal")
        else:

            while isgoal(state1,de1)==False and isgoal(state2,de2)==False:
                explored1.append(state1)
                explored2.append(state2)

                neigh=di.get(state1)

                if neigh is not None:
                    for city in neigh:

                        if city not in explored1 and not(ispresent(queue1,city)):
                            node=bibfs(city,parent1)
                            queue1.append(node)
                            q1.append(node.name)
                neigh=di.get(state2)
                if neigh is not None:
                    for city in neigh:

                        if city not in explored2 and not(ispresent(queue2,city)):
                            node=bibfs(city,parent2)
                            queue2.append(node)
                            q2.append(node.name)
                if(len(queue1)==0 or len(queue2)==0):
                    break


                parent1=queue1.pop(0)
                store1.append(parent1)
                parent2=queue2.pop(0) 
                store2.append(parent2)
                state1=parent1.name
                state2=parent2.name
                flag=common_member(q1,q2)
                if flag==True:

                    break  


        com=common_member_name(q1,q2)
        ele=list(com)
        ele=ele[0]
        print(ele)
        l1=[]
        l2=[]
        for r in queue1 or store1:
            if(r.name==ele):

                n1=r

                while(n1!=None):

                    l1.append(n1.name)

                    n1=n1.parent
                break
        for r in  store1:
            if(r.name==ele):

                n1=r

                while(n1!=None):

                    l1.append(n1.name)

                    n1=n1.parent
                break

        for r in queue2:
            if(r.name==ele):
                n2=r
                n2=r.parent
                while(n2!=None):
                    l2.append(n2.name)

                    n2=n2.parent      
                break
        for r in  store2:
            if(r.name==ele):

                n2=r
                n2=r.parent
                while(n2!=None):

                    l1.append(n2.name)

                    n2=n2.parent
                break
        print(Reverse(l1)+l2)

def delete(queue): 
        try: 
            min = 0
            for i in range(len(queue)): 
                if queue[i].pc < queue[min].pc: 
                    min = i 
            item = queue[min] 
            del queue[min] 
            return item
        except IndexError: 
            print() 
            exit()
def calculate(f,parent,city):
        count=0
        for c in f[parent.name]:

            sos=list(c.keys())
            s=sos[0]
            if(s==city):
                break
            count=count+1
        h=f[parent.name][count]
        return(h[city])
def findhei(c1):
        hei={}
        de=c1
        d2=geocoder.geocode(de)[0]
        for key in di:
            d1=geocoder.geocode(key)[0]

            slat=radians(float(d1['lat']))
            slon=radians(float(d1['lon']))
            elat=radians(float(d2['lat']))
            elon=radians(float(d2['lon']))
            dist=6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon-elon))
            hei[key]=dist 
        return hei


          
class astar():
    
    def __init__(self,name,parent,pc):
        self.name=name
        self.parent=parent
        self.pc=pc
    
    
    
    def search(s,de):
        
        state=s

        explored=[]
        queue=[]
        node=astar(s,None,f[s])
        parent=node
        hei=findhei(de)
        if isgoal(s,de)==True:
            print("You are at the goal")
        else:
            while isgoal(state,de)==False:
                explored.append(state)

                neigh=di.get(state)
                if neigh is not None:
                    for city in neigh:

                        if city not in explored and not(ispresent(queue,city)):
                            distance=calculate(f,parent,city)
                            distance=distance+hei[city]

                            node=astar(city,parent,distance)
                            queue.append(node)


                if(len(queue)==0):
                    break
                parent=delete(queue)    
                state=parent.name


            li=[]
            if(parent.name==de):
                while(parent!=None):
                    li.append(parent.name)

                    parent=parent.parent


            else:
                print("There is no path")
        print(Reverse(li))   


def search_path(source,destination):
    str=int(input("Enter search method:1.BFS 2:DFS 3:BI-BFS 4:A*"))
    print("FINAL ACTION SEQUENCE")
    if(str==1):
        bfs.search(source,destination)
    elif(str==2):
        dfs.search(source,destination)
    elif(str==3):
        bibfs.search(source,destination)
    else:
        astar.search(source,destination)
    
source=input("Enter source")#Intial State
destination=input("Enter destination")#GoalFormulation

if(str==1):
    search_path(source,destination)
elif(str==2):
    search_path(source,destination)
elif(str==3):
    search_path(source,destination)
else:
    search_path(source,destination)
    
