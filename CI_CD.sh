git pull origin main
sh GeneratePages.sh
git add ./docs/pages
now = date
git commit -m "page generated at ${now}"
git push origin main