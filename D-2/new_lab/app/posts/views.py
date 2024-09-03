from flask import request, render_template, redirect, url_for
from app.posts import post_blueprint
from app.models import Post, db

@post_blueprint.route('', endpoint='index' ,methods=['GET', 'POST'])
def index():
    posts= Post.query.all()
    return render_template('posts/index.html', posts=posts)

@post_blueprint.route('/create', endpoint='create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        post = Post(
            title=request.form["title"],
            description=request.form["description"],
            image=request.form["image"],
        )
        db.session.add(post)
        db.session.commit()
        return redirect(post.show_url)
    return render_template('posts/create.html')

@post_blueprint.route('/<int:id>', endpoint='show', methods=['GET'])
def show(id):
    post = db.get_or_404(Post, id)
    return render_template('posts/show.html', post=post)

@post_blueprint.route('/<int:id>', endpoint='delete', methods=['POST'])
def delete(id):
    post = db.get_or_404(Post, id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.index'))

@post_blueprint.route('/<int:id>/edit', endpoint='edit', methods=['GET', 'POST'])
def edit(id):
    post = db.get_or_404(Post, id)
    if request.method == 'POST':
        post.title = request.form["title"]
        post.description = request.form["description"]
        post.image = request.form["image"]
        db.session.commit()
        return redirect(post.show_url)
    return render_template('posts/edit.html', post=post)
