# Chief of Staff — rebuild eastbayservices.com

Use this document as your standing orders. Execute it top to bottom. Stop and hand D.J. the exact click whenever GitHub, hosting, or an inbox needs his login. Do not invent credentials.

## Goal

Put the live eastbayservices.com site under version control in its own repo, then ship the corrected homepage.

Done means:

- `https://github.com/dcrandall2481-rgb/east-bay-services` exists with an unmodified "as live" baseline commit
- A pull request in that repo applies the corrected homepage and the start-form intake fix
- Every check in Task 4 passes, with output pasted into the PR
- D.J. approves, the site is deployed, and a real test submission reaches hello@eastbayservices.com
- You report status with links: submitted / waiting / blocked / live

## Identity (do not change)

- East Bay Services is a **United States** matching hub. It is not the contractor, GC, escrow agent, or chatbot.
- Tampa Bay is the first and only live matching metro. Other US ZIPs join the waitlist.
- Live trades: crawl space, yards & landscaping, irrigation, cleaning, maintenance.
- Contractor fee: 6% / $25 floor / $400 cap. $0 per lead. $0 per bid. East Bay never holds job money.
- No audio recording.
- Contact: hello@eastbayservices.com

## Assets

Rebuild kit (this branch; the same paths live on `main` after merge):
https://github.com/dcrandall2481-rgb/trades-supply-scout/tree/cursor/east-bay-rebuild-runbook-a96d

- Mirror script: `scripts/rebuild-east-bay-site.sh`
- Corrected homepage: `docs/east-bay-rebuild/index.html`
- Start-form intake fix: `docs/east-bay-rebuild/js/start-intake.js`
- Copy lock: `references/east-bay-live.json`

Create-repo page: https://github.com/new

## Task 1 — Create the hub repo

1. Open https://github.com/new signed in as `dcrandall2481-rgb`.
2. Owner `dcrandall2481-rgb`, name `east-bay-services`, Private, no README, no license, no .gitignore.
3. Click **Create repository**.

If you cannot sign in as D.J., stop and send him those three lines.

## Task 2 — Mirror the live site and commit the baseline

Needs `bash`, `git`, `curl`, `wget`.

```bash
git clone -b cursor/east-bay-rebuild-runbook-a96d https://github.com/dcrandall2481-rgb/trades-supply-scout.git kit
bash kit/scripts/rebuild-east-bay-site.sh east-bay-services
cd east-bay-services
git init -b main
git add -A
git commit -m "Baseline: eastbayservices.com as live"
git remote add origin https://github.com/dcrandall2481-rgb/east-bay-services.git
git push -u origin main
```

The script must end with `files: N` and exit 0. It exits 1 and prints `MISSING:` lines if any sitemap page or core JS/CSS file failed to download; rerun once, then report the missing list as blocked.

Do not edit anything before the baseline commit is pushed.

## Task 3 — Apply the homepage fix on a branch

```bash
git checkout -b homepage-us-hub
cp ../kit/docs/east-bay-rebuild/index.html index.html
mkdir -p js
cp ../kit/docs/east-bay-rebuild/js/start-intake.js js/start-intake.js
git add index.html js/start-intake.js
git commit -m "Homepage: US matching hub copy, live-in-Tampa-Bay waitlist, start-form intake"
git push -u origin homepage-us-hub
```

What this changes:

- Positions East Bay as a US matching hub, live now in Tampa Bay, and says "not the contractor"
- Restores the waitlist for non-Tampa ZIPs and non-live trades
- Sends every start-form submission (name, email, phone, ZIP, trade, notes) to hello@ through FormSubmit. Before this, the live form only built a local draft and East Bay never received the contact info.
- Labels the demo as a sample, not a real job or contractor
- Drops "insured" (not verified yet) and points license checks to the state board where the work happens

## Task 4 — Verify before opening the PR

Run from the repo root and paste the output into the PR.

```bash
# Script order must be config -> start-intake -> site
grep -n 'config.js\|start-intake.js\|site.js' index.html

# Must print nothing
grep -nE '813-[0-9]{3}-[0-9]{4}|insured|escrow' index.html

# Every sitemap page must return 200 locally
python3 -m http.server 8765 >/dev/null 2>&1 &
sleep 1
for p in $(grep -oE '<loc>[^<]+' sitemap.xml | sed 's#<loc>https://eastbayservices.com##'); do
  printf '%s %s\n' "$(curl -s -o /dev/null -w '%{http_code}' "http://127.0.0.1:8765$p")" "$p"
done
kill %1
```

Then check the three start-form paths in a browser at http://127.0.0.1:8765/ with DevTools → Network open:

| ZIP | Trade | Expected |
| --- | --- | --- |
| 33578 | Yards & landscaping | One POST to formsubmit.co, then redirect to `/f/new/` |
| 10001 | Yards & landscaping | One POST, waitlist shows, email is prefilled |
| 33578 | Something else / not sure | One POST, waitlist says the trade is not on the Tampa Bay roster |

Local tests do not deliver email. That happens in Task 6.

## Task 5 — Open the PR

Open a PR from `homepage-us-hub` into `main` in `dcrandall2481-rgb/east-bay-services`. Title: "Homepage: US matching hub + start-form intake". Paste in the Task 4 output and the three-row result table. Request D.J.'s review.

Do not merge without D.J.'s approval.

## Task 6 — Deploy and confirm intake (after D.J. approves)

1. Merge the PR.
2. Deploy the merged files to the current host. The site is a static here.now site behind Cloudflare. Upload the repo contents as-is and keep SPA mode on. **Do not change DNS or Cloudflare settings.** If you cannot reach the host account, stop and ask D.J. for the upload step.
3. Submit the live start form once with ZIP 33578, trade Yards & landscaping, and D.J.'s own email.
4. FormSubmit sends a one-time activation email to hello@eastbayservices.com. Ask D.J. to click **Activate Form**, then submit again and confirm the job request arrives in the inbox.
5. Purge the Cloudflare cache for `/` and `/js/*` only if the old homepage still shows.

## Hard lines

- Do not invent a phone number, LLC name, street address, live metro, licensed contractor roster, or payment custody. Founder HOLD values (phone `[813-XXX-XXXX]`, "pending Sunbiz LLC filing", `[VIRTUAL MAILBOX TBD]`) stay as-is until D.J. supplies the real ones.
- Do not make any `tel:` link callable.
- Do not claim any metro besides Tampa Bay is live.
- Do not touch Buffer or social posts.
- No secrets, API keys, or affiliate IDs in either repo.
- Do not edit pages other than `index.html` and `js/start-intake.js` in this pass. Report other defects instead of fixing them.

## Report format

Send D.J. one message per status change:

```
East Bay rebuild — <submitted | waiting | blocked | live>
Repo: <url>
PR: <url>
Checks: <pass | fail + which>
Intake email received: <yes | no | not yet>
Next click for D.J.: <exact URL + button, or "none">
```

## First output

Five lines: what you will do in order, then either start Task 1 or hand D.J. the exact click required.
