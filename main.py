from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models
import schemas

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "https://daddieshinor.com",
        "https://www.daddieshinor.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Subscribe with JSON
@app.post("/subscribe", response_model=schemas.SubscriberResponse)
def subscribe(subscriber: schemas.SubscriberCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Subscriber).filter(
        models.Subscriber.email == subscriber.email
    ).first()

    if existing:
        # ✅ better status for "already exists"
        raise HTTPException(status_code=409, detail="Email already subscribed")

    new_subscriber = models.Subscriber(email=subscriber.email)
    db.add(new_subscriber)
    db.commit()
    db.refresh(new_subscriber)

    return new_subscriber

# ✅ Admin: Get all subscribers
@app.get("/subscribers", response_model=list[schemas.SubscriberResponse])
def get_subscribers(db: Session = Depends(get_db)):
    return db.query(models.Subscriber).order_by(
        models.Subscriber.created_at.desc()
    ).all()

@app.get("/")
def root():
    return {"message": "Daddieshinor API running 🚀"}
