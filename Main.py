from datetime import datetime
from flask import redirect, request
from flask import CORS
from flask import OpenAPI, Info, Tag
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError

from model import Dress, Session
from schemas import DressSchema, ErrorSchema
from schemas.DressSchema import show_dress, DressViewSchema

info = Info(title="Dress Store API", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)


@app.get('/')
def home():
    """TESTE
    """
    return redirect('/openapi')


@app.post('/dress',
          responses={"200": DressViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_dress(form: DressSchema):
    dress = Dress(
        size=form.size,
        color=form.color,
        price=form.price)

    try:
        session = Session()
        session.add(dress)
        session.commit()
        return show_dress(dress), 200

    except IntegrityError as e:
        error_msg = "Dress Id already exists in databse."
        return {"Message": error_msg}, 409

    except Exception as e:
        error_msg = "Failure while registering the dress."
        return {"Message": error_msg}, 400
