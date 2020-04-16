import nltk
import pandas as pd
import re
import sys

def  topicExtract(data):
    para = re.compile("\n[0-9]+[.][ ]").split(data)

    for i in range(len(para)):
        para[i] = re.sub("\n"," ",para[i])

    topic=[]
    for i in range (len(para)):
        temp = para[i].split(".")
        topic.append(temp[0])

    # for i in range (len(topic)):
    #     print(str(i) + "." + topic[i])

    return(topic, para)