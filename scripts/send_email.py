import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
sender_email = "doanvu10492@@gmail.com"
app_password = "xxxx"
receiver_email = "doanvu10492@@gmail.com"

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python 3"

# Email body
body = "Hello, this is a test email sent via Python 3 SMTP!"
message.attach(MIMEText(body, "plain"))

# Connect to Gmail SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # Secure the connection
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")

