
#-*- coding: UTF-8 -*-
"""program for write the Auslander-Reiten quiver fo the companian of an path algebra of type A"""
import time
#import quiver
#import quiverD

#import companian

sfP=False


def headf():
    sss=r"""
\documentclass[a4paper,reqno]{amsart}

\usepackage{geometry}
\geometry{a4paper, landscape, margin=1.5in}

\usepackage{hyperref}

\usepackage{amssymb,amsxtra,amsfonts,dsfont}

\usepackage{graphicx} \usepackage{amsmath} \usepackage{amssymb}

\usepackage[svgnames]{xcolor}

\usepackage[color,matrix,arrow]{xy}

\input xy \xyoption{all}







\renewcommand{\baselinestretch}{1.1}


\begin{document}
\title[ Auslander-Reiten quiver for the companian of path algebra of type $A$]{Quivers and Auslander-Reiten quivers for the companian of representation-finite path algebra of type $A$}


\maketitle



The quiver $Q$ you chosen is

\input txqvgr

From the Auslander-Reiten quiver 
\input txARqA

of the path algebra $kQ$, we get the quiver $Q^c$ for the companian:

\input txcq1

The Auslander-Reiten quiver for the companian is: 

\input txarq1

The dimensional vectors for the indecomposable modules are
\input txarqdmv
\end{document}


"""
    
    f=open('arqq.tex', 'w') #clear the file for write
    f.write(sss) 
    f.close()
    

def getqvA():
    ss=r"""This program produce the Auslander-Reiten for the companian 
    of a path algebra of type A.

    to start it, input the number of the vertices of the quiver, then 
    choose the orientation of the quiver,  input 'y' if you agree with
    the choice made and any other key otherwise.

    the files for the quiver using the xy-pic will be written.

    find the file named 'ARqq.tex' and pdflatex it,you will get a paf 
    file containing the quivers related.
    """
    print(ss)
    #print('\n\n')

    N=int(input('Please input the number of vertices'))
    orq={0:0}
    min=0
    max=0
    mv=0
    print(r'Please choose the orientation:input "y" if you agree with the choice made and any other key otherwise.')
    for i in range(N-1):
        if input(f'input "Y" if you want an arrow from {i+2} to {i+1}') in ('y',"Y"):
            orq.update({i+1:orq[i]+1})
            if max<orq[i]+1:
                max=orq[i]+1
        else: 
            orq.update({i+1:orq[i]-1})
            if min==orq[i]:
                min-=1
                mv=i
    for i in range(N):
        orq[i]=orq[i]-min
    max=max-min
    return {'quiver':orq,'vernm':N,'max':max,'minvertex':mv}

def getqvD():
    """
    0518:change the vertex 2(index 1) as the cross vertex
    """
    N=int(input('the number of vertices'))
    orq={0:0}
    min=0
    miv=0
    max=0
    mav=0
    for i in range(N-2):
        if input(f'you want an arrow from {i+1} to {i+2}') in ('y',"Y"):
            orq.update({i+1:orq[i]+1})
        else: 
            orq.update({i+1:orq[i]-1})
            if min==orq[i]:
                min-=1
                miv=i+1
    if input(f'the arrow from {2} to {N}') in ('y',"Y"):
        orq.update({N-1:orq[1]+1})
    else: 
        orq.update({N-1:orq[1]-1})
        if min==orq[1]:
            min-=1
            miv=N-1
    for i in range(N):
        orq[i]=orq[i]-min        
        if max<orq[i]:
            max=orq[i]
            mav=i
    #orq.update({'max':max})

    return {'quiver':orq,'vernm':N,'max':max,'mav':mav,'mindg':min,'minvertex':miv}

def getqvE():
    N=int(input('the number of vertices'))
    if N<6 or N>8:
        print('the number must between 6 and 8')
    orq={0:0}
    min=0
    miv=0
    max=0
    mav=0
    for i in range(N-2):
        if input(f'you want an arrow from {i+1} to {i+2}') in ('y',"Y"):
            orq.update({i+1:orq[i]+1})
        else: 
            orq.update({i+1:orq[i]-1})
            if min==orq[i]:
                min-=1
                miv=i+1
    if input(f'the arrow from {3} to {N}') in ('y',"Y"):
        orq.update({N-1:orq[2]+1})
    else: 
        orq.update({N-1:orq[2]-1})
        if min==orq[2]:
            min-=1
            miv=N-1
    for i in range(N):
        orq[i]=orq[i]-min        
        if max<orq[i]:
            max=orq[i]
            mav=i
    #orq.update({'max':max})

    return {'quiver':orq,'vernm':N,'max':max,'mav':mav,'mindg':min,'minvertex':miv,}
    

def wtqvgr(ddn,oq,tp):
    """write quiver oq as graded quiver"""
    if tp=='A':
        N=ddn
    else:
        N=ddn-1
    if tp=='D':
        node=1
    elif tp=='E':
        node=2
    else:
        node=-1

    h=open('txqvgr.tex', 'w')
    h.write(r'\Tiny$$\xymatrix@C=1cm@R=0.5 cm{')
    for i in range(N):
        ss=''
        for t in range(oq[i]):
            ss+=r'&'
            if i==node and t==oq[i]-2 and oq[i]>oq[N]:
                ss+=r'\stackrel{'
                ss+=f'{N+1}'
                ss+=r'}{\circ}\ar@{<-}[r]'
            
            #if t==oq[i]-1:
        ss+=r'\stackrel{'
        ss+=f'{i+1}'
        ss+=r'}{\circ}'
        if i<N-1:
            if oq[i]<oq[i+1]:
                ss+=r'\ar@{<-}[dr]'
            else:
                 ss+=r'\ar[dl]'

        if i==node and oq[i]<oq[N]:
            ss+=r'\ar[r] &\stackrel{'
            ss+=f'{N+1}'
            ss+=r'}{\circ}'
                
        ss+=r'\\'
        ss+='\n'

        h.write(ss)

    h.write(r'}$$\normalsize')
    h.write('\n\n')

    h.write
    h.close



def getquiver():
    while input('choose type of the quiver, A,D or E') not in ('A','a','D','d','E','e'):
         input('choose type of the quiver, A,D or E')
    if input('choose type of the quiver, A,D or E') in ('A','a'):
        return {'qv':getqvA(),'type':'A'}
    elif input('choose type of the quiver, A,D or E') in ('D','d'):
        return  {'qv':getqvD(),'type':'D'}
    elif input('choose type of the quiver, A,D or E') in ('E','e'):
        return {'qv':getqvE(),'type':'E'}
    else:
        print('you have chosen wrong type')


def mkhmkA(dian,vert):
    """The hammock the quiver oq at the vertex vert"""
    """if oq==[]:
        if tp=='A':
            for i in range(dian):
                oq[i]=abs(i-vert-1)
        else:
            pass"""
    
    global sfP

    
    jixu=True
    t=0
    hmk=[]
    #vert=vert-1 #correct index
    """The  t*dian+i term is the position (i,t)"""
    while jixu:
        jixu=False
        hmkt={}
        for i in range(dian):

            if (i-vert)%2==0:
                i1=0
            else:
                i1=1
            
            hmkv={}
            hmkv.update({'orb':i,'dis':t})
            
            
            if t==0:
                
                if i==vert:
                    hmkv.update({'sdd':True})                        
                    hmkv.update({'hfv':1})
                    jixu=True
                else:
                    hmkv.update({'sdd':False})                                               
                    hmkv.update({'hfv':0})

                if sfP:
                    print(jixu)

            elif t==1: 
                if abs(i-vert)==1:
                    hmkv.update({'sdd':True})                        
                    hmkv.update({'hfv':1})
                    jixu=True
                else:
                    hmkv.update({'sdd':False})                                               
                    hmkv.update({'hfv':0})
            elif (t-i1)%2==0 and (t-i1)>=0:
                mmm=0
                if i >0: 
                    mmm+=hmk[t-1][i-1].get('hfv')
                if i <dian-1: 
                    mmm+=hmk[t-1][i+1].get('hfv')
                mmm-=hmk[t-2][i].get('hfv')   
                if mmm>0:                     
                        hmkv.update({'sdd':True})  
                        hmkv.update({'hfv':mmm})                      
                        jixu=True
                else:
                    
                    hmkv.update({'sdd':False})                     
                    hmkv.update({'hfv':mmm})

            else:
                hmkv.update({'sdd':False})
                hmkv.update({'hfv':0})
            hmkt.update({i:hmkv})

            """hmkv{'sdd':True,'hfv':the value of hammock function at this vertex,
            'orb':i,'dis':t}, [if it is(sdd) a vertex, index(orb) of orbit, with t times of the action of \tau^{-1}]"""
        hmk.append(hmkt)
        
        if sfP:
            print(t)
            print(hmkt)
        
        t+=1
    return hmk


