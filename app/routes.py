from flask import Flask, request         # from the flask module import the Flask class

# OOP
app = Flask(__name__)           # instantiate the Flask class into app (now an object)

mylist = []

@app.get("/")                   # Flask decorator that maps a route to a view function
def index():                    # a wrapped function is a view function in flask
    me = {
        "first_name": "Rafael",
        "last_name": "GPL",
        "hobbies": "DIY stuff",
        "is_active": True
    }
    return me                   # when you return a dictionary from a flask view function
                                # flask will automatically convert it to JSON.

@app.post("/")
def create_entry():
    raw_data = request.json
    mylist.append(raw_data)
    return "", 204


@app.get("/entries")
def get_entries():
    return mylist
