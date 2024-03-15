class Vacancy:
    def __init__(self, name, salary, experience, roles, requirement):
        self.name = name
        self.salary = salary
        self.experience = experience
        self.roles = roles
        self.requirement = requirement

    def get_requirement(self):
        return self.requirement

    def get_name(self):
        return self.name

    def get_experience(self):
        if self.experience == 'Нет опыта':
            return 'Работодатель рассмотрит соискателей без опыта'
        return self.experience

    def get_salary(self):
        if self.salary is None:
            return f"Зарплата не указана"
        elif self.salary['from'] is None:
            return f'Зарплата до {self.salary["to"]}.{self.salary["currency"]}'
        elif self.salary['to']:
            return f'Зарплата от {self.salary["from"]}.{self.salary["currency"]} до {self.salary["to"]}.{self.salary["currency"]}'
        else:
            return f'Зарплата {self.salary["from"]}.{self.salary["currency"]}'

    def get_role(self):
        return self.roles

    def __str__(self):
        return f'{self.name}, {self.salary}, {self.experience}, {self.roles}'
