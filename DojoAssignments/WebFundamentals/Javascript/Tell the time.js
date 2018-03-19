function time(x,y,z){
if(y<30){
    console.log("It's Just after",x, "in the",z,".")
}
else if(y>29){
    x++;
    console.log("It's almost",x,"in the",z,".")
}
}
time(1,35,"morning")
