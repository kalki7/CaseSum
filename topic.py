import nltk
import pandas as pd
import re
import sys

def  topicExtract(data):
    para = re.compile("\n[0-9]+[.][ ]").split(data)
    for i in range(len(para)):
        para[i] = re.sub("\n"," ",para[i])
    
    topic = [] 
    content = [] 
    info = []


    for i in range (len(para)):
        temp = para[i].split(".")
        topic.append(temp[0])
        content.append(temp[1:])

    for j in range(len(content)):
        x = " ".join(content[j])     
        info.append(x)

    # for i in range (len(topic)):
    #     print(str(i) + "." + topic[i])

    return(topic, info)