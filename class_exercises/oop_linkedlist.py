class Node(object):
    def __init__(self, value, nextnode):
        self.value = value
        self.nextnode = nextnode

class Linkedlist(object):
    def __init__(self, node):
        self.node = node

    def get_at(self, n):
        return self.get_node(n).value

    def lenlinked(self):
        n = 1
        if self.node.nextnode != None:
            currentnode = self.node
            while True:
                n += 1
                currentnode = currentnode.nextnode
                if currentnode.nextnode == None:
                    break
        return n

    def get_node(self, n):
        node = self.node
        while n > 0:
            n -= 1
            if node.nextnode != None:
                node = node.nextnode
        return node

    #still need to test edge cases!
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

    def insert(self, *args):
        if len(args) == 2:
            i = args[0]
            x = args[1]
            node = self.get_node(i-1)
            node.nextnode = Node(x, node.nextnode)
        if len(args) == 1:
            x = args[0]
            nextnode = self.node.nextnode
            self.node = Node(x, self.node.nextnode)

    def printll(self):
        for n in range(0, testlist.lenlinked()):
            print(testlist.get_at(n))


fourthnode = Node(123, None)
thirdnode = Node(12, fourthnode)
secondnode = Node(5, thirdnode)
firstnode = Node(2, secondnode)

testlist = Linkedlist(firstnode)
testlist2 = Linkedlist(fourthnode)

testlist.insert(3, "gralb")
testlist.insert("genesis")
#testlist.append("blarg")

#testlist.insert(0, 994)

#print(testlist.printll())

print(testlist.printll())