def mkhmkD(dian,vert):
    """The hammock the quiver of type D  at the vertex vert    
    """

    global sfP

    
    jixu=True
    t=0
    hmk=[]
    #vert=vert-1 #correct index
    """The  t*dian+i term is the position (i,t)
    if vert=1, the odd terms  dian-1
    if vert=N-1, the even terms is  dian-1, odd term reprents 2
    
    0518:change the vertex 2(index 1) as the cross vertex
    """
    while jixu:
        jixu=False
        hmkt={}
        for i in range(dian):
            if (vert== dian-1):
                if i==dian-1:
                    i1=0
                elif (i-1)%2==0:
                    i1=1
                else:
                    i1=0
            elif i==dian-1:
                if (1-vert)%2==0:
                    i1=1
                else: 
                    i1=0
            elif (i-vert)%2==0:
                i1=0
            else:
                i1=1
            
            hmkv={}
            hmkv.update({'orb':i+1,'dis':t})
            
            
            if t==0:
                
                if i==vert:
                    hmkv.update({'sdd':True})                        
                    hmkv.update({'hfv':1})
                    jixu=True
                else:
                    hmkv.update({'sdd':False})                                               
                    hmkv.update({'hfv':0})

                if sfP:
                    print(jixu)

            elif t==1: 
                if ((i!=dian-1 and vert!=dian-1 and abs(i-vert)==1) or 
                        (i==dian-1 and vert==1) or  (i==1 and vert==dian-1)):
                    hmkv.update({'sdd':True})                        
                    hmkv.update({'hfv':1})
                    jixu=True
                else:
                    hmkv.update({'sdd':False})                                               
                    hmkv.update({'hfv':0})
            elif (t-i1)%2==0 and (t-i1)>=0: #
                mmm=0
                if i >0 and i!=dian-1: 
                    mmm+=hmk[t-1][i-1].get('hfv')
                if i <dian-2: 
                    mmm+=hmk[t-1][i+1].get('hfv')
                if i==1:                    
                    mmm+=hmk[t-1][dian-1].get('hfv')
                if i==dian-1:
                    mmm+=hmk[t-1][1].get('hfv')
                mmm-=hmk[t-2][i].get('hfv')   
                if mmm>0:                     
                        hmkv.update({'sdd':True})  
                        hmkv.update({'hfv':mmm})                      
                        jixu=True
                else:
                    
                    hmkv.update({'sdd':False})                     
                    hmkv.update({'hfv':mmm})

            else:
                hmkv.update({'sdd':False})
                hmkv.update({'hfv':0})
            hmkt.update({i:hmkv})

            """hmkv{'sdd':True,'hfv':the value of hammock function at this vertex,
            'orb':i,'dis':t}, [if it is(sdd) a vertex, index(orb) of orbit, with t times of the action of \tau^{-1}]"""
        hmk.append(hmkt)
        
        if sfP:
            print(t)
            print(hmkt)

        t+=1
    return hmk


def mkhmkE(dian,vert):
    """The hammock the quiver of type E  at the vertex vert"""

    global sfP   
    
    jixu=True
    t=0
    hmk=[]
    #vert=vert-1 #correct index
    """The  t*dian+i term is the position (i,t)
    if vert=3, the odd terms in dian-3 represents dian-1
    if vert=N-1, the even terms in 3 represents dian-1, odd term reprents dian-3
    """
    while jixu:
        jixu=False
        hmkt={}
        for i in range(dian):
            if (vert== dian-1):
                if i==dian-1:
                    i1=0
                elif (i-2)%2==0:
                    i1=1
                else:
                    i1=0
            elif i==dian-1:
                if (2-vert)%2==0:
                    i1=1
                else: 
                    i1=0
            elif (i-vert)%2==0:
                i1=0
            else:
                i1=1
            
            hmkv={}
            hmkv.update({'orb':i+1,'dis':t})
            
            
            if t==0:
                
                if i==vert:
                    hmkv.update({'sdd':True})                        
                    hmkv.update({'hfv':1})
                    jixu=True
                else:
                    hmkv.update({'sdd':False})                                               
                    hmkv.update({'hfv':0})

                if sfP:
                    print(jixu)

            elif t==1: 
                if (i!=dian-1 and vert!=dian-1 and abs(i-vert)==1) or (i==dian-1 and vert==2) or  (i==2 and vert==dian-1):
                    hmkv.update({'sdd':True})                        
                    hmkv.update({'hfv':1})
                    jixu=True
                else:
                    hmkv.update({'sdd':False})                                               
                    hmkv.update({'hfv':0})
            elif (t-i1)%2==0 and (t-i1)>=0: #
                mmm=0
                if i >0 and i!=dian-1: 
                    mmm+=hmk[t-1][i-1].get('hfv')
                if i <dian-2: 
                    mmm+=hmk[t-1][i+1].get('hfv')
                if i==2:                    
                    mmm+=hmk[t-1][dian-1].get('hfv')
                if i==dian-1:
                    mmm+=hmk[t-1][2].get('hfv')
                mmm-=hmk[t-2][i].get('hfv')   
                if mmm>0:                     
                        hmkv.update({'sdd':True})  
                        hmkv.update({'hfv':mmm})                      
                        jixu=True
                else:
                    
                    hmkv.update({'sdd':False})                     
                    hmkv.update({'hfv':mmm})

            else:
                hmkv.update({'sdd':False})
                hmkv.update({'hfv':0})
            hmkt.update({i:hmkv})

            """hmkv{'sdd':True,'hfv':the value of hammock function at this vertex,
            'orb':i,'dis':t}, [if it is(sdd) a vertex, index(orb) of orbit, with t times of the action of \tau^{-1}]"""
        hmk.append(hmkt)
        
        if sfP:
            print(t)
            print(hmkt)
        t+=1
    return hmk

 
def wthmkA(dian,hmk=[],cdu=20):
    """Draw quiver ZQ for the given quiver oq[],fd for the parts divided,cdu for the columns in each parts
    """

    global sfP

     
    with open('txhmk.tex', 'a') as f:
        tta=time.time()
        print('Current date and time:',file=f)
        print(f'{time.ctime(tta)}',file=f)

        if sfP:
            print(len(hmk)/cdu) 
        
        for t in range(len(hmk)//cdu+1):
            print(r'\Tiny$$\xymatrix@C=0.5 cm@R=0.5 cm{', file=f)
            for i in range(dian):
                ss=''
                for j in range(cdu):
                    if t*cdu+j < len(hmk):
                        hvt=hmk[(t*cdu+j)][i]

                        if sfP:
                            print(hvt)

                        if hvt['sdd']:
                            ss+=r'\stackrel{'
                            ss+=f'{hvt['hfv']}'
                            ss+=r'}{'
                            ss+=f'({hvt['orb']+1},{hvt['dis']})'
                            ss+=r'}'                  
                            if i > 0 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i-1]['sdd']: 
                                ss+=r'\ar[ur]'
                            if i< dian-1 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i+1]['sdd']:
                                ss+=r'\ar[dr]'                                  
                        ss+='&'
                ss+=r'\\'            
                print(ss,file=f)
            print(r'}$$\normalsize', file=f)
   


def wthmkD(dian,hmk=[],cdu=12):
    """Draw quiver ZQ for the given quiver oq[],fd for the parts divided,cdu for the columns in each parts
        
        0518:change the vertex 2(index 1) as the cross vertex
    
    """

    global sfP


    with open('txhmkd.tex', 'a') as f:

        

        tta=time.time()
        print('Current date and time:',file=f)
        print(f'{time.ctime(tta)}',file=f)


        if sfP:
            print(len(hmk)/cdu) 
        
        for t in range(len(hmk)//cdu+1):
            print(r'\Tiny$$\xymatrix@C=0.3 cm@R=0.5 cm{', file=f)
            for i in range(dian-1):
                ss=''
                for j in range(cdu):
                    if t*cdu+j < len(hmk):
                        if i==1:
                            hvtt=hmk[(t*cdu+j)][dian-1]
                        hvt=hmk[(t*cdu+j)][i] 
                        
                        if sfP:
                            print(hvt)


                        if hvt['sdd']:
                            ss+=r'\stackrel{'
                            ss+=f'{hvt['hfv']}'
                            ss+=r'}{'
                            ss+=f'({hvt['orb']+1},{hvt['dis']})'
                            ss+=r'}'                  
                            if i > 0 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i-1]['sdd']: 
                                ss+=r'\ar[ur]'
                            if i< dian-1 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i+1]['sdd']:
                                ss+=r'\ar[dr]'  
                            if i== 1 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][dian-1]['sdd']:
                                ss+=r'\ar[r]'   
                        if i==1 and hvtt['sdd']:
                            ss+=r'\stackrel{'
                            ss+=f'{hvtt['hfv']}'
                            ss+=r'}{'
                            ss+=f'({hvtt['orb']+1},{hvtt['dis']})'
                            ss+=r'}'                  
                            if  t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i]['sdd']: 
                                ss+=r'\ar[r]'
                                                      
                        ss+='&'
                ss+=r'\\'            
                print(ss,file=f)
            print(r'}$$\normalsize', file=f)


