from collections import deque


class Node(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, start, dest):
        self.start = start
        self.dest = dest

    def get_start(self):
        return self.start

    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.start.get_name() + '->' + self.dest.get_name()


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        super(Edge, self).__init__()
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.start.get_name() + '->' + str(self.weight) + '->' + self.dest.get_name()


class Digraph(object):
    """
    有向图
    """
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError("Duplicate Nodes")
        else:
            self.nodes.append(node)
            # 添加 node 的同时, 将 node 加入边中
            self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_start()
        dest = edge.get_destination()
        if src in self.nodes and dest in self.nodes:
            self.edges[src].append(dest)
        else:
            raise ValueError('Node not in graph')

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for node in self.nodes:
            for dest in self.edges[node]:
                result += node.get_name() + '->' + dest.get_name + '\n'
        return result[:-1]


def Graph(Digraph):
    """
    无向图
    """
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        # 把 reverse 后的节点当成 edge 处理
        rev = Edge(edge.get_destination(), edge.get_start())
        Digraph.add_edge(self, rev)


def print_path(path):
    if path is None:
        return None
    result = ''
    for i, v in enumerate(path):
        result = result + str(v)
        # 如果不是最后一个, 那么添加 "->"
        if v != path[-1]:
            result += '->'
    return result


def BFS(graph, start, end):
    init_path = deque([start])
    total_path = deque([init_path])
    while len(total_path) != 0:
        current_path = total_path.popleft()
        last_node = current_path[-1]
        print_path(current_path)
        if last_node == end:
            return current_path
        for next_node in graph.children_of(last_node):
            if next_node not in current_path:
                new_path = current_path + deque([next_node])
                total_path.append(new_path)
    return None


def DFS(graph, start, end, path, shortest):
    path = path + [start]
    print('Current DFS path', print_path(path), 'start', start, 'end', end)
    print('shorest', print_path(shortest))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:
            if (shortest is None) or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest)
                if new_path is not None:
                    shortest = new_path
    return shortest


def DFS_norecursive(graph, start, end):
    # 以栈的结构存储
    stack = deque()
    # 栈结构记录当前元素及走过的路径
    stack.append([start])
    shortest = None
    while stack:
        # 弹出栈顶元素, 实现进行深度优先搜索
        path = stack.pop()
        node = path[-1]
        for next in graph.children_of(node):
            # 避免重复, 陷入循环
            if next not in path:
                # 新路径由新的子节点加上之前的路径构成
                current_path = path + [next]
                print(print_path(current_path))
                if next == end:
                    # 最短路径
                    if shortest is None or len(current_path) < len(shortest):
                        shortest = current_path
                else:
                    # 将新路径及当前子节点压入
                    stack.append(current_path)

    return shortest


def test_norec_DFS():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[1], nodes[5]))
    g.add_edge(Edge(nodes[5], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[2]))
    g.add_edge(Edge(nodes[5], nodes[4]))
    sp = DFS_norecursive(g, nodes[1], nodes[4])
    print('dfs 非递归', print_path(sp))


# test_norec_DFS()


def test_sp_dfs():
    """
    递归 DFS
    """
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[1], nodes[5]))
    g.add_edge(Edge(nodes[5], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[2]))
    g.add_edge(Edge(nodes[5], nodes[4]))
    sp = DFS(g, nodes[1], nodes[5], [], None)
    print('dfs 递归', print_path(sp))


test_sp_dfs()


def test_sp_bfs():
    """
    BFS
    """
    nodes = []
    n = 6
    for i in range(n):
        nodes.append(Node(str(i)))
    graph = Digraph()
    for i in nodes:
        graph.add_node(i)
    g = graph
    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[1], nodes[5]))
    g.add_edge(Edge(nodes[5], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[2]))
    g.add_edge(Edge(nodes[5], nodes[4]))
    sp = BFS(g, nodes[5], nodes[2])
    print('bfs', print_path(sp))


# test_sp_bfs()
