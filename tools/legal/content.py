"""Lottka legal pages: one shared core, with Australian, UK and EU versions."""

EFFECTIVE = "1 November 2026"
VERSION = "1.0"

COMPANY = {
    "name": "IHR Group sp. z o.o.",
    "address": "ul. Długa 61, 87-800 Włocławek, Poland",
    "krs": "0000788567",
    "court": "District Court in Toruń, 7th Commercial Division of the National Court Register",
    "nip": "8883141067",
    "regon": "383459865",
    "capital": "PLN 5,000",
    "email": "hello@lottka.com",
}

REGIONS = {
    "au": {
        "label": "Australia",
        "short": "Australia",
        "currency": "AUD",
        "monthly": "A$199",
        "annual": "A$1,990",
        "tax": "GST",
    },
    "nz": {
        "label": "New Zealand",
        "short": "New Zealand",
        "currency": "AUD",
        "monthly": "A$199",
        "annual": "A$1,990",
        "tax": "GST",
    },
    "uk": {
        "label": "United Kingdom",
        "short": "the UK",
        "currency": "GBP",
        "monthly": "£99",
        "annual": "£990",
        "tax": "VAT",
    },
    "eu": {
        "label": "Europe",
        "short": "Europe",
        "currency": "EUR or PLN",
        "monthly": "€115 (495 zł in Poland)",
        "annual": "€1,150 (4,950 zł in Poland)",
        "tax": "VAT",
    },
}


# The order the doors appear in everywhere. Must match ORDER in the app's regions.py.
ORDER = ("au", "nz", "uk", "eu")


def other_versions(kind: str, current: str | None = None) -> str:
    """Links to the same document for the other regions (all of them if current is None)."""
    return " · ".join(
        f"[{REGIONS[k]['label']}](/{k}/{kind}/)" for k in ORDER if k != current
    )


def company_line() -> str:
    c = COMPANY
    return (
        f"{c['name']}, registered office {c['address']}, entered in the register of "
        f"entrepreneurs of the National Court Register under KRS {c['krs']} "
        f"({c['court']}), NIP {c['nip']}, REGON {c['regon']}, share capital {c['capital']}"
    )


