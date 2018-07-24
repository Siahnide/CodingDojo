
$(document).ready(function(){
    function Restart(){
        Fullness =20;
        Happiness =20;
        Meals =3;
        Energy =50;
        Refresh();
        document.getElementById("restart").innerHTML = ""
        document.getElementById("action").innerHTML = "<p></p>";
        document.getElementById("pika").style.background = "url(../images/normal.png)"
    }
    Restart();
    function Feed(){
        chance = Math.floor(Math.random() *3) + 1;
        if(Meals >0 && chance == 4){
            Meals -= 1;
            document.getElementById("action").innerHTML = "<p>You fed your Dojodachi,but they didn't seem to like it... Meals -1 </p>";
            document.getElementById("pika").style.background = "url(../images/angry.png)"
            
        }

        if(Meals >0){
            Meals -= 1;
            x = Math.floor(Math.random() *5) +5;
            Fullness += x;
            document.getElementById("action").innerHTML = "<p>You fed your Dojodachi! Fullness + " + x + " Meals -1 </p>";
            document.getElementById("pika").style.background = "url(../images/happy.png)"
            
        }
        else if(Meals == 0){
            document.getElementById("action").innerHTML = "<p>Oh No! You have no more meals!</p>";
            document.getElementById("pika").style.background = "url(../images/sad.png)"
        }
        Refresh();
    }
    function Play(){
        chance = Math.floor(Math.random() *3) + 1;
        if(Energy >0 && chance == 4 ){
            Energy -= 5;
            document.getElementById("action").innerHTML = "<p>You played with your Dojodachi,but they didn't seem to like it... Energy -5 </p>";
            document.getElementById("pika").style.background = "url(../images/angry.png)"
        }
        if(Energy>0){
            Energy -= 5;
            x = Math.floor(Math.random() *5) +5;
            Happiness += x;
            document.getElementById("action").innerHTML = "<p>You played with your Dojodachi! Happiness + " + x + " Energy -5 </p>";
            document.getElementById("pika").style.background = "url(../images/happy.png)"
            
        }
        else if (Energy == 0){
            document.getElementById("action").innerHTML = "<p>Oh No! Your Dojodachi is Tired!</p>";
            document.getElementById("pika").style.background = "url(../images/tired.png)"
            
        }
        Refresh();
    }
    function Work(){
        if(Energy >0){
            x = Math.floor(Math.random() *2) +1;
            Meals += x;
            Energy -= 5;
            document.getElementById("action").innerHTML = "<p>You worked with your Dojodachi! Meals + " + x + " Energy -5 </p>";
            document.getElementById("pika").style.background = "url(../images/happy.png)"
        }
        else if (Energy == 0){
            document.getElementById("action").innerHTML = "<p>Oh No! Your Dojodachi is Tired!</p>";
            document.getElementById("pika").style.background = "url(../images/tired.png)"
            
        }
        Refresh();
    }
    function Sleep(){
        if(Fullness >0 && Happiness >0){
            Energy += 15;
            Fullness -= 5;
            Happiness -= 5;
            document.getElementById("action").innerHTML = "<p>You rested with your Dojodachi! Energy + 15 Happiness and Fullness -5 </p>";
            document.getElementById("pika").style.background = "url(../images/happy.png)"
        }
        Refresh();
    }
    function Refresh(){
        if(Fullness <= 0){
            document.getElementById("pika").style.background = "url(../images/dead.png)";
            
            document.getElementById("action").innerHTML = "<p>Your Dojodachi Starved to death!</p>";
            document.getElementById("restart").innerHTML = "<button id='restart'>Restart</button>"
        }
        if(Happiness <= 0){
            document.getElementById("pika").style.background = "url(../images/dead.png)";
            
            document.getElementById("action").innerHTML = "<p>Your Dojodachi Ran Away!</p>";
            document.getElementById("restart").innerHTML = "<button id='restart'>Restart</button>"
        }
        if(Fullness >=100 && Happiness >=100){
            document.getElementById("pika").style.background = "url(../images/happy.png)";
            document.getElementById("action").innerHTML = "<p>You Win!</p>";
            document.getElementById("restart").innerHTML = "<button id='restart'>Restart</button>"
        }
        document.getElementById("Fullness").innerHTML = "Fullness: " + Fullness;
        document.getElementById("Happiness").innerHTML = "Happiness: " + Happiness;
        document.getElementById("Meals").innerHTML = "Meals: " + Meals;
        document.getElementById("Energy").innerHTML = "Energy: " + Energy;
    }
    
    
    $("#Feed").on("click",Feed);
    $("#Play").on("click",Play);
    $("#Work").on("click",Work);
    $("#Sleep").on("click",Sleep);
    $("#restart").on("click",Restart)
    
});
