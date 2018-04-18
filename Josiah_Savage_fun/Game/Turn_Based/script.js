
$(document).ready(function(){
    
    
    var map = {
        pos:[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            
        ],
        def:{
            'a':'space',
            0:'blank',
            1:'wall',
        }
    }
    var char={
        heavy:{
            name:'Heavy',
            hp:20,
            armor:3,
            dmg:3,
            speed:4,
            x:3,
            y:3,
            facing:direction
        },
        BlueK:{
            name:"Medium",
            hp:15,
            armor:2,
            dmg:5,
            speed:5,
            x:3,
            y:3,
            facing:direction
        },
        GreenK:{
            name:"Light",
            hp:10,
            armor:1,
            dmg:4,
            speed:7,
            x:3,
            y:3,
            facing:direction
        },
        caster:{
            name:"Caster",
            hp:8,
            armor:2,
            dmg:6,
            speed:6,
            x:3,
            y:3,
            facing:direction
        }
        
    }
    
    var direction = "left",step=1,activePlayer='BlueK'
    var moves=char[activePlayer].speed
    
    
    function start(){
        defMap()
        $('body').append("<div id='"+activePlayer+"'></div>")
        defPlayer()
        defChar()
        defTurn()
    }
    function update(){
        $('body').append("<div id='"+activePlayer+"'></div>")
        
        defPlayer()
        defChar()
        defTurn()
    // defMap()
}
function defMap(){
    var map_str =""
    for (var i=0;i<map.pos.length;i++){
        map_str +="\n<div class='row'>"
        for (var j=0;j<map.pos[i].length;j++){
            map_str += "\n\t<div class=" +map.def[map.pos[i][j]]+ "></div>"
        }
        map_str += "\n</div>"
    }
    document.getElementById('map').innerHTML = map_str;
}

function defPlayer(){
    

    document.getElementById(""+activePlayer+"").style.top = char[activePlayer].y * 30 + 'px';
    document.getElementById(""+activePlayer+"").style.left = char[activePlayer].x * 30 + 'px' ;
    document.getElementById(""+activePlayer+"").style.backgroundImage = "url('img/"+activePlayer+"/step"+direction+""+step+".png')"

}

function defChar(){
    var char_str=""
    char_str += "<h1>"+char[activePlayer].name+"</h1>"
    char_str += "<img src='img/"+activePlayer+"/step"+direction+""+step+".png'>"
    char_str += "<p>Armor:"+char[activePlayer].armor+"</p>"
    char_str += "<p>HP:"+char[activePlayer].hp+"</p>"
    char_str += "<p>Speed:"+char[activePlayer].speed+"</p>"
    char_str += "<p>Damage:"+char[activePlayer].dmg+"</p>"
    $('#charsheet').html(char_str)
}
function defTurn(){
    var turn_str=""
    turn_str="<h1>Moves:"+moves+"</h1>"
    $('#turnsheet').html(turn_str)
}

document.onkeydown = function(e){
                console.log(e.keyCode)
                switch (event.which){
                    case 49:
                    activePlayer = 'BlueK';
                    moves=char[activePlayer].speed

                    update()
                    
                    break;
                    case 50:
                    activePlayer = 'GreenK';
                    moves=char[activePlayer].speed

                    update()
                    break;
                    case 13: //enter
                    start()
                   
                    break;
                    case 87: //w up
                    if(map.def[map.pos[char[activePlayer].y-1][char[activePlayer].x]]!='wall' && moves>0 && char[activePlayer].pos.x !=char){
                    char[activePlayer].y--;
                    direction = 'up';
                    moves--;
                    if(step==1){
                        step=2
                        update()
                        break
                    }
                    else if (step=2){
                        step=1
                        update()
                        break
                    }
                    break;
                    }

                    case 68: //d right
                    if(map.def[map.pos[char[activePlayer].y][char[activePlayer].x+1]]!='wall' && moves>0 && char[activePlayer].pos.x !=char){
                        char[activePlayer].x++;
                        direction = 'right';
                        moves--;
                    if(step==1){
                        step=2
                        update()
                        break
                    }
                    else if (step=2){
                        step=1
                        update()
                        break
                    }
                        
                    }
                      break;  
                    case 83: //s down
                    if(map.def[map.pos[char[activePlayer].y+1][char[activePlayer].x]]!='wall' && moves>0 && char[activePlayer].pos.x !=char){
                        char[activePlayer].y++;
                        direction = 'down';
                        moves--;
                    if(step==1){
                        step=2
                        update()
                        break
                    }
                    else if (step=2){
                        step=1
                        update()
                        break
                    }
                    }
                    break;
                    case 65: //a left
                    if(map.def[map.pos[char[activePlayer].y][char[activePlayer].x-1]]!='wall' && moves>0 && char[activePlayer].pos.x !=char){
                        char[activePlayer].x--;
                        direction = 'left';
                        moves--;
                    if(step==1){
                        step=2
                        update()
                        break
                    }
                    else if (step=2){
                        step=1
                        update()
                        break
                    }
                    break;
                    }
                }
            }


});
