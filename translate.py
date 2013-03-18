#!/usr/bin/python
# -*- coding: utf8 -*-
import glob


def translateOneFile(template, filename):
    print "Translate", filename
    mdContent = None
    title = None
    with open(filename) as f:
        lines = f.readlines()
        title = lines[0][2:].strip()
        mdContent = ''.join(lines[2:])
    assert title
    assert mdContent
    newFile = filename.replace('.md', '.html').replace('_post', 'post')
    with open(newFile, 'wb') as f:
        f.write(template.replace('# title', title).replace('# content here', mdContent))


def translate():
    template = None
    with open('template') as f:
        template = f.read()
    assert template
    for f in glob.glob('_post/*.md'):
        translateOneFile(template, f)

if __name__ == "__main__":
    translate()
