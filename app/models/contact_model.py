from extensions import db

from datetime import datetime

import uuid

class ContactRequest(db.Model):

    __tablename__ = "contact_requests"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    ticket_id = db.Column(
        db.String(100),
        unique=True,
        nullable=False,
        default=lambda:
            f"TICKET-{uuid.uuid4().hex[:8].upper()}"
    )

    name = db.Column(
        db.String(255),
        nullable=False
    )

    email = db.Column(
        db.String(255),
        nullable=False
    )

    subject = db.Column(
        db.String(255),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default="OPEN"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):

        return {
            "ticket_id": self.ticket_id,
            "name": self.name,
            "email": self.email,
            "subject": self.subject,
            "message": self.message,
            "status": self.status
        }