def terms(region: str) -> str:
    r = REGIONS[region]
    c = COMPANY

    eu_switching = ""
    if region == "eu":
        eu_switching = f"""
**6.6 Switching provider (customers established in the EU).** Under the EU Data Act you may switch to another provider, or leave, on up to two months' notice at any time, including during an Annual Plan. We will help you export your data in a structured, commonly used format, free of charge, and the agreement ends once the switch is complete. If you leave an Annual Plan early this way, we refund 25% of the fees for the whole months left in your plan year. The 75% we keep is our early termination charge: it reflects the revenue we planned on for your committed year, less the hosting, AI and support costs we no longer carry. We charge no switching or export fee.
"""

    regional_law = ""
    if region == "au":
        regional_law = """
**18.2 Australian Consumer Law.** Our services come with guarantees under the Australian Consumer Law that cannot be excluded, where they apply to you. Nothing in these terms excludes, restricts or modifies those guarantees or any other right you have under that law. Where the law allows us to limit our liability for failing to meet a guarantee, our liability is limited to supplying the services again or paying the cost of having them supplied again.

**18.3 Where you can bring a claim.** The choice of Polish courts in clause 18.1 is non-exclusive for customers in Australia: you may also bring proceedings in the courts of the state or territory where you are based.
"""
    elif region == "nz":
        regional_law = """
**18.2 Business use and the Consumer Guarantees Act.** You acquire Lottka in trade, for the purposes of a business. To the extent the law allows, the Consumer Guarantees Act 1993 does not apply to this agreement, and we both agree that is fair and reasonable.

**18.3 Fair Trading Act.** We are both in trade, and to the extent the law allows, sections 9, 12A, 13 and 14(1) of the Fair Trading Act 1986 do not apply between us. We both agree that is fair and reasonable: Lottka is a standard business service, its description and these terms are published in full before you sign up, and you may cancel within 14 days of your first payment for a full refund.

**18.4 Where you can bring a claim.** The choice of Polish courts in clause 18.1 is non-exclusive for customers in New Zealand: you may also bring proceedings in the courts of New Zealand.
"""
    elif region == "uk":
        regional_law = """
**18.2 Customers in the United Kingdom.** Nothing in these terms limits or excludes liability that may not be limited or excluded under the Unfair Contract Terms Act 1977 or any other law that applies to you.
"""
    else:
        regional_law = """
**18.2 Customers in the European Union.** Nothing in these terms takes away a right you have under the mandatory law of the EU member state where you are established, including the EU Data Act.

**18.3 Sole traders in Poland.** If you are a natural person running a business in Poland and this agreement is not of a professional character for you, nothing in these terms limits the consumer protections Polish law gives you, including those against abusive clauses and any right of withdrawal.
"""

    return f"""# Lottka Terms of Service — {r['label']}

Version {VERSION}, effective {EFFECTIVE}. These terms apply to customers who choose the {r['label']} region when signing up. Other versions: {other_versions("terms", region)}.

## At a glance

- **Two plans.** Monthly: cancel any time. Annual: 12 months, paid up front, two months free.
- **Price:** {r['monthly']} per user a month on the Monthly Plan, or {r['annual']} per user a year on the Annual Plan, plus {r['tax']} where it applies. The same price applies in every country we serve.
- **First 14 days:** cancel within 14 days of your first payment for a full refund.
- **Your data is yours.** Export it any time, free.
- **Leaving early is free** if we let you down, raise the price or change these terms against you.

## 1. Who we are

Lottka is provided by {company_line()} ("Lottka", "we", "us"). Contact: [{c['email']}](mailto:{c['email']}).

## 2. Who can use Lottka

Lottka is for businesses only. By signing up you confirm that you are acting for a business and have authority to bind it (the "Customer", "you"). Lottka is not offered to consumers.

## 3. The service

Lottka is an online recruitment CRM and business development platform: client and candidate records, outreach from your own mailbox, separate desks, job ads, market watch, meeting notes and AI-assisted drafting, as described at lottka.com.

To use it you need a current web browser and an internet connection. Mailbox and calendar features need a Google Workspace or Microsoft 365 account. We may improve and change features, but we will not materially reduce the core service during a period you have paid for.

These terms also serve as the terms for providing a service by electronic means under Polish law.

## 4. Accounts

You are responsible for your users, their sign-in details and what they do in Lottka. Keep passwords confidential and tell us at once about any unauthorised use. You can require two-step sign-in for your whole agency.

## 5. Plans, prices and payment

**5.1 Plans.**

- **Monthly Plan:** billed each month in advance. No minimum term.
- **Annual Plan:** a 12-month term, paid in full in advance.

**5.2 Prices.** Prices are per user, as shown on our [pricing page](/pricing/) and at checkout. In {r['short']} they are charged in {r['currency']}.

**5.3 Paddle is our reseller.** Our order process is conducted by our online reseller and Merchant of Record, Paddle.com. Paddle takes payment, issues your invoices, adds {r['tax']} or other sales tax where it applies, and handles billing enquiries and refunds. We handle all other support. Your purchase is also subject to Paddle's buyer terms.

**5.4 Users.**

- Users you add are charged pro rata to the end of the current billing period.
- You may move a user's seat to another person at any time at no charge.
- On the Annual Plan, the number of seats can be reduced from your next renewal. On the Monthly Plan, a reduction takes effect from your next month.

**5.5 Price changes.**

- We may change prices with at least 30 days' notice.
- A change applies from your next renewal, never part-way through a period you have paid for.
- If you don't accept it, you may cancel before it takes effect.

**5.6 Failed payments.** If a payment fails, we will tell you. If it isn't fixed within 14 days, we may suspend access until it is. Your data is not deleted while your access is suspended.

## 6. Term, renewal, cancelling and refunds

**6.1 First 14 days.** If you cancel within 14 days of your first payment, we refund all fees paid and the agreement ends.

**6.2 Monthly Plan.** Cancel at any time in Lottka (Admin, then Billing) or by email. Your plan ends at the end of the month you have paid for.

**6.3 Annual Plan.**

- Your plan runs for 12 months and renews for a further 12 months unless you cancel before the renewal date.
- We email the account owner at least 30 days before each renewal with the date and the price.
- If a renewal happens and you didn't mean it to, cancel within 14 days of the renewal date and we refund the renewal in full.
- Otherwise, cancelling an Annual Plan stops it renewing, and you keep access until the end of the year you have paid for.

**6.4 Leaving early at no cost.** You may end the agreement at any time, with a refund of the fees for the whole months left in your paid period, if:

- we materially breach these terms and don't fix the breach within 30 days of your notice;
- we change prices or these terms to your detriment (clauses 5.5 and 16); or
- you object to a new sub-processor and we can't resolve it (clause 6 of our Data Processing Agreement).

**6.5 Other refunds.** Except as set out in this clause 6 or where the law requires, fees already paid are not refunded. Refunds are made by Paddle to the original payment method.
{eu_switching}
## 7. Your data

- Everything you or your users put into Lottka ("Customer Data") remains yours.
- You give us permission to process it only to provide and support the service.
- Our [Data Processing Agreement](/legal/dpa/) forms part of these terms and governs how we process personal data in Customer Data.
- You can export your data at any time.
- After the agreement ends we keep your data for 30 days so you can export it, then delete it. Copies in backups are deleted as the backups rotate, within 90 days.

## 8. Your responsibilities

You are responsible for:

- having a lawful basis for the personal data you put into Lottka;
- who you contact and what you send, including compliance with the email marketing laws that apply to you;
- giving people the privacy notices the law requires; and
- reviewing anything Lottka's AI drafts or suggests before you use it. AI output may be inaccurate, and we don't guarantee it.

## 9. Acceptable use

You must not use Lottka to:

- send unsolicited bulk email in breach of the law, or email that is misleading about who sent it;
- collect data in breach of a website's terms, or upload data you have no right to use;
- store special-category data (such as health or ethnic origin) beyond what a recruitment process lawfully needs;
- break the law, infringe anyone's rights or harass anyone;
- probe, test or interfere with Lottka's security, other than by reporting a vulnerability to us; or
- resell or share access with another business, or copy, reverse-engineer or build a competing product from Lottka.

We may suspend access that breaches this clause. We will tell you why.

## 10. Other services you connect

Connecting Google, Microsoft, Zoom, Icypeas, Apollo or job boards is your choice, and is also governed by their terms. We are not responsible for their availability or actions.

## 11. Availability and support

We use reasonable efforts to keep Lottka available, and we announce planned maintenance in advance. Support is by email at [{c['email']}](mailto:{c['email']}) on working days, Polish time.

## 12. Intellectual property

We own Lottka, its software, brand and content. You get a non-exclusive, non-transferable right to use it while your subscription lasts. If you send us feedback, we may use it freely.

## 13. Confidentiality

Each of us keeps the other's non-public information confidential, and uses it only for this agreement.

## 14. Liability

- Nothing in these terms limits or excludes liability that cannot be limited or excluded by law, including liability for fraud, wilful misconduct, or death or personal injury caused by negligence.
- Otherwise, neither of us is liable to the other for indirect or consequential loss, or for loss of profit, revenue, business or goodwill.
- Otherwise, each party's total liability to the other in any 12 months is limited to the greater of the fees paid or payable for Lottka in the 12 months before the claim arose and €5,000 (or its equivalent in your currency). This limit does not apply to your obligation to pay fees.
- We supply Lottka with reasonable care and skill, as described in clause 3. We give no other warranties, to the extent the law allows.

## 15. Ending the agreement for cause

Either of us may end the agreement by notice if the other materially breaches it and doesn't fix the breach within 30 days of notice, or becomes insolvent. We may also end it on 30 days' notice if you seriously or repeatedly breach clause 9. Clauses 6, 7, 13, 14, 18 and 19 survive the end of the agreement.

## 16. Changes to these terms

- We may update these terms, with at least 30 days' notice of material changes by email and in Lottka.
- Changes to your detriment do not apply to you until your next renewal, unless the law requires them sooner.
- If you don't accept a change, you may cancel before it takes effect, under clause 6.4.

## 17. General

- We may transfer this agreement to a company in our group, or to a successor to the Lottka business, with notice to you.
- If any part of these terms is invalid, the rest stands.
- These terms, the Data Processing Agreement and your order are the whole agreement for Lottka.

## 18. Law, disputes and local rights

**18.1** Polish law governs these terms, and the courts with jurisdiction over our registered office decide disputes. These terms are written in English; any translation is for convenience, and the English text prevails.
{regional_law}
## 19. Complaints

Send complaints to [{c['email']}](mailto:{c['email']}) with your agency's name and a description of the problem. We reply within 14 days.
"""


