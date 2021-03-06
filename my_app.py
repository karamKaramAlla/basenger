from flask import Flask,jsonify,request,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "test"


@app.route("/process",methods=["get","post"])
def process():
    email=request.form['email']
    name=request.form['name']
    
    if  name and email:
        newName=name[::-1]

        return jsonify({'name':newName})
    return jsonify({'error':'missingData'})


if __name__ == '___main__':
    app.run(debug=False,port=1000)