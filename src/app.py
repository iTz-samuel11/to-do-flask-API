from flask import Flask, jsonify, request, json 

app = Flask(__name__)

todos = [{ "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    descoded_object = json.loads(request_body)
    todos.append(descoded_object)
    json_list = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_list, 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos
    print("This is the position to delete: ",position)
    new_todos = []
    for index in range(len(todos)):
        if index != position:
            new_todos.append(todos[index])
    todos = new_todos
    return jsonify(todos), 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)