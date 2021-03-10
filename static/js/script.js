URL = window.URL || window.webkitURL;

//pb.addEventListener("click",CheckQuality);
function CheckQuality() {

    var fixed_acidity = document.getElementById('fixed_acidity').value;
    var volatile_acidity = document.getElementById('volatile_acidity').value;
    var citric_acid = document.getElementById('citric_acid').value;
    var residual_sugar = document.getElementById('residual_sugar').value;
    var chlorides = document.getElementById('chlorides').value;
    var free_sulfur_dioxide = document.getElementById('free_sulfur_dioxide').value;
    var total_sulfur_dioxide = document.getElementById('total_sulfur_dioxide').value;
    var density = document.getElementById('density').value;
    var pH = document.getElementById('pH').value;
    var sulphates = document.getElementById('sulphates').value;
    var alcohol = document.getElementById('alcohol').value;
    var pb=document.getElementById('predict');
    console.log("checking")
    var xhr = new XMLHttpRequest();
    var answer = document.getElementById('answer');
    console.log(volatile_acidity)

    xhr.onload = function (e) {
        console.log("xhr started")
        if (this.readyState === 4) {
            console.log("recieved")
            console.log(e.target.responseText);
            answer.innerHTML = e.target.responseText;
            console.log("mmmm")

        }
    };
    

    var fd = new FormData();

    fd.append("fixed acidity", fixed_acidity);


    fd.append("volatile acidity", volatile_acidity);
    

    fd.append("citric acid", citric_acid);


    fd.append("residual sugar", residual_sugar);


    fd.append("chlorides", chlorides);


    fd.append("free sulfur dioxide", free_sulfur_dioxide);


    fd.append("total sulfur dioxide", total_sulfur_dioxide);


    fd.append("density", density);


    fd.append("pH", pH);


    fd.append("sulphates", sulphates);


    fd.append("alcohol", alcohol);


    xhr.open("POST", "/resultpage", true);
    xhr.send(fd);
}
/* code here */ 