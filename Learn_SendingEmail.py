# import small mail transfer protocol(SMTP), which will handle sending e-mail
# and routing e-mail between mail servers

import smtplib

# SMTP object has an instance method called sendmail, which will typically be
#  used for mailing a message. It takes three parameters:  the sender, the
# receivers, and the message

# For security purpose I have omitted the e-mail address and password. Please put a valid
# email address and password to see it works

def send_email_alart():

    sender = 'xxxxxxxxx@gmail.com'
    # must be a list
    receivers = ["xxxxxxxx@gmail.com", "xxxxxxxxxxxxx@yahoo.com", "xxxxxxxx@tlgaerospace.com"]

    # must have an empty line before the actual message
    message = """ From: Shahin Nahar <shahin.nahar@tlgaerospace.com>
    To: shahin1 <xxxxxxx@yahoo.com>, shahin2 <xxxxxxx@gmail.com>
    Subject: SMTP e-mail test

    This is a test message to see if it works!!!
    """
    # Credentials
    username = 'xxxxxxxxx@gmail.com'
    password = 'xxxxxxxxxx'

    # The actual mail send
    try:
        # sending the message via g-mail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(sender, receivers, message)
        server.quit()
        print "Successfully sent email"
    except Exception, error:
        print "Unable to send email: '%s'. "%str(error)


# The main function to call the other methods to activate
def main():
    send_email_alart()

if __name__ =='__main__':
    main()



