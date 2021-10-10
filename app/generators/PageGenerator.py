## ページ作成実行
def generate(env):

    tmpl = env.get_template('list.j2')

    params = {
        'menu': {
            'links':[
                {'url':'', 'text':'link1'},
                {'url':'', 'text':'link2'},
                {'url':'', 'text':'link3'},
            ]
        },
        'title':'テスト',
        'subtitle':'さぶたいとる',
        'infoList':[
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
            {'releaseDate':'2021/01/01', 'title':'あkjlksjfsdぁ；', 'author':'hogehoge', 'publisher':'marumaru出版', 'isbn':'9784588011054', 'url':'http://aaa', 'urlType':'0'},
        ]
    }
    out = tmpl.render(params)
    f = open('output/list.htm', 'x')
    f.write(out)
    f.close()
