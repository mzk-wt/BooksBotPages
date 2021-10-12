# pages/htmlフォルダをクリア
rm -r docs/pages

# ページの自動生成
cd app
pip3 install jinja2
pip3 install pymusql
python GeneratePages.py
cd ..

# 生成されたページをpages/htmlフォルダへ移動
mkdir docs/pages
cp -r app/output/ docs/pages/
