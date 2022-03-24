from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mystatement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Statement(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.String(50),nullable=False)
    name = db.Column(db.String(100),nullable=False)
    amount = db.Column(db.Integer,nullable=False)
    category = db.Column(db.String(50),nullable=False)

db.create_all()

@app.template_filter()
def currencyFormat(value):
    value=float(value)
    return "{:,.2f}".format(value)



@app.route("/addForm")
def addForm():
    return render_template("addForm.html")

@app.route("/addStatement",methods=['POST'])
def addStatement():
    date = request.form["date"]
    name = request.form["name"]
    amount = request.form["amount"]
    category = request.form["category"]
    statement=Statement(date=date,name=name,amount=amount,category=category)
    db.session.add(statement)
    db.session.commit()
    return redirect("/")

@app.route("/")
def showData():
    statements=Statement.query.all()
    return render_template("statements.html",statements=statements)

@app.route("/delete/<int:id>")
def deleteStatement(id):
    statement=Statement.query.filter_by(id=id).first()
    db.session.delete(statement)
    db.session.commit()
    return redirect("/")

@app.route("/edit/<int:id>")
def editStatement(id):
    statement=Statement.query.filter_by(id=id).first()
    return render_template("editForm.html",statement=statement)

@app.route("/updateStatement",methods=['POST'])
def updateStatement():
    id = request.form["id"]
    date = request.form["date"]
    name = request.form["name"]
    amount = request.form["amount"]
    category = request.form["category"]
    statement=Statement.query.filter_by(id=id).first()
    statement.date=date
    statement.name=name 
    statement.amount = amount
    statement.category=category
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)