from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/register", methods=['POST'])
def register():
	print(request.form)
	#TODO: create block?
	#TODO: make changes to frontend to acknowledge registration
	return render_template('index.html')

@app.route("/transfer", methods=['POST'])
def transfer():
	print(request.form)
	#TODO: backend stuff
	#TODO:make changes to html
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
