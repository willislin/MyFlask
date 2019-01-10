from flask_restplus import Api


from app.service.main import api as main_api

api = Api(
  title='Message Service API',
  version='1.0',
  description='Send Message And Get Report API',
)


api.add_namespace(main_api)
