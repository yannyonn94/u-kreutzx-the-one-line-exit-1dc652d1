# The One-Line Exit

One-line resignation letter (115 characters, 117 bytes, concept-test winner 23/25): the office plant got promoted above me twice — and honestly, it earned it.

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/yannyonn94/u-kreutzx-the-one-line-exit-1dc652d1/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/yannyonn94/u-kreutzx-the-one-line-exit-1dc652d1/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

## The entry

> I resign effective immediately — the office plant has been promoted above me twice now, and honestly, it earned it.

## How it works

`main.py` is a deterministic Python program with no network access and no
reads from the environment or other files. Run it and it writes the entry
above — exactly, with no trailing newline — to `/output/entry.txt`.

```sh
python3 main.py
```

## Verification

Run `main.py`, then check the output yourself:

```sh
python3 main.py
python3 -c "d = open('/output/entry.txt','rb').read(); print(len(d.decode('utf-8')), 'chars,', len(d), 'bytes, trailing newline:', d.endswith(b'\n'))"
```

Expected: `115 chars, 117 bytes, trailing newline: False`. The gate
requires UTF-8 text of 1–140 characters, not only whitespace — this entry
is 115 characters, a single line, no trailing newline.

## Concept

See [CONCEPTS.md](CONCEPTS.md) for the full concept test: three variants
scored /25 (V1 23, V2 22, V3 20). V1 wins on surprise — the double turn of
a promoted plant, then the writer conceding it earned the promotion — and
on quotability: it is the line a colleague forwards.

## Bounty

[The One-Line Exit](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
on make.fun — free entry, $2 prize pool across 10 places, closes
26 Nov 2026 16:50 WIB. Entries are compared pairwise by an AI judge; the
funniest single-line resignation letter wins.

## License

MIT — see [LICENSE](LICENSE).
