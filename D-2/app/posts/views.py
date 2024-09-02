from flask import render_template, request, url_for, redirect, Blueprint
from app.posts import  post_blueprint
from app.models import Post, db

@post_blueprint.route('', endpoint='landpage')
def landpage():
    posts = Post.query.all()
    return render_template('landpage.html', posts=posts)

@post_blueprint.route("<int:id>", endpoint="show")
def show_post(id):
    post = db.get_or_404(Post, id)
    return render_template("show.html", post=post)

@post_blueprint.route('new', endpoint='new', methods= ['POST','GET'])
def new_post():
    if request.method == 'POST':
        post = Post (
            name=request.form['name'],
            image=request.form['image'],
            description=request.form['description'],
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post.show_url'))
    return render_template('new.html')

@post_blueprint.route("<int:id>/edit", endpoint="edit", methods=["GET", "POST"])
def post_edit(id):
    post = db.get_or_404(Post, id)
    if request.method == "POST":
        posts = post
        post.name = request.form["name"]
        post.image = request.form["image"]
        post.description = request.form["description"]
        db.session.add(posts)
        db.session.commit()
        return redirect(url_for("landpage"))
    return render_template("update.html", post=post)

@post_blueprint.route("<int:id>/remove", endpoint="remove")
def remove_post(id):
    post = db.get_or_404(Post, id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("landpage"))