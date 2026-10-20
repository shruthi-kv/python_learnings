exam = {
    "Shruthi" : 12,
    "kv" : 23,
    "reddy" : 13
}

print(exam,type(exam))

exam["kv"] = 87

print(exam)
print(exam.keys())
print(exam.values())
print(exam.items())

exam.clear()
print(exam)


table = {i : 2*i for i in range(1,11)}
print(table)