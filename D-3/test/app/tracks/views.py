from app.tracks import  track_blueprint
from app.models import  db, Track
from flask import  render_template, request, redirect, url_for

@track_blueprint.route('', endpoint='index')
def index():
    tracks = Track.query.all()
    return render_template("tracks/index.html", tracks=tracks)

@track_blueprint.route('/create', endpoint='create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        track = Track(name=request.form['name'])
        db.session.add(track)
        db.session.commit()
        return redirect(url_for('tracks.index'))
    return render_template("tracks/create.html")

@track_blueprint.route('/<int:id>', endpoint='show', methods=['GET'])
def show(id):
    track = db.get_or_404(Track, id)
    return render_template("tracks/show.html", track=track)


