from flask import Flask,render_template,request

from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['Mail_PORT']= 465
app.config['MAIL_USERNAME']= "onlyspammers01@gmail.com"
app.config['MAIL-PASSWORD']= "Spammers@01"
app.config['MAIL-USE_TLS']= False
app.config['MAIL_USE_SSL']=True


mail = Mail(app)

@app.route('/')
def index():
    return render_template("Home.html")

@app.route('/Send_Message',methods=['GET','POST'])
def Send_Message():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']

        message = Message(subject,sender="onlyspammers01@gmail.com",recipients=[email])

        message.body = msg

        mail.send(message)

        success = "message sent"

        return render_template("result.html")





if __name__ == "__main__":
    app.run(debug=True)