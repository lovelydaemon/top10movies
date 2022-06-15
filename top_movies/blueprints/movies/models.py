from top_movies.database import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)

    def create_and_commit(data: dict):
        """Create Model object and commit it

        :param data: should have keys: 'Title' 'Year' 'Plot' 'Poster'
        """
        new_movie = Movie(
            title=data.get('Title'),
            year=data.get('Year'),
            description=data.get('Plot'),
            img_url=data.get('Poster')
        )
        db.session.add(new_movie)
        db.session.commit()
        return new_movie
