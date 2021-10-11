git pull origin main
sh GeneratePages.sh
git add .
git commit -m "page generated at ${date}"
git push origin main