def privacy(region: str) -> str:
    r = REGIONS[region]
    c = COMPANY
    regulators = {
        "au": "the Office of the Australian Information Commissioner ([oaic.gov.au](https://www.oaic.gov.au))",
        "nz": "the Office of the Privacy Commissioner ([privacy.org.nz](https://www.privacy.org.nz))",
        "uk": "the Information Commissioner's Office ([ico.org.uk](https://ico.org.uk))",
        "eu": "the Polish data protection authority, Prezes Urzędu Ochrony Danych Osobowych ([uodo.gov.pl](https://uodo.gov.pl)), which is our lead authority, or the authority in the EU country where you live or work",
    }
    law = {
        "au": "the Privacy Act 1988 and the Australian Privacy Principles, and the EU GDPR, which applies to us as a company established in Poland",
        "nz": "the Privacy Act 2020 and its Information Privacy Principles, and the EU GDPR, which applies to us as a company established in Poland",
        "uk": "the UK GDPR and the Data Protection Act 2018, as amended by the Data (Use and Access) Act 2025, and the EU GDPR, which applies to us as a company established in Poland",
        "eu": "the EU General Data Protection Regulation (GDPR) and Polish law",
    }
    extra = ""
    if region == "uk":
        extra = """
## Our UK representative

As we are established in Poland, we are appointing a representative in the UK under Article 27 of the UK GDPR. Their name and address will be published here once appointed. Until then, contact us directly.
"""
    if region == "au":
        extra = """
## Australian Privacy Principles

- **Overseas storage.** Lottka is hosted in Finland (EU), so personal information you give us is held outside Australia, and some may be processed in the United States by our AI provider. EU law and our contracts give it protection at least comparable to the Australian Privacy Principles.
- **Anonymity.** You can contact us without identifying yourself, but we need your details to open an account.
- **Access and correction.** You can ask for access to, or correction of, your personal information at any time, as set out below.
- **Automated decisions.** Lottka does not make automated decisions about the people this notice covers.
"""
    if region == "nz":
        extra = """
## New Zealand Information Privacy Principles

- **Privacy officer.** Our privacy officer can be reached at the email address above.
- **Where your information is held.** Lottka is hosted in Finland (EU) by a provider that stores it for us and does not use it for its own purposes. Some information may be processed in the United States by our AI provider, under contracts that require safeguards comparable to New Zealand's Privacy Act.
- **Information we get from someone else.** If we collect your details from another source, such as your company's website or a business directory, we tell you when we first contact you: who we are, where we got your details, why, and how to see or correct them, unless an exception in the Privacy Act applies.
- **Access and correction.** You can ask to see or correct your personal information at any time. We respond within 20 working days.
- **Privacy breaches.** If a privacy breach is likely to cause you serious harm, we notify you and the Privacy Commissioner as soon as practicable.
- **Automated decisions.** Lottka does not make automated decisions about the people this notice covers.
"""
    return f"""# Lottka Privacy Notice — {r['label']}

Version {VERSION}, effective {EFFECTIVE}. Other versions: {other_versions("privacy", region)}.

## Who we are

{company_line()} ("Lottka", "we") controls the personal data described in this notice, under {law[region]}. Contact: [{c['email']}](mailto:{c['email']}).

## What this notice covers

This notice covers personal data about:

- our customers' users;
- people who ask us for a demo;
- visitors to lottka.com; and
- business contacts we approach about Lottka.

It does not cover the contacts, candidates and emails that our customers keep in Lottka. For that data the customer is the controller, and we process it on their behalf under our [Data Processing Agreement](/legal/dpa/). If you are a candidate or contact of one of our customers, please contact that agency.

## What we collect, why, and for how long

| What we collect | Why | Legal basis | How long |
| --- | --- | --- | --- |
| Account details: name, work email, agency name, password (stored only as a hash), two-step sign-in settings | To provide your account and keep it secure | Contract | While the account is open, then 30 days |
| Billing details: subscription, plan and number of users, invoices, billing country (Paddle holds card and payment details) | To charge for Lottka and keep tax records | Contract; legal obligation | 5 years after the end of the tax year, as Polish tax law requires |
| Security records: sign-ins, browser, IP address, audit trail of actions | To protect accounts, investigate misuse and show accountability | Legitimate interests | The audit trail is kept with the account; rate-limit counters for one day |
| Usage: which areas of Lottka a user opened each day | To improve Lottka and show agency owners how it is used | Legitimate interests | While the account is open |
| Demo requests: name, work email, agency, team size, message | To reply and arrange a demo | Legitimate interests | 24 months, or sooner on request |
| Business contacts we approach: name, job title, work email, company, where we found it | To offer Lottka to recruitment businesses | Legitimate interests; consent where the law requires it | Until you object, or 24 months without contact |
| Support emails | To answer you | Contract; legitimate interests | 24 months |

## Who we share it with

- **Hetzner Online GmbH**, which hosts Lottka in Finland (EU).
- **Paddle.com**, our reseller and Merchant of Record, which takes payment, issues invoices and handles tax. Paddle processes payment data as an independent controller under its own privacy notice.
- **Google**, which runs our own email.
- **Anthropic**, our AI provider, only for the features described under "Google user data" below.

We also share data where the law requires it. We never sell personal data.

## Transfers outside Europe

Our customer account data is held in the EU. Where any processing takes place outside the EU and UK (for example by Anthropic in the United States), it is protected by standard contractual clauses and, for UK data, the UK addendum to them.

## Google user data

When you connect a Google account, Lottka reads, drafts and sends email, and reads calendar events and Meet transcripts, only to provide the features you switch on. Lottka's use and transfer of information received from Google APIs adheres to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements.

- We don't use Google user data for advertising, and we don't sell it.
- We don't use it to train AI models.
- When you ask Lottka to learn your writing style, up to ten of your sent emails, with greeting names, email addresses, phone numbers and links removed, go to Anthropic, only to draft emails for you. Anthropic doesn't train on them.
- People at Lottka read Google user data only with your permission, for security, or where the law requires.
- Disconnecting the account revokes our access and removes stored calendar data.

## Cookies

Lottka sets only the cookies it needs to keep you signed in and to protect forms. There is no advertising or analytics tracking, and public job pages set no cookies at all.

## Your rights

You can ask for access to your data, a copy to take elsewhere, correction or deletion. You can object at any time to processing based on legitimate interests, including all marketing, and every email we send has an unsubscribe link.

Write to [{c['email']}](mailto:{c['email']}). We reply within {"20 working days" if region == "nz" else "one month"}.

## Complaints

You can complain to {regulators[region]}. Please tell us first, so we can put it right.
{extra}
## Changes

We post updates here, and email account owners about material changes.
"""


