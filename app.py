from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db = SQLAlchemy(app)

"""Creates an Task entity 

It creates an Task instance and when save returns the id
"""
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/',  methods=['POST'])
def create_task():
    task_content = request.form['content']
    new_task = Task(content=task_content)
    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue adding your task'


@app.route('/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return render_template('update.html', task=task)


@app.route('/', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.order_by(Task.date_created).all()
    return render_template('index.html', tasks=tasks)

@app.route('/update/<int:id>', methods=['POST'])
def update_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'


@app.route('/delete/<int:id>')
def delete_task(id):
    task_to_delete = Task.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'


if __name__ == "__main__":
    app.run(debug=True)