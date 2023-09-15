"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

def create_user(name, username, password):
    """Create and return a new user."""

    user = User(name=name, 
                username=username, 
                password=password
                )

    return user


def create_movie(title, description, release_date, poster_path):
    """Create and return a new movie."""

    new_movie = Movie(title=title, 
                      description=description, 
                      release_date=release_date, 
                      poster_path=poster_path
                      )

    return new_movie


def create_rating(user, movie, score, comment):
    """Create and return a new rating."""

    rating = Rating(user=user,
                    movie=movie,
                    score=score, 
                    comment=comment
                    )
    
    return rating


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
