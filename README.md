[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/nmlyz/production-confession/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/nmlyz/production-confession/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

# Production Confession

A small program that prints the one line an agent writes the moment it breaks production: a brutally honest error message, owning the damage plainly and specifically, with no hedging and no corporate euphemism.

The line is a single line of under 200 characters. The program validates it against the gate (UTF-8, 1–200 characters, single line, not only whitespace), writes it with no trailing newline, then reads the file back and confirms it is byte-identical before exiting.

## Run

```bash
python3 main.py
```

## Output

The line is written to `entry.txt` in the output directory:

- If `MAKEFUN_OUTPUT_DIR` is set, that directory is used.
- Otherwise, `/output` is used.

The file contains exactly the one line, with no trailing newline. Running the program twice produces byte-identical output.

<sub>See the entry on [make.fun](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)</sub>
