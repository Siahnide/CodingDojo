function count(){
    
    var students = [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
   ]
    console.log("Students")
    for (var i = 0;i<students.length;i++){
        
        console.log(i,"-",students[i].first_name,students[i].last_name,"-",students[i].first_name.length + students[i].last_name.length)
        
        
   }
   var Instructors = [ 
    {first_name:  'Michael', last_name : 'Choi'},
    {first_name : 'Martin', last_name : 'Puryear'},
]

    console.log("Instructors")
    for (var i = 0;i<Instructors.length;i++){
        
        console.log(i,"-",Instructors[i].first_name,Instructors[i].last_name,"-",Instructors[i].first_name.length + Instructors[i].last_name.length)
        
        
   }
}