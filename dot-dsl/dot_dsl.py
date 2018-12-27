NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        if not isinstance(attrs, dict):
            raise ValueError("Graph node attributes must be a dict")

        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


class Graph(object):
    def __init__(self, data=[]):
        if not isinstance(data, list):
            raise TypeError("Graph data must be a list")

        if [n for n in data if len(n) is 0]:
            raise TypeError("Graph data must each have a type")

        if [n for n in data if n[0] > ATTR]:
            raise ValueError("Graph data must be a node, edge, or attribute")

        try:
            self.nodes = [Node(n[1], n[2]) for n in data if n[0] is NODE]
            self.edges = [Edge(e[1], e[2], e[3]) for e in data if e[0] is EDGE]
            self.attrs = {
                a[1]: a[2] for a in data if a[0] is ATTR and validateAttribute(a)
            }
        except IndexError as e:
            raise ValueError("Graph nodes must have a type")


def validateAttribute(attr):
    if len(attr) < 3:
        raise TypeError("Graph attributes must have a key and value")

    if len(attr) is not 3:
        raise ValueError("Graph attributes must be a tuple of three members")

    return True
