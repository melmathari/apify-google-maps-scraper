# 🚀 Getting Started with Google Maps Scraper

## Quick Start Guide

### Option 1: Test Locally (5 minutes)

1. **Navigate to project**
   ```bash
   cd /home/wombat/Projects/apify-monetized/google-maps-scraper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

3. **Run test**
   ```bash
   python test_local.py
   ```

4. **View results**
   - Console will show first 3 results
   - Full data saved to `test_output.json`

---

### Option 2: Deploy to Apify (30 minutes)

1. **Create Apify account**
   - Visit: https://apify.com
   - Sign up (free $5 credit)

2. **Create new actor**
   - Go to: https://console.apify.com/actors
   - Click "Create new"
   - Choose "Source type: Zip file"

3. **Upload code**
   ```bash
   # Create zip
   cd /home/wombat/Projects/apify-monetized
   zip -r google-maps-scraper.zip google-maps-scraper/ -x "*.git*" "*__pycache__*"
   
   # Upload the zip file to Apify Console
   ```

4. **Build actor**
   - Click "Build" button
   - Wait 2-3 minutes for build

5. **Test run**
   - Use this input:
   ```json
   {
     "searchQuery": "coffee shops",
     "location": "New York, NY",
     "maxResults": 20
   }
   ```

6. **Publish**
   - Set pricing: $0.015 per result
   - Minimum: $0.50
   - Click "Publish to Store"

---

## File Reference

| File | Purpose |
|------|---------|
| `src/main.py` | Apify actor entry point |
| `src/scraper.py` | Core scraping logic |
| `src/parser.py` | Data extraction |
| `src/utils.py` | Helper functions |
| `src/config.py` | Configuration |
| `.actor/actor.json` | Apify metadata |
| `.actor/input_schema.json` | Input form |
| `Dockerfile` | Container config |
| `requirements.txt` | Python dependencies |
| `README.md` | User documentation |
| `DEPLOYMENT.md` | Deployment guide |
| `test_local.py` | Local testing |

---

## Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "playwright not installed"
```bash
playwright install chromium
```

### "No results found"
- Check if location is valid
- Try different search query
- Verify internet connection

### Need Help?
- Check [README.md](README.md) for detailed docs
- See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment steps
- Read [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) for technical details

---

**🎉 You're all set! Happy scraping!**
