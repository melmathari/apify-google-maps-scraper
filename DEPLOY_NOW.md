# 🚀 Deploy to Apify - Step by Step Guide

**Time Required**: 15-20 minutes  
**Cost**: Free ($5 credit included)

---

## Step 1: Create Apify Account (3 minutes)

1. Go to **https://apify.com**
2. Click "**Sign up for free**"
3. Use your email or GitHub/Google to register
4. Verify your email
5. You'll get **$5 free credits** automatically

✅ **Done?** Proceed to Step 2

---

## Step 2: Prepare Your Code (2 minutes)

### Option A: Create ZIP File (Easiest)

**On your computer:**

1. Navigate to `/home/wombat/Projects/apify-monetized/`
2. Right-click on `google-maps-scraper` folder
3. Select "**Compress**" or "**Create Archive**"
4. Save as `google-maps-scraper.zip`

**OR use terminal:**
```bash
cd /home/wombat/Projects/apify-monetized
zip -r google-maps-scraper.zip google-maps-scraper/ -x "*venv/*" "*__pycache__/*" "*.pyc"
```

### Option B: Use GitHub (Advanced)

1. Create new GitHub repository
2. Push the `google-maps-scraper` folder
3. You'll connect it to Apify in next step

✅ **Done?** You have the ZIP file ready

---

## Step 3: Create New Actor on Apify (5 minutes)

1. **Login to Apify Console**
   - Go to: https://console.apify.com

2. **Navigate to Actors**
   - Click "**Actors**" in left sidebar
   - Click "**Create new**" button (top right)

3. **Choose Source Type**
   - Select "**Source files**"
   - Click "**Create empty actor**"

4. **Name Your Actor**
   - Name: `google-maps-business-scraper`
   - Click "**Create**"

✅ **Done?** You now have an empty actor

---

## Step 4: Upload Your Code (3 minutes)

### If Using ZIP:

1. **Go to "Source" tab**
   - You should see file editor

2. **Delete default files**
   - Click on `main.py` → Delete
   - Click on `Dockerfile` → Delete
   - Delete any other default files

3. **Upload ZIP**
   - Look for "**Upload**" button or "**Import**" option
   - **OR** manually create files:
     - Click "**Add file**" 
     - Copy-paste from your local files

4. **Verify Files Are There**
   - Check you have all these:
     ```
     ├── .actor/
     │   ├── actor.json
     │   └── input_schema.json
     ├── src/
     │   ├── main.py
     │   ├── scraper.py
     │   ├── parser.py
     │   ├── utils.py
     │   └── config.py
     ├── Dockerfile
     ├── requirements.txt
     └── README.md
     ```

### If Using GitHub:

1. Click "**Git integration**" tab
2. Connect your GitHub account
3. Select your repository
4. Select branch (usually `main`)
5. Click "**Save**"

✅ **Done?** All files uploaded

---

## Step 5: Build the Actor (2-3 minutes)

1. **Click "Build" button** (top right)
2. **Wait for build to complete**
   - You'll see logs streaming
   - Takes 2-3 minutes
   - ✅ Success = green checkmark
   - ❌ Error = red X (see Step 8 for fixes)

3. **Build succeeded?**
   - You'll see: "Build finished successfully"

✅ **Done?** Build completed

---

## Step 6: Test Run (2 minutes)

1. **Click "Start" button** or go to "**Console**" tab

2. **Enter test input:**
   ```json
   {
     "searchQuery": "coffee shops",
     "location": "San Francisco, CA",
     "maxResults": 10
   }
   ```

3. **Click "Start"**

4. **Watch it run:**
   - You'll see logs
   - Should complete in 1-2 minutes
   - Look for: "✅ Successfully scraped X businesses"

5. **Check Results:**
   - Click "**Dataset**" tab
   - You should see 10 coffee shops with:
     - Names
     - Addresses  
     - Ratings
     - Phone numbers
     - Websites

✅ **Done?** Test run successful with results

---

## Step 7: Publish to Store (3 minutes)

1. **Go to "Publication" tab**

2. **Set Pricing:**
   - Click "**Monetization**"
   - Enable "**Pay per result**"
   - Price: `0.015` (= $0.015 per business)
   - Minimum charge: `0.50` (= $0.50 minimum)
   - Click "**Save**"

3. **Add Store Details:**
   - **Title**: "Google Maps Business Scraper - No API Key"
   - **Short description**: "Extract business data from Google Maps without API keys. Fast, reliable, cost-effective."
   - **Categories**: Select "Data extraction", "Lead generation"
   - **Tags**: `google-maps`, `lead-generation`, `business-data`, `scraping`

4. **Add README:**
   - Should auto-populate from your README.md
   - If not, copy-paste from your README.md file

5. **Upload Screenshot (Optional but recommended):**
   - Take screenshot of results table
   - Upload it

6. **Click "Publish to Apify Store"**

✅ **Done?** Your actor is LIVE! 🎉

---

## Step 8: Troubleshooting

### Build Failed?

**Error: "Cannot find module"**
- Check `requirements.txt` is uploaded
- Verify `Dockerfile` is present

**Error: "Syntax error"**
- Check Python files for typos
- Verify indentation is correct

**Solution**: Re-upload the files or check file contents

### Test Run Failed?

**Error: "searchQuery is required"**
- Make sure you entered the JSON input correctly
- Include both `searchQuery` and `location`

**Error: "No results found"**
- Try different location (e.g., "New York, NY")
- Use simpler query (e.g., "restaurants")

**Error: "CAPTCHA detected"**
- Enable proxy in input:
  ```json
  "proxyConfig": {
    "useApifyProxy": true
  }
  ```

### No Results Showing?

- Check "Dataset" tab (not logs)
- Look for "Save to dataset" message in logs
- Try running again with maxResults: 5

---

## Step 9: Start Earning! 💰

### Share Your Actor:

1. **Get your actor URL:**
   - Example: `https://apify.com/yourusername/google-maps-business-scraper`

2. **Share on:**
   - LinkedIn: "Just launched my Google Maps scraper!"
   - Twitter/X: Announce with hashtags #apify #webscraping
   - Reddit: r/webscraping, r/SideProject
   - ProductHunt: Launch it there

3. **Market to:**
   - Marketing agencies (for lead generation)
   - Sales teams (for B2B prospecting)
   - Real estate agents (for market research)
   - Entrepreneurs (for competitor analysis)

### Monitor Performance:

- Check Apify dashboard for usage
- Read user reviews and feedback
- Iterate and improve based on feedback

---

## Quick Checklist

Before deploying, verify:

- [ ] Apify account created
- [ ] Code ZIP prepared (or GitHub ready)
- [ ] New actor created on Apify
- [ ] All files uploaded
- [ ] Build successful
- [ ] Test run passed
- [ ] Results look good
- [ ] Pricing configured
- [ ] Store listing complete
- [ ] Actor published

---

## What's Next?

After Google Maps is live:

1. **Monitor** first users and fix any issues
2. **Collect feedback** from users
3. **Build next scraper**:
   - LinkedIn Companies
   - Yellow Pages
   - Yelp
   - Indeed Jobs

4. **Bundle scrapers** for higher pricing
5. **Add AI features** (later phase)

---

## Need Help?

- **Apify Docs**: https://docs.apify.com
- **Apify Discord**: Join for community support
- **Your Files**: Check `DEPLOYMENT.md` for detailed info

---

## 🎉 Congratulations!

Once published, you have a revenue-generating scraper on Apify!

**Expected Timeline to First Sale**: 1-4 weeks with marketing

**Revenue Potential**: $150-3,000+/month

---

**Ready? Start with Step 1! 🚀**
