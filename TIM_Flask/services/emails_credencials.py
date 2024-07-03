"""python script to send a login by mail"""
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string


def generate_login_credentials():
    """Generate login credentials for user"""
    login_credentials = {}
    login_credentials["password"] = "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(10)
    )
    return login_credentials["password"]
def send_login_by_mail(email, username, password):
    """send login by mail"""
    port = 465  # For SSL
    smtp_server = "mail45.lwspanel.com"
    sender_email = "noreply_managx@devinov.fr"
    receiver_email = email
    passwd = "mE7*$2gAQ-N2T8g"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Login credentials"
    message["From"] = sender_email
    message["To"] = receiver_email
    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    Here are your login credentials:
    Username: """ + username + """
    Password: """ + password
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           Here are your login credentials:<br>
           <ul>
             <li>Username: """ + username + """</li>
             <li>Password: """ + password + """</li>
           </ul>
           <p>Please, visit <a href="https://managx.devinov.fr">managx.devinov.fr</a> to access to ManagX or change your password.</p>
           <br>
           <br>
           Thank you for using Managx.<br>
           <br>
           -Managx team
        </p>
        <p> Managx is a project management tool that helps you to manage your projects
            and track your co-workers withoout any waste of time.
                Developed by <a href="https://devinov.fr">Devinov</a>
        </p>
      </body>
    </html>
    """
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port=port, context=context) as server:
        server.login(sender_email, passwd)
        try:
          server.sendmail(
              sender_email, receiver_email, message.as_string()
          )
        except:
          return False
    return True


def send_confirmation_by_mail(email, username):
    """send login by mail"""
    port = 465  # For SSL
    smtp_server = "mail45.lwspanel.com"
    sender_email = "noreply_managx@devinov.fr"
    receiver_email = email
    passwd = "mE7*$2gAQ-N2T8g"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Account Creation"
    message["From"] = sender_email
    message["To"] = receiver_email
    # Create the plain-text and HTML version of your message
    text = """\
      Hi """+ username + """!
      Thank you for signing up for our ManageX services<br>
      To get you started, please click on the link below to log in to your account for the first time.
      <a href="https://managx.devinov.fr">managx.devinov.fr</a><br>
      If you didn’t submit your email address to join our subscriber list, please ignore this message.
      Regards,<br>
      The Devionv support team
      """
    html = """\
    <html>
      <body>
        <p>Hi """+ username + """!<br>
           Thank you for signing up for our ManageX services<br>
           To get you started, please click on the link below to log in to your account for the first time.
           <a href="https://managx.devinov.fr">managx.devinov.fr</a><br>
            If you didn’t submit your email address to join our subscriber list, please ignore this message.
            Regards,<br>
            The Devionv support team
        </p>
        <p> Managx is a project management tool that helps you to manage your projects
            and track your co-workers withoout any waste of time.
                Developed by <a href="https://devinov.fr">Devinov</a>
        </p>
      </body>
    </html>
    """
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port=port, context=context) as server:
        server.login(sender_email, passwd)
        try:
          server.sendmail(
              sender_email, receiver_email, message.as_string()
          )
        except:
          return False
    return True