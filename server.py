from flask import Flask, jsonify,request
import uuid


app = Flask(__name__)

@app.route("/home", methods = ["GET"])

def home():
    return {"message": "hello cohort 68"} 


@app.route("/greet-students", methods=["GET"])
def say_hi():
    return {"message":"ey hello students"}


@app.route("/cohort68", methods = ["GET"])
def get_students_68():
    students_list = ["courtney", "nico", "cole","adam","titan", "leo"]

    return students_list 

@app.route("/course-information", methods = ["GET"])
def get_course_information():
    course_information = {
        "title": "Introudction  web API with flask",
        "duration": "4 session",
        "level":"beginner"
    }
    return course_information


#-------coupons-----


coupons = [
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}]
@app.route("/api/coupons", methods = ["GET"])

def get_coupons():
    
    return coupons

@app.route("/api/coupons/count", methods = ["GET"])
def count_coupons():
    counter = len(coupons)
    return str(counter)
user_info = {
    "name":"nico",
    "position":"Student",
    "is_active": True,
    "fav_tech":["laravel",'flask']
}
@app.route("/user", methods = ["GET"])
def get_info():
    return jsonify(user_info)


@app.route("/greet/<string:name>", methods = ["GET"])
def say_hello(name):
    return jsonify({"message": f"hello {name}"}) 


products = [{
        "id"   :"1",
        "title": "Iphone 20",
        "price": 599.99,
        "category": "Electronics",
        "image": "https://picsum.photos/300/200?random=1"
        },
            {
        "id"   :"2",
        "title": "samsung s7",
        "price": 329.99,
        "category": "Electronics",
        "image": "https://picsum.photos/300/200?random=1"

        },
        {
        "id"   :"3",
        "title": "huaweii",
        "price":299.99,
        "category": "Electronics",
        "image": "https://picsum.photos/300/200?random=1"

        }
        ]


@app.route("/api/products", methods = ["GET"])
def get_products():
    return jsonify(products) 


@app.route("/api/products/<string:product_id>", methods = ["GET"])
def get_products_by_id(product_id):
    print(f"product id = {product_id}")
    for product in products:
        print(product)
        if product["id"] == product_id:
            return jsonify({
                "success":True,
                "message": "product retrieved succesfully",
                "data": product
    }),200
    return jsonify({
        "success":False,
        "message": "product not retrieved",


    }), 404
# POST http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    new_product["id"] = str(uuid.uuid4())
    products.append(new_product)
    print(new_product)

    return jsonify({
        "success": True,
        "message": "Product created successfully"
    }), 201



#--------------------------------------------------------
############# Assignment 3 #######################
#--------------------------------------------------

coupons = [
  {"id": 1, "code": "WELCOME10", "discount": 10},
  {"id": 2, "code": "SPOOKY25", "discount": 25},
  {"id": 3, "code": "VIP50", "discount": 50}]

@app.route("/api/coupons/<int:id>", methods = ["GET"])
def get_coupon_by_id(id):
    print(f"coupon id = {id}")
    for coupon in coupons:
        print(coupon)
        if coupon["id"] == id:
            return jsonify({
                "success":True,
                "message": "coupon retrieved succesfully",
                "data": coupon
    }),200
    return jsonify({
        "success":False,
        "message": "coupon not retrieved",


    }), 404

@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    new_coupon["id"] = int(uuid.uuid4())
    coupons.append(new_coupon)
    print(new_coupon)

    return jsonify({
        "success": True,
        "message": "Coupon created successfully"
    }), 201


#DELETE http://127.0.0.1:5000/api/products/<>
@app.route("/api/products/<string:product_id>", methods=["DELETE"])
def delete_product(product_id):
    print(f"the product id  is = {product_id}")
    for product in products:
        print(product["id"])
        if product["id"] == product_id:
            products.remove(product)
            return jsonify({
                "success": True,
                "message": "Product deleted successfully"
            }), 200
    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404 # not found


products = [{
        "id"   :"1",
        "title": "Iphone 20",
        "price": 599.99,
        "category": "Electronics",
        "image": "https://picsum.photos/300/200?random=1"
        },
            {
        "id"   :"2",
        "title": "samsung s7",
        "price": 329.99,
        "category": "Electronics",
        "image": "https://picsum.photos/300/200?random=1"

        },
        {
        "id"   :"3",
        "title": "huaweii",
        "price":299.99,
        "category": "Electronics",
        "image": "https://picsum.photos/300/200?random=1"

        }
        ]

#PUT http://127.0.0.1:5000/api/products/
@app.route("/api/products/<string:product_id>", methods=["PUT"])
def update_product_by_id(product_id):
    updated_product = request.get_json()
    print(updated_product)
    for product in products:
        if product["id"] == product_id:
            product["title"] = updated_product["title"]
            product["price"] = updated_product["price"]
            product["category"] = updated_product["category"]
            product["image"] = updated_product["image"]
            

            return jsonify({
                "success": True,
                "message": "Product updated successfully"
                    }), 200
    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404 # not found


#for final report
coupons = [
  {"coupon_id": 1, "code": "WELCOME10", "discount": 10},
  {"coupon_id": 2, "code": "SPOOKY25", "discount": 25},
  {"coupon_id": 3, "code": "VIP50", "discount": 50}]
@app.route("/api/coupons/<int:coupon_id>", methods=["DELETE"])
def delete_coupon_by_id(coupon_id):
    print(f"the coupon id  is = {coupon_id}")
    for coupon in coupons:
        print(coupon["coupon_id"])
        if coupon["coupon_id"] == coupon_id:
            coupons.remove(coupon)
            return jsonify({
                "success": True,
                "message": "Coupon deleted successfully"
            }), 200
    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), 404 # not found
@app.route("/api/coupons/<int:coupon_id>", methods=["PUT"])
def update_coupon_by_id(coupon_id):
    updated_coupon = request.get_json()
    print(updated_coupon)
    for coupon in coupons:
        if coupon["coupon_id"] == coupon_id:
            coupon["code"] = updated_coupon["code"]
            coupon["discount"] = updated_coupon["discount"]
            

            return jsonify({
                "success": True,
                "message": "Coupon updated successfully"
                    }), 200
    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), 404 # not found

app.run(debug=True)