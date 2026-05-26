# Customer Email Samples

## Purpose

These sample emails are used to test email-to-CRM and AI-assisted customer reply workflows.

---

## Email 1 — Complete Request

From: maria.customer@example.com  
Subject: Request for maintenance contract update

Hello,

This is Maria from Northbridge Supplies. We need to update our maintenance contract for the warehouse scanner system.

Please contact me this week. My phone number is +34 600 111 222.

Regards,  
Maria

---

## Expected Extraction

| Field | Expected Value |
|---|---|
| customer_name | Maria |
| company_name | Northbridge Supplies |
| email | maria.customer@example.com |
| phone | +34 600 111 222 |
| request_type | Maintenance contract update |
| urgency | This week |
| required_action | Contact customer |

---

## Email 2 — Ambiguous Request

From: operations@example.com  
Subject: Problem with last delivery

Hi,

We spoke with someone from your team last month about the issue. It still has not been solved. Can you check?

Thanks.

---

## Expected QA Behaviour

The automation should not invent:

- customer name
- company name
- specific previous contact
- exact issue details

Human review should be required.

---

## Email 3 — Angry Customer

From: client@example.com  
Subject: Urgent complaint

This is unacceptable. The report failed again and nobody has replied.

I need this escalated today.

---

## Expected QA Behaviour

The workflow should detect escalation risk and mark the case for human review.
