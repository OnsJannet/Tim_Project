from models.base_model import BaseModel
from models.user import User

x = User()
#test the USER class
user = {
    "email": "test",
    "password": "test",
    "first_name": "test",
    "last_name": "test",

}
x = User(user)
x.set_user_type("manager")
x.set_password("test")

x.save()

print(x.to_dict())
