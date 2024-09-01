from flask import Flask, render_template, url_for, abort, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myblog.db"
db = SQLAlchemy(app)

@app.errorhandler(404)
def error_not_found(error):
    return render_template('404.html')


@app.route("/home", endpoint='landpage')
def landpage():
    posts = Post.query.all
    return  render_template('landpage.html', posts=posts)

@app.route("/posts/<int:id>", endpoint='show')
def show_post(id):
    post = Post.query.get_or_404(id)
    return render_template('show.html', post=post)

@app.route ("/posts/new", endpoint='post.new', methods=["POST", "GET"])
def new_post():
    if request.method == "POST":
        new_post = Post(
            name=request.form["name"],
            description=request.form["description"],
            image=request.form["image"])
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("landpage"))
    return render_template("new.html")

@app.route("/posts/<int:id>/remove", endpoint='post.remove', methods=['Post'])
def remove_post(id):
    post = Post.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for("landpage"))

@app.route("/posts/<int:id>/edit", endpoint='post.edit', methods= ["POST , GET"])
def post_edit(id):
    post = Post.query.get_or_404(id)
    if request.method == "POST":
        post.name = request.form["name"]
        post.description = request.form["description"]
        post.image = request.form["image"]
        db.session.commit()
        return redirect(url_for("landpage"))
    return render_template("edit.html", post=post)

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(250))
    image = db.Column(db.String(250))

    def __str__(self):
        return f"{self.name}"

    @property
    def show_url(self):
        return url_for('show', id=self.id)

    @property
    def edit_url(self):
        return url_for('post.edit', id=self.id)

    @property
    def remove_url(self):
        return url_for('post.remove', id=self.id)

    @property
    def image_url(self):
        return url_for ('static', filename=f"posts/{self.image}")