def wthmkE(dian,hmk=[],cdu=12):
    """Draw quiver ZQ for the given quiver oq[],fd for the parts divided,cdu for the columns in each parts
    """

    global sfP

    with open('txhmke.tex', 'a') as f:
        

        tta=time.time()
        print('Current date and time:',file=f)
        print(f'{time.ctime(tta)}',file=f)


        if sfP:
            print(len(hmk)/cdu) 
        
        for t in range(len(hmk)//cdu+1):
            print(r'\Tiny$$\xymatrix@C=0.3 cm@R=0.5 cm{', file=f)
            for i in range(dian-1):
                ss=''
                for j in range(cdu):
                    if t*cdu+j < len(hmk):
                        if i==2:
                            hvtt=hmk[(t*cdu+j)][dian-1]
                        hvt=hmk[(t*cdu+j)][i] 
                        
                        if sfP:
                            print(hvt)
                        if hvt['sdd']:
                            ss+=r'\stackrel{'
                            ss+=f'{hvt['hfv']}'
                            ss+=r'}{'
                            ss+=f'({hvt['orb']},{hvt['dis']})'
                            ss+=r'}'                  
                            if i > 0 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i-1]['sdd']: 
                                ss+=r'\ar[ur]'
                            if i< dian-2 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i+1]['sdd']:
                                ss+=r'\ar[dr]'  
                            if i== 2 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][dian-1]['sdd']:
                                ss+=r'\ar[r]'   
                        if i==2 and hvtt['sdd']:
                            ss+=r'\stackrel{'
                            ss+=f'{hvtt['hfv']}'
                            ss+=r'}{'
                            ss+=f'({hvtt['orb']},{hvtt['dis']})'
                            ss+=r'}'                  
                            if  t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][2]['sdd']: 
                                ss+=r'\ar[r]'
                                                      
                        ss+='&'
                ss+=r'\\'            
                print(ss,file=f)
            print(r'}$$\normalsize', file=f)


def addhmknew(hmksq,oq,dn,jdn,mmx):#
    """ add all the hammocks to get the Auslander-Reiten quiver
        of path algebra with quiver oq
        
        jdn the max length of the hammocks in hmksq,
        dn number of vertex of the quiver oq
        mmx maximal degree of the quiver oq

        0528get ride of the false terms

    """ 

    global sfP

    #dn=len(oq)-2    
    narq=[]
    t2=0 #=t
    for t in range(jdn+mmx):
        slicetm={}
        addTm=False
        for i in range(dn):
            postm=dict({'orb':i,'dis':t})
            sdd=False
            hfv=0
            dmv={}
            dmvv=0#added 0528 to find the socle of the injectives
            dmvc=mmx

            for i1 in range(dn):
                #dmv.append(hmksq[i1][t-oq[i1]][i]['hfv']) #moved here 0520

                if t>=oq[i1] and t-oq[i1]<len(hmksq[i1]):
                    sdd =(sdd or hmksq[i1][t-oq[i1]][i]['sdd']) 
                    hfv+=hmksq[i1][t-oq[i1]][i]['hfv']
                    dmv.update({i1:hmksq[i1][t-oq[i1]][i]['hfv']})
                    #from here 0520, to get full dmv 0522 changed to dict with vertex:component {i:dmv_i}
                    if oq[i1]<dmvc and hmksq[i1][t-oq[i1]][i]['hfv']!=0:
                        dmvc=oq[i1]
                        dmvv=i1
                postm.update({'sdd':sdd,'hfv':hfv,'dmv':dmv,'dmvv':dmvv,'len':t2})
                addTm=addTm or sdd
            slicetm.update({i:postm})
             
        if addTm:
            narq.append(slicetm)
            t2+=1

    return narq

def lastslice(arq):
    """ Get the last slice of an AR quiver

        Return a dict of {i:ls[i]}, ls[i] = last term in the orbit of i (the last slice) 
        and  a dict of {i:dmv}



        
    """
    ls={}
    lidx={}
    N=len(arq)-1
    doit=True
    for i in range(len(arq[0])):
        t=N
        while not arq[t][i]['sdd']:
            t-=1
        ls.update({i:t})
        lidx.update({i:arq[t][i]['dmv']})
    return {'lstslice':ls,'dmv':lidx}



def lastslicenew(arq):
    """ Get quiver for the companion fron the AR quiver of a path algebra

        Return a dict of {i:ls[i]}, ls[i] = last term in the orbit of i (the last slice) 
        and a quiver narq with the last slice removed 

        narq= the quiver of the companion

        (i:this[lstslice][i])=the removed term in narq
        this[idx][i]= dmv of (i:this[lstslice][i])
        this = the returned function 
        
    """

    global sfP

    ls={}
    idx={}
    N=len(arq)-1
    narq=arq
    doit=True
    for i in range(len(arq[0])):

        if sfP:
            print(i,len(arq[0]))
        
        t=N
        while not arq[t][i]['sdd']:
            t-=1
        ls.update({i:t})
        idx.update({i:arq[t][i]['dmv']})
        narq[t][i]['sdd']=False
    return {'lstslice':ls,'dmv':idx,'quiver':narq}


def getbslicen(arq,t,tp):
    """get the slice at t layer of AR-quiver of type tp
       return the quiver(s) in oq with vertex:degree
       list ddian of the vertices not in the quiver
       and the type ntp of the first component
       the other components are of type A   
    
    """

    oqs=[]
    oq={}
    idx={}
    xdi={}
    ddian=[]
    ntp='A'
    t1=0
    t2=0
    lss={}#vertex:number of cpt or 'no' vertex
    isDE=False
    if tp=='A':
        N=len(arq[t])
    else:
        N=len(arq[t])-1
    for i in range(N):

        if arq[t][i]['sdd']:
            if i==0 or not arq[t+1][i-1]['sdd']: #see if it is the first vertex 
                t1=0#应该用i1
                t2+=1#进入新分支后t2+1，在作为列表指标时应该-1
                if oq!={}:
                    oqs.append({'quiver':oq,'index':idx,'invind':xdi})
                    oq={}
                    idx={}
                    xdi={}
                if (tp=='D' and i==1) or (tp=='E' and i==2):
                    if  arq[t+1][N-1]['sdd']:
                        oq.update({t1:1})
                    
                        idx.update({t1:N-1})
                        xdi.update({N-1:t1})
                        lss.update({N-1:t2-1})
                        t1+=1
                    ntp='A'
            elif (tp=='D' and i==1) or (tp=='E' and i==2):
                isDE=True

            oq.update({t1:0})
            idx.update({t1:i})
            xdi.update({i:t1})
            lss.update({i:t2-1})
            t1+=1

        elif t+1<len(arq) and arq[t+1][i]['sdd']:
            if i==0 or not arq[t][i-1]['sdd']:
                t1=0
                if oq!={}:
                    oqs.append({'quiver':oq,'index':idx,'invind':xdi})
                    oq={}
                    idx={}
                    xdi={}
                t2+=1
                if (tp=='D' and i==1) or (tp=='E' and i==2):
                    if  arq[t][N-1]['sdd']:
                        oq.update({t1:0})
                    
                        idx.update({t1:N-1})
                        xdi.update({N-1:t1})
                        lss.update({N-1:t2-1})
                    t1+=1
                    ntp='A'
            elif (tp=='D' and i==1) or (tp=='E' and i==2):
                isDE=True

            oq.update({t1:1})
            idx.update({t1:i})
            xdi.update({i:t1})
            lss.update({i:t2-1})
            t1+=1 
        else:
            ddian.append(i)
            if isDE:
                if  arq[t][N-1]['sdd']:
                    oq.update({t1:0})                  

                
                    idx.update({t1:N-1})
                    xdi.update({N-1:t1})
                    lss.update({N-1:t2-1})
                    if tp=='E' and arq[t+1][0]['sdd']:
                        ntp=tp
                    else:
                        ntp='D'

                elif  arq[t+1][N-1]['sdd']:
                    oq.update({t1:1})
                
                    idx.update({t1:N-1})
                    xdi.update({N-1:t1})
                    lss.update({N-1:t2-1})
                    if tp=='E' and arq[t][0]['sdd']:
                        ntp=tp
                    else:
                        ntp='D'
                
                
                else:
                    ntp='A'
                    
                isDE=False
    
    if isDE:
        if  arq[t][N-1]['sdd']:
            oq.update({t1:0})
            idx.update({t1:N-1})
            xdi.update({N-1:t1})
            lss.update({N-1:t2-1})
            if tp=='E' and arq[t+1][0]['sdd']:
                ntp=tp
            else:
                ntp='D'
                    

        elif  arq[t+1][N-1]['sdd']:
            oq.update({t1:1})
            idx.update({t1:N-1})
            xdi.update({N-1:t1})
            lss.update({N-1:t2-1})
            if tp=='E' and arq[t][0]['sdd']:
                ntp=tp
            else:
                ntp='D'
        
        else:
            ntp='A'

    if oq!={}:
        oqs.append({'quiver':oq,'index':idx,'invind':xdi})


    return {'quivers':oqs,'ls':lss,'type':ntp,'novertices':ddian}
            

