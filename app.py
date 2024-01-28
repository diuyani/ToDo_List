from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///todo.db" # initialize the sqlalchemy
db= SQLAlchemy(app)
app.app_context().push()

class Todo(db.Model):  
    sno = db.Column(db.Integer, primary_key  = True)
    title= db.Column(db.String(200), nullable= False)
    desc= db.Column(db.String(500), nullable= False)
    date_created= db.Column(db.DateTime,default= datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title= request.form['title']
        desc= request.form['desc']
        todo= Todo(title=title, desc=desc) #created object 
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo = allTodo ) #passing a variable here i.e allTodo. It will dispaly all todo on html 

@app.route('/update')
def update():  #function
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This is a products page'  #created a new page and routeto that page 


@app.route('/delete/<int:sno>')
def delete(sno):  #function
    allTodo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(allTodo)
    db.session.commit()
    return redirect("/")  #created a new page and routeto that page 


@app.route('/show')
def products():  #function
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This is a products page'  #created a new page and routeto that page 

if __name__== '__main__':
    app.run(debug=True)  #if you want change the port 