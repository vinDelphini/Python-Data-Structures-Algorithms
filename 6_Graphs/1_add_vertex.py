class Graph:

    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for key, value in self.adj_list.items():
            print(key, ":", value)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_graph()
