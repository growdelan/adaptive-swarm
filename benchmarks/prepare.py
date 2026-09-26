#!/usr/bin/env python3
"""Prepare one isolated protocol fixture; never overwrite an existing directory."""
import argparse
import json
from pathlib import Path
import shutil


def prepare(case_id, destination):
    root = Path(__file__).resolve().parent
    cases = json.loads((root / 'cases.json').read_text())
    case = cases[case_id]
    destination = Path(destination).absolute()
    repository = root.parent.resolve()
    resolved = destination.resolve()
    if resolved == repository or repository in resolved.parents:
        raise ValueError('Choose a destination outside the repository')
    files = case['files']
    for name in files:
        path = Path(name)
        if path.is_absolute() or '..' in path.parts:
            raise ValueError(f'Invalid fixture path: {name}')
    destination.mkdir(parents=True, exist_ok=False)
    shutil.copytree(repository / 'adaptive-swarm', destination / '.agents/skills/adaptive-swarm')
    (destination / 'REQUEST.md').write_text(case['request'] + '\n')
    for name, content in files.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content + '\n')
    return destination


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('case', nargs='?')
    parser.add_argument('destination', nargs='?')
    args = parser.parse_args()
    cases = json.loads(Path(__file__).with_name('cases.json').read_text())
    if args.case is None:
        print('\n'.join(cases))
    elif args.destination is None:
        parser.error('destination is required')
    else:
        print(prepare(args.case, args.destination))
