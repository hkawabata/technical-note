#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys, xml.dom.minidom

u"""
実行結果の tty 出力は問題ないが、ファイルへ結果をリダイレクトで書き込むと
UnicodeEncodeError: 'ascii' codec can't encode characters
が発生するため、標準出力が常に utf8 で自動的に encode されるように設定
"""
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)


base_url = 'https://hkawabata.github.io/technical-note'
indent_width = 2
page_root_path = os.path.dirname(os.path.abspath(__file__)) + '/../docs'
note_path = 'note'

def extract_title_from_file(filepath):
    u"""
    ドキュメントから title: の部分を抜き出す
    なければファイルパス末尾をタイトルとして扱う
    """
    with open(filepath, 'r') as fr:
        lines = fr.readlines()
        titles = [l for l in lines if re.match(r'title: ', l)]
        if len(titles) == 0:
            return filepath.split('/')[-1]
        else:
            return titles[0].lstrip('title: ')


def search(path, display_depth = 0):
    res = ''
    if os.path.isdir(path):
        res += '<li>'
        dirname = path.split('/')[-1]
        files = os.listdir(path)
        if 'index.md' in files:
            title = extract_title_from_file(path + '/index.md')
            res += '<a href="{}">{}</a>'.format(base_url + '/' + path, title)
            files.remove('index.md')
        else:
            res += '<span>{}</span>'.format(dirname)
        res += '<span class="pagetree-accordion">▼</span>'
        if len(files) > 0:
            res += '<ul>' if display_depth > 0 else '<ul class="pagetree-hidden">'
            for file in files:
                res += search(path + '/' + file, display_depth - 1)
            res += '</ul>'
        res += '</li>'
    else:
        html_path = re.sub(r'\.md$', '', path)
        title = extract_title_from_file(path)
        res += '<li><a href="{}">{}</a></li>'.format(base_url + '/' + html_path, title)
    return res


if __name__ == '__main__':
    os.chdir(page_root_path)
    xml_string = '<ul class="pagetree">{}</ul>'.format(search(note_path, 1))
    xml_dom = xml.dom.minidom.parseString(xml_string)
    print xml_dom.toprettyxml(" " * indent_width)

