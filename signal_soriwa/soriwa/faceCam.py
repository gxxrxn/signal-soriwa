import cv2
import tensorflow as tf
from soriwa.kerasyolo3.yolo import YOLO

class FaceCamera(object):
    def __init__(self):
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        sess = tf.Session(config=config)  # 중요코드

        self.emotion_yolo = YOLO(model_path='C:/Users\kkr12\signal-soriwa/signal_soriwa/soriwa/trained_weights_final.h5',
                            anchors_path='~/signal-soriwa/signal_soriwa/soriwa/kerasyolo3/model_data/yolo_anchors.txt',
                            classes_path='~/signal-soriwa/signal_soriwa/soriwa/class.txt')

        self.video = cv2.VideoCapture(0)
        self.frame_cnt = 0
        self.labels = {}

    def __del__(self):
        self.video.release()

    def get_frame(self): # yolo 코드
        success, image = self.video.read()
        original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        target, label_dic = self.emotion_yolo.detect_image(original_image)
        self.frame_cnt += 1

        # print(label_dic)
        frame_flip = cv2.flip(image, 1)
        ret, jpeg = cv2.imencode('.jpg', frame_flip)
        # target, class_name = self.emotion_yolo.detect_image(jpeg)

        for label in label_dic:
            if label in self.labels and label_dic[label] > self.labels[label]:
                self.labels[label] = label_dic[label]
            elif label not in self.labels:
                self.labels[label] = label_dic[label]

        result = ''
        if self.frame_cnt >= 10:
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
        return [jpeg.tobytes(), result]

    def get_frame_origin(self): # yolo 코드
        success, image = self.video.read()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_flip = cv2.flip(image, 1)
        ret, jpeg = cv2.imencode('.jpg', frame_flip)

        return jpeg.tobytes()

    def challengeStart(self):
        success, image = self.video.read()
        original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        target, label_dic = self.emotion_yolo.detect_image(original_image)
        self.frame_cnt += 1


        # print(label_dic)

        for label in label_dic:
            if label in self.labels and label_dic[label] > self.labels[label]:
                self.labels[label] = label_dic[label]
            elif label not in self.labels:
                self.labels[label] = label_dic[label]

        result = ''
        if self.frame_cnt >= 10:
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

            # print('✨', result)

            self.frame_cnt = 0
            self.labels = {}

        return result
