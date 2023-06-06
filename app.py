from flask import Flask,render_template,request
from flask_cors import cross_origin
import pyautogui as pg
import webbrowser as wb
import time
app = Flask(__name__)

@cross_origin()
@app.route('/')
def hello_world():
	return render_template("index_with_opening_website.html")

@cross_origin()
@app.route('/confirmation_page',methods=["POST"])
def result():
	if (request.method=='POST'):
		url=request.form['url']
		msg=request.form['msg']
		num=int(request.form['num'])
	wb.open(url)
	time.sleep(10)
	for i in range(num):
		pg.write(msg)
		pg.press("enter")
	return render_template("result_page.html")
		

	
if __name__ == '__main__':
    app.run(debug=True)
