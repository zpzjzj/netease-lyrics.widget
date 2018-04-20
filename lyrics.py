#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import re
import json

regex = r"string \"(.*)"
p = subprocess.Popen(['/usr/local/bin/dbus-monitor', 'interface=local.musicbox.Lyrics,member=refresh_lyrics'], stdout=subprocess.PIPE, shell=False, bufsize=1000)
count = 0
res = {}
for line in p.stdout:
    line = line.decode('utf-8')
    matches = re.findall(regex, line)
    if matches:
        match = matches[0]
        if not match or match.startswith(":"):
            continue
        else:
            if match.endswith('"'):
                match = match[:-1]
                lines = match.split(" || ")
                res["a"] = lines[0]
                if len(lines) > 1:
                    res["b"] = lines[1]
            else:
                res["title"] = match
            break
print(json.dumps(res, ensure_ascii=False))
p.kill()