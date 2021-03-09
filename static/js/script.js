
var fixed_cidity = document.getElementById('acidity');
var volatile_acidity = document.getElementById('volatile acidity');
var citric_acid = document.getElementById('citric acid');
var residual_sugar = document.getElementById('residual_sugar');
var chlorides = document.getElementById('chlorides');
var free_sulfur_dioxide = document.getElementById('free_sulfur_dioxide');
var total_sulfur_dioxide = document.getElementById('total_sulfur_dioxide');
var density = document.getElementById('density');
var pH = document.getElementById('pH');
var sulphates = document.getElementById('sulphates');
var alcohol = document.getElementById('alcohol');

function CheckQuality() {
    var xhr = new XMLHttpRequest();

    xhr.onload = function (e) {

        if (this.readyState === 4) {
            console.log(e.target.responseText);

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


    xhr.open("POST", "/result", true);
    xhr.send(fd);
}
{"input_data": [{"fields": ["fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol"],"values":[[7,0.27,0.36,20.7,0.045,45,170,1.001,3,0.45,8.8]]}