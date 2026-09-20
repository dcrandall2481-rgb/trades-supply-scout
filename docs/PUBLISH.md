# Publish checklist

Marketplace listings are free. This plugin must stay free to install. Money comes from disclosed affiliate links and a later optional MCP, not from a paywall on the listing.

## Cursor Marketplace (Grok Bot Settings → Plugins)

1. Confirm the repo is public: https://github.com/dcrandall2481-rgb/trades-supply-scout
2. Sign into Cursor with the account that owns or is tied to that GitHub user.
3. Open https://cursor.com/marketplace/publish
4. Paste the repository URL.
5. Use the text in `docs/CURSOR-SUBMISSION.md`.
6. Wait for manual review. Every later commit that you want listed must be re-submitted or re-reviewed.

## xAI Grok Build catalog

1. Fork https://github.com/xai-org/plugin-marketplace
2. Add a remote-source entry to `.grok-plugin/marketplace.json` that points at this repo and pins a 40-character commit SHA.
3. Run their validate scripts, then open a pull request.

Suggested catalog fields:

- name: `trades-supply-scout`
- category: `productivity`
- homepage: this repo
- keywords: `trades-supply-scout`, `yard-buyer`, `material-takeoff`
- domains: only a hostname you own. Leave empty until then.

## What you still do in a browser

- Cursor publish form (must be signed in as you)
- Affiliate network applications (Impact / Ferguson Home / Lowe's)
- Florida Sunbiz LLC if you want the business entity before taking commissions
