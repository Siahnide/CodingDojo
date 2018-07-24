

document.onkeydown = function(e) {
    
    switch(e.which){
        case 87: //up
            move("up")
            collision()
        
            break
        case 83: //down
            move("down")
            collision()
            break
        case 65: //left
            move("left")
            collision()
            break
        case 68: //right
            move("right")
            collision()
            break

    }


}

function move(direction){
    if(direction == "up" && world[char.pos.y-1][char.pos.x] == 1){
        char.pos.y --
    }
    if(direction == "down" && world[char.pos.y+1][char.pos.x] == 1){
        char.pos.y ++
    }
    if(direction == "right" && world[char.pos.y][char.pos.x+1] == 1){
        char.pos.x ++
    }
    if(direction == "left" && world[char.pos.y][char.pos.x-1] == 1){
        char.pos.x --
    }
    update()
}



function collision(){
    items = []
    
    
    for (var x=0;x<item.length;x++){
        
        b = Object.keys(item[x])[0]
        
        if (char.pos.x == item[x][b].pos.x && char.pos.y == item[x][b].pos.y){
            item[x][b].pos.x = 0
            item[x][b].pos.y = 0
            console.log("Caught by",b,"!")
            equip(b)
        }
        
    }
}



function equip(piece){
    console.log("here",piece)
    document.getElementById("map").getElementsByClassName(""+piece+"")[0].style.left= "0px"
    document.getElementById("map").getElementsByClassName(""+piece+"")[0].style.background= "transparent"
    document.getElementById("char").innerHTML += "<div class='"+piece+"'></div>"
    equipment.push(piece)
    console.log(equipment)
    update()
}



function update(){
    
    document.getElementById("char").style.left = char.pos.x * 37 + 74 + 'px' 
    document.getElementById("char").style.top = char.pos.y * 37 + 'px' 
    for(var x=0;x<equipment.length;x++){
        console.log(equipment[x])
        
        document.getElementById("char").getElementsByClassName(""+equipment[x]+"")[0].style.left = "0px"
        document.getElementById("char").getElementsByClassName(""+equipment[x]+"")[0].style.top = "0px"
        document.getElementById("map").getElementsByClassName(""+equipment[x]+"")[0].style.width = "36px"
        document.getElementById("map").getElementsByClassName(""+equipment[x]+"")[0].style.height = "36px"
        document.getElementById("map").getElementsByClassName(""+equipment[x]+"")[0].style.position = "absolute"
        document.getElementById("map").getElementsByClassName(""+equipment[x]+"")[0].style.background  = "url('../../static/game/img/char/"+equipment[x]+".png')";
        
    
    }


}

update()