def getARq(dnn,cdun,tp,oq,mxdg):
    hmksq=[]
    dm=0
    if tp=='E':
        for i in range(dnn):
    
            hmksq.append(mkhmkE(dnn,i))
            
            if len(hmksq[i])>dm:
                dm = len(hmksq[i])
            wthmkE(dnn,hmksq[i],cdun)    
    elif tp=='D':
        for i in range(dnn):            
            hmksq.append(mkhmkD(dnn,i))
            if len(hmksq[i])>dm:
                dm = len(hmksq[i])
            wthmkE(dnn,hmksq[i],cdun)    
    elif tp=='A': 
        for i in range(dnn):            
            hmksq.append(mkhmkA(dnn,i)) 
            
            if len(hmksq[i])>dm:
                dm = len(hmksq[i])
            wthmkA(dnn,hmksq[i],cdun)    

    arq=addhmknew(hmksq,oq,dnn,dm,mxdg)
    if tp=='E':
        wthmkE(dnn,arq,cdun)
    elif tp=='D':
        wthmkD(dnn,arq,cdun)
    elif tp=='A':
        wthmkA(dnn,arq,cdun)
    return arq #返回型为tp，箭图为oq的路代数的AR箭图


def unitcmpt(ddn,slc1,cpts): #0619 修改作为前半部分的分支。后半部分每个分支应该同时开始见unitcmpt2
    """cpts: sequences of ar quivers with terms as a dict of 
       {'cmp':arq}
       arq: list of rows
       row: dict of {orbit:dic of vertex inf}
       dic of vertex inf: {'orb':轨道号,dist:列号,
       'sdd':是否顶点,'hfv':hmk函数值,'dmv':维数向量,'dmvv':顶点,'len':列号} 
    
    """

    global sfP

    h=open('txcnct.tex', 'a') #open the file for write 

    h.write(f'\n \n \nfor \n {slc1} \n with \n {cpts} \n')

    if len(cpts)==1 and slc1['novertices']==[]:#如果只有一个分支时，直接取该分支

        h.write(f'The whole component \n {cpts[0]['cmp']} \n')
        h.close()

        return cpts[0]['cmp']
    else:

        lcpt=0#找出分支的最大长度
        for t in range(len(cpts)):
            if lcpt<len(cpts[t]['cmp']):
                lcpt=len(cpts[t]['cmp'])

        tm=[]
        
        
        for t in range(lcpt):
            rowtm={}
            #if t==lcpt-2:
            #    inj={}

            for i in range(ddn):
                postm=dict({'orb':i,'dis':t})
                if i in slc1['novertices']:
                    
                   
                    sdd=False
                    hfv=0
                    dmv={}
                    dmvv=-1

                else:# i not in  slc1['novertices']:
                    i1=slc1['ls'][i]#i 所在分支指标
                    arqs=cpts[i1]['cmp']#取该分支（AR箭图）
                    i2=slc1['quivers'][i1]['invind'][i]#i 在分支中对应的指标
                    h.write(f'i: {i}, t: {t}, i1: {i1}, i2: {i2} \n')                    
                    
                    if sfP:
                        print(f'i: {i}, t: {t}, i1: {i1}, i2: {i2} \n')


                    
                    if t >= lcpt-len(arqs):#depends on t2 in getbislicen
                        t1=lcpt-len(arqs)#分支中的列数
                        sdd=arqs[t-t1][i2]['sdd']
                        hfv=arqs[t-t1][i2]['hfv']
                        dmv={}
                        for i3 in range(len(arqs[t-t1])): 
                           if i3 in  arqs[t-t1][i2]['dmv'].keys():
                               dmv.update({slc1['quivers'][i1]['index'][i3]:arqs[t-t1][i2]['dmv'][i3]})
                               
                             
                                   
                                   
                        

                        dmvv=arqs[t-t1][i2]['dmvv']
                        h.write(f'i: {i}, t: {t}, i1: {i1}, i2: {i2}, t-t1: {t-t1},\n  arqs[t-t1][i2]: \n {arqs[t-t1][i2]} \n')                    
                        
                        if sfP:
                            print(f'i: {i}, t: {t}, i1: {i1}, i2: {i2}, t-t1: {t-t1},\n  arqs[t-t1][i2]: \n {arqs[t-t1][i2]} \n')

                    else:

                        sdd=False
                        hfv=0
                        dmv={}
                        dmvv=-1
                
                    

                postm.update({'sdd':sdd,'hfv':hfv,'dmv':dmv,'dmvv':dmvv})
                rowtm.update({i:postm})
                h.write(f'i: {i}, t: {t}, postm:{postm}\n') 
            tm.append(rowtm)
            h.write(f'\n \n t: {i}, tm: \n {rowtm}\n') 
        
        h.write(f'\n \n The whole component\n tm:\n {tm} \n')
        h.close()
        return tm   
    
def unitcmpt2(ddn,slc1,cpts): #0619 修改只考虑后半部分，每个分支应该同时开始
    """cpts: sequences of ar quivers with terms as a dict of 
       {'cmp':arq}
       arq: list of rows
       row: dict of {orbit:dic of vertex inf}
       dic of vertex inf: {'orb':轨道号,dist:列号,
       'sdd':是否顶点,'hfv':hmk函数值,'dmv':维数向量,'dmvv':顶点,'len':列号} 
    
    """

    global sfP

    h=open('txcnct.tex', 'a') #open the file for write 

    h.write(f'\n \n \nfor \n {slc1} \n with \n {cpts} \n')

    #if len(cpts)==1 and slc1['novertices']==[]:#如果只有一个分支时，直接取该分支

    #    h.write(f'The whole component \n {cpts[0]['cmp']} \n')
    
    #    h.close()

    #    return cpts[0]['cmp']
    #else:

    lcpt=0
    for t in range(len(cpts)):
        if lcpt<len(cpts[t]['cmp']):
            lcpt=len(cpts[t]['cmp'])

    tm=[]
       
    for t in range(lcpt):
        rowtm={}
        #if t==lcpt-2:
        #    inj={}

        for i in range(ddn):
            postm=dict({'orb':i,'dis':t})
            if i in slc1['novertices']:
                sdd=False
                hfv=0
                dmv={}
                dmvv=-1

            else:# i not in  slc1['novertices']:
                i1=slc1['ls'][i]#i 所在分支指标
                arqs=cpts[i1]['cmp']#取该分支（AR箭图）
                i2=slc1['quivers'][i1]['invind'][i]#i 在分支中对应的指标
                h.write(f'i: {i}, t: {t}, i1: {i1}, i2: {i2} \n')                    
                
                if sfP:
                    print(f'i: {i}, t: {t}, i1: {i1}, i2: {i2} \n')
                    
                if t <len(arqs):#depends on t2 in getbislicen
                    #t1=lcpt-len(arqs)#分支中的列数
                    sdd=arqs[t][i2]['sdd']
                    hfv=arqs[t][i2]['hfv']
                    dmv={}
                    for i3 in range(len(arqs[t])): 
                       if i3 in  arqs[t][i2]['dmv'].keys():
                            dmv.update({slc1['quivers'][i1]['index'][i3]:arqs[t][i2]['dmv'][i3]})

                    dmvv=arqs[t][i2]['dmvv']
                    h.write(f'i: {i}, t: {t}, i1: {i1}, i2: {i2}, t: {t},\n  arqs[t][i2]: \n {arqs[t][i2]} \n')                    
                    
                    if sfP:
                        print(f'i: {i}, t: {t}, i1: {i1}, i2: {i2}, t: {t},\n  arqs[t][i2]: \n {arqs[t][i2]} \n')

                else:

                    sdd=False
                    hfv=0
                    dmv={}
                    dmvv=-1

            postm.update({'sdd':sdd,'hfv':hfv,'dmv':dmv,'dmvv':dmvv})
            rowtm.update({i:postm})
            h.write(f'i: {i}, t: {t}, postm:{postm}\n') 
        tm.append(rowtm)
        h.write(f'\n \n t: {i}, tm: \n {rowtm}\n') 
    
    h.write(f'\n \n The whole component\n tm:\n {tm} \n')
    h.close()
    return tm

