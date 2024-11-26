class BaseRepository:
    def __init__(self, running_session):
        self.session = running_session
