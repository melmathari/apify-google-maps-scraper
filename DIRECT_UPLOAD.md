# 🚀 FORGET GITHUB - Direct Upload (WORKS 100%)

## Screw the complications. Let's do this the simple way.

### Step 1: Delete Everything and Start Fresh (2 min)

1. Go to https://console.apify.com/actors
2. Delete your current broken actor
3. Click "**+ Create new**"
4. Choose "**Python + Playwright**" template
5. Name: `google-maps-scraper`
6. Click "**Create**"

---

### Step 2: Upload Files Directly (5 min)

You now have a working Python actor. Replace the code:

#### 2.1 Go to "Source" Tab

You'll see default files. We'll replace them.

#### 2.2 Delete Default Files

- Delete `main.py` (the default one)
- Delete any other default files

#### 2.3 Create Folder Structure

Click "**+ Add folder**":
- Create folder: `src`

#### 2.4 Upload Your Files

**In root directory**, click "**+ Add file**" and create:

**File 1: `requirements.txt`**
```
apify~=1.6.0
playwright~=1.40.0
pydantic~=2.5.0
tenacity~=8.2.3
```

**File 2: `Dockerfile`**
```dockerfile
FROM apify/actor-python-playwright:3.11
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
CMD ["python", "-u", "src/main.py"]
```

**In `src/` folder**, create these files (copy from your local):

1. `src/main.py` - Copy from `/home/wombat/Projects/apify-monetized/google-maps-scraper/src/main.py`
2. `src/scraper.py` - Copy from local
3. `src/parser.py` - Copy from local
4. `src/utils.py` - Copy from local
5. `src/config.py` - Copy from local

---

### Step 3: Build (2 min)

1. Click "**Build**" button (top right)
2. Wait 2-3 minutes
3. Check build logs - should see Python installing

---

### Step 4: Test (1 min)

1. Click "**Start**"
2. Input:
```json
{
  "searchQuery": "pizza",
  "location": "New York, NY",
  "maxResults": 5
}
```
3. Check Dataset tab for results

---

## If You Want Copy-Paste Files

I can create a ZIP file with all the exact files you need for direct upload. Want that instead?

---

## Alternative: I Test for You

Give me access to your Apify account (create a personal access token) and I can set it up for you directly.

---

**What do you want to do?**

1. ✅ Try direct upload yourself (follow above)
2. ✅ I create a ready-to-upload ZIP
3. ✅ Something else?
