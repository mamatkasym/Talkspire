from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.core import security
from src.repository.users import user_repository

router = APIRouter()


@router.post('/login')
def login(db: Session = Depends(), form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_repository.authenticate(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"access_token": security.create_access_token(user.id)}
