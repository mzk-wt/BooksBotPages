# pages/htmlフォルダをクリア
rm -r pages/html

# ページの自動生成
cd app
python GeneratePages.py
cd ..

# 生成されたページをpages/htmlフォルダへ移動
mkdir pages/html
cp -r app/output/ pages/html/
