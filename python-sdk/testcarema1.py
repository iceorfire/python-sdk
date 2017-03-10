#coding=utf-8

import cv2
import time
import os


API_KEY = "your API"
API_SECRET = "your API_SECRET"





cap1=cv2.VideoCapture(0)

for i in range(10):
	cap1.read()


Input=raw_input('请输入Q进行拍照\n')
if Input=='Q' or Input=='q':
	_,frame=cap1.read()
	name='qunimade'+'1'+'.png'
	cv2.imwrite(name,frame)
	#os.system('say good,i had done it.')
Input1=raw_input('请再次输入Q进行拍照\n')
if Input1=='Q' or Input1=='q':
	_,frame=cap1.read()
	name='qunimade'+'2'+'.png'
	cv2.imwrite(name,frame)
	#os.system('say good,i had done it.')



cap1.release()


face_two = './qunimade1.png'

face_search = './qunimade2.png'


api_server_international = 'https://api-cn.faceplusplus.com/facepp/v3/'

# Import system libraries and define helper functions
# 导入系统库并定义辅助函数
from pprint import pformat


def print_result(hit, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(v): encode(k) for (v, k) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hit
    result = encode(result)
    print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))


# First import the API class from the SDK
# 首先，导入SDK中的API类
from facepp import API, File


#创建一个API对象，如果你是国际版用户，代码为：api = API(API_KEY, API_SECRET, srv=api_server_international)
#Create a API object, if you are an international user,code: api = API(API_KEY, API_SECRET, srv=api_server_international)
api = API(API_KEY, API_SECRET)



res = api.detect(image_file=File(face_two))
ret = api.detect(image_file=File(face_search))




#print ret["faces"][0]["face_token"],res["faces"][0]["face_token"]
qaq=api.compare(face_token1=ret['faces'][0]['face_token'],face_token2=res['faces'][0]['face_token'])

print qaq['confidence']
#if  float(qaq['confidence'])>90:
#	os.system('say you are one')
#else:
#	os.system('say you are dog')

#print_result('mabi',qaq)



