from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de tarefas (inicialmente vazia)
tasks = []

# Rota para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' in data:
        task = {
            'id': len(tasks) + 1,
            'title': data['title'],
            'done': False
        }
        tasks.append(task)
        return jsonify({'message': 'Tarefa criada com sucesso!'}), 201
    else:
        return jsonify({'error': 'O campo "title" é obrigatório!'}), 400

# Rota para atualizar uma tarefa pelo ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['done'] = data.get('done', task['done']) # Atualiza o status da tarefa
            return jsonify({'message': 'Tarefa atualizada com sucesso!'})
    return jsonify({'error': 'Tarefa não encontrada!'}), 404

# Rota para excluir uma tarefa pelo ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({'message': 'Tarefa excluída com sucesso!'})
    return jsonify({'error': 'Tarefa não encontrada!'}), 404

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
