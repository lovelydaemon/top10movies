import os
from flask import Blueprint, render_template, redirect, request, url_for
from .forms import AddForm, EditForm
from .models import Movie, db
import requests

bp = Blueprint('movie', __name__)

# Constrains
MOVIE_LIMIT = 100
api_key = os.environ.get('MOVIE_API')
url = 'http://www.omdbapi.com'
# This should be in admin console


@bp.before_app_first_request
def create_table():
    db.create_all()


@bp.route('/')
def home():
    films = Movie.query.order_by(-Movie.rating).all()
    for index, item in enumerate(films, start=1):
        item.ranking = index
    db.session.commit()
    return render_template('index.html', films=films)


@bp.route('/find')
def find_movie():
    imdbID = request.args.get('id')
    req = requests.get(url=url, params={'apikey': api_key, 'i': imdbID})
    data = req.json()
    new_movie = Movie.create_and_commit(data)
    return redirect(url_for('.edit', id=new_movie.id))


@bp.route('/add', methods=('GET', 'POST'))
def add():
    if len(Movie.query.all()) >= MOVIE_LIMIT:
        return redirect(url_for('.home'))

    add_form = AddForm()
    if add_form.validate_on_submit():
        title = add_form.data.get('title')
        req = requests.get(url=url, params={'apikey': api_key, 's': title})
        data = req.json().get('Search')
        if data:
            return render_template('select.html', data=data)
    return render_template('add.html', form=add_form)


@bp.route('/edit', methods=('GET', 'POST'))
def edit():
    film_id = request.args.get('id')
    film = Movie.query.get_or_404(film_id)
    edit_form = EditForm(obj=film)
    if edit_form.validate_on_submit():
        film.rating = edit_form.rating.data
        film.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('.home'))
    return render_template('edit.html', film=film, form=edit_form)


@bp.route('/delete')
def delete():
    film_id = request.args.get('id')
    film = Movie.query.get_or_404(film_id)
    db.session.delete(film)
    db.session.commit()
    return redirect(url_for('.home'))
