"""Builds lottka.com's legal, pricing and login-door pages as static HTML.

Run: python3 build.py <site-dir>
"""

import html
import sys
from pathlib import Path

import markdown

import content as c

APP = "https://app.lottka.com"

SYMBOL = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
    <defs>
      <path id="bird" d="M-10 2 Q-5 -5 0 0 Q5 -5 10 2 Q5 -2 0 3 Q-5 -2 -10 2 Z"/>
      <g id="flock">
        <use href="#bird" class="bird rear" transform="translate(27 54) scale(1.1)"/>
        <use href="#bird" class="bird rear" transform="translate(93 54) scale(1.1)"/>
        <use href="#bird" class="bird mid" transform="translate(43 38) scale(1.3)"/>
        <use href="#bird" class="bird mid" transform="translate(77 38) scale(1.3)"/>
        <use href="#bird" class="bird lead" transform="translate(60 22) scale(1.5)"/>
      </g>
    </defs>
  </svg>"""

STYLE = """
    @font-face { font-family: "Inter"; font-weight: 100 900; font-display: swap; src: url("/fonts/inter-latin.woff2") format("woff2"); }
    @font-face { font-family: "Sora"; font-weight: 100 800; font-display: swap; src: url("/fonts/sora-latin.woff2") format("woff2"); }
    :root {
      --navy: #13202e; --navy-2: #1b2b3d; --amber: #e2a33a; --amber-ink: #8a5a10; --slate: #3c4a5a;
      --mist: #c9d3dd; --cream: #f5f2ec; --page: #f7f5f0; --line: #e1ddd3; --muted: #4a5868;
      --font: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
      --display: "Sora", var(--font);
    }
    * { box-sizing: border-box; }
    html { -webkit-text-size-adjust: 100%; }
    body { margin: 0; background: var(--page); color: var(--navy); font: 17px/1.6 var(--font); -webkit-font-smoothing: antialiased; }
    a { color: inherit; }
    :focus-visible { outline: 3px solid var(--amber); outline-offset: 3px; border-radius: 6px; }
    .wrap { width: min(1120px, 100%); margin: 0 auto; padding: 0 24px; }
    .narrow { width: min(820px, 100%); }
    h1, h2, h3 { font-family: var(--display); letter-spacing: -0.03em; line-height: 1.15; text-wrap: balance; }
    .logo { display: inline-flex; align-items: center; gap: 10px; text-decoration: none; }
    .logo svg { width: 40px; height: auto; overflow: visible; }
    .wordmark { font-family: var(--display); font-weight: 700; font-size: 23px; letter-spacing: -0.035em; line-height: 1; }
    .bird { stroke-width: 0.6; stroke-linejoin: round; }
    .lead { fill: var(--amber); stroke: var(--amber); }
    .mid { fill: var(--cream); stroke: var(--cream); }
    .rear { fill: var(--mist); stroke: var(--mist); }
    .top { background: var(--navy); color: var(--cream); }
    .nav { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 18px 0; flex-wrap: wrap; }
    .nav .links { display: flex; gap: 6px 18px; flex-wrap: wrap; align-items: center; }
    .nav .links a { color: var(--cream); font-weight: 600; font-size: 15px; text-decoration: none; padding: 8px 2px; }
    .nav .links a:hover { text-decoration: underline; text-underline-offset: 4px; }
    main { padding: 48px 0 72px; }
    .doc h1 { font-size: clamp(30px, 4.4vw, 42px); margin: 0 0 12px; }
    .doc h2 { font-size: 22px; margin: 40px 0 10px; }
    .doc p, .doc li { color: #24323f; }
    .doc ul { padding-left: 22px; }
    .doc li { margin: 4px 0; }
    .doc > p:first-of-type { color: var(--muted); font-size: 15px; }
    .doc a { color: var(--amber-ink); text-underline-offset: 3px; }
    .table { overflow-x: auto; margin: 16px 0; border: 1px solid var(--line); border-radius: 12px; background: #fff; }
    table { border-collapse: collapse; width: 100%; font-size: 15px; }
    th, td { text-align: left; vertical-align: top; padding: 10px 14px; border-bottom: 1px solid var(--line); }
    th { background: var(--cream); font-weight: 600; }
    tr:last-child td { border-bottom: 0; }
    .doors { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; margin: 28px 0; }
    .door { display: flex; flex-direction: column; gap: 10px; padding: 24px; border-radius: 18px; background: #fff; border: 1px solid var(--line); text-decoration: none; transition: transform .15s, box-shadow .15s; }
    .door:hover { transform: translateY(-2px); box-shadow: 0 14px 30px -18px rgb(19 32 46 / 45%); }
    .door h2 { margin: 0; font-size: 22px; }
    .door p { margin: 0; color: var(--muted); font-size: 15px; }
    .door .price { font-family: var(--display); font-size: 30px; font-weight: 700; color: var(--navy); letter-spacing: -0.03em; }
    .door .go { margin-top: auto; padding-top: 8px; font-weight: 700; color: var(--amber-ink); }
    .note { color: var(--muted); font-size: 15px; }
    .glance { background: var(--cream); border: 1px solid var(--line); border-radius: 16px; padding: 8px 24px; margin: 24px 0; }
    footer { padding: 32px 0 40px; color: var(--muted); font-size: 14px; border-top: 1px solid var(--line); }
    footer .row { display: flex; flex-wrap: wrap; gap: 10px 22px; justify-content: space-between; align-items: center; }
    footer .legal { display: flex; flex-wrap: wrap; gap: 6px 16px; }
    footer .legal a { text-decoration: none; }
    footer .legal a:hover { text-decoration: underline; }
    footer .company { margin-top: 14px; font-size: 13px; line-height: 1.5; }
    footer .logo svg { width: 30px; }
    footer .wordmark { font-size: 18px; color: var(--navy); }
    footer .mid { fill: var(--navy); stroke: var(--navy); }
    footer .rear { fill: var(--slate); stroke: var(--slate); }
    @media (max-width: 600px) { .doors { grid-template-columns: minmax(0, 1fr); } }
"""


def footer() -> str:
    co = c.COMPANY
    return f"""<footer>
    <div class="wrap">
      <div class="row">
        <a class="logo" href="/" aria-label="Lottka home"><svg viewBox="12 10 96 52" aria-hidden="true"><use href="#flock"/></svg><span class="wordmark">lottka</span></a>
        <nav class="legal" aria-label="Legal">
          <a href="/pricing/">Pricing</a>
          <a href="/legal/">Terms and privacy</a>
          <a href="/legal/refunds/">Refunds</a>
          <a href="/legal/dpa/">Data processing</a>
          <a href="/legal/subprocessors/">Sub-processors</a>
          <a href="/security/">Security</a>
          <a href="mailto:{co['email']}">{co['email']}</a>
        </nav>
      </div>
      <p class="company">Lottka is provided by {html.escape(co['name'])}, {html.escape(co['address'])}. KRS {co['krs']}, {html.escape(co['court'])}. NIP {co['nip']}, REGON {co['regon']}, share capital {html.escape(co['capital'])}. Payments are processed by Paddle.com, our reseller and Merchant of Record. lottka.com uses no cookies and no tracking; the Lottka app sets only the cookies needed to keep you signed in and to protect forms.</p>
    </div>
  </footer>"""


def page(title: str, description: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} · Lottka</title>
  <meta name="description" content="{html.escape(description)}">
  <meta name="theme-color" content="#13202e">
  <link rel="icon" href="/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <style>{STYLE}</style>
</head>
<body>
  {SYMBOL}
  <header class="top">
    <div class="wrap">
      <nav class="nav" aria-label="Main">
        <a class="logo" href="/" aria-label="Lottka home"><svg viewBox="12 10 96 52" aria-hidden="true"><use href="#flock"/></svg><span class="wordmark">lottka</span></a>
        <div class="links">
          <a href="/pricing/">Pricing</a>
          <a href="/security/">Security</a>
          <a href="/login/">Log in</a>
          <a href="/signup/">Sign up</a>
        </div>
      </nav>
    </div>
  </header>
  <main>
    <div class="wrap narrow">
{body}
    </div>
  </main>
  {footer()}
</body>
</html>
"""


def md(text: str) -> str:
    out = markdown.markdown(text, extensions=["tables"])
    return out.replace("<table>", '<div class="table"><table>').replace("</table>", "</table></div>")


def doc(text: str) -> str:
    return f'<article class="doc">\n{md(text)}\n</article>'


def doors(kind: str) -> str:
    verb = "Log in" if kind == "login" else "Sign up"
    path = "login" if kind == "login" else "signup"
    cards = []
    blurbs = {
        "au": "Australian Privacy Principles and Consumer Law, prices in AUD. Your data is held in the EU under APP-standard terms.",
        "nz": "New Zealand Privacy Act 2020, prices in NZD. Your data is held in the EU under safeguards comparable to New Zealand law.",
        "uk": "UK GDPR, prices in GBP. Your data is held in the EU, which the UK recognises as adequate.",
        "eu": "GDPR and the EU Data Act, prices in EUR (PLN in Poland). Your data is held in the EU.",
    }
    for key in c.ORDER:
        r = c.REGIONS[key]
        cards.append(
            f"""      <a class="door" href="{APP}/{path}?region={key}">
        <h2>{r['label']}</h2>
        <p>{blurbs[key]}</p>
        <span class="go">{verb} →</span>
      </a>"""
        )
    intro = (
        "Choose where your agency is based. Your account, terms and privacy notice follow your region."
        if kind == "signup"
        else "Choose your region to sign in. You use the same email and password whichever door you pick."
    )
    legal = " · ".join(
        f'<a href="/{k}/terms/">{c.REGIONS[k]["label"]} terms</a>' for k in c.ORDER
    )
    return f"""<article class="doc">
<h1>{verb}</h1>
<p>{intro}</p>
</article>
<div class="doors">
{chr(10).join(cards)}
</div>
<p class="note">{legal}</p>"""


def pricing() -> str:
    cards = []
    for key in c.ORDER:
        r = c.REGIONS[key]
        cards.append(
            f"""      <a class="door" href="{APP}/signup?region={key}">
        <h2>{r['label']}</h2>
        <span class="price">{r['monthly'].split(' (')[0]}</span>
        <p>per user a month on the Monthly Plan. Cancel any time.</p>
        <p><strong>{r['annual'].split(' (')[0]}</strong> per user a year on the Annual Plan: two months free, paid up front.</p>
        {'<p>In Poland: 495 zł a month, or 4,950 zł a year, per user.</p>' if key == 'eu' else ''}
        <span class="go">Sign up →</span>
      </a>"""
        )
    return f"""<article class="doc">
<h1>One price, everything included</h1>
<p>Every desk, every feature, outreach from your own mailbox, market watch and AI drafting. No setup fee, no free trial and no \"sign today\" deals: the same list price for everyone in a region, wherever they are.</p>
</article>
<div class="doors">
{chr(10).join(cards)}
</div>
<article class="doc">
<h2>What you're signing up to</h2>
<ul>
<li><strong>Monthly Plan:</strong> billed monthly, cancel any time, and it ends at the end of the month you've paid for.</li>
<li><strong>Annual Plan:</strong> 12 months paid up front. We email you 30 days before it renews, and if a renewal catches you out, cancel within 14 days for a full refund.</li>
<li><strong>First 14 days:</strong> cancel within 14 days of your first payment and we refund everything.</li>
<li><strong>Your data is yours:</strong> export it any time, free.</li>
<li><strong>Tax:</strong> prices exclude VAT and GST. Paddle, our reseller, adds them at checkout where they apply, and handles reverse charge for VAT-registered businesses.</li>
<li><strong>Contact data:</strong> work-email finding uses your own Icypeas or Apollo account, billed by them.</li>
</ul>
<p>Full details: <a href="/legal/">terms and privacy for your region</a> · <a href="/legal/refunds/">refund policy</a>.</p>
</article>"""


def legal_index() -> str:
    rows = "\n".join(
        f"| {c.REGIONS[k]['label']} | [Terms of service](/{k}/terms/) | [Privacy notice](/{k}/privacy/) |"
        for k in c.ORDER
    )
    text = f"""# Terms and privacy

Your terms and privacy notice depend on where your agency is based: the door you sign up through.

| Region | Terms | Privacy |
| --- | --- | --- |
{rows}

For every region: [Data Processing Agreement](/legal/dpa/) · [Sub-processors](/legal/subprocessors/) · [Refund policy](/legal/refunds/) · [Security](/security/)
"""
    return doc(text)


def write(site: Path, rel: str, title: str, description: str, body: str) -> None:
    target = site / rel / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page(title, description, body), encoding="utf-8")


def build(site: Path) -> None:
    for key in c.ORDER:
        label = c.REGIONS[key]["label"]
        write(site, f"{key}/terms", f"Terms of Service, {label}", f"Lottka's terms of service for customers in {label}.", doc(c.terms(key)))
        write(site, f"{key}/privacy", f"Privacy Notice, {label}", f"How Lottka handles personal data, for {label}.", doc(c.privacy(key)))
    write(site, "legal", "Terms and privacy", "Lottka's terms, privacy notices and data processing documents by region.", legal_index())
    write(site, "legal/dpa", "Data Processing Agreement", "Lottka's data processing agreement for customers.", doc(c.DPA))
    write(site, "legal/subprocessors", "Sub-processors", "The companies that process customer data for Lottka.", doc(c.SUBPROCESSORS))
    write(site, "legal/refunds", "Refund policy", "Lottka's refund policy.", doc(c.REFUNDS))
    write(site, "security", "Security", "How Lottka protects recruitment data.", doc(c.SECURITY))
    write(site, "pricing", "Pricing", "Lottka pricing: one price per user, every feature included.", pricing())
    write(site, "login", "Log in", "Log in to Lottka.", doors("login"))
    write(site, "signup", "Sign up", "Create your Lottka account.", doors("signup"))


if __name__ == "__main__":
    build(Path(sys.argv[1]))
