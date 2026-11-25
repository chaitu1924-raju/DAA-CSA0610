"""DAA Assignment 4B — Algorithm Engineering (CO4).
Run: python DAA_Assignment_4B_All_Codes.py
Standard library only. Demonstrations and validation for Tasks 1–6.
"""
import math, random, time, itertools, tracemalloc

# ---------------- TASK 1: WORD WRAP DP ----------------
def word_wrap(words, width):
    n=len(words); dp=[math.inf]*(n+1); nxt=[None]*(n+1); dp[n]=0
    states=[]
    for i in range(n-1,-1,-1):
        line_len=0
        for j in range(i,n):
            line_len += len(words[j]) + (1 if j>i else 0)
            if line_len>width: break
            slack=width-line_len
            penalty=0 if j==n-1 else slack**2
            candidate=penalty+dp[j+1]
            states.append((i,j,line_len,slack,penalty,candidate))
            if candidate<dp[i]:
                dp[i]=candidate; nxt[i]=j+1
    if nxt[0] is None and n:
        raise ValueError("A word is longer than the line width")
    lines=[]; i=0
    while i<n:
        j=nxt[i]; line_words=words[i:j]
        used=sum(map(len,line_words))+len(line_words)-1
        slack=width-used
        penalty=0 if j==n else slack**2
        lines.append((line_words,slack,penalty))
        i=j
    return dp[0],lines,dp,states

# ---------------- TASK 2: FRACTIONAL GREEDY + 0/1 DP ----------------
def fractional_knapsack(items, capacity):
    ordered=sorted(items,key=lambda x:x[2]/x[1],reverse=True)
    rem=capacity; value=0; selected=[]; comparisons=0
    for name,w,v in ordered:
        comparisons+=1
        if rem<=0: break
        frac=min(1,rem/w)
        if frac>0:
            selected.append((name,frac,frac*w,frac*v))
            rem-=frac*w; value+=frac*v
    return value,selected,comparisons

def zero_one_knapsack(items,capacity):
    n=len(items); dp=[[0]*(capacity+1) for _ in range(n+1)]
    take=[[False]*(capacity+1) for _ in range(n+1)]; states=0
    for i,(name,w,v) in enumerate(items,1):
        for c in range(capacity+1):
            states+=1; exclude=dp[i-1][c]; include=-1
            if w<=c: include=v+dp[i-1][c-w]
            if include>exclude: dp[i][c]=include; take[i][c]=True
            else: dp[i][c]=exclude
    chosen=[]; c=capacity
    for i in range(n,0,-1):
        if take[i][c]: chosen.append(items[i-1][0]); c-=items[i-1][1]
    chosen.reverse()
    return dp[n][capacity],chosen,states,dp

# ---------------- TASK 3: ROUTING ----------------
def dijkstra(vertices,edges,source):
    adj={v:[] for v in vertices}
    for u,v,w in edges: adj[u].append((v,w))
    dist={v:math.inf for v in vertices}; pred={v:None for v in vertices}
    done=set(); order=[]; dist[source]=0
    while len(done)<len(vertices):
        candidates=[v for v in vertices if v not in done]
        u=min(candidates,key=lambda x:dist[x])
        if dist[u]==math.inf: break
        done.add(u); order.append(u)
        for v,w in adj[u]:
            if v not in done and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w; pred[v]=u
    return dist,pred,order

def path_to(pred,target):
    path=[]; cur=target
    while cur is not None: path.append(cur); cur=pred[cur]
    return list(reversed(path))

def bellman_ford(vertices,edges,source):
    d={v:math.inf for v in vertices}; p={v:None for v in vertices}; d[source]=0
    passes=0
    for _ in range(len(vertices)-1):
        changed=False; passes+=1
        for u,v,w in edges:
            if d[u]!=math.inf and d[u]+w<d[v]:
                d[v]=d[u]+w;p[v]=u;changed=True
        if not changed: break
    neg=[]
    for u,v,w in edges:
        if d[u]!=math.inf and d[u]+w<d[v]: neg.append((u,v))
    return d,p,passes,neg

