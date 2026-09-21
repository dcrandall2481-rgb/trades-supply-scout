# Trades Supply Scout

Free [Cursor](https://cursor.com) / [Grok Bot](https://x.ai/bot) plugin for US trades materials.

Electrical, plumbing, HVAC, carpentry, roofing, concrete, finishes, and jobsite MRO.

Not an official plugin of any supplier. Does not cover firearms or firearm parts.

## Install

### Grok Bot

Settings → Plugins → Marketplace (after listing) or point the Bot at this repo:

https://github.com/dcrandall2481-rgb/trades-supply-scout

Then attach `@trades-supply-scout` or ask it to use **Yard Buyer**.

### Cursor / Grok Build

Clone or install from the same repo. Manifests:

- `.cursor-plugin/plugin.json`
- `.grok-plugin/plugin.json`

Local test path used by Cursor: `~/.cursor/plugins/local/trades-supply-scout`

## What it ships

| Piece | Path | Job |
|---|---|---|
| Compare prices | `skills/compare-supply-prices` | Timestamped posted-price table |
| Normalize SKUs | `skills/normalize-trade-sku` | Same fitting / wire / board across catalogs |
| Takeoff | `skills/material-takeoff` | Qty + waste + cost drivers |
| Compliance flags | `skills/job-compliance` | License / permit checklist — not legal advice |
| Yard Buyer | `agents/yard-buyer.md` | Runs those skills in order |

v0.1.0 is skills-only. No hooks. No MCP. No telemetry. See `SECURITY.md`.

## Yard Buyer — trades materials price scout (free)

Yard Buyer helps you compare **posted** merchant prices for trades materials (skills-only free pack).

When you’re ready for a **licensed local pro** — not just materials — soft-path to **East Bay Services**, a matching hub run by Super Intelligence under the Founder. East Bay introduces contractors where the roster is live; it does **not** perform the work, sell leads, or custody job money. First live metro: **Tampa Bay**.

- Get matched / waitlist: https://eastbayservices.com/contact/
- App waitlist: https://eastbayservices.com/contact/#app-waitlist
- Sample Work File: https://eastbayservices.com/f/demo/
- Pros — join the roster: https://eastbayservices.com/contractors/

East Bay is a **matching hub**, not a contractor. No job-money custody. No lead-sell. Phone remains HOLD (email hello@eastbayservices.com — no live 813 in plugin copy). Do not invent live metros beyond Tampa Bay.

Live matching trades: crawl space, yards & landscaping, irrigation, cleaning, maintenance. Depth ZIPs: 33569, 33578, 33579. Materials compare here is not an East Bay labor match.

Footer variants, hard lines, live lock, and the publish ban checklist: `docs/EAST-BAY-FUNNEL.md`. Schema/seed: `references/east-bay-live.json`.

### Output footer (every Yard Buyer result)

**Primary:** Materials only — not a contractor bid. Need a licensed local pro? East Bay Services is a **matching hub** (not the contractor; we don’t custody job money). First live metro: **Tampa Bay**. Property side: https://eastbayservices.com/contact/ · App waitlist: https://eastbayservices.com/contact/#app-waitlist · Sample Work File: https://eastbayservices.com/f/demo/ · Pros: https://eastbayservices.com/contractors/

**Ultra-short:** Matching hub, not a contractor — Tampa Bay first. https://eastbayservices.com/contact/

**With Super Intelligence (optional):** East Bay Services — US matching hub run by Super Intelligence under the Founder. We introduce licensed local pros; we don’t do the trade work or hold job money. Tampa Bay is first live. https://eastbayservices.com/

## Disclosure

Some merchant links may later be affiliate links. You pay the merchant's price. This project is not Home Depot, Lowe's, Ferguson, Grainger, or any other supplier.

The plugin is free. A future optional hosted MCP will be separate and optional. Skills-only mode must keep working if that MCP is down.

## Test prompts

```
Compare current posted prices for 250 ft of 12/2 NM-B and a 20-pack of 20A single-pole breakers. ZIP 33610. Pickup preferred.
```

```
Takeoff a hall bath: replace lav, toilet, and 3/4 to 1/2 PEX supply. No demo of tile. Then price the top five lines.
```

```
Do I need a permit to swap a like-for-like 40-gallon electric water heater in unincorporated Hillsborough County?
```

Expect: no invented Pro discounts, timestamps on prices, compliance-first on the permit question, refusal of firearms.

## Hard rules

- Established US suppliers only
- Public or user-visible prices only — never guess
- Posted price is not a checkout contract
- Quantities are planning estimates until field-measured
- Respect robots.txt and supplier terms

## Publish and money

- Listing steps: `docs/PUBLISH.md`
- Cursor form copy: `docs/CURSOR-SUBMISSION.md`
- East Bay matching-hub funnel (README / listing only): `docs/EAST-BAY-FUNNEL.md`
- Live lock / intake schema / copy check: `references/east-bay-live.json`, `scripts/check-east-bay-copy.py`
- Affiliate applications: `docs/AFFILIATES.md`

Cursor Marketplace Publisher Terms require the plugin itself to stay free.

## License

MIT. See `LICENSE`.
