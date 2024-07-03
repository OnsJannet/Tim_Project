from models.base_model import BaseModel
from hashlib import sha256

"""a class User that inherits from BaseModel"""


class User(BaseModel):
    """a class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    user_types = ["manager", "sales", "accounting", "commercial"]

    def __init__(self, *args, **kwargs):
        """initialize a User instance"""
        super().__init__(*args, **kwargs)
        self.collection = "users"
        if len(args) != 0:
            for k, v in args[0].items():
                if k == "user_type":
                    self.set_user_type(v)
                if k  == "password":
                    self.set_password(v)
                setattr(self, k, v)


    def __str__(self):
        """returns a string representation of a User instance"""
        return "({}) ({}) {} {}".format(self.collection , self._id, self.first_name, self.last_name)

    def check_password(self, pwd):
        """checks if a password matches the password of the user"""
        return sha256(pwd.encode()).hexdigest() == self.password

    def set_password(self, pwd):
        """sets the password of the user"""
        self.password = sha256(pwd.encode()).hexdigest()

    def set_user_type(self, user_type):
        """sets the _type of the user"""
        if user_type in self.user_types:
            self.__dict__["user_type"] = user_type
        else:
            raise ValueError("{} is not a valid user type".format(user_type))
