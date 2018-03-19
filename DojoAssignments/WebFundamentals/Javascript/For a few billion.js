var sum= 0.1
for (var i = 0; sum<31;i++){
    sum *=2
    console.log(sum)
}






var count = 0
for (var sum = 0.1; sum<10000;sum*=2){
    count ++
    console.log(sum)
}
console.log ("It would take",count,"many times")
var count = 0
for (var sum = 0.1; sum<1000000000;sum*=2){
    count ++
    console.log(sum)
}
console.log ("It would take",count,"many times")
for (var sum = 0.1; sum<Infinity;sum*=2){
    count ++
    console.log(sum)
}
console.log ("It would take",count,"many times")