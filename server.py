from flask import Flask


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
app.run(debug=True)