def slcorq(dnn,slccn):
    orqq=[]
    for i in range(dnn): 
        if i in slccn['novertices']:
            orqq.append(-1)
        else:
            ii1=slccn['ls'][i]#i 所在分支下标
            ii2=slccn['quivers'][ii1]['invind'][i]#i 在分支中对应的顶点
            orqq.append(slccn['quivers'][ii1]['quiver'][ii2])
    return orqq     

def crdinj(ddn,orq,tm):
    """to find out the injectives of each orbit"""
    inj1={}
    if len(tm)>1:
        t=len(tm)-2
        for i in range(ddn):        
            for j in range(ddn):
                if j in tm[t][i]['dmv'].keys():
                    if  orq[j]==0 and  tm[t][i]['dmv'][j]!=0:
                        inj1.update({i:j})
    inj2={}
    t=len(tm)-1
    for i in range(ddn):
        for j in  range(ddn):
            if j in tm[t][i]['dmv'].keys():
                #if  orq[j]==1  and tm[t][i]['dmv'][j]!=0:
                if  tm[t][i]['dmv'][j]!=0:
                    inj2.update({i:j})
    return {'radinj':inj1,'simple':inj2}


def startpos(dnn,slccn,cpts):
    
    lcpt=0
    for t in range(len(cpts)):
        if lcpt<len(cpts[t]['cmp']):
            lcpt=len(cpts[t]['cmp'])
    stp={}
    for i in range(dnn):
        if i in slccn['novertices']:
            stp.update({i:-1})
        else:
            
            ii1=slccn['ls'][i]#i 所在分支下标
            ii2=slccn['quivers'][ii1]['invind'][i]#i 在分支中对应的顶点
            stp.update({i:slccn['quivers'][ii1]['quiver'][ii2]+lcpt-len(cpts[ii1]['cmp'])})#???
    return stp

def cntcmpsinfo(ddn,cmpseq):
    info={}
    t1=0
    ll=[]#长度序列

    lll=0
    lls=[]

    mpii0=[]

    #prjv={}#轨道终点对应的入射模指标序列
    #invpr={}
    
    ms=[] #找到不在所有分支的点记（作为list）
    for i in range(ddn):
        ms.append(i)

    for nt in range(len(cmpseq)):
        if len(cmpseq[nt]['slcinfo']['novertices'])<len(ms):
            ms=cmpseq[nt]['slcinfo']['novertices']

    primset=[]
    while cmpseq[t1]['slcinfo']['novertices']!=ms: #找到第一个完整切片
        ll.append(len(cmpseq[t1]['cmp']))          #ll[t]:第t个分支分支长度
        lll+=ll[t1]-1                              #总长度
        lls.append(lll)                            #lls[t]前面t个分支总长度
        prjtm={}             #将t0分支一个投射点对应的其轨道中的入射点对应顶点
        invprtm={}           #prjtm的逆映射
        for i in range(ddn):
            #if i in cmpseq[t1]['slcinfo']['novertices']:
                #pass #prjtm.append(-1)
            if i in cmpseq[t1]['radinj'].keys():

                prjtm.update({i:cmpseq[t1]['radinj'][i]})
                invprtm.update({cmpseq[t1]['radinj'][i]:i})
            
            elif i in cmpseq[t1]['simple']:
                prjtm.update({i:cmpseq[t1]['simple'][i]})                
                invprtm.update({cmpseq[t1]['simple'][i]:i})

        if t1>0:
            for ttt in range(t1):
                for i in range(ddn):
                    if i not in cmpseq[ttt]['slcinfo']['novertices']:
                        mpii0[ttt][i]=prjtm[mpii0[ttt][i]]

        mpii0.append(prjtm)

        #prjv.update({t1:prjtm})
        #invpr.update({t1:invprtm})
                        
        t1+=1

    t0=t1
    
    invmpii0=[]      
    for ttt in range(t1):
        invv={}
        for i in range(ddn):
            if i not in cmpseq[ttt]['slcinfo']['novertices']:
                invv.update({mpii0[ttt][i]:i})
        primset.append(invv.keys())
        invmpii0.append(invv)

    invv={}
    for i in range(ddn):
        invv.update({i:i})
    invmpii0.append(invv)#The i0 term
    
    info.update({'fullcmp':t0})

#    primset=[]
    invvv=set(range(ddn))
    primset.append(invvv)

    for t1 in range(t0,len(cmpseq)):        
        ll.append(len(cmpseq[t1]['cmp']))
        lll+=ll[t1]-1
        lls.append(lll)

        prjtm={}#将t0分支一个投射点对应的其轨道中的投射入射点对应顶点
        invprtm={}#prjitm的逆映射

        #prjstm={}#将t0分支一个投射点对应的其轨道中的单入射点对应顶点
        #invprstm={}#prjstm的逆映射
        for i in range(ddn):
            #if i in cmpseq[t1]['slcinfo']['novertices']:
                #prjtm.append(-1)
            if i in cmpseq[t1]['radinj'].keys():

                prjtm.update({i:cmpseq[t1]['radinj'][i]})
                invprtm.update({cmpseq[t1]['radinj'][i]:i})
            
            elif i in cmpseq[t1]['simple']:
                prjtm.update({i:cmpseq[t1]['simple'][i]})                
                invprtm.update({cmpseq[t1]['simple'][i]:i})
        
        #info.update({'injs':prjitm,'simpls':prjstm})

        invvv=invv
        invv={}
        for i in range(ddn):
            if i in invvv.keys() and invvv[i] in prjtm.keys():# cmpseq[ttt]['slcinfo']['novertices']:
                invv.update({i:prjtm[invvv[i]]})
            #if i in invvv.keys() and invvv[i] in prjtm.keys():# cmpseq[ttt]['slcinfo']['novertices']:
                #invv.update({i:prjtm[invvv[i]]})
        invmpii0.append(invv)
        primset.append(set(invv.keys()))        

        #prjv.update({t1:prjtm})
        #invpr.update({t1:invprtm})
    
    info.update({'mp':invmpii0,'preim':primset})
    """以i0为基准'mp'[t][i]为在第t个分支的投射模（关于标准slice的指标）
        'prim'为它们在i0分支的原像点集"""

    info.update({'totallen':lll,'tlfenduan':ll}) #,'protoinj':prjv,'injtopro':invpr})

    return info

def getcompanianquiver(qqv,tst=True):#0623 from companian, tst:write to the files input in ARqq
    
    global sfP

    tst1=False#write to files for debug
    if tst:
        tst2=True
    else:
        tst2=False
    #qqv
    tp=qqv['type']
    oq=qqv['qv']['quiver']
    dnn=qqv['qv']['vernm']
    mxdg=qqv['qv']['max']
    
    if tst1:
        f=open('txhmk.tex', 'w') #clear the file for write 
        f.close()
    
    if tst1:
        h=open('txcnct.tex', 'w') #clear the file for write 
        h.close()

    if tst1:
        g=open('tstcp.tex', 'w') #clear the file for write 

    dm=0
    hmksq=[]
    if tp=='E':
        for i in range(dnn):
            hmksq.append(mkhmkE(dnn,i))
            if len(hmksq[i])>dm:
                dm = len(hmksq[i])
            if tst1:
                wthmkE(dnn,hmksq[i],12)    

        arq=addhmknew(hmksq,oq,dnn,dm,mxdg)

        if tst1:
            wthmkE(dnn,arq,12)

    if tp=='D':
        for i in range(dnn):
            hmksq.append(mkhmkD(dnn,i))
            if len(hmksq[i])>dm:
                dm = len(hmksq[i])
            if tst1:
                wthmkD(dnn,hmksq[i],12)    

        arq=addhmknew(hmksq,oq,dnn,dm,mxdg)

        if tst2:
            wthmkD(dnn,arq,12)

    if tp=='A':
        for i in range(dnn):
            hmksq.append(mkhmkA(dnn,i))
            if len(hmksq[i])>dm:
                dm = len(hmksq[i])
            if tst1:#we don't need to write these hammocks
                wttrqA(dnn,hmksq[i],10,'txARqA.tex')    

        arq=addhmknew(hmksq,oq,dnn,dm,mxdg)

        if tst:
            wttrqAA(dnn,oq,arq,11,'txARqA.tex')
            
            #wttrqAA(dnn,arq,10,'txARqAd.tex',1)
    if sfP: 
        print('AR quiver')
        print(arq)

    return lastslicenew(arq)
    
