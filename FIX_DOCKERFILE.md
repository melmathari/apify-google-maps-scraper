# 🔧 URGENT FIX - Actor Running Wrong File

## Problem
Your actor is running `main.js` instead of Python `src/main.py`

## Quick Fix (Apply This Now!)

### Fix 1: Update Dockerfile

Replace your `Dockerfile` with this:

```dockerfile
# Use Apify's Python base image with Playwright
FROM apify/actor-python-playwright:3.11

# Set working directory
WORKDIR /usr/src/app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . ./

# Run the main.py from src directory
CMD ["python", "-u", "src/main.py"]
```

### Fix 2: Commit and Push

```bash
cd /home/wombat/Projects/apify-monetized/google-maps-scraper
git add Dockerfile
git commit -m "Fix: Updated Dockerfile CMD to run Python main.py"
git push
```

This will auto-trigger a new build on Apify!

---

## Alternative: Check Build Settings

If you uploaded files manually (not via GitHub):

1. Go to your actor in Apify Console
2. Click "**Source**" tab
3. Make sure these files are present:
   - `Dockerfile` (in root)
   - `.actor/actor.json` (in .actor folder)
   - `src/main.py` (in src folder)
   - All other src files

4. Click "**Build**" button
5. Wait for build to complete
6. Try running again

---

## What Happened?

The build used a default Node.js template instead of recognizing it's a Python actor. The updated Dockerfile explicitly tells Apify to run Python.

---

## After Fixing

You should see in the logs:
```
[INFO] Actor input: {...}
[INFO] Starting Playwright...
[INFO] Starting scraping process...
```

NOT:
```
If you're seeing this text, it means the actor started the default "main.js" file...
```

---

**Push the fix now and rebuild!** 🚀