DPA = f"""# Lottka Data Processing Agreement

Version {VERSION}, effective {EFFECTIVE}. This agreement forms part of the Lottka Terms of Service for every region ({other_versions("terms")}). It applies whenever Lottka processes personal data on a customer's behalf.

## 1. Roles

The Customer is the controller of personal data in Customer Data, and Lottka ({COMPANY['name']}) is its processor. Where the Customer is itself a processor for its own clients, Lottka is its sub-processor on these same terms.

## 2. Scope

Lottka processes Customer Data only to provide the service, for the term of the subscription and the 30 days after it. Schedule 1 sets out the people, data and purposes.

## 3. Instructions

Lottka processes Customer Data only on the Customer's documented instructions. The Terms of Service, and the Customer's settings in Lottka, are those instructions. Lottka will tell the Customer if it thinks an instruction breaks data protection law.

## 4. Confidentiality

Everyone at Lottka with access to Customer Data is bound to keep it confidential.

## 5. Security

Lottka maintains the measures in Schedule 2. It may improve them, but it will not weaken them.

## 6. Sub-processors

- The Customer authorises the sub-processors Lottka engages, listed at [lottka.com/legal/subprocessors](/legal/subprocessors/).
- Lottka gives at least 30 days' notice of a new sub-processor by email.
- The Customer may object on reasonable data protection grounds. If we can't resolve the objection, the Customer may end the agreement with a refund of the fees for the whole months left in its paid period.
- Lottka binds each sub-processor it engages to equivalent terms and remains responsible for them.
- Services the Customer connects under its own account and contract (such as Google, Microsoft, Zoom, Icypeas or Apollo) are not Lottka's sub-processors. The Customer's own agreement with each provider governs them.

## 7. Help with requests

Lottka provides tools in the product (export, correction, erasure and anonymisation) and reasonable help so the Customer can answer requests from individuals. It also helps with impact assessments and with dealings with regulators.

## 8. Breaches

Lottka notifies the Customer without undue delay, and within 48 hours of becoming aware of a breach affecting Customer Data. The notice says what is known and what is being done, and is updated as more is learned.

## 9. Return and deletion

At the end of the agreement the Customer exports its data. Lottka then deletes it within 30 days, and from backups as they rotate, within 90 days.

## 10. Audits

Lottka makes available the information needed to show compliance with this agreement. It allows a reasonable audit once a year on 30 days' notice, at the Customer's cost, or sooner after a breach.

## 11. Transfers

Customer Data is hosted in the EU. Transfers to sub-processors outside the EU and UK are covered by the EU standard contractual clauses (module 3, processor to processor) and, for UK data, the UK International Data Transfer Addendum.

## 12. Australia and New Zealand

For customers in Australia and New Zealand, Lottka:

- handles Customer Data consistently with the Australian Privacy Principles and the New Zealand Information Privacy Principles;
- does not use or disclose it for any purpose other than providing the service; and
- helps the Customer assess a suspected eligible data breach within the timeframe of the Notifiable Data Breaches scheme.

This clause is intended to support the Customer's reasonable steps under APP 8.1.

## 13. Liability and precedence

Each party's liability under this agreement falls within the limits in the Terms of Service. For personal data, this agreement prevails over the Terms of Service if the two conflict.

## Schedule 1 — Processing details

| Processing | People | Data | Purpose | Retention |
| --- | --- | --- | --- | --- |
| Client CRM and outreach | Client contacts (hiring managers) | Name, work email, phone, job title, employer, source, lawful basis, correspondence | Business development | Until erased; optional retention period per desk |
| Candidate records | Candidates and applicants | Contact details, CV, work history, pay expectations, consents | Recruitment | Reviewed after 24 months (UK and EU) or 36 months (Australia and New Zealand) |
| Meeting notes | Meeting participants | Transcript (temporary), summary, follow-ups | Accurate records of meetings | Transcript 1 to 365 days; notes 24 months |
| Calendar | Meeting attendees | Event title, time, attendee addresses | Scheduling, meeting context | Until the calendar is disconnected, and at most 24 months |
| Audit trail | Agency users | Action, time, network address | Security, accountability | Kept with the account |
| Product metrics | Agency users | Areas used each day | Product improvement, reporting | Kept with the account |
| Job applications | Applicants | As candidates, plus a hashed network address for one day | Recruitment, abuse prevention | As candidates; counters one day |

## Schedule 2 — Security measures

- Hosting in the EU (Helsinki, Finland), with access limited to named operators using two-step sign-in.
- Every agency and every desk separated by database row-level security, not only by application code.
- Encryption in transit (HTTPS) for every connection; stored mailbox and integration credentials encrypted.
- Passwords hashed with argon2id; two-step sign-in available to every user, which an owner can make compulsory.
- An append-only audit trail of actions, including any support access by Lottka staff.
- Nightly database backups, kept for 14 days and weekly for 8 weeks.
- Dependency updates through reviewed changes; rate limits on sign-in and public forms.
"""

