import smtplib
import os
import myEnv
myEnv.setVar()
from email.mime.text import MIMEText


def send_email():
    sender = "mymewtwo@gmail.com"
    # password = "your password"
    password = os.environ.get('EMAIL_PASSWORD')
    email_to =  # список получателей сообщения

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        with open("email_template.html", encoding='utf-8') as file:
            template = file.read()
    except IOError:
        return "The template file doesn't found!"

    try:
        server.login(sender, password)
        msg = MIMEText(template, "html")
        msg["From"] = sender
        msg["To"] = # список получателей сообщения
        msg["Subject"] = "От Москаленко В.С. - скрипт рассылки"
        server.sendmail(sender, email_to, msg.as_string())

        return "Сообщение отправлено!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    print(send_email())


if __name__ == "__main__":
    main()