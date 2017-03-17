# coding: utf-8

class Employee(object):

    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary
        self._observers = set()

    def set_salary(self, new_salary):
        self.salary = new_salary
        for observer in self._observers:
            observer(self)

    def add_observer(self, observer):
        self._observers.add(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)


class Payroll(object):

    def update(self, changed_employee):
        print('{name}のために小切手を切ります！'.format(
            name=changed_employee.name))
        print('{name}の給料は現在{salary}円，肩書は{title}です．'.format(
            name=changed_employee.name,
            salary=changed_employee.salary,
            title=changed_employee.title
        ))


class Taxman(object):

    def update(self, changed_employee):
        print('{name}に新しい税金の請求書を送ります.'.format(
            name=changed_employee.name))

if __name__ == '__main__':
    payroll = Payroll()
    taxman = Taxman()
    fred = Employee('フレッド', 'クレーン技師', 300 * 10000)
    fred.add_observer(payroll.update)
    fred.add_observer(taxman.update)
    fred.set_salary(350 * 10000)

    print('-' * 50)

    fred.remove_observer(taxman.update)
    fred.set_salary(400 * 10000)
