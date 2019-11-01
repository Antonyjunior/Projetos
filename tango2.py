from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import pymysql
import json

connection = pymysql.connect(user='root',
                             password='L33tsupah4x0r',
                             host='localhost',
                             db='tango',
                             cursorclass=pymysql.cursors.DictCursor)


app = Flask(__name__)
api = Api(app)


class Products(Resource):
    def get(self):
        with connection.cursor() as cursor:
            query = "SELECT * FROM tango.product"
            cursor.execute(query)
            result = cursor.fetchall()
        return jsonify(result)

    def post(self):
        data = json.loads(request.data)
        name = data['name']
        description = data['description']
        with connection.cursor() as cursor:
            query = f"Insert Into product (product_name, product_description) Values('{name}', '{description}')"
            cursor.execute(query)
            connection.commit()
            query_result = "SELECT * FROM Product"
            cursor.execute(query_result)
            result = cursor.fetchall()
        return jsonify(result)


class ProductsById(Resource):
    def get(self, id):
        try:
            with connection.cursor() as cursor:
                query = f"select * from tango.product where product_id = {id}"
                cursor.execute(query)
                result = cursor.fetchone()
            return jsonify(result)
        except TypeError as e:
            return f"Error on id type: {e}", 400
        
    def delete(self, id):
        with connection.cursor() as cursor:
            cursor.execute("delete from product where product_id=%d " % int(id))
            connection.commit()
            cursor.execute("SELECT * FROM Product")
            result = cursor.fetchall()
        return jsonify(result)
        

    def put(self,id):
        
        data = json.loads(request.data)
        name = data['name']
        description = data['description']

        with connection.cursor() as cursor:
            
            query = "update product set product_name ='" + str(name) + \
                  "', product_description ='" + str(description) + "'  where product_id =%d " % int(id)
            cursor.execute(query)
            connection.commit()
            cursor.execute("SELECT * FROM Product")
            result = cursor.fetchall()
        return jsonify(result)


    
api.add_resource(Products, '/product')
api.add_resource(ProductsById, '/product/<id>')

if __name__ == '__main__':
    app.run()