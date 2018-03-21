function random(quarters){
    var prize = 0

    for(var i = quarters; i>0;i--){
        var z = quarters - i
        var x = Math.trunc(Math.random()*100)+1
        console.log(x)

        if(x==100){
            prize++;
        }  
    }

    if(prize>0){
        return("You won "+prize+" prizes!")

    }
    else{
    return("Aww too bad.")
    }
}