from flask import Flask,render_template,request,jsonify
app=Flask(__name__)

@app.route('/')
def home():
    return "welcome to the home page of the script"

@app.route('/greet/<name>')
def greet(name):
    return f" hello i think your name is{name}"

@app.route('/square')
def square():
    try:
        number = int(request.args.get('number', 0))
        return jsonify({
            'number': number,
            'square': number ** 2
        })
    except ValueError:
        return jsonify({'error': 'Invalid number provided'}), 400


if __name__=='__main__':
    app.run(debug=True)