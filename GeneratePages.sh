# pages/htmlフォルダをクリア
rm -r docs/pages

# ページの自動生成
cd app
python GeneratePages.py
cd ..

# 生成されたページをpages/htmlフォルダへ移動
mkdir docs/pages
cp -r app/output/ docs/pages/
