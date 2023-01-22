from flask import Flask, jsonify, request



app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
    todosJson= jsonify(todos)
    return todosJson


@app.route('/todos', methods=['POST'])
def add_new_todo():
    label=request.json.get('label')
    done=request.json.get('done')
    todo = { "label": label, "done": done }
    todos.append(todo)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)











if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)