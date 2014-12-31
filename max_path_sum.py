class MaxPathProblem:

    def __init__(self,file):
        self.graph = []
        f = open(file, 'r')
        rownum = 0
        text = f.read().rstrip().split("\n")
        for row in text:
            self.graph.append([])
            for cell in row.split(' '):
                self.graph[rownum].append({ 'value': int(cell), 'distance': -1 })
            rownum += 1

    # The tree is perfectly balanced so it doesn't matter
    # which column the node is in, only how close it is
    # to the bottom
    def has_children(self, rownum):
        if rownum >= len(self.graph) - 1:
            return False
        return True

    def left_child(self, rownum, colnum):
        if self.has_children(rownum):
            return [rownum + 1, colnum]
        else:
            raise Exception('No children')

    def right_child(self, rownum, colnum):
        if self.has_children(rownum):
            return [rownum + 1, colnum + 1]
        else:
            raise Exception('No children')

    def find_sum(self, i, j):
        if not self.has_children(i):
            self.graph[i][j]['distance'] = self.graph[i][j]['value']
            return
        else:
            l = self.left_child(i, j)
            r = self.right_child(i, j)
        if self.graph[l[0]][l[1]]['distance'] < 0:
            self.find_sum(l[0], l[1])
        if self.graph[r[0]][r[1]]['distance'] < 0:
            self.find_sum(r[0], r[1])
        self.graph[i][j]['distance'] = self.graph[i][j]['value'] + max(self.graph[l[0]][l[1]]['distance'], self.graph[r[0]][r[1]]['distance'])

    def result(self):
        self.find_sum(0, 0)
        return self.graph[0][0]['distance']
