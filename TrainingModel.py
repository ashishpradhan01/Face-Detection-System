import cv2
import numpy as np
from PIL import Image
from os import listdir,mkdir
from os.path import isfile, join,exists, split as ossplit

class TrainingModel:
    def __init__(self):
        print("Training class")
        self.data_path = 'datasets/'
        self.face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.model = cv2.face.LBPHFaceRecognizer_create()
        self.operationCompleted = False

    def training_data(self):
        Training_data, ids= [], [] # Two Empty List
        for dir_count in range(len(listdir(self.data_path))):
            dir_name = listdir(self.data_path)[dir_count]
            face_path=str(self.data_path+str(dir_name))
            onlyfiles = [f for f in listdir(face_path) if isfile(join(face_path,f))]

            for files in onlyfiles:
                image_path = join(face_path,files)
                # print(image_path)
                # print("id: " ,ossplit(image_path)[-1].split(" ")[0])
                PIL_img = Image.open(image_path).convert('L')
                img_numpy = np.array(PIL_img,'uint8')
                temp_id = ossplit(image_path)[-1].split(" ")[0]
                # print(type(temp_id))
                if temp_id != "pp.jpg":
                    id = int(temp_id)

                face = self.face_detector.detectMultiScale(img_numpy)
                for (x,y,w,h) in face:
                    Training_data.append(img_numpy[y:y+h,x:x+w])
                    ids.append(id)
        
        return Training_data,ids

    def model_train(self):
        print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
        try:
            Training_data,ids= self.training_data()
            self.model.train(Training_data, np.array(ids))
            self.operationCompleted = True
        except Exception as debugError:
            print(f"Expection Occured: {debugError}")

        if not exists('trainer/'):
            mkdir('trainer/')
            
        self.model.write('trainer/trainedModel.yml')  #Save the model into trainer/trainer.yml
        
        

