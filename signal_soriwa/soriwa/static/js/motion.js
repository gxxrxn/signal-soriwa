
// let width = 350, height = 270;
// let width = 490, height = 370;

const constraints = {
    video: { facingMode: "user", }, audio: false
};

const video = document.getElementById("videoInput");

function successCallback(stream) {
    // video.width = width; video.height = height;//prevent Opencv.js error.
    video.srcObject = stream;
    video.play();
}

function errorCallback(error) {
    console.log(error);
}

navigator.getUserMedia(constraints, successCallback, errorCallback);


