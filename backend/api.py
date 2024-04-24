import numpy as np
from typing import Union
from model import Model
from database import DataBase


class FaceRecognitionAPI:

    def __init__(self, model=Model, db=DataBase):
        self.model = model()
        self.db = db()

    def register_user(self, login: str, image: Union[str, np.array]):
        self.db.add_new_face(
                login,
                self.model.get_face_embedding(self.model.detect_face(image)))

    def update_user_info(self, login: str, image: Union[str, np.array]):
        self.db.update_face(
                login,
                self.model.get_face_embedding(self.model.detect_face(image))
        )

    def delete_user_data(self, login: str):
        self.db.delete_user(login)

    def detect_user(self, image: Union[str, np.array]):
        login = self.model.recognize_from_db(image, self.db)
        return login

    def compare_users(self, image1, image2):

        face1 = self.model.detect_face(image1)
        face2 = self.model.detect_face(image2)

        embedding1 = self.model.get_face_embedding(face1)
        embedding2 = self.model.get_face_embedding(face2)

        same = self.model.compare(embedding1, embedding2)
        return same

    def database_stats(self):
        return self.db.count()

    def database_clear(self):
        self.db.clear()
