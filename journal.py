class UniversityMember:
    '''Представляет любого человека в университете'''

    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def getName(self):
        return self._name

    def getSurname(self):
        return self._surname

    def getFullName(self):
        return '{0} {1}'.format(self._name, self._surname)


class Student(UniversityMember):
    '''Класс студента
        Обобщение    '''
    students_number = 0  # классовая переменная для подсчета студентов

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.__stuff = []
        self.__marks = []
        Student.students_number += 1  # счётчик числа студентов

    def add_stuff(self, new_stuff):
        self.__stuff.append(new_stuff)

    def getStuff(self):
        return self.__stuff

    def setNumber(self, new_number):
        self.__number = new_number

    def getNumber(self):
        return self.__number

    def setGroup(self, new_group):
        self.__group = new_group

    def getGroup(self):
        return self.__group

    def add_marks(self, new_mark):
        self.__marks.append(new_mark)

    def getMarks(self):
        return self.__marks


class RecordBook:
    '''Зачетная книжка
                Бинарная ассоциация           '''

    def __init__(self, number):
        self.__number = number

    def getNumber(self):
        return self.__number


class AcademicDiscipline:
    '''Учебная дисциплина
       N-арная ассоциация'''

    def __init__(self, stuff):
        self.__stuff = stuff

    def getStuff(self):
        return self.__stuff


class Group:
    '''Агрегация'''

    def __init__(self, title):
        self.__title = title
        self.__students = []

    def getTitle(self):
        return self.__title

    # добавление студентов в список группы
    def add_students(self, new_student):
        self.__students.append(new_student)

    # исключение студентов из списка группы
    def remove_students(self, new_student):
        self.__students.remove(new_student)

    # показывает список студентов в группе
    def getStudents(self):
        return self.__students


class AcademicPerformance:
    '''Композиция'''

    def __init__(self, marks):
        self.__marks = marks

    def getMarks(self):
        return self.__marks


class Menu:
    '''Зависимость(связь с классом Группа)'''

    def __init__(self, students=[]):
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_students(self, student):
        if student not in self.students:
            self.students.append(student)

    def student_list(self):
        for student in self.students:
            print(student)


if __name__ == '__main__':

    # Бинарная ассоциация
    student1 = Student('Кривошеин', 'Илья')
    student2 = Student('Боровской', 'Алексей')
    new_card1 = RecordBook(123)
    new_card2 = RecordBook(321)
    student1.setNumber(new_card1)
    student2.setNumber(new_card2)
    print("Студент: {0} {1} / номер студенческого билета: {2}".format(
        student1.getName(), student1.getSurname(), student1.getNumber().getNumber()))
    print("Студент: {0} {1} / номер студенческого билета: {2}".format(
        student2.getName(), student2.getSurname(), student2.getNumber().getNumber()))
    print()

    # N-арная ассоциация
    stuff1 = AcademicDiscipline('Языки программирования')
    stuff2 = AcademicDiscipline('Физика')
    student1.add_stuff(stuff1.getStuff())
    student1.add_stuff(stuff2.getStuff())
    print('{} изучает дисциплины: {}'.format(
        student1.getFullName(), '; '.join(student1.getStuff())))
    print()

    # Агрегация
    group1 = Group('748')
    group1.add_students(student1)
    group1.add_students(student2)
    student1.setGroup(group1)
    student2.setGroup(group1)
    print("Студент: {0} {1} из группы № {2}".format(
        student1.getName(), student1.getSurname(), student1.getGroup().getTitle()))
    print("Студент: {0} {1} из группы № {2}".format(
        student2.getName(), student2.getSurname(), student2.getGroup().getTitle()))
    print()

    # Композиция
    marks = [AcademicPerformance(4).getMarks(),
             AcademicPerformance(5).getMarks()
             ]
    marks = float(sum(marks)/len(marks))
    new_mark = AcademicPerformance(marks)
    student1.add_marks(new_mark.getMarks())
    print("Студент {0} имеет средний балл {1}".format(
        student1.getFullName(), student1.getMarks()))
    print()

    # Зависимость
    menu = Menu()
    menu.add_students(student1.getFullName())
    menu.add_students(student2.getFullName())
    print("Список студентов:")
    print(menu.student_list())
