from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
import base64

from django.template.loader import render_to_string
from soriwa.Detection import Detection

# Create your views here.
global detection
detection = None

def main(request):
    return render(request, 'main.html')

def emotion(request):
    global detection
    if detection is None:
        detection = Detection()

    return render(request, 'emotion.html')

def motion(request):
    return render(request, 'motion.html')

def menu(request):
    return render(request, 'menu.html')

def game(request):
    return render(request, 'game/index.html')

def result(request):
    global detection

    emotion = {'happiness':'Happy', 'sadness':'Sad', 'anger':'Angry', 'fear':'Fear', 'surprise':'Surprise', 'neutral':'Neutral', '':'. . .'}
    result = '. . .'

    try:
        data = request.POST.__getitem__('data')
        data = data[22:]
        img = base64.b64decode(data)
        result = emotion[detection.get_class(img)]
    except:
        pass
    return JsonResponse({'result': result})

def emotion_analysis(request):
    global detection
    if detection is None:
        detection = Detection()

    return render(request, 'emotion_analysis.html')

def analysis_result(request):
    print(request)
    if request.method == 'POST':
        print(' post!')
        count = request.POST.__getitem__('count')
        print(count)
        return HttpResponse(render_to_string('analysis_result.html', {'count': count}))

    return render(request, 'analysis_result.html', {'count': '?'})

# def gen_motion(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# def face_video(request):
#     Emotion.objects.create(
#         emotion='. . .'
#     )
#     return StreamingHttpResponse(gen(FaceCamera()), content_type='multipart/x-mixed-replace; boundary=frame')

# def get_emotion(request):
#     result = Emotion.objects.get(pk=1).emotion
#     print('fromModel : ', result)
#     return HttpResponse(json.dumps({'emotion': result}), content_type='application/json')

# def motion_video(request):
#     return StreamingHttpResponse(gen_motion(MotionCamera()), content_type='multipart/x-mixed-replace; boundary=frame')

# def gen_for_analysis(camera):
#     laugh_cnt = 0
#     LaughChallenge.objects.create(
#         count=0
#     )
#     LaughChallenge.objects.filter(pk=1).update(
#         count=0
#     )
#
#     while True:
#         result = camera.challengeStart();
#
#         if result:
#             print('❤❤', result)
#
#         if result == 'happiness':
#             laugh_cnt += 1
#
#             LaughChallenge.objects.filter(pk=1).update(
#                 count=laugh_cnt
#             )
#
#             print('     ✨', laugh_cnt)
#             # yield laugh_cnt

# def get_analysis_result(request):
#     result = LaughChallenge.objects.get(pk=1).count
#     print('     ❤', result)
#     return HttpResponse(json.dumps({'count': result}), content_type='application/json')

