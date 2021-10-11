git pull origin main
sh GeneratePages.sh
git add ./docs/pages
git commit -m "page generated at $(date)"
git push origin main