






world =[ 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,4,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,0,],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
    [5],
    
]
dict = {
    0:"wall",
    1:"sand",
    2:"stonebrick",
    3:"char",
    4:"coal",
    
    
}

item = [
    {Iron_chestplate:{pos:{ x:16, y:4}}},
    {Iron_sword:{pos:{ x:16, y:10}}},
    {Iron_shield:{pos:{ x:8, y:8}}},
    
]
enemy = [

    {goblin:{pos:{ x:4, y:7}}},
    {goblin1:{pos:{ x:5, y:7}}},
    {goblin2:{pos:{ x:4, y:8}}}, 


]

char = {
    pos:{
        x:19,
        y:1
    }
}
equipment = []
x = Object.keys(item[0])[0]




function defWorld(){
    string = ""
    for(var row = 0;row<world.length;row++){
        string += "<div id='row'>"
        for(var x = 0; x<world[row].length;x++){
            string += "<div id='"+dict[world[row][x]]+"'></div>"
        }
        string +="</div>"
    }
    document.getElementById("map").innerHTML += string
    
    
    document.getElementById("char").style.left = char.pos.x * 37 + 74 + 'px' 
    document.getElementById("char").style.top = char.pos.y * 37 + 'px' 
    
    
    for (var x=0;x<item.length;x++){
        document.getElementById("map").innerHTML += "<div class="+Object.keys(item[x])[0]+"></div>"
        console.log(Object.keys(item[x])[0])
        document.getElementById("map").getElementsByClassName(""+Object.keys(item[x])[0]+"")[0].style.top = item[x][Object.keys(item[x])[0]].pos.y * 37 + 'px'  //rendering items
        document.getElementById("map").getElementsByClassName(""+Object.keys(item[x])[0]+"")[0].style.left =item[x][Object.keys(item[x])[0]].pos.x * 37 + 74 + 'px' 
        document.getElementById("map").getElementsByClassName(""+Object.keys(item[x])[0]+"")[0].style.width = "36px"
        document.getElementById("map").getElementsByClassName(""+Object.keys(item[x])[0]+"")[0].style.height = "36px"
        document.getElementById("map").getElementsByClassName(""+Object.keys(item[x])[0]+"")[0].style.position = "absolute"
        document.getElementById("map").getElementsByClassName(""+Object.keys(item[x])[0]+"")[0].style.background  = "url('../../static/game/img/char/"+Object.keys(item[x])+".png')";
    }
    for (var x=0;x<enemy.length;x++){
        document.getElementById("map").innerHTML += "<div class="+Object.keys(enemy[x])[0]+"></div>"
        console.log(Object.keys(enemy[x])[0])
        document.getElementById("map").getElementsByClassName(""+Object.keys(enemy[x])[0]+"")[0].style.top = enemy[x][Object.keys(enemy[x])[0]].pos.y * 37 + 'px'  //rendering enemys
        document.getElementById("map").getElementsByClassName(""+Object.keys(enemy[x])[0]+"")[0].style.left =enemy[x][Object.keys(enemy[x])[0]].pos.x * 37 + 74 + 'px' 
        document.getElementById("map").getElementsByClassName(""+Object.keys(enemy[x])[0]+"")[0].style.width = "36px"
        document.getElementById("map").getElementsByClassName(""+Object.keys(enemy[x])[0]+"")[0].style.height = "36px"
        document.getElementById("map").getElementsByClassName(""+Object.keys(enemy[x])[0]+"")[0].style.position = "absolute"
        document.getElementById("map").getElementsByClassName(""+Object.keys(enemy[x])[0]+"")[0].style.background  = "url('../../static/game/img/char/"+Object.keys(enemy[x])+".png')";
    }
}
defWorld()







