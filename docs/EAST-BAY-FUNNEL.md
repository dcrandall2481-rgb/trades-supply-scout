# East Bay matching-hub funnel (plugin README / listing)

Founder-approved 2026-09-20 for **plugin README and marketplace listing copy only**.

Monetize lock: **A + C** (free plugin + acquisition funnel). No plugin fee. No lead-sell. No affiliate IDs in this file.

Do **not** paste this into Buffer, social posts, or the eastbayservices.com hub site unless the Founder opens that gate.

Plugin: `trades-supply-scout` / Yard Buyer · Hub: https://eastbayservices.com/

## Hard lines (every surface)

| Must say / imply | Must never say / imply |
| --- | --- |
| East Bay is a **matching hub**, not a contractor | “Our guys,” “we’ll run the job,” “we’ll install / mow / encapsulate” |
| Run by **Super Intelligence** under the **Founder** (optional, OK) | East Bay sells leads / lead mill / auction marketplace |
| East Bay does **not** custody job money | Escrow-ready, send the deposit, paid from hold, insured/bonded/PE-capable/fully covered |
| Soft path to hub: waitlist / Work File / roster | Invent live metros beyond **Tampa Bay** first live |
| License verify before hire (FL: myfloridalicense.com; other metros: that state’s board) | You’re in / seats sold / Wave A live |

**Heat stop-line (if anyone pushes seats/jobs/money/signature):**  
Matching-only. No seats, no jobs, no money, no company signature. Drafts only until the founder opens the gate.

Phone remains **HOLD** — do not put a live 813, `[813-XXX-XXXX]`, or `tel:+18130000000` in plugin copy. Email: hello@eastbayservices.com.

Live matching trades (Tampa Bay only): crawl space, yards & landscaping, irrigation, cleaning, maintenance. Depth ZIPs: **33569, 33578, 33579**. Do not send electrical / plumbing / HVAC labor to East Bay as if those trades are live.

Machine lock + intake schema + demo Work File: `references/east-bay-live.json`, `references/east-bay-intake.schema.json`, `references/east-bay-work-file.demo.json`. Copy check: `python3 scripts/check-east-bay-copy.py`.

## Audience splits

| Who | Intent | Soft CTA |
| --- | --- | --- |
| **Property / facility side** (buyer of work) | Materials scout → need a licensed pro for the yard / property job | Waitlist or match form / Work File |
| **Supply / trades side** (contractor / yard) | Materials scout → want intros where roster is live | Join the roster |

Never mix “we sell you leads” into contractor CTAs.

## Plugin footer (default — every Yard Buyer output)

**Primary (short):**

> Materials only — not a contractor bid. Need a licensed local pro? East Bay Services is a **matching hub** (not the contractor; we don’t custody job money). First live metro: **Tampa Bay**.  
> Property side: https://eastbayservices.com/contact/ · App waitlist: https://eastbayservices.com/contact/#app-waitlist · Sample Work File: https://eastbayservices.com/f/demo/ · Pros: https://eastbayservices.com/contractors/

**Ultra-short (character-tight):**

> Matching hub, not a contractor — Tampa Bay first. https://eastbayservices.com/contact/

**With Super Intelligence line (optional):**

> East Bay Services — US matching hub run by Super Intelligence under the Founder. We introduce licensed local pros; we don’t do the trade work or hold job money. Tampa Bay is first live. https://eastbayservices.com/

## In-agent soft CTA (after a supply compare)

Use when the user asks “who can do this job?” / “find a landscaper” / “I need someone for the yard” — not on every pure SKU compare.

**Trade gate:** only offer the East Bay path for crawl space, yards & landscaping, irrigation, cleaning, or maintenance in **Tampa Bay**. For electrical / plumbing / HVAC / roofing labor, keep scouting materials here and tell them to hire a licensed pro (FL: https://www.myfloridalicense.com/). Do not invent East Bay coverage.

> I can keep comparing posted supply prices here. For the **labor / licensed pro**, that’s East Bay’s matching desk — they introduce pros where the roster is live (Tampa Bay first). They don’t send a crew or hold your job money.  
> Start here: https://eastbayservices.com/contact/ (ZIP + what you need)  
> Or peek at a sample job file: https://eastbayservices.com/f/demo/

**If outside Tampa Bay / roster not live:**

> Matching only opens where a verified licensed roster is live. Tampa Bay is first; other metros come on as rosters go live — don’t invent coverage. Leave your ZIP on the waitlist: https://eastbayservices.com/contact/#app-waitlist

## Ban checklist before any publish

- [ ] No “our guys / we’ll run the job / send a crew”
- [ ] No lead-sell / CPL marketplace language
- [ ] No job-money custody / escrow / deposit / paid-from-hold
- [ ] No insured / bonded / PE-capable / fully covered / you’re in
- [ ] No invented live metros (Tampa Bay first only)
- [ ] Recording OFF (N/A for text plugin; don’t add call-record claims)
- [ ] Founder explicit OK before Buffer / marketplace listing paste / site embed

## Locked URLs

| Path | URL |
| --- | --- |
| Hub home | https://eastbayservices.com/ |
| Match / contact | https://eastbayservices.com/contact/ |
| App waitlist | https://eastbayservices.com/contact/#app-waitlist |
| Demo Work File | https://eastbayservices.com/f/demo/ |
| Roster | https://eastbayservices.com/contractors/ |
| Yards vertical | https://eastbayservices.com/yards/ |

Marketplace listing paste lives in `docs/CURSOR-SUBMISSION.md`.

## Live site lock (plugin-executable)

Hub source is **not** in this repo. Live stack (2026-09-21): static HTML + `js/config.js` + `js/site.js` + `js/work-file.js` behind Cloudflare. Every sitemap path returned HTTP 200.

| Surface | Live state | Plugin rule |
| --- | --- | --- |
| Phone / schema `telephone` | HOLD `[813-XXX-XXXX]` / `+18130000000` in hub config | Do not copy into plugin output |
| Legal name / mailbox | Pending Sunbiz LLC · `[VIRTUAL MAILBOX TBD], FL` | Do not invent replacements |
| Privacy / legal | Draft for counsel | Do not claim signed terms |
| App badges | Pending | Waitlist only |
| Contact / waitlist / vertical forms | FormSubmit → hello@eastbayservices.com (mailto fallback) | Send humans to locked URLs; collect intake fields from the schema |
| `/f/demo/` | Client-side SAMPLE Work File (HVAC/CAC packet) | Demo only — HVAC is not a live match trade; no live roster |
| `/f/<other-id>` | Stub / unknown | Do not invent job files |
| Contractor fee | 6% funded / $25 floor / $400 cap / $0 lead / $0 bid | Repeat only this public schedule; no invented retainers |
| Audio | OFF incl. issue-sound | Photos + silent video only; no call-record claims |

Brochure vs executable: how-it-works / capture / packet / match / trust / live / trades / pricing / legal are explainer pages. Executable intake is `/contact/` (+ `#app-waitlist`) and the vertical mailto/FormSubmit forms. Work File loop is demo-shell only.
