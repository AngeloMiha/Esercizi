import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email,
    receiver_email, subject, body, password):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server and send the
        server = smtplib.SMTP(smtp_server,
        smtp_port)
        server.starttls() # Secure the connection
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email,
        receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        # Example usage
        sender_email = "mihalacheangelo099@gmail.com"
        receiver_email = "francorcr@hotmail.com"
        subject = "Test Email del Sugoma"
        body = "sus... Sus... SUs... SUS !!!"
        password = "maTTIA2018"
        send_email(sender_email, receiver_email,
        subject, body, password)
