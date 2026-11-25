import sys

def greedy_value(items, W):
    order=sorted(range(len(items)), key=lambda i: items[i][2]/items[i][1], reverse=True)
    used=val=0
    for i in order:
        name,cost,value=items[i]
        if used+cost<=W:
            used+=cost; val+=value
    return val

def optimal_plan(items,W):
    n=len(items)
    dp=[[None]*(W+1) for _ in range(n+1)]
    take=[[False]*(W+1) for _ in range(n+1)]
    dp[0][0]=0
    for i,(name,cost,value) in enumerate(items,1):
        for w in range(W+1):
            best=dp[i-1][w]
            if w>=cost and dp[i-1][w-cost] is not None:
                candidate=dp[i-1][w-cost]+value
                if best is None or candidate>best:
                    best=candidate; take[i][w]=True
            dp[i][w]=best
    best_value=max(v for v in dp[n] if v is not None)
    best_cost=next(w for w,v in enumerate(dp[n]) if v==best_value)
    chosen=[]; w=best_cost
    for i in range(n,0,-1):
        if take[i][w]:
            chosen.append(i-1); w-=items[i-1][1]
    chosen.reverse()
    return best_value,best_cost,chosen

def solve(text):
    t=iter(text.split()); n=int(next(t)); W=int(next(t)); items=[]
    for _ in range(n):
        items.append((next(t),int(next(t)),int(next(t))))
    gv=greedy_value(items,W); mv,used,ids=optimal_plan(items,W)
    names=" ".join(items[i][0] for i in ids) if ids else "NONE"
    return f"Greedy Value = {gv}\nMaximum Value = {mv}\nSelected = {names}\nBudget Used = {used}"

def tests():
    s1="3 50\nAuth 10 60\nSearch 20 100\nPayments 30 120\n"
    e1="Greedy Value = 160\nMaximum Value = 220\nSelected = Search Payments\nBudget Used = 50"
    s2="6 15\nCache 7 60\nSearch 4 36\nChat 8 33\nReports 5 34\nAlerts 2 47\nBackup 6 63\n"
    e2="Greedy Value = 146\nMaximum Value = 170\nSelected = Cache Alerts Backup\nBudget Used = 15"
    assert solve(s1)==e1
    assert solve(s2)==e2
    assert solve("2 0\nA 1 10\nB 2 20")=="Greedy Value = 0\nMaximum Value = 0\nSelected = NONE\nBudget Used = 0"
    assert solve("2 1\nA 2 10\nB 3 20").endswith("Selected = NONE\nBudget Used = 0")
    assert solve("2 10\nA 3 5\nB 4 6").endswith("Selected = A B\nBudget Used = 7")
    assert solve("2 5\nA 5 10\nB 3 10").endswith("Selected = B\nBudget Used = 3")
    assert solve("1 5\nSolo 5 9").endswith("Selected = Solo\nBudget Used = 5")
    large=[(f"F{i}",i%1000+1,(i*37)%1001) for i in range(200)]
    v,c,ids=optimal_plan(large,10000)
    assert sum(large[i][1] for i in ids)==c and sum(large[i][2] for i in ids)==v
    print("Sample 1: PASS"); print(e1)
    print("\nSample 2: PASS"); print(e2)
    print("\nEdge cases: zero budget, no fit, all fit, tied optimum, single item — PASS")
    print("Maximum constraints n=200, W=10000: PASS")
if __name__=="__main__":
    raw=sys.stdin.read()
    if raw.strip(): print(solve(raw))
    else: tests()
