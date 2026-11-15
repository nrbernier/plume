# Plume — lettres liées

Mobile web app for French schoolchildren to practise joined-up cursive (*lettres liées*) on Seyès-ruled lines.

- A picture and a word; the child writes it one letter at a time with a finger and taps **Valider**.
- Three levels per word: **avec guide** (trace track, dotted lines, start dot) → **avec modèle** (word shown) → **de mémoire** (picture + spoken word).
- Letters unlock in stages (i u t l e n m r → o a c d → s p b → v f h j → rare letters → accents); ~100 words in five themes, plus short sentences.
- Per-letter tracking: weak letters are shown under *À revoir* and come back more often. Points, stars and a daily streak.
- Progress is stored in the browser (localStorage) only.

## Build

`index.html` is self-contained. Edit `src/index.src.html`, then run:

```
python3 build.py
```

which inlines the font into `index.html`. Serve with GitHub Pages from the repo root.

## Font

[Playwrite FR Trad](https://fonts.google.com/specimen/Playwrite+FR+Trad) (traditional French school cursive) (via Fontsource), SIL Open Font License 1.1 — see `fonts/OFL.txt`.
