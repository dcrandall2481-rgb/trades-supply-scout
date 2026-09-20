---
name: normalize-trade-sku
description: Build a canonical trades product key from messy titles so the same fitting, wire, board, or fastener can be matched across suppliers. Use before any price comparison or takeoff line item. Do not use for firearms or firearm parts.
---

# Normalize a trades SKU

Suppliers name the same item differently. Your job is a stable key so price rows actually compare the same thing.

## Canonical fields

Fill what you can. Leave unknown fields blank rather than guessing.

- trade — electrical | plumbing | hvac | carpentry | roofing | concrete | finishes | tools | other
- brand
- series_or_model
- manufacturer_sku if printed
- category — e.g. thhn_wire, emt_conduit, copper_type_l, pex_a_tubing, sch40_pvc, breaker_1p, 2x4_spf, osb_sheet
- attributes — size, length, gauge, schedule, amp, pole, voltage, grade, species, thickness, pack_qty, color, listing (UL, UPC, ASTM)
- unit_of_measure — each, ft, 10-ft stick, box-100, sheet-4x8, bag-80lb, roll
- equivalent_ok — yes only when spec overlap is complete (same listing, size, material, rating)

## Matching rules

1. Prefer manufacturer SKU when both pages show it.
2. Next prefer brand + model + critical spec (size + rating + listing).
3. Commodity items (generic 2x4, Type NM-B 12/2, 1/2 in Sch 40 PVC) may match across house brands if the published spec is the same. Say "commodity equivalent" not "exact."
4. Do not match if any critical spec differs — AWG, schedule, Type L vs M, 20A vs 15A, treated vs untreated, 7/16 vs 1/2 OSB, 10 ft vs 20 ft stick.
5. Pack size is not the same item. Convert to a common unit for the price table (price per foot, per each) and keep pack visible.

## Output

Return a short block the compare skill can reuse:

```
canonical_name:
trade:
brand:
mfr_sku:
key_specs:
uom:
match_confidence: exact | equivalent | weak
notes:
```

If confidence is weak, ask one clarifying question instead of comparing.
