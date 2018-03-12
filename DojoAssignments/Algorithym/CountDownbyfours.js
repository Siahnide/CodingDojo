var x= 2016
function countdown (){
    console.log(x);
    x-=4;
    if(x !=0){
        countdown()
    }
}