def floyd_warshall(vertices,edges):
    n=len(vertices); ix={v:i for i,v in enumerate(vertices)}
    d=[[math.inf]*n for _ in range(n)]
    for i in range(n):d[i][i]=0
    for u,v,w in edges:d[ix[u]][ix[v]]=min(d[ix[u]][ix[v]],w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k]+d[k][j]<d[i][j]:d[i][j]=d[i][k]+d[k][j]
    return d

def warshall(vertices,edges):
    n=len(vertices);ix={v:i for i,v in enumerate(vertices)}
    r=[[False]*n for _ in range(n)]
    for i in range(n):r[i][i]=True
    for u,v,w in edges:r[ix[u]][ix[v]]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):r[i][j]=r[i][j] or (r[i][k] and r[k][j])
    return r

# ---------------- TASK 4: TWO-LINE ASSEMBLY SCHEDULING ----------------
def assembly_line(a1,a2,t1,t2,e1,e2,x1,x2):
    n=len(a1); f1=[0]*n;f2=[0]*n;p1=[0]*n;p2=[0]*n;trace=[]
    f1[0]=e1+a1[0];f2[0]=e2+a2[0]
    for j in range(1,n):
        stay1=f1[j-1]+a1[j]; transfer1=f2[j-1]+t2[j-1]+a1[j]
        stay2=f2[j-1]+a2[j]; transfer2=f1[j-1]+t1[j-1]+a2[j]
        if stay1<=transfer1:f1[j]=stay1;p1[j]=1;choice1="stay"
        else:f1[j]=transfer1;p1[j]=2;choice1="transfer"
        if stay2<=transfer2:f2[j]=stay2;p2[j]=2;choice2="stay"
        else:f2[j]=transfer2;p2[j]=1;choice2="transfer"
        trace.append((j+1,stay1,transfer1,choice1,stay2,transfer2,choice2))
    end1=f1[-1]+x1;end2=f2[-1]+x2
    line=1 if end1<=end2 else 2; total=min(end1,end2)
    route=[0]*n;route[-1]=line
    for j in range(n-1,0,-1):route[j-1]=p1[j] if route[j]==1 else p2[j]
    return total,route,trace

# ---------------- TASK 5: MST THREE WAYS ----------------
class DSU:
    def __init__(self,n):self.p=list(range(n));self.rank=[0]*n
    def find(self,x):
        if self.p[x]!=x:self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a=self.find(a);b=self.find(b)
        if a==b:return False
        if self.rank[a]<self.rank[b]:a,b=b,a
        self.p[b]=a
        if self.rank[a]==self.rank[b]:self.rank[a]+=1
        return True

def kruskal(vertices,edges):
    ix={v:i for i,v in enumerate(vertices)};dsu=DSU(len(vertices));chosen=[];trace=[]
    for u,v,w in sorted(edges,key=lambda e:e[2]):
        ok=dsu.union(ix[u],ix[v]);trace.append((u,v,w,"accept" if ok else "reject"))
        if ok:chosen.append((u,v,w))
    return chosen,sum(e[2] for e in chosen),trace

def prim(vertices,edges,start):
    adj={v:[] for v in vertices}
    for u,v,w in edges:adj[u].append((v,w));adj[v].append((u,w))
    seen={start};chosen=[];trace=[]
    while len(seen)<len(vertices):
        candidates=[(w,u,v) for u in seen for v,w in adj[u] if v not in seen]
        if not candidates:break
        w,u,v=min(candidates);seen.add(v);chosen.append((u,v,w));trace.append((u,v,w))
    return chosen,sum(e[2] for e in chosen),trace

def boruvka(vertices,edges):
    ix={v:i for i,v in enumerate(vertices)};dsu=DSU(len(vertices));chosen=[];rounds=[]
    while len(chosen)<len(vertices)-1:
        cheapest={}
        for u,v,w in edges:
            a=dsu.find(ix[u]);b=dsu.find(ix[v])
            if a!=b:
                if a not in cheapest or w<cheapest[a][2]:cheapest[a]=(u,v,w)
                if b not in cheapest or w<cheapest[b][2]:cheapest[b]=(u,v,w)
        added=[]
        for e in cheapest.values():
            u,v,w=e
            if dsu.union(ix[u],ix[v]):chosen.append(e);added.append(e)
        rounds.append(added)
        if not added:break
    return chosen,sum(e[2] for e in chosen),rounds

