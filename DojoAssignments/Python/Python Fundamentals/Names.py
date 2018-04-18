students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for x in range(0,len(students)):
    print students[x]['first_name'],students[x]['last_name']
print " "
print " "
print " "


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print "Students"
for x in range(0,len(users['Students'])):
    print x,"-",users['Students'][x]['first_name'],users['Students'][x]['last_name']," - ",len(users['Students'][x]['first_name']) + len(users['Students'][x]['last_name'])
print "Instructors"
for x in range(0,len(users['Instructors'])):
    print x,"-",users['Instructors'][x]['first_name'],users['Instructors'][x]['last_name']," - ",len(users['Instructors'][x]['first_name']) + len(users['Instructors'][x]['last_name'])
