# GeM Sahayak — Surety Bonds

An educational reference on Insurance Surety Bonds as Earnest Money Deposit (EMD)
on the Government e-Marketplace (GeM): what the instrument is, the regulatory
framework under which it was adopted, and the procedure for obtaining one.

## Contents

- `index.html` — the site (single page, no build step)
- `i18n.js` — translations for 10 languages
- `docs/` — source government documents linked from the regulatory timelines
- `how-to-apply.pdf` — the application walkthrough deck (30 slides)

## Languages

English, हिंदी, Hinglish, বাংলা, मराठी, ગુજરાતી, தமிழ், తెలుగు, ಕನ್ನಡ, മലയാളം.

All strings live in `i18n.js` as key–value pairs. Missing keys fall back to English.

> The eight non-English translations have not yet been reviewed by native
> speakers. Legal terms (obligee, bid security, EMD) should be verified before
> this is relied upon.

## Running locally

```bash
python3 serve.py 8777 .
# http://localhost:8777
```

`serve.py` sends no-cache headers so edits appear on a normal reload.

## Disclaimer

This is an educational awareness resource. It is not owned or maintained by any
government authority and does not constitute legal or financial advice.
