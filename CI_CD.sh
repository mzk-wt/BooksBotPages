cd `dirname $0`

echo "Get latest apps" 
git pull origin main

#echo "Do generate"
#sh GeneratePages.sh

#echo "Push generated pages"
#git add .
#git commit -m "page generated at $(date)"
#git push origin main
