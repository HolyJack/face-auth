from keras.models import Model as Model_
from keras.models import Sequential
from keras.layers import (
        ZeroPadding2D,
        Convolution2D,
        MaxPooling2D,
        Dropout,
        Flatten,
        Activation
        )
from PIL import Image
import numpy as np
from matplotlib import pyplot
from typing import Union
from scipy.spatial.distance import cosine
from mtcnn.mtcnn import MTCNN


class VGGFace(Sequential):
    def __init__(self):
        super(VGGFace, self).__init__()
        self.add(ZeroPadding2D((1, 1), input_shape=(224, 224, 3)))
        self.add(Convolution2D(64, (3, 3), activation='relu'))
        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(64, (3, 3), activation='relu'))
        self.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(128, (3, 3), activation='relu'))
        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(128, (3, 3), activation='relu'))
        self.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(256, (3, 3), activation='relu'))
        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(256, (3, 3), activation='relu'))
        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(256, (3, 3), activation='relu'))
        self.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(512, (3, 3), activation='relu'))
        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(512, (3, 3), activation='relu'))
        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(512, (3, 3), activation='relu'))
        self.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(512, (3, 3), activation='relu'))
        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(512, (3, 3), activation='relu'))
        self.add(ZeroPadding2D((1, 1)))
        self.add(Convolution2D(512, (3, 3), activation='relu'))
        self.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self.add(Convolution2D(4096, (7, 7), activation='relu'))
        self.add(Dropout(0.5))
        self.add(Convolution2D(4096, (1, 1), activation='relu'))
        self.add(Dropout(0.5))
        self.add(Convolution2D(2622, (1, 1)))
        self.add(Flatten())
        self.add(Activation('softmax'))


# Модель
class Model:

    image_size = (224, 224)
    model = None

    def __init__(self):
        self.model_ready = False

        if not Model.model:
            Model.model = self.VGGFace_model()
        else:
            self.model_ready = True

    def VGGFace_model(self):
        vgg_model = VGGFace()
        vgg_model.load_weights('./misc/vgg_face_weights.h5')
        self.model_ready = True
        vgg_face_descriptor = Model_(
                inputs=vgg_model.layers[0].input,
                outputs=vgg_model.layers[-2].output
        )

        return vgg_face_descriptor

    @classmethod
    def detect_face(cls, image: Union[str, np.array]) -> np.array:
        if type(image) is str:
            image = pyplot.imread(image)

        detector = MTCNN()
        faces = detector.detect_faces(image)

        x1, y1, width, height = faces[0]['box']
        x2, y2 = x1 + width, y1 + height

        face = image[y1:y2, x1:x2]

        face_image = Image.fromarray(face)
        face_array = np.asarray(face_image)

        return face_array

    def get_face_embedding(self, image: Union[str, np.array]) -> np.array:
        if type(image) is str:
            image = pyplot.imread(image)

        img = Image.fromarray(image)
        image = np.asarray(img.resize(self.image_size)).reshape(-1, 224, 224, 3)

        embedding = self.model.predict(image)[0, :]

        return embedding

    def compare(self, image1: np.array, image2: np.array) -> int:
        if not self.model_ready:
            raise RuntimeError("Модель еще не обучена")

        if cosine(image1, image2) < 0.42:
            return 1
        return 0

    def recognize_from_db(self, image: Union[str, np.array], db) -> str:
        face = [self.get_face_embedding(self.detect_face(image))]
        for i, embedding in enumerate(db.get_all()):
            if self.compare(face, embedding):
                return db.df.login[db.df.index == i].item()

        return None
