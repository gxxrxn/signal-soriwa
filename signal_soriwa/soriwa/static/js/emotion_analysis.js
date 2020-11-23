
// let width = 350, height = 270;
let width = 490, height = 370;

let streaming = false;

const constraints = {
    video: { facingMode: "user", }, audio: false
};

const video = document.getElementById("videoInput");
const canvas = document.getElementById('canvasOutput');
canvas.width = width;
canvas.height = height;

let src, dst, cap;
let count = 0;

function successCallback(stream) {
    video.width = width; video.height = height;//prevent Opencv.js error.
    video.srcObject = stream;
    streaming = true;
    video.play();

    src = new cv.Mat(height, width, cv.CV_8UC4);
    dst = new cv.Mat(height, width, cv.CV_8UC1);
    cap = new cv.VideoCapture('videoInput');
    setTimeout(process, 500);
}

function errorCallback(error) {
    console.log(error);
}

navigator.getUserMedia(constraints, successCallback, errorCallback);


function process() {
    cap.read(src);
    cv.cvtColor(src, dst, cv.COLOR_RGBA2GRAY);
    cv.imshow('canvasOutput', dst);

    // uploadCanvasToServer();
    var data = canvas.toDataURL('image/jpeg', 'image/octet-stream');
    $.ajax({
        type: "POST",
        url: '/result/',
        data: {data: data},
        success: function (data) {
            let emotion = data['result'];

            console.log(emotion)
            if (emotion == 'Happy') {
                count += 1;
            }
            console.log(count)

        }
    })
    setTimeout(process, 500);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

