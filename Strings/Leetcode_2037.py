seats = [3,1,5]
students = [2,7,4]

req = 0
seats.sort()
students.sort()
for i in range(len(seats)):
    req += abs(students[i] - seats[i])
print(req)