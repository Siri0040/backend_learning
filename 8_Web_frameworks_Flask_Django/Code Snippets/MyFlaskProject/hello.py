from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello():
	return "Hello World!"
	
@app.route("/greeting/", methods=['GET'])
@app.route("/greeting/<name>", methods=['GET'])	
def hello(name=None):
	return render_template("greet.html", name=name)

@app.route('/basic_op', methods=['POST'])
def basic_op():
    if request.method == 'POST':
        var1 = request.form['var1']
        var2 = request.form['var2']
        op = request.form['op']
        res=0
        if op == '+':
            res = int(var1)+int(var2)
        if op == '-':
            res = int(var1)-int(var2)
        if op == '*':
            res = int(var1)*int(var2)
        if op == '/':
            res = int(var1)*int(var2)
        respose_dict = {"res": res}
        return jsonify(respose_dict)
	
if __name__ == '__main__':
	app.run(debug=True)
