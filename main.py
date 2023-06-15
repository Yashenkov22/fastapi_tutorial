from enum import Enum
from typing import List, Optional
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi_users import fastapi_users, FastAPIUsers
from auth.auth import auth_backend
from auth.schemas import UserCreate, UserRead
from auth.database import User
from auth.manager import get_user_manager

app = FastAPI(
    title='Trading App'
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)







# fake_db = [
#     {'id': 1, 'role': 'admin', 'name': 'Bob'},
#     {'id': 2, 'role': 'trader', 'name': 'Sue'},
#     {'id': 3, 'role': 'investor', 'name': 'John'},
#     {'id': 4, 'role': 'trader', 'name': 'Kolya', 'degree': [
#         {'id': 1, 'created_at': '2020-01-01T00:00:00', 'type_degree': 'newbie'}
#     ]},
    
# ]

# fake_trades = [
#     {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.12},
#     {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 125, 'amount': 2.12},
# ]


# class DegreeType(Enum):
#     newbie = 'newbie'
#     expert = 'expert'

# class Degree(BaseModel):
#     id: int
#     created_at: datetime
#     type_degree: DegreeType


# class User(BaseModel):
#     id: int
#     role: str
#     name: str
#     degree: Optional[List[Degree]]

# @app.get('/users/{user_id}', response_model=List[User])
# def get_user(user_id: int):
#     return [user for user in fake_db if user_id == user.get('id')]

# @app.get('/trades/')
# def get_trade_by_user(limit: int = 10, offset: int = 0):
#     return fake_trades[offset:][:limit]

# fake_db2 = [
#     {'id': 1, 'role': 'admin', 'name': 'Bob'},
#     {'id': 2, 'role': 'trader', 'name': 'Sue'},
#     {'id': 3, 'role': 'investor', 'name': 'John'},
# ]

# @app.post('/users/{user_id}')
# def change_user_name(user_id: int, new_name: str):
#     current_user = list(filter(lambda user: user.get('id') == user_id, fake_db2))[0]
#     current_user['name'] = new_name
#     return {'status': 200, 'data' : current_user}

# # fake_trades = [
# #     {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.12},
# #     {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 125, 'amount': 2.12},
# # ]



# class Trade(BaseModel):
#     id: int
#     user_id: int
#     currency: str = Field(max_length=5)
#     side: str
#     price: float = Field(ge=0)
#     amount: float    


# @app.post('/trades')
# def add_trade(trades: List[Trade]):
#     fake_trades.extend(trades)
#     return {'status': 200, 'data': fake_trades}