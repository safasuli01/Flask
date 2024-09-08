from dominate.svg import image
from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from app.posts import post_blueprint
from app.models import Post, db, Account
from app.accounts import account_blueprint
import os


@post_blueprint.route('', endpoint='index' ,methods=['GET', 'POST'])
def index():
    posts= Post.query.all()
    return render_template('posts/index.html', posts=posts)

@post_blueprint.route('/create', endpoint='create', methods=['GET', 'POST'])
def create():
    accounts = Account.query.all()
    if request.method == 'POST':
        title = request.form.get("title")
        description = request.form.get("description")
        image = request.files.get("image")
        account_id = request.form.get("account")

        if not title or not description or not account_id:
            return "Title, description, and account are required fields.", 400

        image_name = None
        if image and image.filename:
            image_name = secure_filename(image.filename)
            image.save(os.path.join('static/posts/images/', image_name))

        post = Post(
            title=title,
            description=description,
            image=image_name,
            account_id=account_id
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.show', id=post.id))
    return render_template('posts/create.html', accounts=accounts)

@post_blueprint.route("<int:id>", endpoint="show")
def show(id):
    post = db.get_or_404(Post, id)
    account=db.get_or_404(Account, post.account_id)
    return  render_template("posts/show.html", post=post, account=account)

@post_blueprint.route('/<int:id>/delete', endpoint='delete', methods=['POST'])
def delete(id):
    post = db.get_or_404(Post, id)
    db.session.delete(post )
    db.session.commit()
    return redirect(url_for('posts.index'))

@post_blueprint.route('/<int:id>/edit', endpoint='edit', methods=['GET', 'POST'])
def edit(id):
    post = db.get_or_404(Post, id)
    if request.method == 'POST':
        post.title=request.form["title"]
        post.description = request.form["description"]
        if 'image' in request.files:
            image = request.files["image"]
            image_name = secure_filename(image.filename)
            image.save(os.path.join('static/posts/images/', image_name))
            post.image = request.files["image"]
        db.session.commit()
        return redirect(post.show_url)
    return render_template('posts/edit.html', post=post)

from app.posts.forms import PostForm

@post_blueprint.route("/form/create", endpoint="form_create", methods=["POST", "GET"])
def create_post():
    form = PostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            image_name = None
            if form.image.data:
                image = form.image.data
                image_name = secure_filename(image.filename)
                image.save(os.path.join('static/posts/images/', image_name))

            # Collect form data and remove unnecessary keys
            data = dict(request.form)
            data.pop('csrf_token', None)
            data.pop('submit', None)

            # Add the image name to the form data (if any image was uploaded)
            data["image"] = image_name

            # Create the Post object with the form data
            post = Post(**data)

            # Add to the database and commit the changes
            db.session.add(post)
            db.session.commit()

            return redirect(post.show_url)
    return  render_template("posts/forms/create.html", form=form)
