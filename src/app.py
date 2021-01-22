from flask import Flask, jsonify, request
import json

app = Flask(__name__) #instancia del servidor Flask

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET']) #decorador
def hello_world():
    #return "<h1>Hello!</h1>"
    return jsonify(todos)
#se mostraria en gitpod en: https://3245-c181d190-54dc-4dba-a45a-442802d9cead.ws-us03.gitpod.io/todos

@app.route('/todos', methods=['POST']) #debería recibir una lista de diccionarios
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    print("Incoming request with the following body", request_body)
    if isinstance(decoded_object, list):
        for task in decoded_object:
            todos.append(task)
    elif isinstance(decoded_object, dict):
        todos.append(task)
    else:
        return "Error 400"
    #return 'Response for the POST todo'
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    return jsonify(todos)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
