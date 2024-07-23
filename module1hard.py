#grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,3,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students = sorted(students)
grades1=[5,3,3,5,4]
grades2=[2,2,2,3]
grades3=[4,5,5,2]
grades4=[4,3,3]
grades5=[5,5,5,4,5]
student1=sum(grades1)/len(grades1)
student2=sum(grades2)/len(grades2)
student3=sum(grades3)/len(grades3)
student4=sum(grades4)/len(grades4)
student5=sum(grades5)/len(grades5)
#print(sorted(students))
grades=[student1,student2,student3,student4,student5]
res={}
for key in students:
    for value in grades:
        res[key] = value
        grades.remove(value)
        break
print("Results" + str(res))
