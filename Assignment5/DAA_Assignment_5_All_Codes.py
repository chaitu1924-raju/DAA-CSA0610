"""DAA Assignment 5 (CO5) — Part B implementations.
Run in Colab: %run /content/DAA_Assignment_5_All_Codes.py
Standard library only.
"""
from itertools import combinations
import time

# B1/B2: Backtracking graph colouring with instrumentation and vertex-order heuristic.
def graph_coloring(graph, colors, heuristic=False):
    n=len(graph); assignment=[-1]*n
    stats={"nodes":0,"attempts":0,"rejected":0,"backtracks":0,"max_depth":0}
    if heuristic:
        # Static descending-degree order: colour the most constrained/high-degree vertex first.
        order=sorted(range(n),key=lambda v:len(graph[v]),reverse=True)
    else:
        order=list(range(n))
    def feasible(v,c):
        return all(assignment[u]!=c for u in graph[v])
    def search(depth):
        stats["nodes"]+=1; stats["max_depth"]=max(stats["max_depth"],depth)
        if depth==n:return True
        v=order[depth]
        for c in range(colors):
            stats["attempts"]+=1
            if feasible(v,c):
                assignment[v]=c
                if search(depth+1):return True
                assignment[v]=-1
                stats["backtracks"]+=1
            else:stats["rejected"]+=1
        return False
    ok=search(0)
    return ok,(assignment[:] if ok else None),stats

# B3: Exact minimum set cover by subset enumeration; greedy maximum uncovered coverage.
def exact_set_cover(universe, sets):
    zones=set(universe); m=len(sets); checked=0
    for size in range(m+1):
        for ids in combinations(range(m),size):
            checked+=1; covered=set()
            for i in ids:covered |= set(sets[i])
            if zones<=covered:return list(ids),checked
    return None,checked

def greedy_set_cover(universe, sets):
    uncovered=set(universe); chosen=[]; steps=0
    while uncovered:
        candidates=[(len(set(s)&uncovered),-i,i) for i,s in enumerate(sets) if i not in chosen]
        steps+=len(candidates)
        if not candidates: return None,steps
        gain,_,best=max(candidates)
        if gain==0:return None,steps
        chosen.append(best);uncovered-=set(sets[best])
    return chosen,steps

# B4: First Fit Decreasing bin packing heuristic.
def first_fit_decreasing(items, capacity):
    ordered=sorted(enumerate(items),key=lambda x:x[1],reverse=True)
    bins=[]; placements=[]
    for original,w in ordered:
        placed=False
        for i,b in enumerate(bins):
            if sum(b)+w<=capacity:
                b.append(w);placements.append((original,w,i));placed=True;break
        if not placed:bins.append([w]);placements.append((original,w,len(bins)-1))
    return bins,placements

def main():
    print("DAA ASSIGNMENT 5 — CO5 | IMPLEMENTATION OUTPUTS")
    print("\\nB1 — GRAPH COLOURING VALIDATION AND SEARCH ORDER")
    # Colourable 5-cycle; uncolourable triangle with two colours; boundary empty graph.
    graphs=[
      ("5-cycle",[{1,4},{0,2},{1,3},{2,4},{3,0}],2),
      ("triangle-2-colours",[{1,2},{0,2},{0,1}],2),
      ("empty-boundary",[],3)]
    for name,g,k in graphs:
        if not g: g=[]
        a=graph_coloring(g,k,False);b=graph_coloring(g,k,True)
        print(name,"input-order:",a,"degree-order:",b)
    print("Note: empty graph boundary has zero vertices; success is an empty colouring.")

    print("\\nB2 — SAME SIZE, DIFFERENT SEARCH BEHAVIOUR")
    # 8-vertex easy cycle vs hard complete graph under 3 colours (unsatisfiable).
    easy=[set() for _ in range(8)]
    for i in range(8):easy[i].update({(i-1)%8,(i+1)%8})
    hard=[set(j for j in range(8) if j!=i) for i in range(8)]
    print("Prediction: K8 with 3 colours will backtrack more than the 8-cycle.")
    for name,g in [("Cycle-8",easy),("Complete-K8",hard)]:
        ok,col,st=graph_coloring(g,3,False)
        print(name,"colourable:",ok,"colours:",col,"stats:",st)

    print("\\nB3 — EXACT VS GREEDY SET COVER")
    tests=[
      ("Case-1",set("1234"),[set("12"),set("34"),set("13")]),
      ("Case-2",set("abcdef"),[set("abc"),set("def"),set("ad"),set("be"),set("cf")]),
      ("Case-3",set("abcdef"),[set("abcd"),set("cdef"),set("ab"),set("ef")]),
      ("Greedy-counterexample",set("123456"),[set("1234"),set("125"),set("346"),set("5"),set("6")])]
    for name,u,s in tests:
        ex,ec=exact_set_cover(u,s);gr,gc=greedy_set_cover(u,s)
        print(name,"exact indices:",ex,"size:",None if ex is None else len(ex),"combinations:",ec,
              "| greedy indices:",gr,"size:",None if gr is None else len(gr),"candidate checks:",gc)
    # Scale-up deterministic family; operation counts rather than relying on timing.
    print("Scaling: exact subset combinations vs greedy candidate evaluations")
    for m in (8,10,12,14):
        u=set(range(2*m))
        sets=[{2*i,2*i+1} for i in range(m)]
        ex,ec=exact_set_cover(u,sets);gr,gc=greedy_set_cover(u,sets)
        print("centres",m,"exact combinations",ec,"greedy candidate checks",gc,"cover sizes",len(ex),len(gr))

    print("\\nB4 — BIN PACKING FIRST-FIT DECREASING")
    capacity=10
    workloads=[6,6,4,4,4,2,2,2]
    bins,placed=first_fit_decreasing(workloads,capacity)
    print("Capacity:",capacity,"workloads:",workloads)
    for i,b in enumerate(bins):print("Server",i+1,"workloads",b,"used",sum(b),"remaining",capacity-sum(b))
    print("Servers used:",len(bins),"placements(original_index, workload, server_index):",placed)
    # A compact comparison with exact lower bound for this test.
    lower=(sum(workloads)+capacity-1)//capacity
    print("Volume lower bound:",lower,"heuristic server count:",len(bins))
    print("Decision note: FFD is fast (sorting plus first-fit scans) but is not guaranteed optimal.")
    print("\\nVALIDATION COMPLETE")
if __name__=="__main__":main()