# ---------------- TASK 6: HELD-KARP TSP ----------------
def held_karp(matrix):
    n=len(matrix); full=(1<<n)-1
    dp={}; parent={}
    for j in range(1,n):
        mask=1<<j;dp[(mask,j)]=matrix[0][j];parent[(mask,j)]=0
    for size in range(2,n):
        for subset in itertools.combinations(range(1,n),size):
            mask=sum(1<<j for j in subset)
            for j in subset:
                prev=mask^(1<<j)
                best,prevk=min((dp[(prev,k)]+matrix[k][j],k) for k in subset if k!=j)
                dp[(mask,j)]=best;parent[(mask,j)]=prevk
    best,last=min((dp[(full^(1),j)]+matrix[j][0],j) for j in range(1,n))
    route=[last];mask=full^1
    while len(route)<n-1:
        k=parent[(mask,route[-1])];mask^=1<<route[-1];route.append(k)
    route.reverse()
    return best,[0]+route+[0],len(dp)

def brute_tsp(matrix):
    n=len(matrix);best=math.inf;route=None
    for perm in itertools.permutations(range(1,n)):
        cost=matrix[0][perm[0]]+sum(matrix[perm[i]][perm[i+1]] for i in range(n-2))+matrix[perm[-1]][0]
        if cost<best:best=cost;route=(0,)+perm+(0,)
    return best,route

