from flask import Flask,flash, render_template, request

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def  feedbackmail(message,email,phone,name):

    subject = "DANCE ASYLUM FEEDBACK !!"
    body = str(name) +"\n"+str(email)+"\n"+ message +"\n"+ str(phone)
    sender_email = "danceasylum7@gmail.com"
    receiver_email = "danceasylum7@gmail.com"
    password = "d@nce123"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["body"] = body

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            return True
    except Exception:
            return False




app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def danceasylumhome():
    if request.method == 'POST':
        name = request.form['FullName']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        if(feedbackmail(message,email,phone,name)):
            return render_template("index.html",message="Feedback Sumbittedd !")
        else:
            return render_template("index.html", message="Invalid Credentials !")
    return render_template("index.html" )




if __name__ == '__main__':
    app.run(debug=True)