def vertmorb(mspi,lpos,lst,uu):
    """mspi=lst[i]['ii']: i 行所在轨道的第一个投射模，
       lpos=lcol[i]:当前位置
       lst=lst[i]['st']: i 行轨道第一个出现的位置
       
       """
    ss=''
    if lpos-lst>0:
        ss+=r'\tau^{-'        
        ss+=f'{(lpos-lst)//2}'
        ss+=r'}'
    if lpos-lst>=0:    
            
        ss+=r'P_{('            
        ss+=f'{mspi},{uu}'
        ss+=r')}'
        #ss+=f'{uu}'
    return ss


def vertmpi(pi,ini,ui):#ui:=u[i],分离箭图的指标
    """write proj-inj
       
       """
    ss=''

    ss+=r'PI^{'        
    ss+=f'{pi},{ui+2}'#ui, the slice of the socle, counting from 1
    ss+=r'}_{'            
    ss+=f'-,{ui}'#-:ini the injective comes from which proj 
    ss+=r'}'
    return ss

def dmvtm(ddn,isPI,isSK,ver,hdmv,isRd=False,tp='A'):
    """ddn:顶点个数
       isPI：是否投射入射,
       isRd:hdmv是否其根的维数向量
       isSK：第二个顶点是否sink
       ver：如果是投射入射，投射顶,
       hdmv：维数向量
    """

    sss=r'\begin{array}{'
    if isPI:
        sss+='ccc'
    else:
        sss+='cc'
    sss+=r'}'


    if isSK:
        if isPI and not isRd:
            if ver==0:
                sss+='1&&'
            else:
                sss+='&&'
        else:
            sss+="&"
        ct=1
    else:
        ct=0

    for i in range(ddn):
        if ct==0:
            if isPI and not isRd: 
                #if i==ver or (ver<ddn-1 and i==ver+1) or (ver==ddn-1 and i==ver-1):
                if ver>0 and i==ver-1:
                    sss+='1'
                if i  in hdmv.keys():
                    sss+=f' & {hdmv[i]} &'
                else:
                    sss+=f' & 0 &'
                    #sss+=r'\\'                    
                #else:
                #    if i  in hdmv.keys():
                #        sss+=f'&{hdmv[i]} &'
                #    else:
                #        sss+=f'&0 &'
                    #sss+=r'\\'



            else:
                if i  in hdmv.keys():
                    sss+=f'{hdmv[i]} '
                    sss+=r'&'
                else:
                    sss+=r'0 &'


                if isPI and isRd:
                    if ver==ddn-1 and i==ver:
                        sss+=' 1'


            ct=1
        else:

            if isPI and isRd: 

                #if i==ver or (ver<ddn-1 and i==ver+1) or (ver==ddn-1 and i==ver-1):
                
                if i  in hdmv.keys():
                    sss+=f'{hdmv[i]} &'
                    if ver<ddn-1 and i==ver+1: #   if i  in hdmv.keys():
                        sss+=f'  1'
                
                else:
                    sss+=f'0 &'

            else:


                if i  in hdmv.keys():
                    sss+=f'{hdmv[i]} '
                else: 
                    sss+='0 '
            sss+=r'\\ '
            ct=0
     
       
        #i+=1
    sss+=r'\end{array}'

    return sss


