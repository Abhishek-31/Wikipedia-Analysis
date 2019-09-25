from matplotlib import pyplot as plt
import xml.etree.cElementTree as ec
d={}

for _ in range(1,13):
    print('/home/wanderer/Downloads/JOCWIKI1/week'+str(_)+'wiki.xml')
    tree = ec.parse('/home/wanderer/Downloads/JOCWIKI1/week'+str(_)+'wiki.xml')
    flag=0
    root = tree.getroot()
    i=0
    for page in root:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        for child in page:
            if 'title' in child.tag:
                if 'Week '+str(_) in child.text:
                    #print('yes')
                    flag=1
                else:
                    flag=0
        
            if 'revision' in child.tag and flag==1:
                    #print(flag)
                for each in child:
                    if 'timestamp' in each.tag:
                        if i==0:
                            st=each.text
                            i=1
                        else:
                            et=each.text
    d[_]={}
    d[_]['start']=st[:st.index('T')]
    d[_]['end']=et[:et.index('T')]
    xaxis=[]
    yaxis=[]
for key,val in d.items():
    x,y,z=d[key]['start'].split('-')
    x=int(x)
    y=int(y)
    z=int(z)
    x1,y1,z1=d[key]['end'].split("-")
    x1=int(x1)
    y1=int(y1)
    z1=int(z1)
    count=0
    if y in [1,3,5,7,8,10,12]:
        count+=31-z
    elif y==2:
        count+=28-z
    else:
        count+=30-z
    count+=z1-1
    d[_]["days"]=(x1-x)*365+count
    print(d[_]["days"])
    xaxis.append(key)
    yaxis.append(d[_]["days"])
print(xaxis)
print(yaxis)
plt.plot(xaxis,yaxis,label='Week1')
d={}

for _ in range(1,13):
    print('/home/wanderer/Downloads/JOCWIKI2/week'+str(_)+'wiki.xml')
    tree = ec.parse('/home/wanderer/Downloads/JOCWIKI2/week'+str(_)+'wiki_2.xml')
    flag=0
    root = tree.getroot()
    i=0
    for page in root:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        for child in page:
            if 'title' in child.tag:
                if 'Week '+str(_) in child.text:
                    #print('yes')
                    flag=1
                else:
                    flag=0
        
            if 'revision' in child.tag and flag==1:
                    #print(flag)
                for each in child:
                    if 'timestamp' in each.tag:
                        if i==0:
                            st=each.text
                            i=1
                        else:
                            et=each.text
    d[_]={}
    d[_]['start']=st[:st.index('T')]
    d[_]['end']=et[:et.index('T')]
    xaxis2=[]
    yaxis2=[]
for key,val in d.items():
    x,y,z=d[key]['start'].split('-')
    x=int(x)
    y=int(y)
    z=int(z)
    x1,y1,z1=d[key]['end'].split("-")
    x1=int(x1)
    y1=int(y1)
    z1=int(z1)
    count=0
    if y in [1,3,5,7,8,10,12]:
        count+=31-z
    elif y==2:
        count+=28-z
    else:
        count+=30-z
    count+=z1-1
    d[_]["days"]=(x1-x)*365+count
    print(d[_]["days"])
    xaxis2.append(key)
    yaxis2.append(d[_]["days"])
print(xaxis2)
print(yaxis2)
plt.plot(xaxis2,yaxis2,label='Week2')
plt.xlabel("Article")
plt.ylabel("Number of days (Lifetime)")
plt.legend()
plt.savefig("Lifetime.png")
plt.show()
