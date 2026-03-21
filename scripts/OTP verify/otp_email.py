import random
import smtplib
import ssl
from email.message import EmailMessage
from config import Config

def generate_otp(length=6):
	digits = "0123456789"
	return "".join(random.choices(digits, k=length))

def send_otp(receiver_email, otp):
		message = EmailMessage()
		message["Subject"] = "Your OTP Code"
		message["From"] = Config.SENDER_EMAIL
		message["To"] = receiver_email
		message.set_content(f"{otp} is your OTP")

		context = ssl.create_default_context()

		with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
			server.starttls(context=context)
			server.login(Config.SENDER_EMAIL, Config.APP_PASSWORD)
			server.send_message(message)

def verify_otp(sent_otp):
	user_otp = input("Enter your OTP: ").strip()

	if user_otp == sent_otp:
		print("Verified")
	else:
		print("Incorrect OTP")


def main():
	email = input("Enter your email: ").strip()

	otp = generate_otp()
	send_otp(email, otp)

	print("OTP send successfully.")
	verify_otp(otp)

if __name__ == "__main__":
	main()