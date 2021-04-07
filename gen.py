#!/usr/bin/env python3

import os

def README(d, s):
    files = sorted([f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f)) and '.md' in f and not 'README.md' in f])
    c = f"# {d}\n\n"
    for f in files:
        c += f"* {f.strip('.md')}\n"
    if len(files) != 0:
        c += "\n"
    c += s
    with open(os.path.join(d, 'README.md'), 'w') as fp:
        fp.write(c)
    return c

def inc(c):
    r = ""
    for l in c.splitlines():
        if len(l) > 0 and "#" in l[0]:
            r += f"#{l}\n"
        else:
            r += f"{l}\n"
    return r

def dirs(d):
    return sorted([f for f in os.listdir(d) if os.path.isdir(os.path.join(d, f)) and not '.' in f[0]])

def render(d):
    c = ""
    for dir in dirs(d):
        c += inc(render(os.path.join(d, dir)))
    return README(d, c)

render('.')
