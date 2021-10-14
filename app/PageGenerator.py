# coding=utf-8

import db

PAGE_ROOT = "https://mzk-wt.github.io/BooksBotPages/"

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
            'pageurl': PAGE_ROOT + "pages/list" + page['id'] + ".htm",
            'menu': menu,
            'title': page['title'],
            'subtitle': page['subtitle'],
            'list': list,
            'listtype': page['dbtable'],
            'username': "@" + page['username'],
            'twurl': "https://twitter.com/" + page['username'],
            'twcardimg': PAGE_ROOT + "pages/img/tw_card.png",
            'amazon': {'category': page['amazon_search_category'], 'key': page['amazon_search_key']}
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
    if page['dbtable'] == "SHINKAN":
        return generateShinkanList(page)
    elif page['dbtable'] == "SHINPU":
        return generateShinpuList(page)
    elif page['dbtable'] == "MOVIENEW":
        return generateMovieList(page)

## 新刊情報一覧を作成
def generateShinkanList(page):
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

## 新曲情報一覧を作成
def generateShinpuList(page):
    list = []
    result = db.select("SELECT * FROM SHINPU WHERE GENRE=%s ORDER BY RELEASE_DATE", (page['genre']))
    for data in result:
        list.append({
            'releaseDate': data['RELEASE_DATE'],
            'title': data['TITLE'],
            'artist': data['ARTIST'],
            'publisher': data['PUBLISHER'],
            'url': data['URL'],
            'urlType': page['urltype']
        })
    return list

## 新作映画一覧を作成
def generateMovieList(page):
    list = []
    result = db.select("SELECT * FROM MOVIENEW WHERE GENRE=%s ORDER BY RELEASE_DATE", (page['genre']))
    for data in result:
        list.append({
            'releaseDate': data['RELEASE_DATE'],
            'title': data['TITLE'],
            'artist': data['ARTIST'],
            'label': data['LABEL'],
            'jan': data['JAN'],
            'url': data['URL'],
            'urlType': page['urltype']
        })
    return list

## HTMLファイルのパスを取得
def getPagePath(root_path, page_id):
    return root_path + "list" + page_id + ".htm"
