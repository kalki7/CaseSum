from flask import Flask, render_template, request
from topic import topicExtract

app = Flask(__name__)

@app.route('/')
def indexDisp():
    return render_template('index.html')

@app.route('/topics', methods = ['POST', 'GET'])
def summaryTime():
    if request.method == 'POST':
        topic = topicExtract(request.form.get("message"))
        html = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Topics Available</title></head><body><h1>Topics : </h1>"
        
        for i in range (len(topic)):
           html = html + "<h4>" + str(i) + ". " + str(topic[i]) + "<br></h4>"

        html = html + "</body></html>"

        return (html)




if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)