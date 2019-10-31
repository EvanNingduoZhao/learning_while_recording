import get_triple
from py2neo import Node, Relationship, Graph, NodeMatcher

text = "德勤有三个业务部门，分别是税务，法律和审计。"
# text = "德勤有三个业务部门，分别是税务，法律和审计."
dic = get_triple.ret(text)
print(dic)

'''
#create a new graph
graph = Graph('http://localhost:7474', username='neo4j', password='leah')

graph.delete_all()
def node_exist(graph, node_name):
    match = NodeMatcher(graph)
    a = match.match(name = node_name).first()
    return a
#draw the graph
node_list = []
for key, values in dic.items():
    if node_exist(graph, values[0]) == None:
        a = Node("entity1", name = values[0])
    else:
        a = node_exist(graph, values[0])
    b = Node("entity2", name = values[1])
    node_list.append(a)
    node_list.append(b)
    graph.create(a)
    graph.create(b)
    r = Relationship(a, key, b)
    graph.create(r)
'''
