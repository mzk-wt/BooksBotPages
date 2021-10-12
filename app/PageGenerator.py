# coding=utf-8

import db

## ページ作成実行
def generate(env, settings):
    # メニュー情報を作成
    menu = {
        'shinkan': generateMenu(settings, "SHINKAN"),
        'shinpu': generateMenu(settings, "SHINPU"),
        'movie': generateMenu(settings, "MOVIENEW")
    }

    # ページを作成
    for page in settings['pages']:
        # 一覧情報を作成
        list = generateList(page)

        # テンプレートへ渡すパラメータを用意
        params = {
            'menu': menu,
            'title': page['title'],
            'subtitle': page['subtitle'],
            'list': list,
            'username': "@" + page['username'],
            'twurl': "https://twitter.com/" + page['username']
        }

        # ページ出力
        tmpl = env.get_template('list.j2')
        out = tmpl.render(params)
        f = open(getPagePath('output/', page['id']), 'x')
        f.write(out)
        f.close()

## メニュー情報を作成
def generateMenu(settings, dbtable):
    links = []
    menu = {'links': links}
    for page in settings['pages']:
        if dbtable == page['dbtable']:
            links.append({
                'url': getPagePath('./', page['id']),
                'text': page['name']
            })
    return menu

## 一覧情報を作成
def generateList(page):
    list = []
    result = db.select("SELECT * FROM SHINKAN WHERE GENRE=%s ORDER BY RELEASE_DATE", (page['genre']))
    for data in result:
        list.append({
            'releaseDate': data['RELEASE_DATE'],
            'title': data['TITLE'],
            'author': data['AUTHOR'],
            'publisher': data['PUBLISHER'],
            'isbn': data['ISBN'] if not data['ISBN'].startswith('B') else '-',
            'url': data['URL'],
            'urlType': page['urltype']
        })
    return list

## HTMLファイルのパスを取得
def getPagePath(root_path, page_id):
    return root_path + "list" + page_id + ".htm"
