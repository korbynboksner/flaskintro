from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)


@app.route("/<operation>")
def handle_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if operation == 'add':
        result = add(a, b)
        return str(result)
    
    elif operation == 'sub':
        result = sub(a, b)
        return str(result)
    
    elif operation == 'mult':
        result = sub(a, b)
        return str(mult)
    
    elif operation == 'div':
        result = sub(a, b)
        return str(div)
    
    else:
        return None
    