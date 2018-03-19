function count(x,y,z){
   
    if(typeof z==="undefined"){
        for (var i = x;x<y;i++){
            console.log(x)
            x+=1;
        }
    }
    if (typeof z==="undefined" && typeof y==="undefined"){
        for (var i = 0;i<x;i++){
            console.log(i)
            

        }
    }

    else{
        for (var i = x;x<y;i++){
            console.log(x)
            x+=z;
               
        }      
    }

    
}