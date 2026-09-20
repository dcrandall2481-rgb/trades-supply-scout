# Cursor Marketplace submission copy

Paste or adapt this on https://cursor.com/marketplace/publish

## Repository

https://github.com/dcrandall2481-rgb/trades-supply-scout

## Plugin name

trades-supply-scout

## Short description

Compare posted prices and build material takeoffs for US trades jobs across established American suppliers.

## Long description

Trades Supply Scout is a free, open-source plugin for Cursor and Grok Bot.

A contractor or estimator can ask for a buy list and a lowest-posted-price table for electrical, plumbing, HVAC, carpentry, roofing, concrete, finishes, and jobsite MRO. The Yard Buyer agent runs four skills in order: job-compliance flags, material-takeoff, SKU normalization, then supplier comparison.

v0.1.0 is skills-only. It does not ship hooks, install scripts, or an MCP server. The Bot may open public supplier pages when the user asks for a live check. Posted prices are not checkout prices. Quantities are planning estimates until field-measured.

This is not an official plugin of Home Depot, Lowe's, Ferguson, Grainger, or any other merchant. Supplier names are used only to describe public catalogs the user already shops.

The plugin stays useful with no account and no paid key. A later optional hosted MCP may add watch lists. That service will be separate. The listing itself is free.

Firearms and firearm parts are out of scope and are refused.

## Test task for reviewers

Ask:

Compare current posted prices for 250 ft of 12/2 NM-B and a 20-pack of 20A single-pole breakers. ZIP 33610. Pickup preferred.

Expect a normalized spec, a timestamped table, no invented Pro discount, and a note that posted price may differ at checkout.

## License

MIT
