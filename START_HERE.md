# 🎯 START HERE - GitHub Deployment

## What You Have Now

✅ **Complete scraper** ready to deploy  
✅ **All code files** in `/home/wombat/Projects/apify-monetized/google-maps-scraper/`  
✅ **GitHub deployment guide** created

---

## 🚀 Deploy in 3 Steps (25 minutes)

### Step 1: Create GitHub Repo (5 min)

1. Go to **https://github.com** → Log in
2. Click "+" → "New repository"
3. Name: `google-maps-scraper`
4. Choose Private or Public
5. Click "Create repository"
6. **Keep the page open** - you'll need the URL

---

### Step 2: Push Your Code (3 min)

Copy-paste these commands one by one:

```bash
cd /home/wombat/Projects/apify-monetized/google-maps-scraper
git init
git add .
git commit -m "Initial commit: Google Maps Scraper v1.0"
git remote add origin https://github.com/YOUR_USERNAME/google-maps-scraper.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your GitHub username!**

---

### Step 3: Connect to Apify (15 min)

1. **Sign up**: https://apify.com (use GitHub login)
2. **Create actor**: Console → Actors → Create new → Git repository
3. **Connect GitHub**:
   - Paste your repo URL: `https://github.com/YOUR_USERNAME/google-maps-scraper`
   - Branch: `main`
   - Enable "Auto-build on push" ✅
4. **Build**: Click "Build" button → Wait 2-3 min
5. **Test**: Run with:
   ```json
   {
     "searchQuery": "coffee shops",
     "location": "San Francisco, CA",
     "maxResults": 10
   }
   ```
6. **Publish**: Set pricing ($0.015/result) → Publish to Store

---

## 🔄 Auto-Updates Magic

Every time you push to GitHub:
```bash
git add .
git commit -m "Updated selectors"
git push
```

→ **Apify automatically rebuilds** your actor! 🎉

---

## 📚 Full Guides Available

- **DEPLOY_GITHUB.md** - Complete step-by-step (9 steps)
- **GIT_COMMANDS.md** - Quick command reference
- **CHECKLIST.md** - Deployment checklist

---

## ✅ You're Ready!

1. Create GitHub repo now
2. Run the commands in Step 2
3. Connect to Apify in Step 3
4. Start earning! 💰

**Questions?** Check DEPLOY_GITHUB.md for full details.

---

**Let's go! 🚀**
