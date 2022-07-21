STUDENTS_LIMIT = 10

class Student:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'{self.name}, {self.surname}'

class Group:

    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        if student not in self.students and len(self.students) < STUDENTS_LIMIT:
            self.students.append(student)

    def __str__(self):
        res = f'--- {self.title} ---\n\n'
        res += '\n'.join(map(str, self.students))
        return res

    def __iter__(self):
        return GroupIter(self.students)

class GroupIter:
    
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        raise StopIteration

st1 = Student('Qwe', 'Wsa')
st2 = Student('Fsv', 'Rtg')
st3 = Student('Hjk', 'Poi')

group = Group('Python Course')
group.add_student(st1)
group.add_student(st2)
group.add_student(st3)

print(group)
print()

for item in group:
    print(item)
