from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from confirmationmail import email_sender

app = Flask(__name__)
app.config["SECRET_KEY"] = "jobapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db=SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.String(80))
    occupation = db.Column(db.String(80))

@app.route("/", methods=["GET","POST"])
def index():
    print(request.method)
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email_id = request.form["email"]
        date = request.form["date"]
        employment_status = request.form["employment"]
        form = Form(first_name=first_name,last_name=last_name,email=email_id,date=date,occupation=employment_status)
        db.session.add(form)
        db.session.commit()
        flash(f"{first_name}, your form has been submitted successfully! ","success")
        message = (f"{first_name}, your form has been submitted successfully! \nRegistration Details: "
                   f"\n{first_name} {last_name} "
                   f"\n{email_id}"
                   f"\n{date}")
        email_sender(subject="Successful Registration to Wipro Ltd.", message=message, mail_address=email_id)
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)