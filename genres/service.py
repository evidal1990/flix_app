from genres.repository import GenreRepository


class GenreService:

    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self):
        return self.genre_repository.get_genres()

    def create_genre(self, name):
        genre = dict(name=name)
        return self.genre_repository.create_genre(genre)

    def get_genre_by_id(self, id):
        genre = self.genre_repository.get_genre_by_id(id)
        if not genre:
            return None
        return genre["name"]

    def get_genres_name(self):
        genres = self.get_genres()
        if not genres:
            return []
        return {genre["name"]: genre["id"] for genre in genres}
