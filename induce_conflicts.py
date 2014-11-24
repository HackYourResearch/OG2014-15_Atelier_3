# -*- coding: utf8 -*-

from path import path

for f in path('.').walkfiles(u'*.md'):
    if f.fnmatch(u'README.md'):
        continue
    print u'Edition du fichier {0} ...'.format(f.name),
    with f.in_place() as (reader, writer):
        for number, line in enumerate(reader, 1):
            writer.write(u'> ')
            writer.write(line)
    print u'Terminé !'
