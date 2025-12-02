# 🚀 Deploy via GitHub (Auto-Updates!) - RECOMMENDED

**Why GitHub Integration?**
- ✅ Push updates → Apify auto-rebuilds
- ✅ Version control included
- ✅ Professional workflow
- ✅ Easy rollbacks
- ✅ Manage all scrapers from one place

**Time**: 25 minutes total

---

## Step 1: Initialize Git Repository (3 minutes)

### 1.1 Navigate to Project
```bash
cd /home/wombat/Projects/apify-monetized/google-maps-scraper
```

### 1.2 Initialize Git
```bash
git init
```

### 1.3 Add All Files
```bash
git add .
```

### 1.4 Create First Commit
```bash
git commit -m "Initial commit: Google Maps Business Scraper v1.0"
```

✅ **Done!** Local repository created

---

## Step 2: Create GitHub Repository (5 minutes)

### 2.1 Go to GitHub
- Visit: https://github.com
- Log in (or create account if you don't have one)

### 2.2 Create New Repository
1. Click "**+**" icon (top right) → "**New repository**"
2. **Repository name**: `google-maps-scraper`
3. **Description**: "Production-grade Google Maps business scraper for Apify - No API key required"
4. **Visibility**: 
   - 🔒 **Private** (recommended for monetization)
   - 🌍 **Public** (if you want to showcase)
5. **DO NOT** check:
   - ❌ Add README (we already have one)
   - ❌ Add .gitignore (we already have one)
   - ❌ Choose a license
6. Click "**Create repository**"

✅ **Done!** GitHub repo created

---

## Step 3: Push Code to GitHub (2 minutes)

You'll see instructions on GitHub. Follow these:

### 3.1 Add Remote
```bash
git remote add origin https://github.com/YOUR_USERNAME/google-maps-scraper.git
```
*(Replace YOUR_USERNAME with your actual GitHub username)*

### 3.2 Rename Branch (if needed)
```bash
git branch -M main
```

### 3.3 Push Code
```bash
git push -u origin main
```

**You may need to authenticate:**
- Use Personal Access Token (recommended)
- Or SSH key
- GitHub will guide you through this

✅ **Done!** Code is on GitHub

---

## Step 4: Create Apify Account (3 minutes)

1. Go to: https://apify.com
2. Click "**Sign up for free**"
3. **Use GitHub to sign up** (easiest for integration)
   - Click "Sign up with GitHub"
   - Authorize Apify
4. You get **$5 free credits**

✅ **Done!** Apify account ready

---

## Step 5: Create Actor on Apify (2 minutes)

### 5.1 Navigate to Actors
- Go to: https://console.apify.com/actors
- Click "**Create new**" button

### 5.2 Choose Git Repository
1. Select "**Git repository**" tab
2. Click "**Create empty actor**"

### 5.3 Name Your Actor
- **Name**: `google-maps-business-scraper`
- **Title**: "Google Maps Business Scraper"
- Click "**Create**"

✅ **Done!** Empty actor created

---

## Step 6: Connect GitHub Repository (3 minutes)

### 6.1 Go to Settings Tab
- You should be in your new actor
- Click "**Settings**" tab in the left sidebar

### 6.2 Configure Git Integration
Scroll to "**Git integration**" section:

1. **Git URL**: 
   ```
   https://github.com/YOUR_USERNAME/google-maps-scraper
   ```
   *(Replace YOUR_USERNAME)*

2. **Branch**: `main`

3. **Folder** (leave empty unless code is in subfolder)

4. **GitHub integration**:
   - Click "**Connect GitHub account**"
   - Authorize Apify to access your repos
   - Select your repository

### 6.3 Configure Auto-Build
Still in Settings:

1. Find "**Auto-build**" section
2. ✅ Enable "**Automatically build on push**"
3. ✅ Enable "**Automatically build on GitHub commit**"

### 6.4 Save Settings
- Click "**Save**" at the bottom

✅ **Done!** GitHub connected with auto-rebuild

---

## Step 7: Initial Build (3 minutes)

### 7.1 Trigger First Build
- Go to "**Builds**" tab
- Click "**Build**" button
- Or it may auto-build after connecting

### 7.2 Wait for Build
- Takes 2-3 minutes
- You'll see logs streaming
- ✅ Success = green checkmark
- ❌ Failure = see troubleshooting below

### 7.3 Build Successful?
You should see: "**Build finished successfully**"

✅ **Done!** Actor built from GitHub

---

## Step 8: Test Your Actor (2 minutes)

### 8.1 Go to Console
- Click "**Console**" tab or "**Start**" button

### 8.2 Enter Test Input
```json
{
  "searchQuery": "coffee shops",
  "location": "San Francisco, CA",
  "maxResults": 10
}
```

### 8.3 Run It
- Click "**Start**"
- Wait 1-2 minutes
- Check logs for: "✅ Successfully scraped X businesses"

### 8.4 Check Results
- Click "**Dataset**" tab
- You should see 10 coffee shops with data

✅ **Done!** Actor works!

---

## Step 9: Publish to Store (3 minutes)

### 9.1 Go to Publication Tab
- Click "**Publication**" in left sidebar

### 9.2 Set Pricing
1. Click "**Monetization**"
2. Enable "**Pay per result**"
3. **Price per result**: `0.015` ($0.015)
4. **Minimum charge**: `0.50` ($0.50)
5. Click "**Save**"

### 9.3 Complete Store Listing
1. **Title**: "Google Maps Business Scraper - No API Key Required"
2. **Short description**: 
   ```
   Extract business data from Google Maps without API keys. 
   Fast, reliable, cost-effective. Get names, addresses, phones, 
   ratings, reviews & more.
   ```
3. **Categories**: 
   - Data extraction
   - Lead generation
4. **Tags**: 
   ```
   google-maps, lead-generation, business-data, 
   web-scraping, local-seo, b2b-leads
   ```
5. **README**: Auto-populated from your README.md

### 9.4 Publish
- Review everything
- Click "**Publish to Apify Store**"
- ✅ Your actor is LIVE!

✅ **DONE! You're published!** 🎉

---

## 🔄 How Auto-Updates Work

### When You Make Changes:

1. **Edit code locally**:
   ```bash
   cd /home/wombat/Projects/apify-monetized/google-maps-scraper
   # Make your changes...
   ```

2. **Commit changes**:
   ```bash
   git add .
   git commit -m "Fix: Updated selectors for Google Maps UI change"
   ```

3. **Push to GitHub**:
   ```bash
   git push
   ```

4. **Apify auto-rebuilds**:
   - Apify detects the push
   - Automatically triggers new build
   - Users get updated version
   - No manual intervention needed!

### Check Build Status:
- Go to your actor → "Builds" tab
- See all builds with timestamps
- Click any build to see logs

---

## 🎯 Future Updates Workflow

### Adding New Features

1. **Create feature branch** (optional but recommended):
   ```bash
   git checkout -b feature/add-reviews-extraction
   ```

2. **Make changes and test**

3. **Commit**:
   ```bash
   git commit -m "Feature: Added review extraction capability"
   ```

4. **Merge to main**:
   ```bash
   git checkout main
   git merge feature/add-reviews-extraction
   ```

5. **Push**:
   ```bash
   git push
   ```

6. **Apify auto-rebuilds** ✅

### Rollback if Needed

If new version has bugs:

1. **In Apify Console**:
   - Go to "Builds" tab
   - Find previous working build
   - Click "Promote to production"

2. **Fix locally**:
   ```bash
   git revert HEAD  # Or fix the issue
   git push
   ```

---

## 📊 Managing Multiple Scrapers

### Project Structure (Recommended)

```
/home/wombat/Projects/apify-monetized/
├── google-maps-scraper/        (this one)
├── linkedin-scraper/            (next)
├── yellowpages-scraper/         (future)
├── yelp-scraper/                (future)
└── shared/                      (shared utilities)
```

### Each Gets Own Repo:
- `github.com/you/google-maps-scraper`
- `github.com/you/linkedin-scraper`
- `github.com/you/yellowpages-scraper`

### Benefits:
- ✅ Independent versioning
- ✅ Separate deployment
- ✅ Easy to sell individually
- ✅ Can bundle later

---

## 🐛 Troubleshooting

### Build Fails

**Error: "Unable to clone repository"**
- Check GitHub URL is correct
- Verify Apify has access to your repo
- Make sure repo is not empty

**Error: "requirements.txt not found"**
- Verify file is committed to git
- Check capitalization (case-sensitive)

**Solution**: 
```bash
cd /home/wombat/Projects/apify-monetized/google-maps-scraper
git add requirements.txt
git commit -m "Add requirements.txt"
git push
```

### Auto-Build Not Triggering

1. Check Settings → Git integration → Auto-build is enabled
2. Verify GitHub webhook is set up:
   - Go to your GitHub repo → Settings → Webhooks
   - Should see Apify webhook

### Need to Rebuild Manually

- Just click "Build" button anytime
- Or push empty commit:
  ```bash
  git commit --allow-empty -m "Trigger rebuild"
  git push
  ```

---

## 📚 Version Tagging (Best Practice)

### Tag Releases

```bash
# After successful deployment
git tag -a v1.0.0 -m "First production release"
git push origin v1.0.0

# After updates
git tag -a v1.1.0 -m "Added email extraction"
git push origin v1.1.0
```

### Benefits:
- Easy rollback to specific version
- Clear version history
- Professional release management

---

## ✅ Complete Checklist

### Initial Setup
- [ ] Git initialized
- [ ] Code committed locally
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Apify account created (via GitHub)
- [ ] Actor created on Apify
- [ ] GitHub repo connected to Apify
- [ ] Auto-build enabled
- [ ] First build successful
- [ ] Test run passed
- [ ] Actor published to store

### Ongoing
- [ ] GitHub webhook working
- [ ] Auto-builds on push
- [ ] Version tags created
- [ ] README.md stays updated

---

## 🎓 Pro Tips

### 1. Use .gitignore
Already included! Prevents committing:
- `venv/`
- `__pycache__/`
- `*.pyc`
- `apify_storage/`

### 2. Branch Strategy
```bash
main        → Production (Apify uses this)
develop     → Development/testing
feature/*   → New features
hotfix/*    → Bug fixes
```

### 3. Commit Messages
Good format:
```
Type: Short description

- Detailed change 1
- Detailed change 2

Fixes #issue_number
```

Types: `Feature`, `Fix`, `Update`, `Refactor`, `Docs`

### 4. Keep README Updated
Update README.md whenever you:
- Add features
- Change pricing
- Update usage examples
- Fix major bugs

Auto-syncs to Apify Store!

---

## 🚀 What's Next?

### After GitHub Integration:

1. ✅ **Monitor first users**
   - Check Apify dashboard
   - Read reviews
   - Track usage

2. ✅ **Start next scraper**:
   ```bash
   cd /home/wombat/Projects/apify-monetized
   mkdir linkedin-scraper
   cd linkedin-scraper
   # Repeat this process!
   ```

3. ✅ **Marketing**:
   - Share GitHub repo (if public)
   - Write blog post about your stack
   - Show commit history (proves active development)

---

## 📞 Resources

- **GitHub Docs**: https://docs.github.com
- **Apify Git Integration**: https://docs.apify.com/actors/development/source-code#git-integration
- **Your Repo**: `https://github.com/YOUR_USERNAME/google-maps-scraper`
- **Apify Console**: https://console.apify.com

---

## 🎉 Success!

You now have:
- ✅ Professional Git workflow
- ✅ Auto-updating actor
- ✅ Version control
- ✅ Easy rollbacks
- ✅ Scalable for multiple scrapers

**Total Time**: ~25 minutes
**Benefit**: Lifetime auto-updates! 🔄

---

**Ready? Start with Step 1! 🚀**
