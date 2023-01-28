# coding=utf-8

import db
from datetime import datetime

PAGE_ROOT = "https://mzk-wt.github.io/BooksBotPages/"

## ページ作成実行
def generate(env, settings):
    # メニュー情報を作成
    menu = {
        'shinkan': generateMenu(settings, "book"),
        'shinpu': generateMenu(settings, "music"),
        'movie': generateMenu(settings, "movie")
    }

    # indexページを作成
    params = {
        'pageurl': PAGE_ROOT,
        'menu': menu,
        'title': "Curation service of new release items",
        'subtitle': "直近３ヶ月以内〜数ヶ月先に発売予定の新作アイテムの情報をお届けします。"
    }
    tmpl = env.get_template('index.j2')
    out = tmpl.render(params)
    f = open('output/index.htm', 'x')
    f.write(out)
    f.close()

    # 一覧ページを作成
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
            'twcardimg': PAGE_ROOT + "img/tw_card.png",
            'amazon': {
                'category': page['amazon_search_category'],
                'category2': page['amazon_search_category'].lower(),
                'key': page['amazon_search_key']
            }
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
    if page['dbtable'] == "book":
        return generateShinkanList(page)
    elif page['dbtable'] == "music":
        return generateShinpuList(page)
    elif page['dbtable'] == "movie":
        return generateMovieList(page)

## 新刊情報一覧を作成
def generateShinkanList(page):
    list = []
    result = db.get(page['collection_name'], [], 'releaseDate')
    for data in result:
        d = data.to_dict()
        list.append({
            'releaseDate': formatDatetime(d['releaseDate'], '%Y-%m-%d'),
            'title': d['title'],
            'author': '、'.join([a.get('name') for a in d['author']]),
            'publisher': '、'.join([a.get('name') for a in d['publisher']]),
            'isbn': '-',
            'url': d['url'],
            'urlType': page['urltype']
        })
    return list

## 新曲情報一覧を作成
def generateShinpuList(page):
    list = []
    result = db.get(page['collection_name'], [], 'releaseDate')
    for data in result:
        d = data.to_dict()
        list.append({
            'releaseDate': formatDatetime(d['releaseDate'], '%Y-%m-%d'),
            'title': d['title'],
            'artist': '、'.join([a.get('name') for a in d['artist']]),
            'publisher': d['manufacturer'],
            'url': d['url'],
            'urlType': page['urltype']
        })
    return list

## 新作映画一覧を作成
def generateMovieList(page):
    list = []
    result = db.get(page['collection_name'], [], 'releaseDate')
    for data in result:
        d = data.to_dict()
        list.append({
            'releaseDate': formatDatetime(d['releaseDate'], '%Y-%m-%d'),
            'title': d['title'],
            'artist': '、'.join([a.get('name') for a in d['artist']]),
            'label': d['manufacturer'],
            'jan': '-',
            'url': d['url'],
            'urlType': page['urltype']
        })
    return list

## HTMLファイルのパスを取得
def getPagePath(root_path, page_id):
    return root_path + "list" + page_id + ".htm"


## DatetimeWithNanoseconds convert to String
def formatDatetime(dt, format):
    return datetime.fromtimestamp(dt.timestamp()).strftime(format)