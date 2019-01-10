from flask_restplus import Namespace, Resource, fields
from flask import request
from app.model import hello_model


api = Namespace('main', description='發送簡訊')

sendHello = api.model('Hello', {
  'username': fields.String(required=False, description='username'),
  #'password': fields.String(required=True, description='password'),
  'message': fields.String(required=False, description='message')
})


@api.route('/hello')
class Hello(Resource):
  @api.doc('hello')
  @api.marshal_list_with(sendHello)
  def post(self):
    '''Hello'''


    content = request.get_json()
    print('username=',content['username'],', password=',content['password'])
    helloreturnObject = hello_model.HelloReturn()
    helloreturnObject.username = content['username']
    #helloreturnObject.password = content['password']
    helloreturnObject.message = "Hello Word!!"



    return helloreturnObject
    #return None
