from marshmallow import Schema, fields


class HelloReturn(Schema):
  username = fields.Str()
  password = fields.Str()
  message = fields.Str()