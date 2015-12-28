class Node(object):
    def __init__(self, value, nextnode):
        self.value = value
        self.nextnode = nextnode

class Linkedlist(object):
    def __init__(self, node):
        self.node = node

    def get_at(self, n):
        return self.get_node(n).value

    def get_node(self, n):
        node = self.node
        while n > 0:
            n -= 1
            node = node.nextnode
        return node

    def append(self, x):
        if self.node.nextnode != None:
            currentnode = self.node.nextnode
            while True:
                #print(currentnode.value)
                if currentnode.nextnode == None:
                    currentnode.nextnode =  Node(x, None)
                if currentnode.nextnode.value == x:
                    break
                currentnode = currentnode.nextnode 

    def insert(self, x, i=0,):
        node = self.get_node(i-1)
        node.nextnode = Node(x, node.nextnode)
    
fourthnode = Node(123, None)
thirdnode = Node(12, fourthnode)
secondnode = Node(5, thirdnode)
firstnode = Node(2, secondnode)

testlist = Linkedlist(firstnode)

print(testlist.get_at(3))

testlist.append("blarg")

print(testlist.get_at(4))


    
