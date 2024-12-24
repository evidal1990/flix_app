from actors.repository import ActorRepository


class ActorService:
    def __init__(self):
        self.__actor_repository = ActorRepository()

    def get_actors(self):
        return self.__actor_repository.get_actors()

    def create_actor(self, name, birthday, nationality):
        actor = dict(name=name, birthday=birthday, nationality=nationality)
        return self.__actor_repository.create_actor(actor)

    def get_nationalities(self):
        nationalities_dict = self.__actor_repository.get_nationalities()["nationalities"]
        nationalities = []
        for nationality in nationalities_dict:
            nationalities.append(nationality[0])
        return nationalities
