class Node():
    node_count=0
    def __init__(self,node_id:str,cpu:int,memory:int):
        self.node_id=node_id
        self.cpu=cpu
        self.memory=memory
        Node.node_count+=1
    @classmethod
    def get_count(cls):
        print("total nodes created is :",cls.node_count)


nodes=[]
node1=Node("0001",12,1024)
nodes.append(node1)
node2=Node("0002",13,2048)
nodes.append(node2)
node3=Node("0003",13,256)
nodes.append(node3)
n=len(nodes)
for i in nodes:
    print(i.node_id)

[print((n.node_id)) for n in nodes]
Node.get_count()









