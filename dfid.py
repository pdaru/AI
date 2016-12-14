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


def dfid(search_tree, start):
    depthbound = 1
    previouscount = 0
    newnode = True

    while newnode:
        count = 0
        stack = [[start, None, 0]]
        closed = []

        while stack:
            nodepair = stack.pop()
            node = nodepair[0]
            if node == 'F':
                return reconstructpath(nodepair, closed, stack)
            else:
                closed.extend([nodepair])
                if nodepair[-1] < depthbound:
                    children = search_tree[node]
                    noloop = removeseen(children, stack, closed)
                    new = makepairs(noloop, node, nodepair[-1]+1)
                    stack.extend(new)
                    count += len(new)

        if previouscount == count:
            newnode = False

        previouscount = count
        depthbound += 1
    print "No solution found"


def reconstructpath(nodepair, closed, stack):
    path = [nodepair[0]]
    node = nodepair[1]
    while node is not None:
        for x in closed:
            if x[0] == node:
                path.append(x[0])
                node = x[1]
                break
    print path
    print stack
    print closed


def removeseen(nodelist, openlist, closedlist):
    if nodelist is None:
        return []
    else:
        nodelist = [n for n in nodelist if n not in openlist or n not in closedlist]
    return nodelist


def makepairs(children, parent, bound):
    if children is None:
        return []
    else:
        child_list = []
        for n in children:
            child_list.append([n, parent, bound])
        child_list.reverse()
    return child_list


if __name__ == '__main__':
    dfid(tree, 'A')