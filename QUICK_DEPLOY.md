# ⚡ SUPER QUICK DEPLOY (3 Steps)

## 1️⃣ Create ZIP (1 min)

```bash
cd /home/wombat/Projects/apify-monetized
zip -r google-maps-scraper.zip google-maps-scraper/ -x "*venv/*" "*__pycache__/*"
```

Your ZIP is ready at: `/home/wombat/Projects/apify-monetized/google-maps-scraper.zip`

---

## 2️⃣ Deploy to Apify (10 min)

1. **Sign up**: https://apify.com (free $5 credit)
2. **Create actor**: Console → Actors → Create new → Source files
3. **Upload**: Manually copy-paste these files (in order):

### Core Files to Copy-Paste:

**File 1: `.actor/actor.json`**
- Location: `/home/wombat/Projects/apify-monetized/google-maps-scraper/.actor/actor.json`

**File 2: `.actor/input_schema.json`**
- Location: `/home/wombat/Projects/apify-monetized/google-maps-scraper/.actor/input_schema.json`

**File 3: `src/main.py`**
- Location: `/home/wombat/Projects/apify-monetized/google-maps-scraper/src/main.py`

**File 4: `src/scraper.py`**
- Location: `/home/wombat/Projects/apify-monetized/google-maps-scraper/src/scraper.py`

**File 5: `src/parser.py`**
- Location: `/home/wombat/Projects/apify-monetized/google-maps-scraper/src/parser.py`

**File 6: `src/utils.py`**
- Location: `/home/wombat/Projects/apify-monetized/google-maps-scraper/src/utils.py`

**File 7: `src/config.py`**
- Location: `/home/wombat/Projects/apify-monetized/google-maps-scraper/src/config.py`

**File 8: `requirements.txt`**
- Location: `/home/wombat/Projects/apify-monetized/google-maps-scraper/requirements.txt`

**File 9: `Dockerfile`**
- Location: `/home/wombat/Projects/apify-monetized/google-maps-scraper/Dockerfile`

**File 10: `README.md`**
- Location: `/home/wombat/Projects/apify-monetized/google-maps-scraper/README.md`

4. **Build**: Click "Build" button → Wait 2-3 min
5. **Test**: Run with this input:
   ```json
   {
     "searchQuery": "coffee shops",
     "location": "San Francisco, CA",
     "maxResults": 10
   }
   ```

---

## 3️⃣ Publish (5 min)

1. **Pricing**: $0.015 per result, $0.50 minimum
2. **Tags**: `google-maps`, `lead-generation`, `business-data`
3. **Publish**: Click "Publish to Store"

✅ **DONE! You're live on Apify!**

---

## Test Input Examples

```json
{
  "searchQuery": "restaurants",
  "location": "New York, NY",
  "maxResults": 20
}
```

```json
{
  "searchQuery": "dentists",
  "location": "Los Angeles, CA",
  "maxResults": 50
}
```

```json
{
  "searchQuery": "coffee shops near me",
  "location": "10001",
  "maxResults": 100
}
```

---

## If Build Fails

Common fix: Verify all files are in correct structure:
```
.actor/actor.json
.actor/input_schema.json
src/main.py
src/scraper.py
src/parser.py
src/utils.py
src/config.py
Dockerfile
requirements.txt
README.md
```

---

**Total Time: 15-20 minutes**  
**Next: Start marketing and earning!** 💰
