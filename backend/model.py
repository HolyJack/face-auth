from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
import os
from PIL import Image


class Model:
    def __init__(self):
        self.workers = 0 if os.name == 'nt' else 4
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        print('Running on device: {}'.format(self.device))
        self.mtcnn = MTCNN(
            image_size=160, margin=0, min_face_size=20,
            thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True,
            device=self.device
        )

        self.resnet = InceptionResnetV1(pretrained='vggface2').eval().to(self.device)
        self.resnet.classify = False

    def get_crop(self, img, save_path=None):
        # Get cropped and prewhitened image tensor
        img_cropped = self.mtcnn(img)
        return img_cropped

    def get_embedding_from_crop(self, img_cropped):
        # Calculate embedding (unsqueeze to add batch dimension)
        return self.resnet(img_cropped.unsqueeze(0))

    def get_embedding(self, img):
        img_cropped = self.get_crop(img)
        return self.get_embedding_from_crop(img_cropped)

    def get_distance(self, e1, e2):
        return (e1 - e2).norm().item()


if __name__ == '__main__':
    model = Model()

    img = Image.open("./photo.jpg")
    e1 = model.get_embedding(img)

    print(e1.size())
    print(type(e1))
    numpy_e1 = e1.detach().cpu().numpy()
    print(numpy_e1.size)
    print(type(numpy_e1))
    tuple_e1 = tuple(numpy_e1)
    print(tuple_e1[0])
