from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{ "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def get_todo():
    resp = jsonify(todos)
    return resp

@app.route('/todos', methods=['POST'])
def add_new_todo():
    result = request.get_json(force=True)
    print("Incoming request with the following body", result)
    todos.append(result)
    return_result = jsonify(todos)
    return return_result

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    del todos[position]
    return_result = jsonify(todos)
    return return_result

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)