SUBPROCESSORS = f"""# Lottka sub-processors

Effective {EFFECTIVE}. These are the companies that process Customer Data for Lottka, under our [Data Processing Agreement](/legal/dpa/). We give customers at least 30 days' notice of any addition.

| Sub-processor | What for | Location | When used |
| --- | --- | --- | --- |
| Hetzner Online GmbH | Hosting, database, files and backups | Finland (EU) | Always |
| Anthropic, PBC | AI drafting, summaries, call scripts and classification | United States (standard contractual clauses) | Whenever AI features are used. The agency can set its allowance to zero |

## Services you connect under your own account

These are not Lottka's sub-processors. The agency connects them under its own account and contract with each provider, which governs how they handle data.

| Service | What for | Location |
| --- | --- | --- |
| Google | Mail, calendar and Meet transcripts | Per the agency's Google Workspace |
| Microsoft | Mail, calendar and Teams transcripts | Per the agency's Microsoft 365 tenant |
| Zoom Video Communications | Zoom transcripts | Per the agency's Zoom account |
| Icypeas | Finding work email addresses | France (EU) |
| Apollo.io | Finding work email addresses | United States |

**Not a sub-processor:** Paddle.com, our reseller and Merchant of Record, processes billing and payment data as an independent controller. It does not process Customer Data.
"""

