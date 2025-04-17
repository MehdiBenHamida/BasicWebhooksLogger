from pydantic import BaseModel
from datetime import datetime

class WebhookLogBase(BaseModel):
    headers: str
    payload: str
    method: str
    url: str

class WebhookLogCreate(WebhookLogBase):
    pass

class WebhookLogOut(WebhookLogBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True