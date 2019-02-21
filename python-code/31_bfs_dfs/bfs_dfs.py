from collections import deque


class Graph(object):
    """
    无向图
    使用动态数组存储相邻顶点
    """

    def __init__(self, num):
        # 顶点个数
        self.vertexnum = num
        # 邻接表, 不能用 [[]] * self.vertexnum, 这样产生的每个 [] id 都是相同的
        self.adjacency_table = [[] for _ in range(self.vertexnum)]

    def add_edge(self, s, t):
        # 无向图，一条边存两次
        self.adjacency_table[s].append(t)
        self.adjacency_table[t].append(s)

    def print_path(self, s, t, prev):
        if prev[t] is not None and s != t:
            yield from self.print_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s, t):
        if s == t:
            return
        # visited 记录已访问节点
        visited = [False] * self.vertexnum
        visited[s] = True
        # 队列形式记录未访问节点
        q = deque()
        q.append(s)
        # 记录搜索路径，也就是节点的前驱结点
        prev = [None] * self.vertexnum
        while q:
            v = q.popleft()
            for neighbor in self.adjacency_table[v]:
                if visited[neighbor] is False:
                    visited[neighbor] = True
                    prev[neighbor] = v
                    if neighbor == t:
                        print('->'.join(self.print_path(s, t, prev)))
                    q.append(neighbor)

    def dfs(self, s, t):
        """
        found 作用，找到终点 t 后，不再继续寻找
        如果需要求最短路径，不用 found 标记，先找出所有的路径，再取最短的那条路径
        """
        found = False
        visited = [False] * self.vertexnum
        prev = [None] * self.vertexnum

        def _recurdfs(v):
            nonlocal found
            if found is True:
                return
            visited[v] = True
            if v == t:
                found = True
                return
            for neighbor in self.adjacency_table[v]:
                if visited[neighbor] is False:
                    prev[neighbor] = v
                    _recurdfs(neighbor)

        _recurdfs(s)
        print('->'.join(self.print_path(s, t, prev)))


if __name__ == '__main__':
    g = Graph(8)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 7)

    g.bfs(0, 6)
    g.dfs(0, 6)
