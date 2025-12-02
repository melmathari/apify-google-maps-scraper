# Google Maps Scraper - Deployment Guide

## 📋 Prerequisites

1. **Apify Account**
   - Sign up at https://apify.com
   - Get $5 free credit monthly

2. **Apify CLI** (Optional for local testing)
   ```bash
   npm install -g apify-cli
   apify login
   ```

## 🚀 Deployment Methods

### Method 1: Web Interface (Easiest)

1. **Prepare Your Code**
   - Ensure all files are ready
   - Test locally if possible

2. **Create New Actor**
   - Go to https://console.apify.com/actors
   - Click "Create new"
   - Choose "Source type: Git repository" or "Zip file"

3. **Upload Code**
   - **Option A - GitHub**: Push code to GitHub, connect repository
   - **Option B - Zip**: Create zip of project, upload directly

4. **Configure Build**
   - Dockerfile: `./Dockerfile`
   - Base image: `apify/actor-python-playwright:3.11`

5. **Build & Test**
   - Click "Build"
   - Wait for build to complete
   - Run test with sample input

6. **Publish to Store**
   - Set pricing
   - Add screenshots
   - Write store description
   - Publish!

### Method 2: Apify CLI (Advanced)

1. **Initialize**
   ```bash
   cd google-maps-scraper
   apify init
   ```

2. **Test Locally**
   ```bash
   apify run
   ```

3. **Deploy**
   ```bash
   apify push
   ```

## 🧪 Local Testing (Without Apify)

1. **Install Dependencies**
   ```bash
   cd google-maps-scraper
   pip install -r requirements.txt
   playwright install chromium
   ```

2. **Create Test Input**
   Create `test_input.json`:
   ```json
   {
     "searchQuery": "coffee shops",
     "location": "New York, NY",
     "maxResults": 10
   }
   ```

3. **Run Locally**
   ```bash
   python -m src.main
   ```

## 💰 Monetization Setup

### Pricing Strategy

1. **Usage-based Pricing**
   - Go to Actor settings → Monetization
   - Enable "Pay per result"
   - Set price: $0.01-0.02 per business
   - Minimum charge: $0.50

2. **Subscription (Alternative)**
   - Monthly tier: $49/month (up to 5,000 results)
   - Pro tier: $99/month (up to 20,000 results)

### Store Listing Optimization

1. **Title**: "Google Maps Business Scraper - No API Key Required"

2. **Description**:
   ```
   Extract business data from Google Maps without API keys.
   Get names, addresses, phones, ratings, reviews & more.
   Fast, reliable, cost-effective alternative to Google Places API.
   ```

3. **Tags**: 
   - google-maps
   - lead-generation
   - business-data
   - web-scraping
   - local-seo

4. **Categories**:
   - Data extraction
   - Lead generation
   - Business intelligence

## 📸 Required Assets

### Screenshots (Recommended)
1. Input form filled out
2. Running actor (progress)
3. Results table view
4. Sample JSON output

### Video Demo (Optional but recommended)
- 30-60 second screencast
- Shows form → run → results

## ✅ Pre-Launch Checklist

- [ ] All code files created
- [ ] Requirements.txt complete
- [ ] Dockerfile configured
- [ ] README.md comprehensive
- [ ] Input schema tested
- [ ] Local test successful
- [ ] Apify account created
- [ ] Actor built successfully
- [ ] Test run completed
- [ ] Pricing configured
- [ ] Store listing written
- [ ] Screenshots prepared
- [ ] Published to store

## 🔧 Troubleshooting

### Build Fails
- Check Dockerfile syntax
- Verify requirements.txt versions
- Review build logs in Apify console

### Runtime Errors
- Check logs in run details
- Verify input schema
- Test locally first

### Proxy Issues
- Ensure Apify proxy is enabled
- Check proxy configuration
- Verify country code

## 📈 Post-Launch

### Monitor Performance
- Track success rate
- Monitor compute usage
- Review user feedback

### Iterate
- Fix bugs quickly
- Add features based on feedback
- Update documentation

### Marketing
- Share on social media
- Post on Reddit (r/webscraping)
- Write blog post
- Reach out to potential users

## 🎯 Next Steps

After successful deployment:
1. Monitor first users
2. Collect feedback
3. Fix any issues
4. Start building next scraper (LinkedIn, Yellow Pages, etc.)

---

**Ready to deploy? Start with Method 1! 🚀**
