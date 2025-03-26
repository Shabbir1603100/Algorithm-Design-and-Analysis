from collections import defaultdict, deque
import sys

def maximize_project_weight(n, weights, dependencies):
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    in_degree = [0] * n
    
    for u, v in dependencies:
        graph[u].append(v)
        reverse_graph[v].append(u)
        in_degree[v] += 1

    topo_order = []
    queue = deque()
    
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    dp = weights[:]
    best_subset = {i: {i} for i in range(n)}
    
    for u in topo_order:
        for v in graph[u]:
            if dp[v] < dp[u] + weights[v]:
                dp[v] = dp[u] + weights[v]
                best_subset[v] = best_subset[u] | {v} 
    
    max_weight = float('-inf')
    optimal_subset = set()
    
    for i in range(n):
        if dp[i] > max_weight:
            max_weight = dp[i]
            optimal_subset = best_subset[i]
    
    final_selected = set()
    def collect_dependencies(node):
        if node in final_selected:
            return
        final_selected.add(node)
        for prev in reverse_graph[node]:
            collect_dependencies(prev)
    
    for proj in optimal_subset:
        collect_dependencies(proj)
    
    selected_projects = sorted(final_selected)
    
    print(sum(weights[i] for i in selected_projects))
    print(f"The optimum solution selects projects {', '.join(str(i + 1) for i in selected_projects)}.")

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    weights = list(map(int, sys.stdin.readline().split()))
    dependencies = [tuple(map(lambda x: int(x) - 1, sys.stdin.readline().split())) for _ in range(m)]
    
    maximize_project_weight(n, weights, dependencies)
