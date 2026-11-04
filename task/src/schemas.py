from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    name: str=Field(max_length=20)
    last_name: str=Field(max_length=20)
    email: EmailStr= Field(max_length=40)
    phone_number: str=Field(max_length=15)
    birthday: datetime
    additional: Optional[str] = Field(default=None, max_length=500)

class ContactResponse(ContactModel):
    id: int
    class Config:
        from_attributes = True

class ContactSearch(BaseModel):
    name: Optional[str]=Field(default=None,max_length=20)
    last_name: Optional[str]=Field(default=None,max_length=20)
    email: Optional[str]= Field(default=None,max_length=40)

class ContactUpdate(ContactModel):
    pass

class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: EmailStr
    password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"

class UserLogin(BaseModel):
    email: EmailStr = Field(min_length=5, max_lenght=40)
    password:str  = Field(min_length=6, max_length=10)


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"