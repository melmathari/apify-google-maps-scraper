# 🔍 Troubleshooting: No Output on Apify

## Quick Fixes (Try These First)

### 1. Check the Dataset Tab (Most Common Issue!)

**Problem**: You're looking at the logs, not the results

**Solution**:
1. In your Apify run page, look for tabs at the top
2. Click "**Dataset**" tab (NOT "Log" tab)
3. You should see a table with coffee shop data

**The logs show "success" but the actual data is in the Dataset tab!**

---

### 2. Check Logs for Errors

Look in the Log tab for these messages:

✅ **Good signs**:
```
✅ Successfully scraped X businesses
Saving X businesses to dataset...
```

❌ **Bad signs**:
```
❌ Error during scraping
No results found
CAPTCHA detected
searchQuery is required
```

---

### 3. Common Issues & Solutions

#### Issue: "Successfully scraped 0 businesses"

**Cause**: Search returned no results or script couldn't find elements

**Solutions**:
1. Try different location: `"New York, NY"` instead of `"San Francisco, CA"`
2. Try simpler query: `"restaurants"` instead of `"coffee shops"`
3. Enable proxy:
   ```json
   {
     "searchQuery": "restaurants",
     "location": "New York, NY",
     "maxResults": 10,
     "proxyConfig": {
       "useApifyProxy": true
     }
   }
   ```

#### Issue: "CAPTCHA detected"

**Cause**: Google blocked the request

**Solution**: Enable Apify proxy in your input:
```json
{
  "searchQuery": "coffee shops",
  "location": "San Francisco, CA",
  "maxResults": 10,
  "proxyConfig": {
    "useApifyProxy": true,
    "apifyProxyCountry": "US"
  }
}
```

#### Issue: Logs show errors about imports

**Cause**: Build issue or missing dependencies

**Solution**: 
1. Go to "Builds" tab
2. Check if build was successful
3. If build failed, check build logs
4. Rebuild: Click "Build" button again

---

## Step-by-Step Debugging

### Step 1: Check Build Status
1. Go to your actor page
2. Click "**Builds**" tab
3. Latest build should be ✅ green
4. If ❌ red, click it and check logs

### Step 2: Check Run Logs
1. Go to your run (the one that says "success")
2. Click "**Log**" tab
3. Search for:
   - "Starting scraping process"
   - "Successfully scraped X businesses"
   - Any error messages with ❌

### Step 3: Check Dataset
1. Click "**Dataset**" tab
2. Should see table with columns:
   - title
   - address
   - phone
   - rating
   - etc.
3. If empty, check logs for why

### Step 4: Check Input
Verify your input is exactly:
```json
{
  "searchQuery": "coffee shops",
  "location": "San Francisco, CA",
  "maxResults": 10
}
```
- No extra commas
- Proper quotes
- Valid JSON format

---

## Test Different Inputs

### Try These Known-Working Inputs:

**Test 1: Simple Restaurant Search**
```json
{
  "searchQuery": "restaurants",
  "location": "10001",
  "maxResults": 5
}
```

**Test 2: Big City**
```json
{
  "searchQuery": "pizza",
  "location": "New York, NY",
  "maxResults": 10
}
```

**Test 3: With Proxy**
```json
{
  "searchQuery": "coffee shops",
  "location": "Los Angeles, CA",
  "maxResults": 10,
  "proxyConfig": {
    "useApifyProxy": true,
    "apifyProxyCountry": "US"
  }
}
```

---

## Check Apify Run Details

### Where to Look:

1. **Run overview**: Shows status (succeeded/failed)
2. **Log tab**: Shows execution logs
3. **Dataset tab**: Shows actual scraped data ⭐
4. **Info tab**: Shows compute units used, runtime
5. **Output tab**: Shows summary statistics

### What "Success" Means:

- ✅ Script ran without crashing
- ❌ Doesn't mean data was found!

Check Dataset tab to see if data was actually scraped.

---

## Code Issue: Missing Module Import

If logs show: `"Cannot import name 'scraper'"` or similar

**Fix**: Check file structure in Apify:
```
src/
  ├── main.py
  ├── scraper.py
  ├── parser.py
  ├── utils.py
  └── config.py
```

All files must be in `src/` folder!

---

## Google Maps Selectors Changed?

If logs show:
- "Could not find search input"
- "Results container not found"

**Cause**: Google updated their HTML

**Fix**: Update selectors in `config.py`:

Contact me or check current Google Maps HTML structure.

---

## Still No Output?

### Share These Details:

1. **Full log output** (copy-paste from Log tab)
2. **Dataset status** (empty or has data?)
3. **Build status** (successful?)
4. **Input used** (exact JSON)
5. **Error messages** (if any)

### Quick Test:

Run this minimal input:
```json
{
  "searchQuery": "pizza",
  "location": "10001",
  "maxResults": 3,
  "proxyConfig": {
    "useApifyProxy": true
  }
}
```

If this works → original input had an issue  
If this fails → check build/code issue

---

## Expected Behavior

### Logs Should Show:
```
[INFO] Actor input: {...}
[INFO] Search query: coffee shops
[INFO] Location: San Francisco, CA
[INFO] Max results: 10
[INFO] Starting Playwright...
[INFO] Starting scraping process...
[INFO] Searching for: coffee shops San Francisco, CA
[INFO] Waiting for search results...
[INFO] Extracting business cards (max 10)...
[INFO] Found X business cards
[INFO] Successfully extracted X unique businesses
[INFO] Saving X businesses to dataset...
[INFO] ✅ Successfully scraped X businesses
```

### Dataset Should Have:
- Row 1: Coffee Shop Name | Address | Phone | Rating | ...
- Row 2: Another Coffee Shop | ...
- Row 3: ...

---

## Emergency: Rebuild from Scratch

If nothing works:

1. Go to actor Settings
2. Delete actor
3. Create new actor
4. Re-upload code from GitHub
5. Build
6. Test again

---

## Contact Support

**Apify Support**: help@apify.com  
**Apify Discord**: https://discord.gg/jyEM2PRvMU  

Provide:
- Actor name
- Run ID
- Full log output

---

**Most likely**: You just need to click the "Dataset" tab! 📊
