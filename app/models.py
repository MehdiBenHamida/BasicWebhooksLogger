from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base

class WebhookLog(Base):
    __tablename__ = "webhook_logs"

    id = Column(Integer, primary_key=True, index=True)
    headers = Column(Text)
    payload = Column(Text)
    method = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)