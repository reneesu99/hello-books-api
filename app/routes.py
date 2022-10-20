from flask import Blueprint, jsonify

hello_world_bp = Blueprint("hello_world", __name__)
@hello_world_bp.route("/hello_world", methods = ["GET"])
def hello_world_response():
    return "Hello, World"

@hello_world_bp.route("/hello/JSON", methods = ["GET"])
def hello_json_response():
    response = {
                "name": "Renee Su",
                "message": "Hello!",
                "hobbies": ["Skateboarding", "Running", "Video Games"]
                }
    return response

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body


# Books section

class Book():
    def __init__(self, id, title, desc):
        self.id = id
        self.title = title
        self.description = desc

books = [Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")]



books_bp = Blueprint("books", __name__, url_prefix = "/books")

# get all books
@books_bp.route("", methods = ["GET"])
def get_all_books():
    books_cleaned = []
    for book in books:
        item = {"id": book.id, "title": book.title, "description": book.description}
        books_cleaned.append(item)
    return jsonify(books_cleaned)