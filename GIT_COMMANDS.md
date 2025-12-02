# Quick GitHub Setup Commands

## One-Time Setup (Run Once)

```bash
# Navigate to project
cd /home/wombat/Projects/apify-monetized/google-maps-scraper

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: Google Maps Business Scraper v1.0"

# Add GitHub remote (REPLACE YOUR_USERNAME!)
git remote add origin https://github.com/YOUR_USERNAME/google-maps-scraper.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## After Making Changes

```bash
# See what changed
git status

# Add all changes
git add .

# Commit with message
git commit -m "Update: Description of your changes"

# Push (auto-triggers Apify rebuild!)
git push
```

## Create Version Tags

```bash
# After successful deployment
git tag -a v1.0.0 -m "First production release"
git push origin v1.0.0

# After updates
git tag -a v1.1.0 -m "Feature: Added new capability"
git push origin v1.1.0
```

## Rollback to Previous Commit

```bash
# See commit history
git log --oneline

# Revert last commit
git revert HEAD
git push

# Or rollback to specific commit
git reset --hard <commit-hash>
git push --force
```

## Check Status

```bash
# See current status
git status

# See commit history
git log --oneline -10

# See remote URL
git remote -v
```

## Branches (Advanced)

```bash
# Create feature branch
git checkout -b feature/new-feature

# Work on feature...
git add .
git commit -m "Feature: Added X"

# Switch back to main
git checkout main

# Merge feature
git merge feature/new-feature

# Push
git push
```

---

**Note**: Every `git push` to `main` branch triggers automatic rebuild on Apify! 🔄
