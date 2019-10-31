# encoding=utf-8
from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher
import json

# 问题
# 德勤有三个业务部门，分别是税务，法律和审计，其中税务与审计部门已经使用了知识图谱的技术，法律部门使用了人工智能的技术
ask = input("请输入您的问题：")  # 德勤 知识图谱 使用

# 输入信息
a = "德勤 业务 审计 德勤 业务 税务 德勤 业务 法律 税务 使用 知识图谱 法律 使用 人工智能 审计 使用 知识图谱 知识图谱 属于 人工智能"
b = a.split(' ')
new_list = []
for i in range(0, len(b), 3):
    new_list.append(b[i:i + 3])

# create a new graph
graph = Graph('http://localhost:7474', username='neo4j', password='leah')
# graph = Graph('http://localhost:7474', username='neo4j', password='neo4j')

graph.delete_all()


def node_exist(graph, node_name):
    """
    判断一个node是否存在于图中
    :param graph:
    :param node_name:
    :return:
    """
    match = NodeMatcher(graph)
    a = match.match(name=node_name).first()
    return a


# draw the graph
for item in new_list:  # every item is a list of three elements: 实体1 关系 实体2
    if node_exist(graph, item[0]) is None:
        a = Node("entity1", name=item[0])
    else:
        a = node_exist(graph, item[0])
    if node_exist(graph, item[2]) is None:
        b = Node("entity2", name=item[2])  # if node not exist in graph, construct a new node and name it b
    else:
        b = node_exist(graph, item[2])  # if node does exist in graph, name the existing node b

    graph.create(a)
    graph.create(b)
    r = Relationship(a, item[1], b, name=item[1])
    graph.create(r)

# 构建实体和关系的list
node_list = []
all_nodes = graph.run("MATCH (p) RETURN p").data()
print("all node is")
print(all_nodes)
for i in range(len(all_nodes)):
    node_list.append(all_nodes[i]['p']['name'])
node_list = list(set(node_list))

relationship_list = []
all_relationships = graph.run("MATCH (p)-[r]->(q) RETURN r").data()
for j in range(len(all_relationships)):
    relationship_list.append(all_relationships[j]['r']['name'])
relationship_list = list(set(relationship_list))

# 从问句中提取关键实体和关系
node_in_ask = []
relationship_in_ask = []
for n in node_list:
    if n in ask:  # identify key words
        node_in_ask.append(n)  # store all the node key words appearing in the question into a list

for r in relationship_list:
    if r in ask:
        relationship_in_ask.append(r)  # store all the relationship key words appearing in the question into a list


def en2r1(e1, e2, r1):
    """
    两个实体一个关系寻找中间实体的情况，寻找另外一个实体
    :param e1: entity1
    :param e2: entity2
    :param r1: relationship1
    :return: result or none
    """
    print("en2r1 is revoked")
    query = "MATCH (p) WHERE p.name = '{}'  MATCH (p)-[r]-(q)  MATCH (q)-[rr]-(s) WHERE s.name = '{}' RETURN q, r, rr".format(
        e1, e2)
    result = graph.run(query).data()
    if len(result) == 0:
        return None

    ret_nodes = []
    for i in range(len(result)):
        ret_entity = result[i]['q']['name']
        ret_r = result[i]['r']['name']
        ret_rr = result[i]['rr']['name']
        if ret_r == r1 or ret_rr == r1:
            ret_nodes.append(ret_entity)
    if len(ret_nodes) == 0:
        return None
    return ret_nodes


def en2r1_2(e1, e2, r1):
    """
    两个实体一个关系推出第三个实体
    :param e1:
    :param e2:
    :param r1:
    :return:
    """
    print("en2r1_2 is revoked")
    query = "MATCH (p)-[r]-(q) WHERE p.name = '{}' and q.name = '{}'  MATCH (pp)-[r1]-(t) WHERE r1.name = '{}' and (pp = p or pp = q) RETURN t".format(
        e1, e2, r1)
    result = graph.run(query).data()
    if len(result) == 0:
        return None
    ret_nodes = []
    for i in range(len(result)):
        ret_entity = result[i]['t']['name']
        ret_nodes.append(ret_entity)
    if len(ret_nodes) == 0:
        return None
    return ret_nodes


def en1r1(en1, r1):
    """
    一个实体一个关系的查询
    :param en1:
    :param r1:
    :return:
    """
    print("en1r1 is revoked")
    query = "MATCH (p) WHERE p.name = '{}' MATCH (p)-[r]-(q) WHERE r.name = '{}' RETURN p, r, q".format(en1, r1)
    result = graph.run(query).data()
    if len(result) == 0:
        print("Sorry, I don't know.")
        return None
    ret_nodes = []
    for i in range(len(result)):
        ret_nodes.append(result[i]['q']['name'])
    return ret_nodes


# 判断问题的不同情形
en_number = len(node_in_ask)
r_number = len(relationship_in_ask)
if en_number == 1 and r_number == 1:
    result = en1r1(node_in_ask[0], relationship_in_ask[0])
    if result is not None:
        print(result)
    else:
        print("Sorry, I don't know.")
elif en_number == 2 and r_number >= 1:
    scene1 = en2r1(node_in_ask[0], node_in_ask[1], relationship_in_ask[0])
    scene2 = en2r1_2(node_in_ask[0], node_in_ask[1], relationship_in_ask[0])
    if scene1 is not None:
        print(scene1)
    elif scene2 is not None:
        print(scene2)
    else:
        print("Sorry, I don't know.")
else:
    print("Sorry, I don't know.")
