from pydantic import BaseModel, field_validator, EmailStr, ValidationError, Field
from datetime import datetime, timedelta

class Event(BaseModel):
    title: str
    date: datetime
    location: str

    @field_validator('date')
    def validate_date(cls, v):
        if v < datetime.now():
            raise ValueError('date must be not before today')
        return v

try:
    event = Event(title='restaurants', date="2025-04-03 14:05:03", location='NY' )
    print(event)
except ValueError as e:
    print(e)

class UserProfile(BaseModel):
    username: str
    password: str = Field(..., min_length=8, description="Password must be more then 8")
    email: EmailStr

try:
    user = UserProfile(username="Tom", password="12345678", email="tom.gmail.com")
    print(user)
except ValueError as e:
    print(e)

class Transaction(BaseModel):
    amount: int = Field(..., ge = 0,  description="positiv value" )
    transaction_type: str = Field(..., pattern=r'^(debit|credit)$')
    currency: str

try:
    trans = Transaction(amount=100, transaction_type="debit", currency="USD")
    print(trans)
except ValueError as e:
    print(e)

class Appointment(BaseModel):
    appointment_date: datetime
    patient_name: str

    @field_validator("appointment_date")
    def validate_patient_name(cls, v):
        if v < datetime.now() + timedelta(days=1):
            raise ValueError('appointment_date must be more then tomorrow')
        return v

try:
    appoin = Appointment(appointment_date=(datetime.now() + timedelta(days=3)), patient_name="Tom")
    print(appoin)
except ValueError as e:
    print(e)


from sqlalchemy import create_engine, declarative_base
Base = declarative_base()

engine = create_engine('sqlite:///example.db')