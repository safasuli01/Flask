from flask import request, render_template, redirect, url_for
from app.students import student_blueprint
from app.models import Student, db, Track
from app.tracks import track_blueprint


@student_blueprint.route('', endpoint='index' ,methods=['GET', 'POST'])
def index():
    students= Student.query.all()
    return render_template('students/index.html', students=students)

@student_blueprint.route('/create', endpoint='create', methods=['GET', 'POST'])
def create():
    tracks = Track.query.all()
    if request.method == 'POST':
        print(request.form['track_id'])
        student = Student(name=request.form["name"],
            grade=request.form["grade"],
            image=request.form["image"],
            track_id=request.form["track_id"])
        db.session.add(student)
        db.session.commit()
        return redirect(student.show_url)
    return render_template('students/create.html', tracks=tracks)

@student_blueprint.route("<int:id>", endpoint="show")
def show(id):
    student = db.get_or_404(Student, id)
    track=db.get_or_404(Track, student.track_id)
    return  render_template("students/show.html", student=student, track=track)

@student_blueprint.route('/<int:id>/delete', endpoint='delete', methods=['POST'])
def delete(id):
    student = db.get_or_404(Student, id)
    db.session.delete(student )
    db.session.commit()
    return redirect(url_for('students.index'))

@student_blueprint.route('/<int:id>/edit', endpoint='edit', methods=['GET', 'POST'])
def edit(id):
    student = db.get_or_404(Student, id)
    if request.method == 'POST':
        student.name=request.form["name"],
        student.grade = request.form["grade"],
        student.image = request.form["image"]
        db.session.commit()
        return redirect(student.show_url)
    return render_template('students/edit.html', student=student)
