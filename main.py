from flask              import Flask,url_for,flash,redirect,request
from flask_sqlalchemy   import SQLAlchemy
from flask_bcrypt       import Bcrypt
from datetime           import datetime
from flask              import render_template
from flask_login        import LoginManager,UserMixin,login_user,current_user,logout_user,login_required


app=Flask(__name__)
app.config['SECRET_KEY']='3bb2be46'
app.config['0']='sqlite:///database.db'
sqlite=SQLAlchemy(app)
login=LoginManager(app)
bcrypt=Bcrypt(app)
login.login_view                =   "dashboard"
login.login_message_category    =   "message"


class User(sqlite.Model,UserMixin):
    id=sqlite.Column("id",sqlite.Integer,primary_key=True)
    user_name=sqlite.Column(sqlite.String(25),unique=True,nullable=False)
    email = sqlite.Column(sqlite.String(100), unique=True, nullable=False)
    password=sqlite.Column(sqlite.String(50),nullable=False)
    posts = sqlite.relationship("Posts", backref="writer", lazy=True)

    def __repr__(self):
        return f"User('{self.user_name}','{self.email}')"

class Posts(sqlite.Model, UserMixin):    
    id = sqlite.Column(sqlite.Integer, primary_key=True)
    user_id = sqlite.Column(sqlite.Integer, sqlite.ForeignKey('user.id'))
    sender  = sqlite.Column(sqlite.String(25),nullable=False) 
    posts=sqlite.Column(sqlite.String(2000),nullable=False)

    def __repr__(self):
        return f"Posts('{self.posts}','{self.sender}')"

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#start facebook alternative{
@app.route('/',methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route("/signup")
def signup():
    return  render_template("signup.html") 

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/posts")
def posts():
    return render_template("posts.html")
#end facebook alternative}


#todo whatsapp alternative:

if __name__ == '__main__':
    app.run(port=5000,debug=True)