def wtarq(ddn,tp,cntinfo,cmpseq,cdun,oq0,fV):

    global sfP

    sfDmv=True #to write the dimensional vector
    sfA=False #to write marks for positions:k-l-m-
    sfB=False #to write infos to file  

    tllen=cntinfo['totallen']+1#总列数
    lls=cntinfo['tlfenduan']#每一段长度
    blocknb=tllen//cdun+1 #总部分数
    f=open('txarq1.tex', 'w')
    
    if sfDmv:
        h=open('txarqdmv.tex', 'w')
    #h=open('txarqorb.tex', 'w')    
    if sfB:
        g=open('tstarq1.tex', 'w')

        g.write(f'{cntinfo}\n')
    #g.write(f'{cmpseq}')
    #g.close

    if tp=='D' or tp=='E':
        N=ddn-1
    else:
        N=ddn
    

    if tp=='D' or tp=='E':
        tptp=True
    else:
        tptp=False

    if tp=='D':
        node=1
    elif  tp=='E':
        node=2
    else:
        node=-1

    u1=0
    u=[]
    utt1=[]
    utta=0
    uttb=0
    for i in range(ddn):
        u.append(0)
        utt1.append(0)

    ull=cntinfo['tlfenduan']
    
    hmk=cmpseq 
    mpp=cntinfo['mp']
    preset=cntinfo['preim']

    #ptoi=cntinfo['injs']

    lst=[]#lst[i]='st'第i行开始位置 'ii'开始的顶点（i行是其轨道）'sf'第一出现与否（出现前为False）
    lcol=[]#lcol[i]第i行当前位置
    for i in range(ddn):
        lst.append({'ii':0, 'st':0,'sf':False,'ui':0})
        lcol.append(0)



    for t in range(blocknb):
    #    if u1>=len(ull):
    #        continue
        f.write(r'\Tiny$$\xymatrix@C=0.3 cm@R=0.5 cm{')
        if sfDmv:
            h.write(r'\Tiny$$\begin{array}{')
            for t2 in range(cdun+2):
                h.write('c')
            h.write(r'}')
            h.write('\n')

            for t2 in range(cdun+2):#标记列号
                if t2>0 and u1<=len(hmk):
                    h.write('&')
                    h.write(f'{t2}')
            h.write(r'\\')
            h.write('\n')

        ss=f'{t}:'

        if sfDmv:
            sss=''

        ut1=utta
        for t1 in range(cdun):#reserved for write informations of the slice
            if t1>0:
                ss=f'{t1}'

            if sfDmv:
                sss=''

            if ut1==ull[u1]-1:
                u1+=1
                ut1=0
                ss+=f',{u1}'
                if tp=='D' and  node in preset[u1-1]:#对'D'型。node的投射入射放在这里
                    hvtm=hmk[u1-1]['cmp'][lls[u1-1]-2][mpp[u1-1][node]]
                    miv=mpp[u1-1][node]+1 
                    mpv=mpp[u1][node]+1                   
                    if  hvtm['sdd']: 
                        ss+=vertmpi(mpv,miv,u1)    
                        ss+=r'\ar[ddr]'

                        if sfDmv:                            
                            if (u1+oq0)%2==1:
                                isSS=True
                            else:
                                isSS=False
                            sss+=vertmpi(mpv,miv,u1)  
                            sss+='='   
                            sss+=dmvtm(ddn,True,isSS,mpv-1,hvtm['dmv']) 
                            #sss+=r'\ar[ddr]'
            #elif u1>0:
            #    ut1=t*cdun+t1-ull[u1-1]
            #else:
            #    ut1=t*cdun+t1

            f.write(ss)
            f.write(r'&')

            if sfDmv:
                sss+=r'&'
                h.write(sss)
         
            ut1+=1
        f.write(rf'{cdun} &\\')
        
        if sfDmv:
            h.write(r'\\')
        
        utta=ut1

        ss=''
        if sfDmv:
            sss=''
        ut1=uttb
        for t1 in range(cdun):#reserved for write informations of the slice
            ss=''
            if sfDmv:
                sss=''
            if ut1==ull[u1]-1:
                u1+=1
                ut1=0
                if tp=='E' and  node in preset[u1-1]:#对'E'型。node的投射入射放在这里
                    hvtm=hmk[u1-1]['cmp'][lls[u1-1]-2][mpp[u1-1][node]]
                    miv=mpp[u1-1][node]+1
                    mpv=mpp[u1][node]+1
                    if  hvtm['sdd']:                           
                        ss+=vertmpi(mpv,miv,u1) 
                        ss+=r'\ar[ddr]'

                        if sfDmv:                             
                            if (u1+oq0)%2==1:
                                isSS=True
                            else:
                                isSS=False
                            sss+=vertmpi(mpv,miv,u1) 
                            sss+='='
                            sss+=dmvtm(ddn,True,isSS,mpv-1,hvtm['dmv']) 
                            #sss+=r'\ar[ddr]'


            #elif u1>0:
            #    ut1=t*cdun+t1-ull[u1-1]
            #else:
            #    ut1=t*cdun+t1
            ss+=r'&'
            f.write(ss)
            if sfDmv:
                sss+='&'
                h.write(sss)


            ut1+=1
        f.write(r'\\')
        f.write('\n')
        if sfDmv:
            h.write(r'\\')
            h.write('\n')
        uttb=ut1


        for i in range(N):
            ss=''
            if sfDmv:
                sss=''
            if i in preset[u[i]]:
                ui=mpp[u[i]][i]
            ut1=utt1[i]
            for t1 in range(cdun):#reserved for write the proj-inj for type D and E
                if  ut1>=ull[u[i]]-1: #(u[i]==0 and) or u[i]>0 and  t*cdun+t1==ull[u[i]-1]:
                    u[i]+=1
                    ut1=0
                    if u[i]>=len(ull):
                        break
                    if i in preset[u[i]]:
                        ui=mpp[u[i]][i]
                #elif u[i]>0: 
                #    ut1=t*cdun+t1-ull[u[i]-1]
                #else:
                #    ut1=t*cdun+t1

                #tmseq=cmpseq[u[i]]['cmp'][ut1][i]

                #g.write(vertmbinfo(tmseq,cntinfo,t,t1,ut1,i,u)) 

                if ull[u[i]]>1 and ut1==ull[u[i]]-1:
                    ss+=''


                elif ut1<ull[u[i]] and i in preset[u[i]]:
                    hvt=hmk[u[i]]['cmp'][ut1][ui]
                    mpv=ui+1 
                    if sfB:
                        if u[i]>=len(ull)-3:#for test                        
                            g.write(f'~~{ull[u[i]]}:{hvt['sdd']}')
                                             
                    if sfA:
                        f.write('k')#for test
                    #ss+=vertm(hvt,mpv,u[i],ut1)    
                    if hvt['sdd']:
                        if not lst[i]['sf']:
                            lst[i]['st']=lcol[i]
                            lst[i]['ii']=mpv
                            lst[i]['ui']=u[i]
                            lst[i]['sf']=True
                        ss+=vertmorb(lst[i]['ii'],lcol[i],lst[i]['st'],fV[lst[i]['ii']-1]) 
                        #oqq[i]=0如果i在lst[i]['ui]切片中为source否则为0

                        if sfA:                        
                            f.write('-')#for test

                        if sfDmv: 
                            if (u[i]+oq0)%2==1:
                                isSS=True
                            else:
                                isSS=False
                            sss+=vertmorb(lst[i]['ii'],lcol[i],lst[i]['st'],u[i])
                            sss+='='
                            sss+=dmvtm(ddn,False,isSS,mpv,hvt['dmv']) 
                            

                        if (i > 0 and t*cdun+t1+1 < tllen and i-1 in preset[u[i]] 
                            and ut1+1<ull[u[i]] and
                            hmk[u[i]]['cmp'][ut1+1][mpp[u[i]][i-1]]['sdd']): 
                            ss+=r'\ar[ur]'
                            #if sfDmv: 
                            #    sss+=r'\ar[ur]'
                        if (i< N-1 and t*cdun+t1+1 < tllen and i+1 in preset[u[i]] and
                            ut1+1<ull[u[i]] and 
                            hmk[u[i]]['cmp'][ut1+1][mpp[u[i]][i+1]]['sdd']):
                            ss+=r'\ar[dr]' 
                            #if sfDmv: 
                            #    sss+=r'\ar[dr]'
                        
                        if (i== node and t*cdun+t1+1 < tllen and N in preset[u[i]] and 
                            hmk[u[i]]['cmp'][ut1+1][mpp[u[i]][N]]['sdd']):
                            ss+=r'\ar[r]' 
                            #if sfDmv: 
                            #    sss+=r'\ar[r]'  

                    if ut1==ull[u[i]]-2:

                        if sfA:                        
                            f.write('m')#for test

                        if i in preset[u[i]] and i in preset[u[i]+1]:
                            hvtt=hmk[u[i]]['cmp'][ut1][ui]
                            if ull[u[i]+1]>1:
                                 hvttn=hmk[u[i]+1]['cmp'][1][mpp[u[i]+1][i]]
                            #mpv=ui+1
                            #ss+=vertm(hvtt,mpv,'PI',ut1)
                            if  ull[u[i]+1]>1 and  hvtt['sdd'] and hvttn['sdd']: 
                                

                                if sfA:     
                                    f.write('-')
                                if i==node:

                                    ss+=r'\ar[uur]'
                                    #if sfDmv: 
                                    #     sss+=r'\ar[uur]'
                                else:        
                                    ss+=r'\ar[r]'
                                    #if sfDmv: 
                                    #     sss+=r'\ar[r]'

                    if ut1==0:
                        
                        if i!=node and u[i]>0 and lls[u[i]-1]>2 and  i in preset[u[i]-1] and i in preset[u[i]] :
                            hvtm=hmk[u[i]-1]['cmp'][lls[u[i]-1]-2][mpp[u[i]-1][i]]
                            if lls[u[i]]>1:
                                hvtmn=hmk[u[i]]['cmp'][1][mpp[u[i]][i]]

                                if sfA: 
                                    f.write('l')#for test

                                if sfB:
                                    if ui>len(ull)-3:#for test
                                        g.write(f'\n {hmk[u[i]]}\n{hmk[u[i]-1]}\n') 
                                
                                if hvtmn['sdd']:                          
                                    miv=mpp[u[i]-1][i]+1
                                    mpv=mpp[u[i]][i]+1
                                    if  hvtm['sdd']:
                                        ss+=vertmpi(mpv,miv,u[i])

                                    if sfDmv: 
                                        if (u[i]+oq0)%2==1:
                                            isSS=True
                                        else:
                                            isSS=False
                                        
                                        if  hvtm['sdd']:
                                            sss+=vertmpi(mpv,miv,u[i])
                                            sss+='='
                                            sss+=dmvtm(ddn,True,isSS,mpv-1,hvtmn['dmv'])

                                    if sfA: 
                                        f.write('-')#for test

                                    if hvtm['sdd']:
                                        ss+=r'\ar[r]'
                                        #if sfDmv:
                                        #    sss+=r'\ar[r]'


                    if tptp and i==node:
                        if N in preset[u[i]]:
                            hvtt=hmk[u[i]]['cmp'][ut1][mpp[u[i]][N]]
                            mpv=mpp[u[i]][N]+1

                            if  hvtt['sdd']:
                                
                                if not lst[N]['sf']:
                                    lst[N]['st']=lcol[i]
                                    lst[N]['ii']=mpv
                                    lst[N]['ui']=u[i]
                                    lst[N]['sf']=True
                                ss+=vertmorb(lst[N]['ii'],lst[N]['st'],lcol[N])     

                                
                                if sfDmv: 
                                    if (u[i]+oq0)%2==1:
                                        isSS=True
                                    else:
                                        isSS=False
                                    sss+=vertmorb(lst[N]['ii'],lst[N]['st'],lcol[N])
                                    sss+='='
                                    sss+=dmvtm(ddn,False,isSS,mpv,hvtt['dmv']) 

                                if  t*cdun+t1+1 < tllen and hmk[u[i]]['cmp'][ut1+1][ui]['sdd']: 
                                    ss+=r'\ar[r]'
                                    #if sfDmv:
                                    #    sss+=r'\ar[r]'
                        
                    
                
                #elif :
                if sfB:
                    g.write(f'({i},{lcol[i]},{lst[i]['st']}), [{u[i]},{ut1} ],{mpp[u[i]].get(i)}& ')

                lcol[i]+=1
                if i==node:
                    lcol[N]+1
                ss+='&'
                if sfDmv:
                    sss+='&'
                ut1+=1
                #if ut1>=ull[u[i]]-1:
                #    ut1=ull[u[i]]-1
            ss+=r'\\'  
            ss+='\n'

            if sfDmv:
                sss+=r'\\'
                sss+='\n'

            if sfB:
                g.write('\n') 

            f.write(f"{i}")# 标记行号 
            f.write("&")

            f.write(ss)

            if sfDmv:
                h.write(f"{i}")# 标记行号 
                h.write("&")

                h.write(sss)
            
            utt1[i]=ut1
            

        f.write(r'}$$\normalsize')
        if sfDmv:
            h.write(r'\end{array}$$\normalsize')

        if sfB:
            g.write('\n \n') 
    if sfB:
        g.write(f'{lst}')
        g.close()

    f.close()
    return


