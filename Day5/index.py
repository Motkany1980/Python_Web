import datas

# for n in range(0,len(datas.students_scores)):
#     print(datas.students_scores[n])
    
max_number=0    
for student in datas.students_scores:
    if int(max_number) <= int(student):
        max_number=student
print(f'''The highest student score is : {max_number}''')
        