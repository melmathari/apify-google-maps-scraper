# 🚨 APIFY CONSOLE FIX - Do This RIGHT NOW

## The Real Problem

Your actor was created as **Node.js** type. Apify is **completely ignoring** your Dockerfile and Python code.

You MUST fix this in **Apify Console** (the website), not in code.

---

## ✅ SOLUTION 1: Delete & Recreate (EASIEST - 10 minutes)

This is the fastest way to fix it:

### 1. Delete Current Actor

1. Go to: https://console.apify.com/actors
2. Find your `google-maps-business-scraper` actor
3. Click on it
4. Click "**Settings**" (left sidebar)
5. Scroll to bottom
6. Click "**Delete actor**" (red button)
7. Confirm deletion

### 2. Create NEW Actor (The Right Way)

1. Click "**+ Create new**" button
2. **IMPORTANT**: Choose "**From template**"
3. Select **"Python + Playwright"** template (NOT empty, NOT Node.js!)
4. Name it: `google-maps-business-scraper`
5. Click "**Create**"

### 3. Connect GitHub

1. In the new actor, go to "**Settings**"
2. Scroll to "**Git integration**"
3. Paste your repo URL: `https://github.com/wombatsyoks/apify-google-maps-scraper`
4. Branch: `main`
5. Enable "**Auto-build on push**"
6. Click "**Save**"

### 4. Build

1. Go to "**Builds**" tab
2. Click "**Build**"
3. Watch build logs - should now show Python!

---

## ✅ SOLUTION 2: Fix Current Actor (If you can't delete)

### Check What Build Type It Is

1. Go to your actor in Apify Console
2. Click "**Builds**" tab
3. Click on latest build
4. Look at the **build logs**

If you see:
```
Using apify/actor-node:20
npm install
```
→ It's set to Node.js (WRONG!)

Should see:
```
Step 1/5 : FROM apify/actor-python-playwright:3.11
```
→ It's using Dockerfile (CORRECT!)

### Force Python Build

1. Go to actor "**Settings**"
2. Look for "**Build**" section
3. Find "**Build tag**" or "**Base image**"
4. Change to: **"Custom Dockerfile"** or **"Python 3.11"**
5. Make sure it says to use `./Dockerfile`
6. Save settings

### Rebuild Without Cache

1. Go to "**Builds**" tab
2. Click "**Build**"
3. **UNCHECK** "Use cache"
4. Build

---

## ✅ SOLUTION 3: Add .apifyignore & Force Detection

Sometimes Apify doesn't detect the Dockerfile. Force it:

### Create .apifyignore

In your repo, create `.apifyignore`:
```
venv/
__pycache__/
*.pyc
.git/
```

Then push:
```bash
cd /home/wombat/Projects/apify-monetized/google-maps-scraper
echo "venv/" > .apifyignore
echo "__pycache__/" >> .apifyignore
echo "*.pyc" >> .apifyignore
git add .apifyignore
git commit -m "Add .apifyignore"
git push
```

---

## 🎯 How to Verify It's Fixed

After rebuilding, check build logs:

### ✅ SUCCESS (Using Dockerfile):
```
Step 1/5 : FROM apify/actor-python-playwright:3.11
 ---> Using cache
Step 2/5 : WORKDIR /usr/src/app
 ---> Using cache
Step 3/5 : COPY requirements.txt ./
Step 4/5 : RUN pip install --no-cache-dir -r requirements.txt
Collecting apify~=1.6.0
Collecting playwright~=1.40.0
...
Step 5/5 : CMD ["python", "-u", "src/main.py"]
Build finished successfully
```

### ❌ FAILURE (Still Using Node):
```
Using apify/actor-node:20
npm install
Installing dependencies...
```

---

## 🔥 RECOMMENDED: Just Delete & Recreate

**Seriously, it's faster.**

1. Delete the current actor (Settings → Delete)
2. Create new from "**Python + Playwright**" template
3. Connect GitHub
4. Build
5. Done!

Takes 10 minutes vs hours of debugging.

---

## After It's Fixed

Run logs should show:
```
[INFO] Actor input: {...}
[INFO] Starting Playwright...
[INFO] Starting scraping process...
```

NOT:
```
If you're seeing this text, it means...
```

---

## What To Do Right Now

1. Go to https://console.apify.com/actors
2. **Delete** your current actor
3. **Create new** from Python template  
4. **Connect** your GitHub repo
5. **Build**
6. **Test**

**Do this now!** The code is fine, it's just the wrong actor type. 🔧
