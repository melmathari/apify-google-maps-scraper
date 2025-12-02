# 🔴 STILL GETTING main.js ERROR? Do This Now!

## The Real Issue

Apify isn't using your Dockerfile during build. It's using a default Node.js template instead.

## Fix in Apify Console (5 minutes)

### Step 1: Check Build Settings

1. Go to your actor in Apify Console
2. Click "**Settings**" tab (left sidebar)
3. Scroll to "**Build**" section
4. Look for "**Base Docker image**" or "**Build tag**"

### Step 2: Set Correct Build Configuration

You should see one of these options:

**Option A: Dockerfile detected**
- ✅ Set to: "Use Dockerfile"
- ✅ Dockerfile path: `./Dockerfile`

**Option B: Base image dropdown**
- ✅ Select: "Custom" or "Python 3.11"
- ✅ NOT "Node.js" (that's your problem!)

### Step 3: Verify File Structure

In Apify Console, click "**Source**" tab and verify:

```
/ (root)
├── .actor/
│   ├── actor.json
│   └── input_schema.json
├── src/
│   ├── main.py       ← THIS must exist!
│   ├── scraper.py
│   ├── parser.py
│   ├── utils.py
│   └── config.py
├── Dockerfile        ← THIS must be in ROOT!
├── requirements.txt
└── README.md
```

**CRITICAL**: Dockerfile must be in the **root directory**, not in any subfolder!

### Step 4: Manual Rebuild

1. Go to "**Builds**" tab
2. Click "**Build**" button (top right)
3. In build options:
   - ✅ Build tag: `latest`
   - ✅ Use cache: Unchecked (force fresh build)
4. Click "**Build**"
5. Watch the build logs

### Step 5: Check Build Logs

Look for these lines in build logs:

✅ **GOOD** - Using your Dockerfile:
```
Step 1/5 : FROM apify/actor-python-playwright:3.11
Step 2/5 : WORKDIR /usr/src/app
Step 3/5 : COPY requirements.txt ./
```

❌ **BAD** - Using default template:
```
Using default Node.js template
npm install...
```

---

## Alternative: Remove actor.json Dockerfile Reference

If Apify still ignores your Dockerfile:

### Edit `.actor/actor.json`

Remove this line:
```json
"dockerfile": "./Dockerfile",
```

Your actor.json should look like:
```json
{
  "actorSpecification": 1,
  "name": "google-maps-business-scraper",
  "title": "Google Maps Business Scraper",
  "description": "...",
  "version": "1.0.0",
  "input": "./.actor/input_schema.json",
  "readme": "./README.md",
  ...
}
```

Then Apify will auto-detect the Dockerfile in the root.

Push this change:
```bash
git add .actor/actor.json
git commit -m "Remove dockerfile reference to let Apify auto-detect"
git push
```

---

## Nuclear Option: Recreate Actor

If nothing works:

1. **In Apify Console**:
   - Go to actor Settings
   - Scroll to bottom
   - Click "Delete actor"

2. **Create new actor**:
   - Console → Actors → Create new
   - Choose "**Python Playwright**" template (NOT empty!)
   - Connect your GitHub repo
   - Branch: main
   - Build

This forces Apify to recognize it as a Python actor.

---

## Verify Success

After rebuild, run logs should show:

```
Actor starting...
[INFO] Actor input: {...}
[INFO] Search query: coffee shops
[INFO] Starting Playwright...
```

NOT:
```
If you're seeing this text...
```

---

## What to Check Right Now

1. ✅ Is `Dockerfile` in the **root** of your repo? (not in a subfolder)
2. ✅ Does Apify Settings → Build show "Python" or "Dockerfile"?
3. ✅ Did you trigger a **fresh build** (not cached)?

**Start with Step 1 above!** 🔧
