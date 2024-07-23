grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,3,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students = sorted(students)
grades1=[sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
res={}
for key in students:
    for value in grades1:
        res[key] = value
        grades1.remove(value)
        break
print("Results" + str(res))
