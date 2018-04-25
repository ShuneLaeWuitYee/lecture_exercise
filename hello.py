from flask import Flask , render_template 
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	user = {'name': name} 
	return render_template('hello.html', user=user)

@app.route('/users/')
def users():
	names=['simon','thomas','lee','jamie','sylvester']
	return render_template('hello.html', names=names)

@app.route('/inherits/') 
def inherits(): 
 	return render_template('base.html') 
 
@app.route('/inherits/one/') 
def inherits_one():
 	return render_template('inherits1.html') 
 
@app.route('/inherits/two/')
def inherits_two():
 	return render_template('inherits2.html') 

@app.route('/bootstrap/')
def bootstrap():
	return render_template('bos.html'), 200

if __name__ == "__main__": 
	app.run(host='0.0.0.0', debug=True)
