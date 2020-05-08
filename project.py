from flask import Flask, render_template, request
from topic import topicExtract
from sum import extra

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
        html = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Topics Available</title></head><body><h1>Topics : </h1><br><h3>Do not select any if you want a summary of the whole document</h3><br>"
        
        html = html + "<form action=\"/summary\" method=\"POST\" name=\"topicsum\">"

        for i in range (len(topic)):
           html = html + "<input type=\"checkbox\" id=\"op" + str(i) + "\" name=\"op" + str(i) + "\" value=\"" + str(i) + "\"> " + str(topic[i]) + "<br>" 
        
        html = html + '''<br><br><h1>Choose Summariser : </h1><br><input type=\"radio\" id=\"1\" name=\"sum\" value=\"1\" checked>
  <label for=\"1\">BOW</label><br>
  <input type=\"radio\" id=\"2\" name=\"sum\" value=\"2\">
  <label for=\"2\">LexSum</label><br>
  <input type=\"radio\" id=\"3\" name=\"sum\" value=\"3\">
  <label for=\"3\">Luhn</label><br>
  <input type=\"radio\" id=\"4\" name=\"sum\" value=\"4\">
  <label for=\"4\">LSA</label><br>
  <input type=\"radio\" id=\"5\" name=\"sum\" value=\"5\">
  <label for=\"5\">TextRank</label><br>
  <input type=\"radio\" id=\"6\" name=\"sum\" value=\"6\">
  <label for=\"6\">Sumbasic</label><br>
  <input type=\"radio\" id=\"7\" name=\"sum\" value=\"7\">
  <label for=\"7\">KLSum</label><br>
  <input type=\"radio\" id=\"8\" name=\"sum\" value=\"8\">
  <label for=\"8\">Reduciton</label><br>
  <input type=\"radio\" id=\"9\" name=\"sum\" value=\"9\">
  <label for=\"9\">TF-IDF</label><br><br>

  
   ''' 

        html = html + "<br><h1> Summary Level </h1><br><input name=\"thres\" id=\"thres\" type=\"range\" min=\"1\" max=\"100\" value=\"50\"><br><br><button name=\"forwardBtn\" onclick=\"move_forward()\">Submit</button></form></body></html>"

        return (html)

@app.route('/summary', methods = ['POST', 'GET'])
def summ():
    if request.method == 'POST':
        temp = ''
        data = ''
        for i in range (len(topic)-1):
            op = "op" + str(i)
            val1 = request.form.get(op)
            if val1 == str(i):
                data = data + para[i]
            temp = temp + para[i]
    
    val2 = int(request.form.get('thres'))

    op = request.form.get('sum')
    

    #summary = sumTopic(data,thres)
    if data == '':
        length = len(temp.split('.'))
        thres = int((length/100)*val2)
        if thres == 0:
            thres = 1
        summary = extra(temp,thres,int(op))
    else:
        length = len(data.split('.'))
        thres = int((length/100)*val2)
        if thres == 0:
            thres = 1
        summary = extra(data,thres,int(op))

    html = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Summary</title></head><body><h1>Your Summary : </h1><br><h4>" + str(summary) + "</h4>"
    html = html + "</body></html>"
    return(str(html))





if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)