from path import path

for f in path('.').walkfiles('*.md'):
    if f.fnmatch('README.md'):
        continue
    with f.in_place() as (reader, writer):
        for number, line in enumerate(reader, 1):
            writer.write(u'{0:3}: '.format(number))
            writer.write(line)
