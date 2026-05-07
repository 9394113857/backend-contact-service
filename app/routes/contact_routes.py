from flask import Blueprint
from flask import request
from flask import jsonify

from extensions import db

from app.models.contact_model import ContactRequest

from app.services.email_service import (
    send_contact_email
)

contact_bp = Blueprint(
    "contact_bp",
    __name__
)

@contact_bp.route(
    "/api/v1/contact/create",
    methods=["POST"]
)
def create_contact():

    try:

        data = request.get_json()

        required_fields = [
            "name",
            "email",
            "subject",
            "message"
        ]

        for field in required_fields:

            if not data.get(field):

                return jsonify({
                    "success": False,
                    "message":
                        f"{field} is required"
                }), 400

        contact = ContactRequest(

            name=data["name"],

            email=data["email"],

            subject=data["subject"],

            message=data["message"]
        )

        db.session.add(contact)

        db.session.commit()

        # SEND EMAIL
        send_contact_email(contact)

        return jsonify({

            "success": True,

            "message":
                "Contact request submitted successfully",

            "ticket_id":
                contact.ticket_id

        }), 201

    except Exception as e:

        db.session.rollback()

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500