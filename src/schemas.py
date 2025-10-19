# src/schemas.py
from marshmallow import Schema, fields, validate

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=64))

class InvestimentoSchema(Schema):
    nome = fields.String(
        required=True,
        validate=validate.Regexp(r"^[\w\s\-\.,]{1,60}$", error="Nome contém caracteres inválidos."),
    )
    risco = fields.String(required=True, validate=validate.OneOf(["baixo", "medio", "alto"]))