def wttrqA(dian,hmk=[],cdu=10,fname='txtrq.tex',sfT=False):#revised from wthmk, 0621
    """Draw translation quiver given by hmk
    """

    global sfP

    firstV=[]
    isFF=[]
    for i in range(dian):
        isFF.append(False)

    sfS=False 
    with open(fname, 'w') as f:
        if sfS:
            tta=time.time()
            print('Current date and time:',file=f)
            print(f'{time.ctime(tta)}',file=f)

        if sfP:
            print(len(hmk)/cdu) 
        for t in range(len(hmk)//cdu+1):
            print(r'\Tiny$$\xymatrix@C=0.5 cm@R=0.5 cm{', file=f)
            for i in range(dian):
                ss=''
                for j in range(cdu):
                    if t*cdu+j < len(hmk):
                        hvt=hmk[(t*cdu+j)][i] 
                        
                        if sfP:
                            print(hvt)
                        
                        if hvt['sdd']:
                            #ss+=r'\stackrel{'
                            #ss+=f'{hvt['hfv']}'
                            #ss+=r'}{'
                            ss+=f'({hvt['orb']+1},{hvt['dis']})'
                            #ss+=r'}'
                            if not isFF[i]:
                                firstV.append(hvt['dis'])
                                isFF[i]=True


                            if i > 0 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i-1]['sdd']: 
                                ss+=r'\ar@{<-}[ur]'
                            if i< dian-1 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i+1]['sdd']:
                                ss+=r'\ar@{<-}[dr]'                                  
                        ss+='&'
                ss+=r'\\'            
                print(ss,file=f)
            print(r'}$$\normalsize', file=f)
    return firstV

   
def wttrqAA(dian,oq,hmk=[],cdu=10,fname='txtrq.tex',sfT=2):#revised from wthmk, 0621
    """Draw translation quiver given by hmk
    sfT =0:     write dimension,
        =1:     write dimensionalvector
        =other: write as \tau^{-t} P_i
    """

    global sfP

    sfS=False 
    with open(fname, 'w') as f:
        if sfS:
            tta=time.time()
            print('Current date and time:',file=f)
            print(f'{time.ctime(tta)}',file=f)

        if sfP:
            print(len(hmk)/cdu) 
        for t in range(len(hmk)//cdu+1):
            print(r'\Tiny$$\xymatrix@C=0.5 cm@R=0.5 cm{', file=f)
            for i in range(dian):
                ss=''
                for j in range(cdu):
                    if t*cdu+j < len(hmk):
                        hvt=hmk[(t*cdu+j)][i]

                        if sfP:
                            print(hvt)
                        
                        if hvt['sdd']:
                            if sfT==0:
                                ss+=f'{hvt['hfv']}'
                            elif sfT==1:
                                for i1 in range(dian):
                                    if i1 in hvt['dmv'].keys():
                                        ss+=f'{hvt['dmv'][i1]}'
                                    else:
                                        ss+='0'
                                    if i1<dian-1:
                                        ss+=','
                            else:
                                if hvt['dis']-oq[i]>0:
                                    ss+=r'\tau^{-'
                                    ss+=f'{(hvt['dis']-oq[i])//2}'
                                    ss+=r'}'

                                ss+=r'P_{'
                                ss+=f'{hvt['orb']+1}'
                                ss+=r'}'
                            

                            if i > 0 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i-1]['sdd']: 
                                ss+=r'\ar[ur]'
                            if i< dian-1 and t*cdu+j+1 < len(hmk) and hmk[(t*cdu+j+1)][i+1]['sdd']:
                                ss+=r'\ar[dr]'                                  
                        ss+='&'
                ss+=r'\\'            
                print(ss,file=f)
            print(r'}$$\normalsize', file=f)

def arqcA(cdun,sfC,sfD):    #revise 0621 sfC:write on screen,sfD:write on files
    qqv=getqvA()
    tp='A'
    oq=qqv['quiver']
    dnn=qqv['vernm']
    mxdg=qqv['max']
    wtqvgr(dnn,oq,'A')#added 0623

    qqvv={'type':tp,'qv': {'quiver':oq,'vernm':dnn,'max':mxdg}}

    oq00=oq[0]#0的次数，用于确定维数向量定位


    cpqs=getcompanianquiver(qqvv) #replace the code of getcompanianquiver()
    
    fstV=wttrqA(dnn,cpqs['quiver'],11,'txcq1')#added 0621
    print(fstV)



    if sfD:
        f=open('txhmk.tex', 'w') #clear the file for write 
        f.close()
    
        h=open('txcnct.tex', 'w') #clear the file for write 
        h.close()

        g=open('tstcp.tex', 'w') #clear the file for write 


    if sfC:
        print('the companian quiver')
        print(cpqs)
    
    if sfD:
        wthmkA(dnn,cpqs['quiver'],cdun)#under sfD, 0621

    cmpseq={}   
    isFstHlf=True
    for t in range(len(cpqs['quiver'])):
        #slcc=getbslice(cpqs['quiver'],t,tp)
        #print(t)
        #print(slcc) 
        
    
        slccn=getbslicen(cpqs['quiver'],t,tp)
        
        if sfC:
            print('getbislicen')
            print(slccn) 
         
        cpts=[]
        istypecpt=True

        for t1 in range(len(slccn['quivers'])):
            if t1==0 and len(slccn['quivers'][t1]['quiver'])==1:
                arqcpt=([{0:{'orb':0,'dis':0,'sdd':True,'hfv':1,'dmv':{0:1},'dmvv':0}}])
                lcpt=({'lstslice':{0,0},'dmv':{0:{0:1}}})


                if sfD:
                    g.write(f'the {t}th algebra,{t1} the component')               
                    g.write(f'{arqcpt}')
                    g.write(f'{lcpt}')

            elif istypecpt and len(slccn['quivers'][t1]['quiver'])>2:
                arqcpt=getARq(len(slccn['quivers'][t1]['quiver']),cdun,slccn['type'],slccn['quivers'][t1]['quiver'],1)
                lcpt=lastslice(arqcpt)
                istypecpt=False
           
                if sfD:
                    g.write(f'\n the {t}th algebra,{t1} the component,typed component\n') 

                    g.write(f'{arqcpt} \n ')
                    g.write(f'{lcpt} \n')

            else:
                arqcpt=getARq(len(slccn['quivers'][t1]['quiver']),cdun,'A',slccn['quivers'][t1]['quiver'],1) 
                
                if sfC:
                    print(f'{arqcpt}')
                
                if arqcpt!=[]:
                    lcpt=lastslice(arqcpt)
              
                if sfD:
                    g.write(f'\n the {t}th algebra,{t1} the component\n')              
                    g.write(f'{arqcpt} \n')
                    g.write(f'{lcpt} \n')


            if sfD:
                g.write(f'\n the {t}th algebra \n')                
                #g.write(f'{slcc} \n')
                g.write(f'{slccn} \n')   
             
            cpts.append({'cmp':arqcpt,'lss':lcpt}) 

            if sfD:
                g.write(f'\n cpts \n')            
                g.write(f'{cpts} \n')  

        if  len(cpts)==1 and slccn['novertices']==[]:#如果只有一个分支时，直接取该分支

            acntcpt=cpts[0]['cmp']
            if  isFstHlf:
                isFstHlf=False 
        if isFstHlf:
            acntcpt=unitcmpt(dnn,slccn,cpts)
        else:
            acntcpt=unitcmpt2(dnn,slccn,cpts)
       

        if sfD:
            g.write(f'\n acntcpt \n')
            g.write(f'{acntcpt} \n')

        if acntcpt!=[]:        
            orqq=slcorq(dnn,slccn)

        if len(acntcpt)>0:
            rdinj=crdinj(dnn,orqq,acntcpt)
            startp=startpos(dnn,slccn,cpts)

            cmptm={'cmp':acntcpt,'slcinfo':slccn,'startinfo':startp}

            cmptm.update(rdinj)
        
        #if len(cmptm)>0:
            cmpseq.update({t:cmptm})


        if sfD:
            g.write(f'\n slccn\n {slccn} \n')   
            g.write(f'\n orqq:\n  {orqq} \n')
            g.write(f'\n rdinj:\n  {rdinj} \n')        
            g.write(f'\n startpos:\n  {startp} \n')
            
            
    cmpinfo=cntcmpsinfo(dnn,cmpseq)

    wtarq(dnn,tp,cmpinfo,cmpseq,cdun,oq00,fstV)



    

    if sfD:
        g.close()


if __name__ == "__main__":
    dnn=5
    vt=2
    cdun=8

    sfC=False
    sfD=False
    headf()
    arqcA(cdun,sfC,sfD)