from flask import Flask, render_template, request
from topic import topicExtract
from sum import sumTopic

app = Flask(__name__)

para = []
topic = []

@app.route('/')
def indexDisp():
    return render_template('index.html')

@app.route('/topics', methods = ['POST', 'GET'])
def summaryTime():
    global para 
    global topic
    if request.method == 'POST':
        topic,para = topicExtract(request.form.get("message"))
        html = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Topics Available</title></head><body><h1>Topics : </h1><br>"
        
        html = html + "<form action=\"/summary\" method=\"POST\" name=\"topicsum\">"

        for i in range (len(topic)):
           html = html + "<input type=\"checkbox\" id=\"op" + str(i) + "\" name=\"op" + str(i) + "\" value=\"" + str(i) + "\"> " + str(topic[i]) + "<br>" 

        html = html + "<br><br> Summary Level <br><input name=\"thres\" id=\"thres\" type=\"range\" min=\"1\" max=\"100\" value=\"50\"><br><br><button name=\"forwardBtn\" onclick=\"move_forward()\">Submit</button></form></body></html>"

        return (html)

@app.route('/summary', methods = ['POST', 'GET'])
def summ():
    if request.method == 'POST':
        data = ''
        for i in range (len(topic)-1):
            op = "op" + str(i)
            val1 = request.form.get(op)
            if val1 == str(i):
                data = data + para[i]
            val2 = int(request.form.get('thres'))

    length = len(data.split('.'))
    thres = int((length/100)*val2)
    summary = sumTopic(data,thres)

    html = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Summary</title></head><body><h1>Your Summary : </h1><br><h4>" + str(summary) + "</h4>"
    html = html + "</body></html>"
    return(str(summary))





if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)