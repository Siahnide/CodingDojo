function birthday (x){
if(x>0){
    x--;
    setTimeout(birthday,500)
}
else{
    console.log("HAPPY BIRTHDAY!")
}
}
birthday (20)