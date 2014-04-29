from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello, World!"

@app.route('/rob')
def say_my_name():
	return "Hello, I'm rob!!"
 
if __name__ == '__main__':
	app.run(port=1337)