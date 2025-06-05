import os
import glob
from collections import defaultdict

ROOT = os.path.join(os.path.dirname(__file__), '..', 'units')

langs = [d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d))]

counts = defaultdict(int)
for lang in langs:
    mdx_files = glob.glob(os.path.join(ROOT, lang, '**', '*.mdx'), recursive=True)
    counts[lang] = len(mdx_files)

for lang in sorted(counts):
    print(f"{lang}: {counts[lang]} MDX files")
