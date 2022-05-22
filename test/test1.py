import sys
from collections import deque

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    n, q = map(int, lines[0].split())
    abc = [list(map(int, line.split())) for line in lines[1:]]
    graph = [[] for _ in range(n)]
    for a, b, c in abc:
      if c>=0:
        graph[a-1].append((b-1, c))
      else:
        graph[b-1].append((a-1, -c))

    ages = [float('inf')]*n

    for i in range(len(graph)):
      if len(graph[i]) != 0:
        start = i
        break
    ages[i] = 0
    stack = deque([(start, 0)])
    visited = [-1]*n
    error = False
    while stack:
      node, cost = stack.popleft()
      visited[node] = 1
      for child, c_cost in graph[node]:
        if ages[child] == float('inf'):
          ages[child] = ages[node]+c_cost
          stack.append((child, c_cost))
        else:
          if ages[child] != ages[node]+c_cost:
            error = True
    for age in ages:
      if age >= 100:
        error = True
    
    if error:
      print(-1)
    else:
      print(max(ages)-min(ages))
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)