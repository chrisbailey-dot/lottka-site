# Legal pages

The terms, privacy notices, DPA, sub-processors, refund policy, security,
pricing, login and sign-up pages are generated from `content.py` by `build.py`.
Edit the wording in `content.py`, then from this folder run:

    python3 build.py ../..

It rewrites the pages in place (au/, uk/, eu/, legal/, security/, pricing/,
login/, signup/). Needs the `markdown` package. Commit the changed pages.
