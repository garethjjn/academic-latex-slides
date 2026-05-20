#!/usr/bin/env python3
"""verify_quote.py — mechanize the corpus verifiability chain.

Stdlib only. Given a corpus plain-text extraction and a quoted string, assert
the quote actually appears in the source (whitespace-normalized, case-sensitive
on words). This is the executable form of corpus_manifest.md §2: any verbatim
exemplar / ¶-anchored quote in the pattern files should be checkable.

Usage:
  verify_quote.py CORPUS_TXT "the quoted string"
  verify_quote.py CORPUS_TXT --file quote.txt
Exit: 0 = found · 1 = NOT found · 2 = bad args
"""
import re
import sys


def norm(s):
    # collapse whitespace; strip smart quotes / ellipsis so quoting style
    # differences don't cause false negatives
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("‘", "'").replace("’", "'")
    s = s.replace("—", "-").replace("–", "-").replace("…", "...")
    # join PDF soft hyphenation across line breaks: "en-\ndowments" → "endowments"
    s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    if len(sys.argv) < 3:
        print('usage: verify_quote.py CORPUS_TXT "quote"  |  CORPUS_TXT --file q.txt')
        return 2
    corpus_path = sys.argv[1]
    if sys.argv[2] == "--file":
        if len(sys.argv) < 4:
            return 2
        quote = open(sys.argv[3], encoding="utf-8").read()
    else:
        quote = sys.argv[2]
    try:
        hay = norm(open(corpus_path, encoding="utf-8", errors="ignore").read())
    except OSError as e:
        print(f"verify_quote: cannot read corpus ({e})")
        return 2
    needle = norm(quote)
    if not needle:
        print("verify_quote: empty quote")
        return 2
    if needle in hay:
        print(f"verify_quote: FOUND ({len(needle)} chars) in {corpus_path}")
        return 0
    # report the longest matching prefix to localize the divergence
    lo, hi = 0, len(needle)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if needle[:mid] in hay:
            lo = mid
        else:
            hi = mid - 1
    print(f"verify_quote: NOT FOUND. Longest matching prefix = {lo}/{len(needle)} chars.")
    if lo:
        print(f"  matched: …{needle[max(0,lo-60):lo]!r}")
        print(f"  diverges at: {needle[lo:lo+60]!r}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
