#!/usr/bin/env python3
# PearEditor patch generator
# Usage: python3 generate_patch.py

import json, os, subprocess


dict_path = os.path.expanduser("~/Downloads/gairaigo_final.json")

with open(dict_path) as f:
    jmdict = json.load(f)

jmdict = {k: v for k, v in jmdict.items() if len(k) >= 3}
print(f"辞書件数: {len(jmdict)}")
print("APIキーを設定してパッチを生成してください")
