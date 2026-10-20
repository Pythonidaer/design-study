# Design Study

An illustrated, click-through guide to 32 design directions, published at:

https://pythonidaer.github.io/design-study/

The starting set is the 20 presets from Pythonidaer/design-lab's Theme Workshop. Twelve additions cover Victorian, Art Nouveau, Gothic, Pop Art, Cottagecore, pixel design, grunge, Flash-era worlds, skeuomorphism, Frutiger Aero, flat design, and neumorphism.

Each study has Overview, Origins, Visual vocabulary, Examples, and Construction sections, with practice prompts and source links. The guide also includes a timeline, a construction reading path, resource index, searchable gallery, and a neutral/styled illustration comparison.

## Design

The desktop header is an original CSS interpretation of Apple's 2001 silver tabs, pinstripes, inset controls, and blue selected states. The reading layout borrows the calm typography and clear hierarchy of typography-learning. A compact mobile navigation keeps text readable. The user explicitly requested these material-looking treatments; they are intentional exceptions to generic modern styling defaults.

All SVG study illustrations are original educational compositions, not historical screenshots. Selected Web Design Museum screenshots are included locally as attributed educational references, with captions and direct source links. They remain copyrighted by their respective creators and are not claimed as reusable assets. Dates distinguish historical roots from later digital interpretations; labels include movements, eras, moods, and techniques rather than presenting them as one taxonomy.

## Source and workflow

`build.py` contains the curriculum and generates the HTML and SVG illustrations in `dist/`. Shared CSS and JavaScript are maintained in `dist/assets/`. `curriculum.json` is an exported readable content snapshot. No package installation or framework is required.

Run:

```sh
python3 build.py
python3 verify.py
node --check dist/assets/site.js
```

GitHub Actions publishes `dist/` on pushes to main. Repository Pages source should be GitHub Actions.

Primary reference collections:

- https://styleshift.design/
- https://www.webdesignmuseum.org/exhibitions
- https://www.webdesignmuseum.org/gallery/apple-2001
- https://pythonidaer.github.io/typography-learning/

Individual lessons link to specific sources and distinguish original practice exercises from historical references. No source article is reproduced in full. The four historical screenshot files in dist/assets/references/ are credited study references, not original illustrations or open-licensed assets. No analytics, accounts, data collection, or externally loaded JavaScript is used.

## Verification

Source checks validate all 36 HTML pages, chapter targets, local links, illustration XML, per-style content, source URLs, and unique IDs. Browser observations are recorded separately in DESIGN_DECISIONS.md. Native iOS, pinch zoom, and external archive availability require device/source-specific review.
