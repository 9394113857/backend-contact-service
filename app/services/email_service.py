from flask_mail import Message
from flask import current_app

from extensions import mail

def send_contact_email(contact):

    msg = Message(
        subject="Support Request Received",

        sender=current_app.config["SUPPORT_EMAIL"],

        recipients=[contact.email]
    )

    msg.body = f"""
Hello {contact.name},

Thank you for contacting E-COMM support.

Your support request has been received.

Ticket ID:
{contact.ticket_id}

Subject:
{contact.subject}

Message:
{contact.message}

Our support/helpdesk team will contact you shortly.

Regards,
E-COMM Support Team
"""

    mail.send(msg)