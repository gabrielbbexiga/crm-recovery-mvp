from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class LeadRecord(BaseModel):
    """Normalized representation of one synthetic CRM lead record."""

    model_config = ConfigDict(extra="ignore")

    lead_id: str
    company_name: str
    contact_name: Optional[str] = None
    job_title: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    source: Optional[str] = None
    created_at: Optional[date] = None
    last_contact_at: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    previous_demo: bool = False
    previous_proposal: bool = False
    missing_fields: list[str] = Field(default_factory=list)

    @field_validator(
        "lead_id",
        "company_name",
        "contact_name",
        "job_title",
        "email",
        "phone",
        "source",
        "status",
        "notes",
        mode="before",
    )
    @classmethod
    def normalize_text(cls, value):
        if value is None:
            return None
        if isinstance(value, str):
            value = value.strip()
            return value or None
        return value

    @model_validator(mode="after")
    def detect_missing_fields(self):
        optional_fields = (
            "contact_name",
            "job_title",
            "email",
            "phone",
            "source",
            "created_at",
            "last_contact_at",
            "status",
            "notes",
        )
        self.missing_fields = [
            field_name
            for field_name in optional_fields
            if getattr(self, field_name) is None
        ]
        return self
