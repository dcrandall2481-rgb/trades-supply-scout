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
- Affiliate applications: `docs/AFFILIATES.md`

Cursor Marketplace Publisher Terms require the plugin itself to stay free.

## License

MIT. See `LICENSE`.
