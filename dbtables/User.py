class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.__email = email

    def get_email(self):
        return self.__email

    def set_password(self, password):
        pass
