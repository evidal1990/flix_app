from actors.repository import ActorRepository


class ActorService:
    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actors(self):
        return self.actor_repository.get_actors()

    def create_actor(self, name, birthday, nationality):
        actor = dict(name=name, birthday=birthday, nationality=nationality)
        return self.actor_repository.create_actor(actor)

    def get_nationalities(self):
        nationalities = self.actor_repository.get_nationalities()["nationalities"]
        if not nationalities:
            return []

        return sorted([f'{value} ({key})' for key, value in nationalities])

    def get_nationality_key(self, nationality):
        if not nationality:
            return None

        return nationality[(nationality.index("(") + 1):nationality.index(")")]
