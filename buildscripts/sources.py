import re
import os
import yaml
import argparse
import marko
import marko.ext.gfm

m = marko.Markdown(extensions=[marko.ext.gfm.GFM])
metadata_re = re.compile(r'<!--(.*?)-->', re.DOTALL)

def extract(paths: str):
    return list(sorted(sum(map(parse_md, paths), []), key=lambda x: x.get('filename', x.get('runs', x))))


def save_sources(extracted, to: str) -> str:
    for e in extracted:
        if 'filename' in e and 'code' in e:
            p = os.path.join(to, e['filename'])
            d = os.path.dirname(p)

            if not os.path.exists(d):
                os.makedirs(d)

            with open(p, 'w') as f:
                f.write(e['code'])

    return to


def save_metadata(extracted, to: str) -> str:
    with open(to, 'w') as f:
        yaml.dump(extracted, f, default_flow_style=False, allow_unicode=True)


def compress(path: str):
    p = path.strip('/')
    os.system(f'tar -czvf {p}.tar.gz {p}')


def parse_md(filename: str) -> list:
    def extract_element(a):

        metadata = None

        if list(map(type, a)) == [marko.block.HTMLBlock, marko.block.BlankLine, marko.block.FencedCode]:
            match = metadata_re.match(a[0].children)
            if match:
                metadata = yaml.safe_load(match.group(1))

            return dict(metadata, lang=a[2].lang, code=a[2].children[0].children)

    with open(filename, 'r') as f:
        c = m.parse(f.read()).children
        return list(filter(lambda a: a, map(extract_element, zip(c[:-2], c[1:-1], c[2:]))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extracts code from markdown files'
                                     'Code blocks must have metadata in comment above them'
                                     )

    parser.add_argument('paths', metavar='PATH', type=str, nargs='+',
                        help='Markdown files. Supports globs')

    parser.add_argument('-o', metavar='OUTPUT', dest='output', type=str,
                        required=True, help='directory to put source files to'
                        'NOTE THAT ANYTHING AT GIVEN PATH WILL BE ERASED'
                        )

    args = parser.parse_args()

    e = extract(args.paths)

    save_metadata(e, 'sources-metadata.yaml')

    compress(save_sources(e, args.output))
