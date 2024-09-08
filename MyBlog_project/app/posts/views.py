from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from app.posts import post_blueprint
from app.models import Post, db, Account
import os
from app.posts.forms import PostForm

@post_blueprint.route('', endpoint='index', methods=['GET', 'POST'])
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

@post_blueprint.route('/create', endpoint='create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        image_name = None
        if form.image.data:
            image = form.image.data
            image_name = secure_filename(image.filename)
            image.save(os.path.join('static/posts/images/', image_name))

        post = Post(
            title=form.title.data,
            description=form.description.data,
            image=image_name,
            account_id=form.account_id.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.show', id=post.id))
    return render_template('posts/create.html', form=form)

@post_blueprint.route('/<int:id>', endpoint='show')
def show(id):
    post = db.get_or_404(Post, id)
    account = db.get_or_404(Account, post.account_id)
    return render_template('posts/show.html', post=post, account=account)

@post_blueprint.route('/<int:id>/delete', endpoint='delete', methods=['POST'])
def delete(id):
    post = db.get_or_404(Post, id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.index'))

@post_blueprint.route('/<int:id>/edit', endpoint='edit', methods=['GET', 'POST'])
def edit(id):
    post = db.get_or_404(Post, id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.description = form.description.data
        if form.image.data:
            image = form.image.data
            image_name = secure_filename(image.filename)
            image.save(os.path.join('static/posts/images/', image_name))
            post.image = image_name
        post.account_id = form.account_id.data
        db.session.commit()
        return redirect(post.show_url)
    return render_template('posts/edit.html', form=form, post=post)
