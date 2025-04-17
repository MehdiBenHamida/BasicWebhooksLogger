import json
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    logs = crud.get_logs(db)
    # Convert header JSON strings to dicts
    for log in logs:
        try:
            log.header_dict = json.loads(log.headers)
        except Exception as e:
            log.header_dict = {}
        try:
            parsed_payload = json.loads(log.payload)
            log.pretty_payload = json.dumps(parsed_payload, indent=2)
        except Exception as e:
            print(e)
            log.pretty_payload = log.payload
    return templates.TemplateResponse("index.html", {"request": request, "logs": logs})

@router.post("/delete")
def delete_selected(request: Request, db: Session = Depends(get_db), ids: list[int] = Form(...)):
    crud.bulk_delete_logs(db, ids)
    return RedirectResponse("/", status_code=303)
