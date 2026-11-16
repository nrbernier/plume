# Plume — lettres liées

Mobile web app for French schoolchildren to practise joined-up cursive (*lettres liées*) on Seyès-ruled lines.

- A picture and a word; the child writes it one letter at a time with a finger and taps **Valider**.
- Three levels per word: **avec guide** (trace track, dotted lines, start dot) → **avec modèle** (word shown) → **de mémoire** (picture + spoken word).
- Letters unlock in stages (i u t l e n m r → o a c d → s p b → v f h j → rare letters → accents); ~100 words in five themes, plus short sentences.
- Per-letter tracking: weak letters are shown under *À revoir* and come back more often. Points, stars and a daily streak.
- Progress is stored in the browser (localStorage) only.

## Custom word lists

Settings → *Listes de mots perso*. Lists can be opened as files (for example from a repository folder in the Files app) or loaded from a GitHub repository, including a private one. For a private repository, use a fine-grained personal access token with read-only *Contents* access to that repository only; it is stored in the browser on that device.

One `.txt` file per list, one word or sentence per line, with an optional picture after a bar: an emoji, or the file name of a photo in the same folder (photos are shrunk and kept on the device).

```
# Title of the list
chat 🐱
maison | 🏠
vélo | velo.jpg
Le chat dort. | 🐱
```

`.csv` / `.tsv` (word, picture) and `.json` (`{"title": "…", "items": [{"t": "…", "image": "…"}]}`) also work. Custom lists appear as themes and are not limited by the letters unlocked so far.

## Build

`index.html` is self-contained. Edit `src/index.src.html`, then run:

```
python3 build.py
```

which inlines the font into `index.html`. Serve with GitHub Pages from the repo root.

## Font

[Playwrite FR Trad](https://fonts.google.com/specimen/Playwrite+FR+Trad) (traditional French school cursive) (via Fontsource), SIL Open Font License 1.1 — see `fonts/OFL.txt`.
