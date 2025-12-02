# 🔑 GitHub Authentication Fix

## The Error

```
fatal: could not read Username for 'https://github.com': No such device or address
```

**Meaning**: Apify can't access your GitHub repository (it's private and not authorized).

---

## ✅ QUICK FIX: Make Repo Public (2 minutes)

### Option A: Public Repository (Easiest)

1. Go to: https://github.com/wombatsyoks/apify-google-maps-scraper
2. Click "**Settings**" tab (top right)
3. Scroll to bottom → "**Danger Zone**"
4. Click "**Change visibility**"
5. Select "**Make public**"
6. Type repo name to confirm
7. Click "**I understand**"

Then in Apify:
- Go to your actor → Builds tab
- Click "**Build**" again
- Should work now!

**Pros**: Simple, works immediately  
**Cons**: Code is public (but that's fine for a scraper)

---

## ✅ ALTERNATIVE: Keep Private + Connect GitHub (5 minutes)

### Option B: Private Repo with GitHub Integration

1. **In Apify Console**:
   - Go to your actor
   - Click "**Settings**" (left sidebar)
   - Scroll to "**Git integration**" section

2. **Connect GitHub Account**:
   - Click "**Connect GitHub account**" button
   - You'll be redirected to GitHub
   - Click "**Authorize Apify**"
   - Select which repos Apify can access:
     - Either "All repositories"
     - Or select just `apify-google-maps-scraper`
   - Click "**Install & Authorize**"

3. **Back in Apify**:
   - You should now see your repo in dropdown
   - Select: `wombatsyoks/apify-google-maps-scraper`
   - Branch: `main`
   - Click "**Save**"

4. **Build**:
   - Go to "**Builds**" tab
   - Click "**Build**"
   - Should clone successfully!

---

## ✅ FASTEST: Just Use Public Repo

For Apify monetization, **public repos are totally fine**:
- ✅ Shows your work (builds trust)
- ✅ Users can see you maintain it
- ✅ No authentication issues
- ✅ Open source is good for marketing

**Most Apify actors have public source code!**

---

## If You Choose Public Repo

After making it public:

1. **In Apify actor Settings**:
   - Git URL: `https://github.com/wombatsyoks/apify-google-maps-scraper`
   - Branch: `main`
   - No authentication needed!

2. **Build**:
   - Builds tab → Build button
   - Should clone and build successfully

---

## Expected After Fix

Build logs should show:
```
ACTOR: Cloning https://github.com/wombatsyoks/apify-google-maps-scraper.git
Cloning into '.'...
remote: Enumerating objects: X, done.
remote: Counting objects: 100%, done.
Receiving objects: 100%, done.
✓ Git repository cloned
```

Then:
```
Step 1/5 : FROM apify/actor-python-playwright:3.11
Step 2/5 : WORKDIR /usr/src/app
...
Build finished successfully
```

---

## What To Do RIGHT NOW

**Choose one**:

### Path 1: Public Repo (Recommended - 2 min)
1. Make repo public on GitHub
2. Rebuild in Apify
3. Done!

### Path 2: Private Repo (5 min)
1. Connect GitHub account in Apify Settings
2. Authorize Apify
3. Select your repo
4. Rebuild
5. Done!

**I recommend Path 1 (public repo)** - it's how most Apify actors work!

---

**Do this now, then rebuild!** 🔓
