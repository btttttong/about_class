from datetime import datetime, date, time

# class Person:
#     def __init__(self, name, family_name, sex):
#         self.name = name
#         # if >> name = name << will be local variable
#         self.family_name = family_name
#         self.sex = sex
#     def greeting(self):
#         return f'Hello {"Mr." if self.sex == "male" else "Miss"}'
#
# person = Person('Supakavadee BT','Rodklang', 'female')
#
# print(person.greeting())

def send_sms(msg, phone):
    """Sends a given message to a given phone via SMS.

    You don't have to implement this function.
    """
    ...


def send_email(msg, email):
    """Sends a given message to a given address as email.

    You don't have to implement this function.
    """
    ...


class Patient:
    def __init__(self, name, family_name, sex, dob, email, main_no, mobile_no):
        self.name = name
        self.family_name = family_name
        self.sex = sex
        self.dob = dob
        self.email = email
        self.main_no = main_no
        self.mobile_no = mobile_no

    def greeting(self):
        current_age = patient1.get_current_age()
        return f'{self.sex.upper()} {self.name} {self.family_name} (Age: {current_age})'
    def send_appointment_reminder(self, date):
        patientdata = patient1.greeting()
        message = f'Hello, {patientdata}, \nThis is a message from X hospital. \nYou have an appointment on {date}'
        print(message)
        send_email(message, {self.email})
        send_sms(message, {self.mobile_no})

    def get_current_age(self):
        today = datetime.today()
        diff = today - self.dob
        diff = diff.days

        years = diff // 365
        months = (diff % 365) // 30
        days = (diff % 365) % 30

        current_age = f'{years} years, {months} months, and {days} days'

        return current_age

patient1 = Patient(
    'John',
    'Doe',
    'mr.',
    datetime(1990, 2, 28),
    'john.doe@gmail.com',
    '+3345451555',
    '+6693932030',
)

# print(patient1.greeting())
# print(patient1.get_current_age())

patient1.send_appointment_reminder(datetime(2023, 10, 13, 13, 0))
