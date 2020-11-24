import tensorflow as tf
from soriwa.kerasyolo3.yolo import YOLO
import cv2
import numpy as np
import os

class Detection(object):
    def __init__(self):
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        sess = tf.Session(config=config)  # 중요코드
        res_path = os.getcwd()
        self.emotion_yolo = YOLO(model_path=str(res_path) + '/soriwa/trained_weights_final.h5',
                            anchors_path='~/Desktop/signal-soriwa/signal_soriwa/soriwa/kerasyolo3/model_data/yolo_anchors.txt',
                            classes_path='~/Desktop/signal-soriwa/signal_soriwa/soriwa/class.txt')

        self.frame_cnt = 0
        self.labels = {}


    def get_class(self, image): # yolo 코드

        img = cv2.imdecode(np.fromstring(image, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        original_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        target, label_dic = self.emotion_yolo.detect_image(original_image)

        self.frame_cnt += 1

        for label in label_dic:
            if label in self.labels and label_dic[label] > self.labels[label]:
                self.labels[label] = label_dic[label]
            elif label not in self.labels:
                self.labels[label] = label_dic[label]

        result = ''
        if self.frame_cnt >= 2:
            if len(self.labels) == 0:
                print('pass!!')
                self.frame_cnt = 0
                self.labels = {}

                return result

            # 딕셔너리가 튜플로 바뀜
            self.labels = sorted(self.labels.items(),
                                 reverse=True,
                                 key=lambda item: item[1])

            # print('🎉class labels: ', self.labels)

            result = self.labels[0][0]

            # neutral 확률이 높게 나와서 조절하기 위한 부분..
            index = 0
            score_sub = 0
            top_two = []
            for tuple in self.labels:
                label = tuple[0]
                score = tuple[1]

                if index > 1:
                    break

                if index == 0 and label != 'neutral':
                    break

                if index == 0:
                    top_two.append(label)
                    score_sub = score
                elif index == 1:
                    top_two.append(label)
                    score_sub -= score

                index += 1

            # print(top_two, score_sub)

            if score_sub > 0.2:
                result = top_two[0]
            elif score_sub < -0.2:
                result = top_two[1]

            print('✨', result)

            self.frame_cnt = 0
            self.labels = {}


        # print('✨', result)
        return result

