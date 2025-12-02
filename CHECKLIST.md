# 📋 Deployment Checklist

## Before You Start

- [ ] Apify account created (https://apify.com)
- [ ] You have all project files at `/home/wombat/Projects/apify-monetized/google-maps-scraper`

---

## Files Verification

Verify these files exist:

### Configuration Files
- [ ] `.actor/actor.json` ✓
- [ ] `.actor/input_schema.json` ✓
- [ ] `Dockerfile` ✓
- [ ] `requirements.txt` ✓

### Source Code
- [ ] `src/main.py` ✓
- [ ] `src/scraper.py` ✓
- [ ] `src/parser.py` ✓
- [ ] `src/utils.py` ✓
- [ ] `src/config.py` ✓

### Documentation
- [ ] `README.md` ✓

---

## Deployment Steps

### Phase 1: Setup
- [ ] Created Apify account
- [ ] Logged into Apify Console
- [ ] Clicked "Create new actor"
- [ ] Named actor: `google-maps-business-scraper`

### Phase 2: Upload Code
- [ ] Opened actor editor
- [ ] Created `.actor` folder
- [ ] Created `src` folder
- [ ] Copied all 10 files from local to Apify
- [ ] Verified file structure matches

### Phase 3: Build
- [ ] Clicked "Build" button
- [ ] Waited for build (2-3 min)
- [ ] ✅ Build succeeded (green checkmark)

### Phase 4: Test
- [ ] Clicked "Start" or "Console" tab
- [ ] Entered test input:
  ```json
  {
    "searchQuery": "coffee shops",
    "location": "San Francisco, CA",
    "maxResults": 10
  }
  ```
- [ ] Run completed successfully
- [ ] Checked "Dataset" tab
- [ ] Saw 10 coffee shop results
- [ ] Data looks correct (names, addresses, phones, ratings)

### Phase 5: Publish
- [ ] Went to "Publication" tab
- [ ] Set pricing: $0.015 per result
- [ ] Set minimum: $0.50
- [ ] Added title and description
- [ ] Added tags: `google-maps`, `lead-generation`, `business-data`, `scraping`
- [ ] Selected categories: "Data extraction", "Lead generation"
- [ ] Clicked "Publish to Apify Store"
- [ ] ✅ Actor is LIVE!

---

## Post-Launch

### Immediate (Day 1)
- [ ] Share on LinkedIn
- [ ] Share on Twitter/X
- [ ] Post on Reddit (r/webscraping)
- [ ] Send to 3 potential users

### Week 1
- [ ] Monitor first runs
- [ ] Check for errors
- [ ] Read user feedback
- [ ] Fix any bugs

### Week 2-4
- [ ] Start building next scraper (LinkedIn/Yellow Pages)
- [ ] Collect testimonials
- [ ] Refine marketing message
- [ ] Track revenue

---

## Troubleshooting Reference

| Issue | Solution |
|-------|----------|
| Build fails | Check file structure, verify Dockerfile |
| No results | Check Dataset tab, not logs |
| Test fails | Verify input JSON format |
| CAPTCHA | Enable proxy in input config |

---

## Success Metrics

**Week 1:**
- [ ] 5+ test runs completed
- [ ] 1+ user signed up
- [ ] $5+ revenue

**Month 1:**
- [ ] 50+ runs
- [ ] 5+ active users
- [ ] $100+ revenue
- [ ] 4.5+ star rating

**Month 3:**
- [ ] Build LinkedIn scraper
- [ ] Build Yellow Pages scraper
- [ ] Bundle offering created
- [ ] $500+ monthly recurring

---

## Quick Links

- **Apify Console**: https://console.apify.com
- **Your Project**: `/home/wombat/Projects/apify-monetized/google-maps-scraper`
- **Deployment Guides**:
  - Detailed: `DEPLOY_NOW.md`
  - Quick: `QUICK_DEPLOY.md`
  - Full docs: `DEPLOYMENT.md`

---

**Current Status**: ⏳ Ready to deploy
**Next Action**: Follow DEPLOY_NOW.md or QUICK_DEPLOY.md

🚀 **Let's get this live!**
