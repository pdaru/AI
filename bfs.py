
tree = {'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G', 'H'],
        'D': ['I'],
        'E': ['J', 'K'],
        'F': ['L', 'M'],
        'G': [],
        'H': ['N'],
        'I': [],
        'J': [],
        'K': [],
        'L': [],
        'M': [],
        'N': []
        }


def bfs(search_tree, start):
    queue = [[start, None]]
    closed = []

    while queue:
        nodepair = queue.pop(0)
        node = nodepair[0]
        if node == 'N':
            return reconstructpath(nodepair, closed, queue)
        else:
            closed.extend([nodepair])
            children = search_tree[node]
            noloop = removeseen(children, queue, closed)
            new = makepairs(noloop, node)
            queue.extend(new)
    print "No solution found"


def reconstructpath(nodepair, closed, queue):
    path = [nodepair[0]]
    node = nodepair[1]
    while node is not None:
        for x in closed:
            if x[0] == node:
                path.append(x[0])
                node = x[1]
                break
    print path
    print queue
    print closed


def removeseen(nodelist, openlist, closedlist):
    if nodelist is None:
        return []
    else:
        nodelist = [n for n in nodelist if n not in openlist or n not in closedlist]
    return nodelist


def makepairs(children, parent):
    child_list = []
    if children is None:
        return []
    else:
        for n in children:
            child_list.append([n, parent])
    return child_list


if __name__ == '__main__':
    bfs(tree, 'A')
