from sqlalchemy.orm import Session
from . import models, schemas

def create_log(db: Session, log: schemas.WebhookLogCreate):
    db_log = models.WebhookLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_logs(db: Session):
    return db.query(models.WebhookLog).order_by(models.WebhookLog.created_at.desc()).all()

def delete_log(db: Session, log_id: int):
    log = db.query(models.WebhookLog).get(log_id)
    if log:
        db.delete(log)
        db.commit()
    return log

def bulk_delete_logs(db: Session, ids: list[int]):
    db.query(models.WebhookLog).filter(models.WebhookLog.id.in_(ids)).delete(synchronize_session=False)
    db.commit()