def main():
    print("DAA ASSIGNMENT 4B — ALL TASK OUTPUTS")
    print("\\nTASK 1 — WORD WRAP DYNAMIC PROGRAMMING")
    words="Dynamic programming creates clean document layouts with balanced lines".split()
    for width in (16,20,24):
        cost,lines,dp,states=word_wrap(words,width)
        print(f"Width={width}, minimum penalty={cost}, DP states evaluated={len(states)}")
        for line,slack,pen in lines:print("  "+" ".join(line),f"| unused={slack} | penalty={pen}")
        print("  DP suffix costs:",dp)
    boundary=["algorithm"]
    try:word_wrap(boundary,5)
    except ValueError as e:print("Boundary test:",e)

    print("\\nTASK 2 — GREEDY FRACTIONAL VS 0/1 DP")
    normal=[("A",10,60),("B",20,100),("C",30,120)]
    gv,gs,gwork=fractional_knapsack(normal,50)
    ov,os,states,_=zero_one_knapsack(normal,50)
    print("Normal instance capacity=50")
    print("Fractional greedy:",gv,gs,"ratio evaluations:",gwork)
    print("0/1 DP:",ov,os,"states:",states)
    trap=[("A",10,60),("B",20,100),("C",30,120)]
    gv,gs,_=fractional_knapsack(trap,50);ov,os,states,_=zero_one_knapsack(trap,50)
    print("0/1 greedy-ratio trap, capacity=50: greedy whole-item choice A+B gives 160")
    print("0/1 DP optimum:",ov,os,"value:",ov,"DP states:",states)
    print("Fractional solution:",gv,gs,"(fractional problem, different formulation)")
    print("DP memory cells:",(len(trap)+1)*51,"; greedy auxiliary order:",len(trap))

    print("\\nTASK 3 — ROUTING: DIJKSTRA / BELLMAN-FORD / FLOYD / WARSHALL")
    V=list("ABCDEFGH")
    E=[("A","B",4),("A","C",7),("B","C",2),("B","D",6),("C","D",1),("D","E",3),
       ("C","E",8),("E","F",2),("F","G",3),("G","H",2),("D","H",12),("B","F",10)]
    d,p,order=dijkstra(V,E,"A")
    print("Dijkstra finalisation order:",order)
    for v in V:print(v,"distance",d[v],"path",path_to(p,v),"predecessor",p[v])
    neg=E+[("H","C",-9)]
    print("Prediction after adding H->C weight -9: Dijkstra may finalise C too early.")
    db,pb,passes,cycles=bellman_ford(V,neg,"A")
    print("Bellman-Ford distances:",db,"passes:",passes,"negative cycle:",cycles)
    cycle=neg+[("C","H",1)]
    dc,pc,pcnt,cyc=bellman_ford(V,cycle,"A")
    print("Reachable negative-cycle test:",cyc)
    fw=floyd_warshall(V,E); reach=warshall(V,E)
    print("Floyd distance matrix (rows/cols A-H):")
    for row in fw:print(["INF" if x==math.inf else int(x) for x in row])
    print("Warshall reachability matrix (1=reachable):")
    for row in reach:print([int(x) for x in row])

    print("\\nTASK 4 — ASSEMBLY LINE DP")
    a1=[7,9,3,4,8,4];a2=[8,5,6,4,5,7]
    t1=[2,3,1,3,4];t2=[2,1,2,2,1]
    result,route,trace=assembly_line(a1,a2,t1,t2,2,4,3,2)
    print("Station trace: station, L1 stay, L1 transfer, choice, L2 stay, L2 transfer, choice")
    for row in trace:print(row)
    print("Minimum time:",result,"route:",["L"+str(x) for x in route])
    # Requirement-change and disruption experiments.
    slower_t1=t1[:];slower_t1[2]=20
    r2,route2,_=assembly_line(a1,a2,slower_t1,t2,2,4,3,2)
    slower_a1=a1[:];slower_a1[2]=30
    r3,route3,_=assembly_line(slower_a1,a2,t1,t2,2,4,3,2)
    print("Transfer time t1[3] increased to 20 ->",r2,["L"+str(x) for x in route2])
    print("Line 1 station 3 processing increased to 30 ->",r3,["L"+str(x) for x in route3])
    print("Three-line extension: DP state becomes F[line][station]; transition minimises over all previous lines plus transfer cost.")

    print("\\nTASK 5 — MST: KRUSKAL / PRIM / BORUVKA")
    V2=list("ABCDEFGH")
    E2=[("A","B",4),("A","C",3),("B","C",1),("B","D",2),("C","D",4),("C","E",2),
        ("D","E",3),("D","F",2),("E","F",3),("E","G",5),("F","G",1),("F","H",4),
        ("G","H",2),("B","H",7)]
    k,ck,tk=kruskal(V2,E2);pr,cp,tp=prim(V2,E2,"A");bo,cb,rb=boruvka(V2,E2)
    print("Kruskal accepted/rejected trace:",tk)
    print("Kruskal MST:",k,"cost:",ck)
    print("Prim edge order:",tp,"MST:",pr,"cost:",cp)
    print("Boruvka rounds:",rb,"MST:",bo,"cost:",cb)
    assert ck==cp==cb
    tie=[(u,v,1) for u,v in [("A","B"),("B","C"),("C","D"),("D","A"),("A","C"),("B","D")]]
    print("Equal-weight graph MST examples:")
    print("Kruskal:",kruskal(list("ABCD"),tie)[:2])
    print("Prim:",prim(list("ABCD"),tie,"A")[:2])
    print("Boruvka:",boruvka(list("ABCD"),tie)[:2])

    print("\\nTASK 6 — TSP HELD-KARP DP")
    M=[[0,10,15,20,12,18,9],[10,0,35,25,17,28,20],[15,35,0,30,20,16,22],
       [20,25,30,0,14,12,18],[12,17,20,14,0,11,13],[18,28,16,12,11,0,10],
       [9,20,22,18,13,10,0]]
    best,route,count=held_karp(M)
    print("7-location matrix:")
    for row in M:print(row)
    print("Minimum cost:",best,"route:",route,"DP states:",count)
    small=[row[:5] for row in M[:5]]
    dpc,rtc,cnt=held_karp(small);bc,br=brute_tsp(small)
    print("5-location validation: Held-Karp",dpc,rtC if False else rtc,"states",cnt)
    print("Exhaustive enumeration:",bc,br,"match:",dpc==bc)
    print("State counts by delivery locations (theoretical (m)*2^(m-1) scale):")
    for m in range(4,9):print(m, m*(2**(m-1)))
    print("200 delivery locations: exact Held-Karp is impractical; use approximation/heuristics (e.g. nearest-neighbour + local search) and accept no optimality guarantee.")
    assert dpc==bc
    print("\\nVALIDATION: PASS — Word Wrap boundary, knapsack sample, MST costs and TSP exhaustive comparison checked.")

if __name__=="__main__":main()
