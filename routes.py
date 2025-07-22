from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = models.User(name=name, email=email)
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except:
        db.rollback()
        raise HTTPException(status_code=400, detail="User with this email may already exist.")
    return user

@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
