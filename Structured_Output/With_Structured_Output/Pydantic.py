from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class review(BaseModel):
    name:str
    age:Optional[int] = 18      #optional value for age , user can pass or it will be 18 by default
    hobby:str = 'football'     #default value for hobby , doesnt need to be passed by user
    email:EmailStr
    CGPA:float = Field(gt=0, lt=10,default=9,description="CGPA of the student") #greater than 0 and less than 10

student = {"name":"John", "age":30, "email":"john@example.com", "CGPA":8.5}

response = review(**student)

print(student)
print(type(student))
print(response)
print(type(response)) 