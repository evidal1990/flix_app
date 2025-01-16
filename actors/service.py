from actors.repository import ActorRepository
import streamlit as st


class ActorService:
    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actors(self):
        if "actors" in st.session_state:
            return st.session_state.actors
        actors = self.actor_repository.get_actors()
        st.session_state.actors = actors
        return actors

    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        new_actor = self.actor_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor

    def get_nationalities(self):
        nationalities = self.actor_repository.get_nationalities()["nationalities"]
        if not nationalities:
            return []

        return sorted([f'{value} ({key})' for key, value in nationalities])

    def get_nationality_key(self, nationality):
        if not nationality:
            return None

        return nationality[(nationality.index("(") + 1):nationality.index(")")]

    def get_actors_name(self):
        actors = self.get_actors()
        if not actors:
            return []
        return {actor["name"]: actor["id"] for actor in actors}
