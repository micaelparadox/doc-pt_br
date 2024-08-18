import pyotp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

secret = pyotp.random_base32()
print(f"Sua chave secreta OTP é: {secret}")

totp = pyotp.TOTP(secret)

otp = totp.now()
print(f"OTP gerado: {otp}")

def enviar_otp_por_email(email_destinatario, otp):
    remetente = "Micael Paradox <micaelparadox@gmail.com>"
    destinatario = f"Um Usuário <{email_destinatario}>"
    
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = email_destinatario
    mensagem["Subject"] = "Seu Código OTP"
    
    corpo = f"Seu OTP é: {otp}\nEste OTP expirará em 30 segundos."
    mensagem.attach(MIMEText(corpo, "plain"))

    try:
        print("Conectando ao servidor SMTP...")
        with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
            server.starttls()
            server.login("ccdedf589af33e", "3abc0311131986")
            server.sendmail(remetente, email_destinatario, mensagem.as_string())
            print(f"OTP enviado para {email_destinatario}")
    except Exception as e:
        print(f"Falha ao enviar o e-mail com OTP: {e}")

email_destinatario = "micaelparadox@gmail.com"
enviar_otp_por_email(email_destinatario, otp)

user_input = input("Digite o OTP que você recebeu: ")

if totp.verify(user_input, valid_window=1):
    print("OTP é válido!")
else:
    print("OTP inválido!")
