from datetime import date

from src.models import LeadRecord


def test_blank_optional_fields_become_none_and_are_flagged():
    record = LeadRecord(
        lead_id="SYN-001",
        company_name="Sample Company",
        contact_name="  ",
        email="person@example.com",
        previous_demo="false",
        previous_proposal="true",
    )

    assert record.contact_name is None
    assert "contact_name" in record.missing_fields
    assert record.previous_demo is False
    assert record.previous_proposal is True


def test_iso_dates_are_parsed():
    record = LeadRecord(
        lead_id="SYN-002",
        company_name="Sample Company",
        created_at="2025-01-10",
        last_contact_at="2025-02-20",
    )

    assert record.created_at == date(2025, 1, 10)
    assert record.last_contact_at == date(2025, 2, 20)


def test_text_is_trimmed():
    record = LeadRecord(
        lead_id=" SYN-003 ",
        company_name=" Sample Company ",
        notes="  Follow up later  ",
    )

    assert record.lead_id == "SYN-003"
    assert record.company_name == "Sample Company"
    assert record.notes == "Follow up later"
