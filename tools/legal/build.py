"""Builds lottka.com's legal and pricing pages, and the login and sign-up redirects, as static HTML.

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
          <a href="/pricing/">Book a demo</a>
          <a href="/legal/">Terms and privacy</a>
          <a href="/legal/refunds/">Refunds</a>
          <a href="/legal/dpa/">Data processing</a>
          <a href="/legal/subprocessors/">Sub-processors</a>
          <a href="/security/">Security</a>
          <a href="mailto:{co['email']}">{co['email']}</a>
        </nav>
      </div>
      <p class="company">Lottka is provided by {html.escape(co['name'])}, {html.escape(co['address'])}. KRS {co['krs']}, {html.escape(co['court'])}. NIP {co['nip']}, REGON {co['regon']}, share capital {html.escape(co['capital'])}. Payments are processed by Stripe. lottka.com uses no cookies and no tracking; the Lottka app sets only the cookies needed to keep you signed in and to protect forms.</p>
    </div>
  </footer>"""


def page(title: str, description: str, body: str, rel: str) -> str:
    url = f"https://lottka.com/{rel}/"
    full_title = html.escape(f"{title} · Lottka")
    return f"""<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{html.escape(description)}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Lottka">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="https://lottka.com/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
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
          <a href="/pricing/">Book a demo</a>
          <a href="/security/">Security</a>
          <a href="{APP}/login">Log in</a>
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


def redirect(title: str, url: str) -> str:
    """lottka.com/login passes people on to the app's one sign-in page. /signup goes to
    Book a demo: an agency is sent the sign-up address after we have spoken."""
    return f"""<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · Lottka</title>
  <meta name="robots" content="noindex">
  <link rel="canonical" href="{url}">
  <meta http-equiv="refresh" content="0; url={url}">
  <link rel="icon" href="/icon.svg" type="image/svg+xml">
</head>
<body>
  <p><a href="{url}">{title}</a></p>
</body>
</html>
"""


def pricing() -> str:
    cards = []
    for key in c.ORDER:
        r = c.REGIONS[key]
        cards.append(
            f"""      <a class="door" href="{APP}/signup?region={key}">
        <h2>{r['label']}</h2>
        <span class="price">{r['contract']}</span>
        <p>per seat a month on a 12-month contract, billed monthly.</p>
        <p><strong>{r['monthly']}</strong> per seat a month, month by month. Cancel any time.</p>
        {'<p>In Poland: 1,040 zł on a contract, or 1,250 zł month by month, per seat a month.</p>' if key == 'eu' else ''}
        <span class="go">Sign up →</span>
      </a>"""
        )
    return f"""<article class="doc">
<h1>One price, everything in one place</h1>
<p>CRM, business development, temps, reference checks and CV formatting, with every desk and every feature. The job of five or six separate tools, on one bill. No setup fee, no free trial and no \"sign today\" deals: the same list price for everyone in a region, wherever they are.</p>
<p class="note">Prices are set at the same value in each currency. Small differences between regions come from exchange rates, and we review them once a year.</p>
</article>
<div class="doors">
{chr(10).join(cards)}
</div>
<article class="doc">
<h2>What you're signing up to</h2>
<ul>
<li><strong>12-month contract:</strong> commit seats for 12 months at the lower price, billed monthly. It doesn't renew for another 12 months by itself: we email you 30 days before it ends, and if you do nothing you move to month by month.</li>
<li><strong>Extra seats:</strong> agencies grow and shrink, so seats beyond your contract are at the month-by-month price, and you can add or remove them whenever you need.</li>
<li><strong>Month by month:</strong> no minimum term. Cancel any time, and it ends at the end of the month you've paid for.</li>
<li><strong>Temps and contractors:</strong> included for up to 150 active at a time. Each one over is {html.escape(c.REGIONS['uk']['extra_temp'])} a month, or the same value in your currency.</li>
<li><strong>AI and email lookups:</strong> a monthly allowance is included, and credits above it are charged at about cost.</li>
<li><strong>First 14 days:</strong> cancel within 14 days of your first payment and we refund everything.</li>
<li><strong>Your data is yours:</strong> export it any time, free.</li>
<li><strong>Tax:</strong> prices exclude VAT and GST. Customers in Poland pay Polish VAT, EU businesses with a VAT number use the reverse charge, and we add nothing outside the EU.</li>
</ul>
<p>Full details: <a href="/legal/">terms and privacy for your region</a> · <a href="/legal/refunds/">refund policy</a>.</p>
</article>"""


def legal_index() -> str:
    rows = "\n".join(
        f"| {c.REGIONS[k]['label']} | [Terms of service](/{k}/terms/) | [Privacy notice](/{k}/privacy/) |"
        for k in c.ORDER
    )
    text = f"""# Terms and privacy

Your terms and privacy notice depend on the country your business is registered in.

| Region | Terms | Privacy |
| --- | --- | --- |
{rows}

For every region: [Data Processing Agreement](/legal/dpa/) · [Sub-processors](/legal/subprocessors/) · [Refund policy](/legal/refunds/) · [Security](/security/)
"""
    return doc(text)


def write(site: Path, rel: str, title: str, description: str, body: str) -> None:
    target = site / rel / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page(title, description, body, rel), encoding="utf-8")


def build(site: Path) -> None:
    for key in c.ORDER:
        label = c.REGIONS[key]["label"]
        place = f"the {label}" if key == "uk" else label
        write(site, f"{key}/terms", f"Terms of Service, {label}", f"Lottka's terms of service for customers in {place}.", doc(c.terms(key)))
        write(site, f"{key}/privacy", f"Privacy Notice, {label}", f"How Lottka handles personal data, for {place}.", doc(c.privacy(key)))
    write(site, "legal", "Terms and privacy", "Lottka's terms, privacy notices and data processing documents by region.", legal_index())
    write(site, "legal/dpa", "Data Processing Agreement", "Lottka's data processing agreement for customers.", doc(c.DPA))
    write(site, "legal/subprocessors", "Sub-processors", "The companies that process customer data for Lottka.", doc(c.SUBPROCESSORS))
    write(site, "legal/refunds", "Refund policy", "Lottka's refund policy.", doc(c.REFUNDS))
    write(site, "security", "Security and data protection", "How Lottka protects recruitment data: EU hosting, encryption, strong sign-in and privacy rules applied per desk.", doc(c.SECURITY))
    # pricing/ is the Book a demo page and is edited by hand: prices are not published.
    for rel, title, url in (
        ("login", "Log in", f"{APP}/login"),
        ("signup", "Book a demo", "https://lottka.com/pricing/"),
    ):
        (site / rel).mkdir(parents=True, exist_ok=True)
        (site / rel / "index.html").write_text(redirect(title, url), encoding="utf-8")


if __name__ == "__main__":
    build(Path(sys.argv[1]))
