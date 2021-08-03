# Importing module

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from variables import MY_ADDRESS
from variables import MY_PASSWORD


# First we need to retrive contacts from a file

def get_contact(filen):
    emails = []
    with open(filen, mode="r", encoding="utf-8") as contact_file:
        for contact in contact_file:
            emails.append(contact)
    return emails


# Now we'r searching the msg in a message file ( Quite the same as get_contact() )

def get_message(filen):
    with open(filen, mode="r", encoding="utf-8") as message_file:
        msg = message_file.read()
    return msg


def main():
    # Retrive info
    emails = get_contact("contact.txt")
    msg = get_message("message.txt")

    # Setting up the Simple Mail Transfer Protocol server
    server = smtplib.SMTP(host= "smtp.gmail.com", port= 587)
    server.starttls()
    server.set_debuglevel(0) # Turn it to 1 to have a debug in logs
    server.login(MY_ADDRESS, MY_PASSWORD)

    # Now let's send the mail
    for email in emails:
        message = MIMEMultipart()   # Creating a message

        # Setting up the message
        message["From"] = MY_ADDRESS
        message["To"] = email
        message["Subject"] = "Test"

        # Adding the message body
        message.attach(MIMEText(msg, 'plain'))

        server.send_message(message) # Time to send the message


        # I'm deleting the message object each time I iterate the loop
        del message

        print("Mail sent to: " + email)



if __name__ == "__main__":
    main()