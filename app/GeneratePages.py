# coding=utf-8

import shutil
import os
import json
from jinja2 import Environment, FileSystemLoader
import PageGenerator

## jinja2用の環境設定
env = Environment(
    loader = FileSystemLoader('templates', encoding='utf8'),
    trim_blocks = True
)

## ページ作成
def generate():
    # 出力先フォルダをクリア
    shutil.rmtree('output')
    os.mkdir('output')

    # 設定ファイル読み込み
    settings_file = open('settings.json', 'r')
    settings = json.load(settings_file)

    # ページ出力
    PageGenerator.generate(env, settings)

if __name__ == '__main__':
    generate()
