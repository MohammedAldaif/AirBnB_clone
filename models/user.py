class User(BaseModel):
    def init(self, email, password, first_name, last_name):
        self.email = str(email)
        self.password = str(password)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