REFUNDS = f"""# Refund policy

Effective {EFFECTIVE}. Lottka is sold through Paddle.com, our reseller and Merchant of Record, which processes all refunds to the original payment method.

- **First 14 days.** Cancel within 14 days of your first payment and we refund everything you paid.
- **Annual renewals.** If your Annual Plan renews and you didn't mean it to, cancel within 14 days of the renewal date and we refund the renewal in full. We email you at least 30 days before each renewal.
- **If we let you down.** If we materially breach our terms, raise the price, change the terms to your detriment, or you object to a new sub-processor and we can't resolve it, you can leave and we refund the fees for the whole months left in your paid period.
- **Customers in the EU** switching provider under the EU Data Act: see clause 6.6 of the [European terms](/eu/terms/).
- **Otherwise,** fees already paid are not refunded, except where the law requires. Cancelling stops the next renewal, and you keep access until the end of the period you paid for.

To ask for a refund, email [{COMPANY['email']}](mailto:{COMPANY['email']}) or contact Paddle through the link on your receipt.
"""

SECURITY = f"""# Security at Lottka

Recruitment data is personal data about real people. This is how we look after it.

- **Hosted in the EU.** Lottka runs on Hetzner servers in Helsinki, Finland.
- **Desks walled off in the database.** Every agency, and every desk inside an agency, is separated by PostgreSQL row-level security, a second wall behind the application's own checks.
- **Encrypted in transit.** Every connection uses HTTPS. Stored mailbox and integration credentials are encrypted.
- **Strong sign-in.** Passwords are hashed with argon2id. Two-step sign-in is available to every user, and an owner can make it compulsory for the whole agency. You can see every browser you're signed in on and end any session.
- **Everything audited.** An append-only audit trail records actions, including any time a Lottka operator opens an agency to give support.
- **Backups.** Nightly backups, kept for 14 days, plus weekly backups for 8 weeks.
- **Your mailbox stays yours.** Email is sent from each recruiter's own Google or Microsoft account. Lottka stores only the mail between a desk and its known client contacts, and never fetches attachments.
- **AI with a person in charge.** Every AI-written email is a draft until a person approves it. Candidate records are not used to write outreach drafts.

**Found a problem?** Email [{COMPANY['email']}](mailto:{COMPANY['email']}) with the subject "Security". Please give us a chance to fix it before telling anyone else. We reply within two working days.

Read more: [Data Processing Agreement](/legal/dpa/) · [Sub-processors](/legal/subprocessors/)
"""
