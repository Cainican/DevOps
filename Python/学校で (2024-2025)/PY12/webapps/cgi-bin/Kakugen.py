#!/usr/bin/env py

# P.216 kakugen.py（↓のプログラムです）
# cg-binフォルダに入れる

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type:text/html;charset=utf-8")
print("")

print("<html><head><meta charset='utf-8'></head><body>")
print("聞くことに速く語ることに遅くあるべき")
print("</body></html>")