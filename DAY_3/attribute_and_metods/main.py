
class UserProfile:

    def setup_profile(self, username, email):
        self.username = username,
        self.email = email,
        self.is_active = True


    def display_detailes(self):
        status = "Active" if self.is_active else "Inactive"

        print(f"User : {self.username} | Email : {self.email} | Status : {status}")




u1 = UserProfile()

u1.setup_profile("Chirag","chiragjogi@gmail.com")

print(f"Direct Attribute Access -> Username: {u1.username}")
u1.display_detailes()