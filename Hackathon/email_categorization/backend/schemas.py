from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class EmailIn(BaseModel):
    subject: str = Field("", description="Email subject")
    body: str = Field("", description="Plaintext body")

class BulkIn(BaseModel):
    emails: List[EmailIn]

class ClassificationOut(BaseModel):
    label: str
    confidence: float
    reasons: List[str]
    suggested_actions: List[str]
    priority: int | None = None
    sla_hours: int | None = None
    routed_queue: str
    extracted: Dict[str, Any]
    alt_labels: List[Dict[str, float]]

class FeedbackIn(BaseModel):
    subject: str
    body: str
    predicted: str
    correct: str
