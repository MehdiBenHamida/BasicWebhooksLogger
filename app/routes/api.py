import json
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/webhooks")
async def log_webhook(request: Request, db: Session = Depends(get_db)):
    headers = str(dict(request.headers))
    payload = await request.body()
    log = schemas.WebhookLogCreate(
        headers = json.dumps(dict(request.headers)),
        payload=payload.decode(),
        method=request.method,
        url=str(request.url)
    )
    return crud.create_log(db, log)

@router.get("/api/webhooks", response_model=list[schemas.WebhookLogOut])
def read_logs(db: Session = Depends(get_db)):
    return crud.get_logs(db)