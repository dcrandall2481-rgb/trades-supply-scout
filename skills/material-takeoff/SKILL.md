---
name: material-takeoff
description: Turn a job description, photo, or rough scope into a materials list with quantities, waste factors, and supplier comparison hooks. Use for electrical, plumbing, HVAC, carpentry, roofing, and similar trades takeoffs. Do not use for firearms or firearm parts.
---

# Material takeoff

Produce a buy list a contractor can take to a yard. You are not the engineer of record and you do not stamp drawings.

## Inputs to collect if missing

- Trade and city/ZIP (stock and code notes change by market)
- Scope in plain language or a photo of the existing condition
- Quantity basis — rooms, linear feet, squares, fixtures, circuits
- Grade target — code-minimum vs spec-grade
- Pickup vs delivery, and whether Pro pricing is available

## Method

1. Split the job into assemblies.
2. List each stock item with qty, UOM, and waste factor.
3. Mark each line as required, optional upgrade, or consumable.
4. Do not invent loads, pipe sizing, or structural members when the description is incomplete. Ask.
5. After the list is stable, offer to run compare-supply-prices on the top 5 cost lines.

## Waste defaults (override if the user has a number)

- NM-B / THHN pulls — 10 percent
- Copper / PEX / PVC pipe — 10 percent plus listed fittings
- Drywall / OSB / plywood — round up to sheets; 10 percent cut waste on remodel
- Shingles — 10 percent + ridge/hip/starter as separate lines
- Paint — state coverage from the can, then add 10 percent

## Output

```
Job: [one line]
Location assumption: [ZIP or city if given]
Not a design or permit set.

| Line | Item | Qty | UOM | Waste | Notes |
|------|------|-----|-----|-------|-------|

Open questions:
Cost drivers to price first:
```

State that quantities are planning estimates. Field measure before order.
