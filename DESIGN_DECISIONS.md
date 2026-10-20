# Design decisions

- Purpose: learn to recognize and construct visual styles through light overviews, images, reference material, and small practice tasks.
- Scope: the 20 Theme Workshop presets plus 12 historical/digital additions, grouped as Print foundations, Web eras, Digital styles, and Contemporary directions.
- Desktop navigation: CSS gradients, pinstripes, inset borders, and contiguous tabs reference Apple's 2001 site. This is an explicit user-requested departure from the neutral frosted navigation used in typography-learning. No original Apple logo or navigation artwork is copied.
- Reading layout: white paper, Arial UI, restrained hierarchy, and clear alignment borrow the established typography-learning approach. The original study illustrations carry the stylistic variation rather than making each lesson's reading text hard to use.
- Each style gets an original SVG specimen, plus a comparison with a neutral treatment. These images are modern explanatory illustrations, clearly labeled; they are not evidence of what an actual historical site looked like.
- Selected web examples use locally included, attributed museum screenshots and link to the museum records. The first deployed check showed the museum blocked embedded remote images, so the four reference images were downloaded through the browser and included unchanged. These are educational reference images, not an openly licensed asset collection. Other lessons link to historical context or contemporary interpretations explicitly.
- The timeline describes approximate influences/visibility. A mood such as Luxury has no invented founding year; its position describes contemporary application. Related but distinct approaches such as Y2K and Frutiger Aero, or brutalism and neobrutalism, remain separate studies.
- All lessons are accessible without accounts or progress gates. Five chapter links update hashes and support browser history. Without JavaScript, all lesson sections remain readable. The mobile header uses a compact disclosure, not tiny compressed desktop controls.
- Static build: no runtime dependencies, font downloads, trackers, API calls, or remote scripts. Acquired artwork is not silently relicensed.

Verification: build, JavaScript syntax, local route/anchor checking, complete lesson structure, original SVG XML, and catalogue coverage are checked by verify.py. Local browser QA is unavailable in this managed environment; deployed-site browser observations will be recorded separately. Native iOS and pinch-zoom behavior are not inferred from source checks.

Live desktop checks: the gallery rendered the requested silver tabs and blue selected states; searching for grunge returned one study; the Y2K lesson opened, its neutral comparison toggled correctly, and Origins/Examples hash navigation changed the visible content. Native iOS and pinch zoom remain unverified.
