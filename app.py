from flask import Flask, render_template, request, redirect, url_for, flash
import os
import smtplib
from email.message import EmailMessage



app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()


app.secret_key = os.getenv('SECRET_KEY')
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        print(request.form)
        product = request.form.get('productSelect')
        number = request.form.get('number')
        date_start = request.form.get('date-start')
        date_end = request.form.get('date-end')
        deposit = request.form.get('deposit')
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('content')
        if not all([product,number, date_start, date_end, deposit,  name, email, message]):
            flash("Please fill in all fields", category="error")
            return render_template('index.html', productSelect=product,number=number, date_start=date_start, date_end=date_end, deposit=deposit,  name=name, email=email, content=message)
        else:
            send_email(product,number, date_start, date_end, deposit,  name, email, message)
            flash("Feedback submitted successfully!", category="success")
            title = email = content = ""
        # flash('Your request has been submitted successfully!', 'success')


            return redirect(url_for('home'))
    else:
        return render_template('index.html')


def send_email(product,number, date_start, date_end, deposit,  name, email, message ):
    # scootalong2024 @ gmail.com
    email_sp = 'gail_grant_knight@yahoo.co.uk,waynebruton@icloud.com'
    smtp_server = os.getenv('SMTP_SERVER')
    port = os.getenv('SMTP_PORT')
    sender_email = os.getenv('SENDER_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')

    message = f"""
                <html>
                  <body>
                    <p>Dear Gail and Grant,<br>
                    <br>
                    A new Rental enquiry has been received:<br>
                    <br>
                    <b>Lead Details</b><br>
                    <br>
                    <b>Name:</b> {name}<br>
                    <b>Product:</b> {product}<br>
                    <b>Number:</b> {number}<br>
                    <b>Est Start Date:</b> {date_start}<br>
                    <b>Est End Date:</b> {date_end}<br>
                    <b>Deposit:</b> {deposit}<br>
                    <br>


                    <b>Email:</b> {email}<br>
                    <b>Message:</b> {message}<br>
                    <br>
                    Kind Regards<br>

                  </body>
                </html>
                """

    msg = EmailMessage()
    msg['Subject'] = "Rental Enquiry"
    msg['From'] = sender_email
    msg['To'] = email_sp
    msg.set_content(message, subtype='html')

    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.ehlo()
            server.login(sender_email, password=password)
            server.send_message(msg)
            return {"message": "Email sent successfully"}
    except Exception as e:
        print("Error:", e)
        return {"message": "Email not sent"}

# @app.route('/about')
# def about():
#     return render_template('about.html')


# @app.route('/products')
# def products():
#     return render_template('products.html')


# @app.route('/services')
# def services():
#     return render_template('services.html')


# @app.route('/news')
# def news():
#     return render_template('news.html')


# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         # Handle form submission
#         pass
#     return render_template('contact.html')





if __name__ == '__main__':
    app.run(debug=True)
