


var world = [
    [1,1,1,1,1,1,1,1,1,1,1,1], //each number is a block
    [1,2,0,0,0,2,2,0,0,0,2,1],
    [1,0,1,1,2,1,1,2,1,1,0,1],
    [1,0,0,0,0,3,3,0,0,0,0,1],
    [1,0,1,1,2,1,1,2,1,1,0,1],
    [1,2,0,0,0,2,2,0,0,0,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
        ];
var worldDict = {
    0: 'element1',
    1: 'element2',
    2: 'element3',
    3: 'element4',
    

}
function drawWorld() {
    output = ""

    for (var row = 0; row < world.length; row++) {
        output += "<div class = 'row'>"

        for (var x = 0; x < world[row].length; x++) {
            output += "<div class = '" + worldDict[world[row][x]] + "'></div>"
        }
        output += '</div>'
    }

    document.getElementById('world').innerHTML = output; // requires div class and id for define
}
drawWorld()