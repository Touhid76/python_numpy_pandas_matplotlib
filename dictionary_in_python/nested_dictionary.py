#nested dictionary in python
student={
    'student1':{
        'name':'tafsir','blood':'O+'
    },
    'student2':{
        'name':'niel','blood':'A+'
    },
    'student3':{
        'name':'atik','blood':'B+'
    }

}

print(student['student1'])

#specific value from nested dictionary
print(student['student2']['blood'])

#values of a specific key from all nested dictionary
print(student['student1'].values())