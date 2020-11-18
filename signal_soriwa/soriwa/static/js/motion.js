function toggleImg(e) {
    const element_name = $(e).attr('class');
    const resultElement = document.getElementsByClassName('.examplebox');
    switch (element_name) {
        case "sentence_1":
            // const item_1_img = document.getElementById("img").src = "{% static 'src/motion_gesture/greet.gif' %}";
            // resultElement.appendChild(item_1_img);
            document.getElementById("img").src = "{% static 'src/motion_gesture/greet.gif' %}";
        case "sentence_2":
            // const item_2_img = document.getElementById("img").src = "{% static 'src/motion_gesture/nicemeet.gif' %}";
            // resultElement.appendChild(item_2_img);
            document.getElementById("img").src = "{% static 'src/motion_gesture/nicemeet.gif' %}";
        case "sentence_3":
            // const item_3_img = document.getElementById("img").src = "{% static 'src/motion_gesture/hard.gif' %}";
            // resultElement.appendChild(item_3_img);
            document.getElementById("img").src = "{% static 'src/motion_gesture/hard.gif' %}";
        case "sentence_4":
            // const item_4_img = document.getElementById("img").src = "{% static 'src/motion_gesture/understand.gif' %}";
            // resultElement.appendChild(item_4_img);
            document.getElementById("img").src = "{% static 'src/motion_gesture/understand.gif' %}";
        case "sentence_5":
            // const item_5_img = document.getElementById("img").src = "{% static 'src/motion_gesture/funny.gif' %}";
            // resultElement.appendChild(item_5_img);
            document.getElementById("img").src = "{% static 'src/motion_gesture/funny.gif' %}";
        case "sentence_6":
            // const item_6_img = document.getElementById("img").src = "{% static 'src/motion_gesture/thank.gif' %}";
            // resultElement.appendChild(item_6_img);
            document.getElementById("img").src = "{% static 'src/motion_gesture/thank.gif' %}";
        case "sentence_7":
            // const item_7_img = document.getElementById("img").src = "{% static 'src/motion_gesture/takecare.gif' %}";
            // resultElement.appendChild(item_7_img);
            document.getElementById("img").src = "{% static 'src/motion_gesture/takecare.gif' %}";
        case "sentence_8":
            // const item_8_img = document.getElementById("img").src = "{% static 'src/motion_gesture/seenext4.gif' %}";
            // resultElement.appendChild(item_8_img);
            document.getElementById("img").src = "{% static 'src/motion_gesture/seenext4.gif' %}";
        case "sentence_9":
            // const item_9_img = document.getElementById("img").src = "{% static 'src/motion_gesture/love.gif' %}";
            // resultElement.appendChild(item_9_img);
            document.getElementById("img").src = "{% static 'src/motion_gesture/love.gif' %}";
    }

};