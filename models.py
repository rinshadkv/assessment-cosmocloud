from pydantic import BaseModel, Field, validator

class Address(BaseModel):
    city: str = Field(..., description="The city where the student resides")
    country: str = Field(..., description="The country where the student resides")

class Student(BaseModel):
    name: str = Field(..., description="The name of the student", min_length=1)
    age: int = Field(..., description="The age of the student", gt=0)
    address: Address

    @validator('address')
    def address_must_contain_city_and_country(cls, v):
        if not (v.city and v.country):
            raise ValueError("Both city and country must be provided")
        return v

class StudentDTO(BaseModel):
    name: str = Field(..., description="The name of the student", min_length=1)
    age: int = Field(..., description="The age of the student", gt=0)   