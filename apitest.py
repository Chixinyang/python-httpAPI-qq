import requests
import schedule
#localIp = '192.168.0.106'
localIp = 'localhost'
def SendPrivateMsg(qq,msg,PlainText=False):
    funcname = 'send_private_msg'
    url = "http://" + localIp + ":5700/" + funcname
    params = {
        'user_id': qq,
        'message': msg,
        'auto_escape':PlainText
    }
    req = requests.get(url=url,params=params)
    print(req.status_code)
#酷Q表情CQ码获取方法：1，百度 2，主动发送给qq，从日志中提取
def GetCQFaceId(face):
    FaceDict = {
        '拜拜':39,
        '吓':110
    }
    return FaceDict[face]
def GetGroupList():
    url = "http://"+localIp+":5700/get_group_list"
    req = requests.get(url=url)
    print(req.status_code)
    resDict = req.json()
    #print(resDict)
    grouplists = [];
    for val in resDict['data']:
        print("group id is : {},group name is :{}".format(val['group_id'],val['group_name']))
        grouplists.append(val['group_id'])
    return grouplists
def SendGroupMsg(groupid,msg,PlainText=False):
    funcname = 'send_group_msg'
    url = "http://"+localIp+":5700/"+funcname
    params = {
        'group_id': groupid,
        'message': msg,
        'auto_escape': PlainText
    }
    req = requests.get(url=url,params=params)
    print(req.content)
    print('send group [{}] : {}'.format(groupid,req.status_code))
def SendGroupsMsg():
    groupslists = GetGroupList()
    if len(groupslists):
        for val in groupslists:
            r = SendGroupMsg(val, "[CQ:face,id={}]".format(GetCQFaceId("拜拜")))
            print(r)
        pass
    else:
        print("no group")
    pass
if __name__ == '__main__':
    #SendPrivateMsg(1220462431,"[CQ:face,id={}]".format(GetCQFaceId("拜拜")))
    schedule.every(10).seconds.do(SendGroupsMsg)
    while True:
        schedule.run_pending()
        import time
        time.sleep(1)
