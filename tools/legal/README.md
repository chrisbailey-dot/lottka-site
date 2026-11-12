# Legal pages

The terms, privacy notices, DPA, sub-processors, refund policy, security,
login and sign-up pages are generated from `content.py` by `build.py`.
Edit the wording in `content.py`, then from this folder run:

    python3 build.py ../..

It rewrites the pages in place (au/, uk/, eu/, legal/, security/, login/,
signup/). pricing/ is the Book a demo page and is edited by hand. Needs the `markdown` package. Commit the changed pages.
