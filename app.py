from flask import Flask,request,jsonify
from flask_restful import Api,Resource
from pymongo import MongoClient
import urllib.parse
import json


app = Flask(__name__)
app.secret_key = 'audbgsj'
api = Api(app)

username = urllib.parse.quote_plus("test@123")
password = urllib.parse.quote_plus("ecommerce")


DB_URI = "mongodb+srv://test:{0}@cluster0.08uix.mongodb.net/{1}?retryWrites=true&w=majority".format(username,password)


client = MongoClient(DB_URI)
db = client.ecommerce
prod = db["products"]


def retRes(status,message):
    retMap = {
            'status': status,
            'message': message
    }
    return retMap
    

def retData(status,data):
    retMap = {
            'status': status,
            'data': json.dumps(data,default=str)
    }
    return retMap


class ProductsList(Resource):
    def get(self):
        product_data= []
        for i in prod.find():
            product_data.append(i)
        return jsonify(retData(status = 200, data = product_data))


    def post(self):
        content = request.json
        if len([content]) == 1:
            prod.insert_one(content)
        else:
            prod.insert_many(content)
        return jsonify(retRes(status = 200, message = "Data Added Successfully"))
    

class Product(Resource):
    def get(self,name):
        my_query = {'name':name}
        data = []
        for i in prod.find(my_query):
            data.append(i)
        return jsonify(retData(status = 200, data = data))
    

    def put(self,name):
        my_query = {'name':name}
        content = request.json
        newvalues = {"$set": content}
        prod.update_one(my_query,newvalues)
        return jsonify(retRes(status = 200, message = "Product Data Updated Successfully"))


    def delete(self,name):
        my_query = {'name':name}
        prod.delete_one(my_query)
        return jsonify(retRes(status = 200, message = "Product deleted Successfully"))

class ProductBrand(Resource):
    def get(self,brand_name):
        my_query = {'brand_name':brand_name}
        data = []
        for i in prod.find(my_query):
            data.append(i)
        return jsonify(retData(status = 200, data = data))
    

class ProductCurrency(Resource):
    def get(self,currency):
        my_query = {'currency':currency}
        print(my_query)
        data = []
        for i in prod.find(my_query):
            data.append(i)
        return jsonify(retData(status = 200, data = data))


class Populate(Resource):
    def post(self):
        f = open("Greendeck SE Assignment Task 1.json",'r')
        data = json.load(f)
        prod.insert_many(data)
        return jsonify(retRes(status = 200, message = "Data Added Successfully"))




api.add_resource(Product,'/api/product/<string:name>',endpoint = 'product')
api.add_resource(ProductBrand,'/api/product/brand/<string:brand_name>',endpoint = 'brand')
api.add_resource(ProductCurrency,'/api/product/currency/<string:currency>',endpoint = 'currency')
api.add_resource(ProductsList,"/api/products",endpoint = 'products')
api.add_resource(Populate,"/api/populate",endpoint = 'populate')


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5001)