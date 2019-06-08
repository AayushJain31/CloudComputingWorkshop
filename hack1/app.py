from flask import Flask, render_template, request
import os
app=Flask(__name__)

@app.route('/')
def hello():
	return render_template('basicform.html')

@app.route('/result', methods=['POST','GET'])
def result():
	if request.method == 'POST':
		result=request.form
		print(result['fullname'])
		contents=''
		# file = open('names.txt','r+')
		# contents=file.read()
		# contents=contents+result['fullname']+'\n'
		# file.close()
		os.chdir('..')
		os.chdir('data1')
		with open('names.txt','a+') as f:
			f.write(result['fullname']+'\n')
		f.close()
	return "Done"

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=8080)