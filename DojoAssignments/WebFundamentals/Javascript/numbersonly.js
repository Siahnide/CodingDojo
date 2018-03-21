function numbersonly(){
    var arr = [1,2,3,"a","b","c",4,5,"d"]
    var newarr= []
for (i=0;i<arr.length;i++){
    if (typeof arr[i]=='number'){
        newarr.push(arr[i])
    }
}
console.log(newarr)
}
 