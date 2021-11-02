from flask import Flask, render_template, request, url_for, flash, redirect
import os, datetime
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'you secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    nome = db.Column(db.String(80), nullable=False)
    bairro = db.Column(db.String(30), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(20), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

def get_post(post_id):
    post = Posts.query.filter_by(id=post_id).first()
    if post is None:
        abort(404)
    return post

@app.route('/sobre')
def sobre():
    posts = Posts.query.all()
    return render_template('sobre.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/cadastrar', methods=('GET', 'POST'))
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        email = request.form['email']

        if not nome:
                flash('Todos os campos são obrigatórios!')
        elif not bairro:
            flash('Todos os campos são obrigatórios!')
        elif not cidade:
            flash('Todos os campos são obrigatórios!')
        elif not email:
            flash('Todos os campos são obrigatórios!')

        else:
                post = Posts(nome=nome, bairro=bairro, cidade=cidade, email=email)
                db.session.add(post)
                db.session.commit()
                return redirect(url_for('index'))

    return render_template('cadastrar.html')

@app.route('/doar', methods=('GET', 'POST'))
def doar():
    posts = Posts.query.all()
    return render_template('doar.html', posts=posts)
def filtro():
    if request.method == 'GET':
       db.query.filter(db.bairro.endswith('@example.com')).all()
       return render_template('filtro.html', posts=posts)

