# docs/pagesフォルダを削除
rm -r docs/pages

# ページの自動生成
#cd app
cd app2
~/.pyenv/versions/anaconda3-2022.10/bin/python GeneratePages.py
cd ..

# 生成されたページをdocsフォルダへ移動
mv -f app2/output/index.htm docs
mkdir docs/pages
cp -r app2/output/ docs/pages/
