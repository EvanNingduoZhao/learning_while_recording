#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64

TEXT = "公有住房和廉租住房需要交房产税么"


def ret(TEXT):
    """
    从中文text中获取三元组并返回
    :param TEXT: input chinese text
    :return: triples list, each element of the list is a triple
    """
    # 开放平台应用ID
    x_appid = "5c867fda"
    # 开放平台应用接口秘钥
    api_key = "4a6e622ec997202bd713ef62d81321ed"
    # 语言文本
    # TEXT = "现行的中华人民共和国个人所得税法于2011年6月30日公布，自2011年9月1日起施行。"

    body = urllib.parse.urlencode({'text': TEXT}).encode('utf-8')

    # print("body is ")
    # print(body)

    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}

    srl_url = "http://ltpapi.xfyun.cn/v1/srl"
    req = urllib.request.Request(srl_url, body, x_header)  # invoke api
    result = urllib.request.urlopen(req)
    result = result.read()
    result = result.decode('utf-8')  # tranlate result
    srl_dic = {}
    a = str(result)

    print("result is " + a)

    srl_dic = json.loads(a)
    print(srl_dic)

    cws_url = "http://ltpapi.xfyun.cn/v1/cws"
    req = urllib.request.Request(cws_url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    result = result.decode('utf-8')
    cws_dic = {}
    b = str(result)
    cws_dic = json.loads(b)
    print(cws_dic)

    # 将运行结果预处理为需要的list
    srl_list = srl_dic.get('data').get('srl')

    print("srl_list is ")
    print(srl_list)

    cws_list = cws_dic.get('data').get('word')

    print("cws_list is ")
    print(cws_list)

    # 生成三元组的dictionary SVO

    ret_dic = {}
    for item in srl_list:
        id = item.get('id')
        entity = ''.join(cws_list[item.get('beg'):item.get('end') + 1])
        if id not in ret_dic:
            ret_dic[id] = [entity]
        else:
            ret_dic[id].append(entity)

    print("ret_dic is ")
    print(ret_dic)

    ret_list = []
    for key, values in ret_dic.items():
        if len(values) == 2:
            newlist = [values[0], cws_list[id], values[1]]
            ret_list.append(newlist)

    print("ret_list is")
    print(ret_list)
    return ret_list


ret(TEXT)
