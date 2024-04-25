from model import Model
from database import DataBase


class FaceRecognitionAPI:

    def __init__(self, model=Model, db=DataBase):
        self.model = model()
        self.db = db()

    def register_user(self, login, img):
        embedding = self.model.get_embedding(img)
        embedding = embedding.detach().cpu().numpy().flatten()
        self.db.add_user(login, embedding)
        return "User registered."

    def delete_user_data(self, login: str):
        try:
            self.db.delete_user(login)
        except KeyError:
            return "User not found."
        return "User deleted."

    def detect_user(self, img):
        embedding = self.model.get_embedding(img)
        embedding = embedding.detach().cpu().numpy().flatten()
        login = self.db.get_user(embedding)
        return login

    def compare_users(self, img1, img2):
        e1 = self.model.get_embedding(img1)
        e2 = self.model.get_embedding(img2)
        distance = self.model.compare_embeddings(e1, e2)

        return distance < 0.6

    def database_stats(self):
        return self.db.count()

    def database_clear(self):
        return self.db.clear()
