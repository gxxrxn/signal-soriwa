from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from soriwa.faceCam import FaceCamera
from soriwa.motionCam import MotionCamera

# Create your views here.
def main(request):
    return render(request, 'main.html')

def emotion(request):
    return render(request, 'emotion.html')

def motion(request):
    return render(request, 'motion.html')

def face(request):
    return render(request, 'face.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def face_video(request):
    return StreamingHttpResponse(gen(FaceCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

def motion_video(request):
    return StreamingHttpResponse(gen(MotionCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
