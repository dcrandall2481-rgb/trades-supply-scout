# Chief of Staff — publish Trades Supply Scout

Use this document as your standing orders. Execute it. Do not rebuild the plugin. Do not add firearms. Do not add a paid install wall. The listing itself must stay free.

Source thread: https://grok.com/share/bGVnYWN5LWNvcHk_97f2c52a-a191-477d-bcec-ac713bfd3f75

## Goal

Get **trades-supply-scout** listed so any Cursor user and any Grok Bot user can install it.

Done means:

- A Cursor Marketplace page exists for `trades-supply-scout`
- Grok Bot Settings → Plugins can find it
- `xai-org/plugin-marketplace` has a merged or clearly reviewed catalog entry pinned to SHA `83094dda7ea2f91881598251bcc2f0e40c5043a1`
- You report status with links: submitted / waiting / blocked / live

## Assets

Plugin repo: https://github.com/dcrandall2481-rgb/trades-supply-scout

Pinned SHA: `83094dda7ea2f91881598251bcc2f0e40c5043a1`

xAI fork branch: https://github.com/dcrandall2481-rgb/plugin-marketplace/tree/add-trades-supply-scout

Open the xAI PR from this compare URL:  
https://github.com/xai-org/plugin-marketplace/compare/main...dcrandall2481-rgb:plugin-marketplace:add-trades-supply-scout

Cursor publish form: https://cursor.com/marketplace/publish

Cursor publisher terms: https://cursor.com/marketplace-publisher-terms

xAI contributing rules: https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md

Cursor form copy: https://github.com/dcrandall2481-rgb/trades-supply-scout/blob/main/docs/CURSOR-SUBMISSION.md

## Task 1 — Cursor Marketplace

This listing is what Grok Bot Settings → Plugins uses.

1. Open https://cursor.com/marketplace/publish while signed into the Cursor account tied to GitHub user `dcrandall2481-rgb`.
2. Submit repository `https://github.com/dcrandall2481-rgb/trades-supply-scout`.
3. Use the short and long descriptions in `docs/CURSOR-SUBMISSION.md`.
4. Reviewer test task: Compare current posted prices for 250 ft of 12/2 NM-B and a 20-pack of 20A single-pole breakers. ZIP 33610. Pickup preferred.
5. Record the confirmation URL or screenshot of the submitted state.

If the form requires D.J.'s login, stop and send one screen of instructions plus the exact URL. Do not invent credentials.

## Task 2 — xAI / SpaceXAI Grok Build catalog

1. Open the compare URL above.
2. File the pull request against `xai-org/plugin-marketplace`.
3. Proposed catalog object: `proposed-plugins/trades-supply-scout.json` on the fork branch.
4. If reviewers require the object inside `.grok-plugin/marketplace.json` plus a regenerated `plugin-index.json`, make that edit on the branch and update the PR.
5. Keywords only: `trades-supply-scout`, `yard-buyer`, `material-takeoff`. No generic terms. No supplier domains we do not own.

## Rules

- Plugin stays free. No required paid key to install.
- Not an official Home Depot, Lowe's, Ferguson, or Grainger product.
- No affiliate IDs or secrets in the public repo.
- Follow up every 48 hours until live or a reviewer names a blocker.
- If blocked, fix the repo and resubmit.

## First output

Five lines: what you will do in order, then either submit or hand D.J. the exact click required.
