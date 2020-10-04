# rest-api-products

API allows user to perform basic CRUD operations.

# Installation 

### Clone the repository
> git clone https://github.com/devvsaurabh/rest-api-products.git

### Build Docker image
> docker build -t rest_api_products:app .

### Install with Docker
> docker run -p 5001:5001 -d rest_api_products:app


# Usage

This is an example of running a service locally (localhost), using port 5051.

## Access API on localhost with the given link :
> http://0.0.0.0:5001/api/

## API Endpoints

| Endpoint | URL | Methods | 
| -------- | --- | ------- | 
| products | http://0.0.0.0:5001/api/products | ['GET','POST'] | 
| populate | http://0.0.0.0:5001/api/populate | ['POST'] |
| product  | http://0.0.0.0:5001/api/product/<<string:name>> | ['GET','PUT','DELETE'] |
| brand | http://0.0.0.0:5001/api/product/brand/<<string:brand_name>> | ['GET'] |
| currency | http://0.0.0.0:5001/api/product/currency/<<string:currency>> | ['GET'] |

#


| Endpoint | Method | Description |
| -------- | ------ | ----------- | 
| products | GET | Returns all the products details |
| products | POST | Inserts product data into the database |
| populate | POST | Insert the product data from json file (Used to populate data into db initially) |
| product | GET | Returns the product details by passing product name |
| product | PUT | Updates product details by passing product name |
| product | DELETE | Deletes a product by passing product name |
|brand | GET | Returns product details of a particular brand |
| currency | GET | Returns product details with a given currency |


## REST API
#
Detailed overview of the API with input and output samples in POSTMAN

### Get list of all Products
#
### Request
`GET /api/products`
> http://0.0.0.0:5001/api/products

### Response
![ ](https://github.com/devvsaurabh/rest-api-products/blob/main/img/all_data.png?raw=true)


### Create new product
#
### Request
`POST /api/products`
> http://0.0.0.0:5001/api/products

### Response
![ ](https://github.com/devvsaurabh/rest-api-products/blob/main/img/post_data.png?raw=true)



### Get product using product name
#
### Request
`GET /api/product/<string:name>`
> http://0.0.0.0:5001/api/product/Simon Carter Laser Engraved Button Cufflinks, Gunmetal

### Response
![ ](https://github.com/devvsaurabh/rest-api-products/blob/main/img/get_product.png?raw=true)


### Update product details
#
### Request
`PUT /api/product/<string:name>`
> http://0.0.0.0:5001/api/product/Simon Carter Laser Engraved Button Cufflinks, Gunmetal

### Response
![ ](https://github.com/devvsaurabh/rest-api-products/blob/main/img/update_data.png?raw=true)


### Delete the product
#
### Request
`DELETE /api/product/<string:name>`
> http://0.0.0.0:5001/api/product/Simon Carter Laser Engraved Button Cufflinks, Gunmetal

### Response
![ ](https://github.com/devvsaurabh/rest-api-products/blob/main/img/delete_data.png?raw=true)


### Get the products with brand name
#
### Request
`DELETE /api/product/brand/<string:name>`
> http://0.0.0.0:5001/api/product/brand/icandy

### Response
![ ](https://github.com/devvsaurabh/rest-api-products/blob/main/img/brand.png?raw=true)


### Get the products with currency
#
### Request
`GET /api/product/currency/<string:name>`
> http://0.0.0.0:5001/api/product/currency/GBP

### Response
![ ](https://github.com/devvsaurabh/rest-api-products/blob/main/img/currency.png?raw=true)










