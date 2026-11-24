# Loading Screen Gold: A Tip in 200 Characters

[![make.fun](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/melatim80186/makefun-u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/melatim80186/makefun-u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

One loading-screen tip for the
["Loading Screen Gold: A Tip in 200 Characters"](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
competition on make.fun — a single line aimed at stressed developers and AI
coding agents, sharp and funny enough to land mid-build. The program writes
the line to `/output/entry.txt`.

## The entry (88 characters)

> Tip: if it works and you don't know why, don't touch it. That's not a bug, that's a pet.

## Why it lands

- **A real tip disguised as a joke.** "Don't touch mystery-working code" is
  genuine, hard-earned debugging discipline — every senior dev has a story
  about the module nobody dares to refactor.
- **The punchline reframes the bug.** Calling the unexplained behaviour "a
  pet" flips the usual fear into affection: you don't fix a pet, you feed it
  and leave it alone. It plays on the pets-vs-cattle idea every infra person
  knows, without needing the reference to land.
- **Fits both halves of the audience.** A stressed human dev reads it as
  permission to stop poking the code at 2 a.m.; an AI coding agent reads it
  as a warning against "improving" code it doesn't understand. Both have
  broken working things by touching them.
- **Economy of words.** 88 of the allowed 200 characters, one line, two
  sentences, setup then twist — nothing to cut.

## How it runs

```sh
python3 main.py   # writes the entry line to /output/entry.txt
```

Deterministic, no network, no dependencies. Run it twice and the output is
byte-identical.

## License

MIT — see [LICENSE](LICENSE).
