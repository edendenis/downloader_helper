# -*- coding: utf-8 -*-
import json
from pathlib import Path


def convert(ipynb_path: str):
    path = Path(ipynb_path)
    data = json.loads(path.read_text(encoding='utf-8'))

    md_lines = []
    py_lines = []

    for cell in data.get('cells', []):
        source = ''.join(cell.get('source', []))
        if cell.get('cell_type') == 'markdown':
            md_lines.append(source)
            md_lines.append('\n')
        elif cell.get('cell_type') == 'code':
            md_lines.append('```python\n' + source + '\n```\n')
            py_lines.append(source + '\n')

    Path('README.md').write_text(''.join(md_lines), encoding='utf-8')
    Path('README.py').write_text(''.join(py_lines), encoding='utf-8')


def main():
    convert('README.ipynb')
    print('README.md e README.py atualizados')


if __name__ == '__main__':
    main()
