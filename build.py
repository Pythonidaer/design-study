"""Build a dependency-free, source-linked design study site."""
from pathlib import Path
from html import escape as e
import json
ROOT=Path(__file__).parent
OUT=ROOT/'dist'
OUT.mkdir(exist_ok=True)
S='https://styleshift.design/styles/'
M='https://www.webdesignmuseum.org/'
T='https://pythonidaer.github.io/typography-learning/'
# Each overview is original educational copy, not a reproduction of a source.
# Dates describe the stated influence or visibility, not exclusive invention dates.
styles=[]
def add(id,name,group,era,year,kind,origin,traits,build,exercise,source,examples,colors):
 styles.append(dict(id=id,name=name,group=group,era=era,year=year,kind=kind,origin=origin,traits=traits,build=build,exercise=exercise,source=source,examples=examples,colors=colors))
add('victorian','Victorian','Print foundations','19th century',1837,'Period and revival traditions',
 'Victorian print brought together many revival styles, ornate advertising, and expanding production methods. Treat the period as a family of approaches, rather than a single mandatory palette.',
 ['Layered serif display lettering','Engraved ornaments and patterned grounds','Formal framing and dense information'],
 ['Draw a decorative border as SVG; keep its ornament separate from the text.','Combine a restrained reading face with one ornate heading treatment. Use a scanned or painted paper texture sparingly.'],
 'Frame one event announcement with original ornament. Remove half the decoration and compare what remains legible.',
 S+'victorian',[['Victorian history and examples',S+'victorian'],['William Morris: books and typography','https://www.vam.ac.uk/articles/william-morris-text']],['#f3ead7','#2b3129','#85553b'])
add('art-nouveau','Art Nouveau','Print foundations','Around 1890–1910',1890,'Historical movement',
 'Art Nouveau linked applied art, illustration, architecture, and lettering through flowing natural forms. On a website, its curves can guide attention around a clear content structure.',
 ['Plant-like curves and branching lines','Integrated decorative lettering','Tall panels and organic framing'],
 ['Draw flowing paths and botanical ornaments in Inkscape. Export reusable SVG frames.','Place readable HTML text inside the frame; preserve generous room around elaborate letterforms.'],
 'Draw one stem that branches into three section dividers. Reuse the same line weight and curve rhythm.',
 S+'art-nouveau',[['Art Nouveau origins and visual examples',S+'art-nouveau']],['#eee9cc','#254d43','#aa733d'])
add('art-deco','Art Deco','Print foundations','1920s–1930s influences',1925,'Historical design movement',
 'Art Deco connects decorative craft with geometric modernity. Its stepped silhouettes and organized symmetry offer a different kind of richness from botanical ornament.',
 ['Stepped and radiating geometry','Symmetry and strong central axes','Fine borders with contrasting display type'],
 ['Construct a small library of stepped corners, fans, and repeated lines as SVG.','Use a clear central grid and carefully spaced display lettering; test all fine rules at mobile sizes.'],
 'Make a title frame from rectangles and straight lines only. Compare a centered and an asymmetric arrangement.',
 S+'art-deco',[['Art Deco principles and examples',S+'art-deco']],['#142e32','#f5e8bd','#c19b55'])
add('bauhaus','Bauhaus','Print foundations','School active 1919–1933',1919,'School and design influence',
 'The Bauhaus brought art, craft, and industrial production into a shared educational project. Its legacy is broader than red circles and yellow triangles: structure and making matter.',
 ['Geometric construction','Asymmetric balance','Type and image aligned to a deliberate structure'],
 ['Build an asymmetric CSS grid with a small set of geometric SVG shapes.','Use size and position to establish hierarchy before adding color. Make every decorative shape earn its place.'],
 'Arrange one heading, one paragraph, and three shapes. Make a second composition with identical content and a different balance.',
 S+'bauhaus',[['Bauhaus history and design vocabulary',S+'bauhaus']],['#f3eee1','#161d25','#d2392b'])
add('swiss','Swiss International','Print foundations','1950s–1960s prominence',1950,'Historical graphic-design movement',
 'Swiss International typography developed a systematic approach to visual communication. Grid relationships, photographic material, and clear information hierarchy are more useful lessons than copying one typeface.',
 ['Consistent alignment and modular grids','Asymmetric sans-serif typography','Contrast through scale and spacing'],
 ['Define columns, gutters, and a type scale in CSS. Align captions and images to the same underlying edges.','Use a few weights and inspect line breaks. Let empty space separate groups before adding borders.'],
 'Set a concert poster in two columns using only type, one photograph, and one accent. Explain every alignment.',
 S+'swiss-international',[['Swiss International history and specimens',S+'swiss-international'],['Typography vocabulary',T+'vocabulary.html']],['#f5f4ef','#171717','#d52b27'])
add('pop-art','Pop Art','Print foundations','1950s–1960s roots',1955,'Art movement and graphic influence',
 'Pop Art brought mass-media imagery and everyday commercial culture into art. Digital interpretations often borrow repetition and graphic punch, but those visual effects are only part of its context.',
 ['Repeated imagery','Halftone dots and flat color areas','Abrupt changes of scale'],
 ['Make a halftone pattern as a tiled SVG and crop an original photograph into repeated panels.','Keep functional labels clear when lettering becomes oversized or highly expressive.'],
 'Repeat one original object image four times. Change only its palette and observe how its mood shifts.',
 S+'pop-art',[['Pop Art context and visual vocabulary',S+'pop-art']],['#ffe12e','#142a54','#e43e63'])
add('memphis','Memphis / Postmodern','Print foundations','1980s origins',1981,'Design movement and influence',
 'Memphis challenged restrained modernist taste with playful patterns, unusual combinations, and emphatic forms. A web adaptation can keep that energy while giving information a stable structure.',
 ['Squiggles and contrasting patterns','Unexpected geometric combinations','Deliberately lively color relationships'],
 ['Create two repeatable SVG patterns and a small shape vocabulary.','Place them around a conventional content layout. Use pattern density to support, rather than obscure, hierarchy.'],
 'Design a section with one pattern, two shapes, and three colors. Test whether the main action is still immediately obvious.',
 S+'memphis',[['Memphis origins and examples',S+'memphis']],['#ffd9e5','#24224e','#386fbb'])
add('gothic','Gothic','Print foundations','Medieval roots; later revivals',1150,'Historical influence and contemporary mood',
 'Gothic architecture and lettering have long histories; a modern dark Gothic interface is a later interpretation. Pointed forms, vertical emphasis, and ornamental lettering do not require an unreadable page.',
 ['Pointed arches and vertical rhythm','Dark grounds with pale highlights','Ornate display lettering'],
 ['Draw pointed frames as SVG and prepare a restrained stone or paper texture.','Reserve elaborate lettering for short headings, with a clear reading face for descriptions and controls.'],
 'Make an original pointed-arch frame for a project title. Test its silhouette in one color before texturing it.',
 S+'gothic',[['Gothic influences and digital interpretation',S+'gothic']],['#17151d','#e9e4d6','#82718e'])
add('editorial','Editorial','Contemporary directions','Print roots; ongoing web use',1900,'Layout approach',
 'Editorial design organizes stories, images, and supporting information. Web editorial layouts adapt publishing practices to fluid screens, links, and changing amounts of content.',
 ['Clear story hierarchy','Captions, rules, and controlled measures','Type and photography composed together'],
 ['Use CSS grid for the story structure and set a comfortable paragraph measure.','Create reusable title, body, caption, and pull-quote roles. Keep the mobile reading order logical.'],
 'Lay out a project case study with a title, a lead paragraph, two images, and captions. Explain the reading order.',
 T+'resources.html',[['Choosing Type roadmap',T+'roadmap/choosing-type.html'],['Print-to-web typography reading path',T+'resources.html#history']],['#f4efe5','#292521','#9b3b2e'])
add('minimal','Minimal','Contemporary directions','Early 2000s web movement; earlier art roots',2000,'Design philosophy and approach',
 'Web minimalism reduces competing elements to focus attention on essential content and tasks. It is a decision process; an almost-empty screen is not automatically useful.',
 ['Few competing emphasis levels','Purposeful empty space','Limited palette and visible actions'],
 ['Start with content and remove elements that do not serve a task.','Use spacing and type hierarchy before containers. Check that links and controls remain recognizable.'],
 'Remove three elements from a project page. Explain whether each removal improves the task or simply makes the page emptier.',
 'https://www.nngroup.com/articles/roots-minimalism-web-design/',[['Minimalism: origins and usability','https://www.nngroup.com/articles/roots-minimalism-web-design/'],['Google in 1998: a comparison, not a movement date',M+'gallery/google-1998']],['#ffffff','#242424','#777777'])
add('playful','Playful','Contemporary directions','Ongoing; no single founding date',2000,'Art-direction label',
 'Playful describes an intended tone rather than one historical movement. Rounded forms, irregular illustration, and unexpected color can support it, but their use should fit the subject and audience.',
 ['Friendly scale changes','Loose illustrative forms','Small surprises within stable navigation'],
 ['Create one original illustrated motif and repeat its line and corner treatment.','Use motion only for specific feedback. Keep forms, labels, and reading order predictable.'],
 'Give one ordinary form a playful heading and illustration without changing the field labels or their order.',
 'https://www.freecodecamp.org/news/design-principles-a-list-of-the-principles-of-design/',[['Design principles for arranging elements','https://www.freecodecamp.org/news/design-principles-a-list-of-the-principles-of-design/']],['#ffe78b','#282345','#df4c7d'])
add('dramatic','Dramatic / Cinematic','Contemporary directions','2000s rich-media sites onward',2002,'Art-direction label',
 'Cinematic sites use composition and timed reveals to establish atmosphere. Film-promotion sites made this especially visible during the Flash era. The drama comes from coordinated assets and pacing.',
 ['Dominant atmospheric images','Strong light-dark separation','Transitions arranged as scenes'],
 ['Prepare separate image, title, and foreground layers. Animate a short sequence with CSS or a JavaScript timeline.','Use user-controlled audio and compressed video only where they add meaning. Provide a reduced-motion presentation.'],
 'Storyboard an entrance in three still frames before writing animation code.',
 M+'gallery/troy-2004',[['Troy, 2004',M+'gallery/troy-2004'],['Douglas Arthur, 2002',M+'flash-websites/douglas-arthur-2002']],['#101820','#f0e3c6','#c19c57'])
add('luxury','Luxury','Contemporary directions','Ongoing branding approach',2000,'Art-direction label',
 'Luxury communicates a desired perception, not a single historic style. Photography, production quality, restraint, or ornament may all contribute. Black and gold alone do not establish it.',
 ['Deliberate spacing and material detail','Restrained competing accents','Careful image and type treatment'],
 ['Choose a material and photographic direction before choosing decorative effects.','Use exact alignment, consistent type roles, and a small accent system. Test fine borders and light type for contrast.'],
 'Design the same project introduction using light and dark backgrounds. Keep the imagery and hierarchy equally deliberate.',
 S+'dark-luxury',[['Luxury as a contemporary visual direction',S+'dark-luxury']],['#1d1d1b','#eee6d5','#b89d63'])
add('nordic','Nordic Minimal','Contemporary directions','20th-century influences; contemporary web interpretation',1950,'Regional influence and modern label',
 'Nordic-inspired digital design borrows ideas of practical simplicity and material warmth. It is a broad interpretation of several design traditions, not a uniform Scandinavian rulebook.',
 ['Quiet color relationships','Practical structure','Warm or natural material cues'],
 ['Use clear typography, a modest spacing scale, and original or licensed material photography.','Avoid filling every surface with decoration; let content and useful controls establish the structure.'],
 'Build a reading panel with one photograph and no decorative container. Compare warm and cool neutrals.',
 S+'nordic',[['Nordic Minimal: principles and interpretation',S+'nordic']],['#edf1eb','#2e413b','#6c8e7c'])
add('collage','Collage','Contemporary directions','20th-century art roots; 1990s–2000s web use',1910,'Image-making technique',
 'Collage combines separate visual fragments into a new composition. On the web it can mix photography, scans, illustration, and lettering while keeping links and text independent.',
 ['Cut edges and visible layering','Mixed image scales','Overlaps with intentional focal points'],
 ['Mask original or licensed source images in an editor. Export fragments with transparency.','Position fragments in a responsive composition; keep essential copy as HTML and preserve a simple reading order.'],
 'Combine three original photographs and one paper texture. Keep a consistent light direction or deliberately explain its absence.',
 M+'all-websites/the-kasander-film-company-2002',[['Kasander, 2002',M+'all-websites/the-kasander-film-company-2002'],['Layer-mask tutorial','https://www.gimp.org/tutorials/community/Layer_Masks/']],['#f4dbc8','#2e2926','#ab4435'])
add('cottagecore','Cottagecore','Contemporary directions','2010s–2020s online visibility',2015,'Internet aesthetic',
 'Cottagecore draws on idealized rural life and handmade domestic imagery. Its contemporary online expression references older craft and pastoral traditions rather than reproducing one period.',
 ['Botanical or handmade motifs','Soft material texture','Gentle, informal compositions'],
 ['Draw original botanical dividers and photograph natural materials.','Use a small repeating texture beneath a clear reading surface, and test patterned areas behind text.'],
 'Create one botanical divider and repeat it across a page without turning every section into an illustrated frame.',
 S+'cottagecore',[['Cottagecore: context and vocabulary',S+'cottagecore']],['#f3eddb','#3b4f37','#b38569'])
add('early-web','Early web','Web eras','1991–1999',1991,'Period of web development',
 'Early websites were shaped by available browsers, network speeds, and HTML capabilities. Their plain documents, image links, and dense directories span many looks rather than one universal style.',
 ['Underlined text links','Default-looking controls and compact layouts','Small images and repeated backgrounds'],
 ['Use semantic HTML first, then deliberate borders and simple tiled graphics.','Keep the historical appearance while retaining keyboard access, responsive widths, and readable modern text sizes.'],
 'Make a small directory page that works without JavaScript. Give every link a meaningful label.',
 M+'early-websites',[['Early websites, 1991–1995',M+'early-websites'],['Google, 1998',M+'gallery/google-1998'],['GeoCities neighborhoods',M+'exhibitions/geocities-neighborhoods']],['#d4d4d4','#151515','#0000a0'])
add('terminal','Terminal','Web eras','Earlier computing roots; ongoing revival',1970,'Computing interface and visual reference',
 'Terminal-inspired sites borrow text-based computing conventions. A green-on-dark screen is one reference, not the only historical terminal appearance. Clarity and useful feedback matter more than imitation.',
 ['Monospaced text','Explicit prompts and status lines','Limited color with clear alignment'],
 ['Use real text, semantic links, and a system monospace stack.','Make any command interface optional and discoverable. Avoid fake error messages or motion that obstructs reading.'],
 'Present your projects as a readable text directory. Make every destination accessible without typing a command.',
 'https://www.computerhistory.org/revolution/input-output/14',[['Computing input and output history','https://www.computerhistory.org/revolution/input-output/14'],['Web history timeline',M+'web-design-history']],['#0b1c12','#b8efc2','#6ac987'])
add('pixel','Pixel design','Web eras','1990s–2000s web visibility',1996,'Graphic technique',
 'Pixel-based graphic styles turn the image grid into a visible part of the design. Small icons and tightly controlled details were common in parts of the early web, alongside many non-pixel styles.',
 ['Hard-edged silhouettes','Limited palettes','Details aligned to an image grid'],
 ['Draw at a small native resolution and preview at the intended display size.','Scale by whole-number factors when preserving hard pixels. Keep paragraph text separate from decorative bitmap lettering.'],
 'Draw one 24-by-24 icon with a four-color palette. Test it at its native size and twice that size.',
 M+'exhibitions/pixel-art-in-web-design',[['Pixel art in web design, 1996–2005',M+'exhibitions/pixel-art-in-web-design']],['#e8eef2','#213644','#468b97'])
add('y2k','Y2K','Web eras','Approximately 1996–2005',1998,'Period aesthetic',
 'Y2K design reflects overlapping visions of a digital future around the millennium. Some sites used metallic surfaces and technical type; others were colorful, playful, and translucent.',
 ['Chrome-like highlights and glossy surfaces','Capsules, rings, and technical details','Layered graphics and assertive color'],
 ['Build precise shapes as SVG and create metallic treatments through gradients or painted assets.','Export decorative graphics independently from labels and links. Low resolution alone does not create the aesthetic.'],
 'Create a capsule navigation button using three lighting bands, then make its normal and pressed states.',
 M+'exhibitions/y2k-aesthetic-in-web-design',[['Y2K historical collection',M+'exhibitions/y2k-aesthetic-in-web-design'],['Kasander, 2002',M+'all-websites/the-kasander-film-company-2002']],['#dbe6f3','#23364e','#508bde'])
add('grunge','Grunge','Web eras','1990s–2000s web visibility',1996,'Graphic aesthetic',
 'Grunge web graphics use roughness and distressed surfaces as expressive material. The look connects to wider print and music cultures; its web examples include many different levels of density.',
 ['Torn edges and worn textures','Imperfect alignment and layered type','Muted grounds with emphatic accents'],
 ['Create masks from original paper scans, marks, or painted textures.','Keep a stable content layout beneath the rough surface. Test texture behind small labels and links.'],
 'Make one heading treatment from an original paper scan. Compare clean and distressed versions at phone size.',
 M+'exhibitions/grunge-in-web-design',[['Grunge historical collection',M+'exhibitions/grunge-in-web-design'],['Adidas, 1996',M+'gallery/adidas-1996'],['Grunge techniques, 2008','https://www.smashingmagazine.com/2008/01/grunge-style-in-modern-web-design/']],['#dbd1b5','#292924','#aa3d29'])
add('flash','Flash-era worlds','Web eras','Late 1990s–2000s',1998,'Technology-enabled approach',
 'Flash was a multimedia platform, not a visual style. Its stage, timeline, and scripting encouraged coordinated animation, unusual navigation, sound, and scene-based websites.',
 ['Scenes instead of ordinary page changes','Coordinated movement and sound','Custom illustrated or rendered navigation'],
 ['Storyboard an interaction and prepare separate background, object, label, and effect layers.','Rebuild behavior using HTML, SVG, Canvas, or WebGL as needed. Sequence sound after user interaction and include reduced-motion alternatives.'],
 'Storyboard a menu entrance, a selection, and a transition. Describe which objects move in each frame.',
 M+'flash-websites',[['Douglas Arthur, 2002',M+'flash-websites/douglas-arthur-2002'],['Troy, 2004',M+'gallery/troy-2004'],['Kasander, 2002',M+'all-websites/the-kasander-film-company-2002']],['#d8eceb','#163e41','#72c1bb'])
add('skeuomorphic','Skeuomorphism','Web eras','Earlier GUI roots; 2000s prominence',2000,'Representational technique',
 'Skeuomorphic interfaces reference familiar objects or materials to communicate use. A leather-bound notebook or physical-looking switch is more specific than a button that merely has a shadow.',
 ['Recognizable physical materials','Controls with apparent depth','Object metaphors tied to function'],
 ['Draw or render the material, frame, and control states separately.','Keep controls as real HTML elements over the artwork. Use consistent lighting and make the pressed state physically plausible.'],
 'Design an original wooden control panel with one blue button. Show its normal, focused, and pressed states.',
 'https://webflow.com/web-design-art-history',[['Apple, 2001: material-looking controls',M+'gallery/apple-2001'],['Art history, realism, and interfaces','https://webflow.com/web-design-art-history']],['#c4a578','#3f3025','#4c8db6'])
add('aero','Frutiger Aero','Web eras','Mid-2000s–early 2010s associations',2005,'Retrospective aesthetic label',
 'Frutiger Aero is a later name for a cluster of optimistic, glossy digital imagery associated with this period. It overlaps with some Y2K traits but often emphasizes natural imagery and clean technological surfaces.',
 ['Gloss and translucency','Sky, water, and natural imagery','Bright blue-green palettes'],
 ['Combine an original landscape image with clear glossy controls and restrained highlights.','Layer a translucent surface above the image, keeping essential text on sufficiently solid backgrounds.'],
 'Make a glossy button on both a plain ground and a sky image. Compare whether the label remains readable.',
 S+'y2k-aero',[['Y2K / Aero: a combined teaching interpretation',S+'y2k-aero'],['Microsoft website evolution',M+'exhibitions/microsoft-windows-websites']],['#d4f1ec','#195879','#50aabd'])
add('synthwave','Synthwave','Digital styles','2000s onward; 1980s references',2005,'Music-linked retro aesthetic',
 'Synthwave looks back at imagined electronic futures, borrowing from 1980s media and later music culture. It is a revival aesthetic, not a faithful copy of what every 1980s interface looked like.',
 ['Neon accents on dark grounds','Perspective grids and glowing horizons','Retro display lettering'],
 ['Draw a perspective grid in SVG and use a small number of glow layers.','Create the horizon and lettering as separate assets. Keep functional text bright and free of heavy blur.'],
 'Create a horizon graphic with a grid and one light source. Make a readable navigation treatment beside it.',
 S+'synthwave',[['Synthwave origins and visual vocabulary',S+'synthwave']],['#1d123a','#f1dcff','#ed64b8'])
add('vaporwave','Vaporwave','Digital styles','2010s online culture',2010,'Music-linked internet aesthetic',
 'Vaporwave remixes consumer imagery, digital nostalgia, and music culture. Pastel palettes and classical fragments are familiar cues, but the broader aesthetic is about juxtaposition and reinterpretation.',
 ['Pastel gradients and nostalgic imagery','Contrasting digital and classical references','Deliberately artificial compositions'],
 ['Combine your own still-life or licensed imagery with geometric digital backdrops.','Use layered images and controlled gradients. Keep decorative lettering distinct from essential interface labels.'],
 'Build a small still life from three original fragments. Change the context with color rather than adding more objects.',
 S+'vaporwave',[['Vaporwave context and examples',S+'vaporwave']],['#f1cde8','#574070','#79bfc7'])
add('flat','Flat design','Digital styles','Early 2010s breakout',2011,'Interface aesthetic',
 'Flat interfaces minimize simulated material and depth. Their simplicity can clarify structure, but overly subtle controls can make interactive elements harder to recognize.',
 ['Solid color areas','Simplified icons','Hierarchy through scale, position, and contrast'],
 ['Use CSS and simple SVG shapes for most surfaces.','Retain visible button boundaries, link styling, focus indicators, and clear hover or pressed feedback.'],
 'Remove decorative depth from one control while preserving all the clues that make it identifiable as a control.',
 'https://www.nngroup.com/articles/flat-design/',[['Flat design: origins and usability','https://www.nngroup.com/articles/flat-design/']],['#f0f4f7','#233b50','#337fa2'])
add('material','Material-inspired','Digital styles','Google system introduced 2014',2014,'Design system and influence',
 'Material is a maintained design system, not merely a shadow recipe. The Workshop preset is an interpretation; the official system includes components, interaction rules, and multiple generations.',
 ['Layering and surface hierarchy','Consistent component behavior','Motion that explains relationships'],
 ['Define surface, elevation, color, and type roles before individual components.','Use component states consistently. Study the official guidance rather than assuming every rounded card is Material.'],
 'Create a button, field, and panel with consistent focused, disabled, and active states.',
 'https://design.google/library/material-design-eras',[['Material Design’s first decade','https://design.google/library/material-design-eras'],['Official Material Design','https://m3.material.io/']],['#f1edf8','#372d47','#786198'])
add('brutalist','Web Brutalism','Digital styles','2010s label; earlier web precedents',2014,'Web aesthetic',
 'Digital brutalism often foregrounds raw structure and utilitarian presentation. It can reference architectural ideas, but it is not a direct translation of concrete buildings into CSS.',
 ['Exposed structure and blunt type','Obvious links','Limited decorative polish'],
 ['Start with semantic HTML and intentionally simple CSS.','Retain reading order and meaningful links. Distinguish purposeful restraint from a broken or inaccessible interface.'],
 'Present a project directory with no images or decorative containers. Make the link hierarchy unmistakable.',
 'https://www.nngroup.com/articles/brutalism-antidesign/',[['Brutalism and antidesign','https://www.nngroup.com/articles/brutalism-antidesign/'],['Brutalist Websites collection','https://brutalistwebsites.com/']],['#ffffff','#121212','#1938bc'])
add('neobrutalist','Neobrutalism','Digital styles','Late 2010s–2020s visibility',2019,'Contemporary interface aesthetic',
 'Neobrutalism combines assertive graphics with more organized interface conventions. Its bold color blocks and hard shadows differ from the stripped-back appearance often associated with web brutalism.',
 ['Heavy outlines','Solid offset shadows','Bright, clearly separated surfaces'],
 ['Use consistent border and shadow tokens in CSS.','Reserve space for shadows and focus rings so they do not collide with neighboring content. Test the layout at enlarged text sizes.'],
 'Build one button with a solid offset shadow. Make pressing it feel like a small physical movement.',
 'https://www.nngroup.com/articles/neobrutalism/',[['Neobrutalism: definition and examples','https://www.nngroup.com/articles/neobrutalism/']],['#f4df88','#1e1d23','#ac83c5'])
add('neumorphism','Neumorphism','Digital styles','Around 2019–2020 visibility',2019,'Surface treatment',
 'Neumorphism makes controls seem molded from the same surface as their background. The soft appearance is recognizable, but weak boundaries can obscure which elements are interactive.',
 ['Paired light and dark shadows','Closely related surface colors','Raised and inset impressions'],
 ['Use paired CSS shadows on a simple surface and build a distinct pressed state.','Add clear labels, boundaries, and focus treatment; do not rely on subtle shading alone to signal action.'],
 'Compare a softly embossed button with a clearly outlined one in dim light and at reduced screen brightness.',
 'https://webflow.com/blog/neumorphism',[['Neumorphism: rise and limitations','https://webflow.com/blog/neumorphism'],['Surface vocabulary and examples',S+'neomorphism']],['#e0e5e8','#3a4b57','#9eaebc'])
add('glass','Glassmorphism','Digital styles','2020s label; earlier translucent UI precedents',2020,'Surface treatment',
 'Glassmorphism uses translucent, blurred surfaces to imply depth. Earlier interfaces used related effects; the modern label describes a treatment that can coexist with many layout styles.',
 ['Blurred backdrop','Translucent surface layers','Fine edges and controlled highlights'],
 ['Use backdrop-filter with a sufficiently opaque background and a solid fallback.','Test text over every part of the underlying image. Keep menus and reading panels opaque when transparency hurts clarity.'],
 'Place one panel over two different backgrounds. Increase its opacity until both versions remain easy to read.',
 'https://www.nngroup.com/articles/glassmorphism/',[['Glassmorphism: examples and best practices','https://www.nngroup.com/articles/glassmorphism/']],['#233b62','#edf5ff','#85c7d6'])
assert len(styles)==32
(ROOT/'curriculum.json').write_text(json.dumps(styles,ensure_ascii=False,indent=2))

# Standalone original teaching illustrations. They are explicitly not archive screenshots.
def specimen(s):
 id=s['id'];bg,ink,accent=s['colors']
 def rect(x,y,w,h,fill,rx=0,stroke='none',sw=1):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
 def text(x,y,t,size=24,fill=None,font='Arial, sans-serif',weight='400',extra=''):return f'<text x="{x}" y="{y}" fill="{fill or ink}" font-family="{font}" font-size="{size}" font-weight="{weight}" {extra}>{e(t)}</text>'
 def line(x,y,xx,yy,color=None,width=2):return f'<path d="M{x} {y}L{xx} {yy}" fill="none" stroke="{color or ink}" stroke-width="{width}"/>'
 a=[rect(0,0,800,500,bg)]
 defs=f'<linearGradient id="metal" x2="0" y2="1"><stop stop-color="#fff"/><stop offset=".3" stop-color="#b0c3d4"/><stop offset=".48" stop-color="#f8fdff"/><stop offset=".52" stop-color="#6d819a"/><stop offset="1" stop-color="#e7eff6"/></linearGradient><linearGradient id="gloss" x2="0" y2="1"><stop stop-color="#c8e5ff"/><stop offset=".49" stop-color="{accent}"/><stop offset=".51" stop-color="#28519a"/><stop offset="1" stop-color="{accent}"/></linearGradient><radialGradient id="sun"><stop stop-color="#ffdb82"/><stop offset="1" stop-color="{accent}"/></radialGradient><pattern id="dots" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="2.5" fill="{ink}"/></pattern><pattern id="grain" width="12" height="8" patternUnits="userSpaceOnUse"><path d="M0 2L12 0M0 7L12 5" stroke="{ink}" opacity=".13"/></pattern><pattern id="wood" width="70" height="150" patternUnits="userSpaceOnUse"><rect width="70" height="150" fill="#806141"/><path d="M1 0V150M15 0Q38 40 16 80T20 150M45 0Q25 60 50 95T53 150" fill="none" stroke="#4c3727" stroke-width="3"/></pattern>'
 serif='Georgia, serif';mono='Courier New, monospace'
 if id in ['swiss','bauhaus','flat','material','neobrutalist','brutalist']:
  if id=='swiss':
   a += [rect(48,48,300,10,ink),rect(410,48,340,220,accent),text(48,128,'Ways',76,weight='700'),text(48,205,'of seeing.',66,weight='700'),text(48,280,'FIELD NOTES / VISUAL STUDIES',16),line(48,314,752,314),text(48,360,'Type. Shape. Space.',25),text(410,360,'A clear structure',20),text(410,392,'for a complex idea.',20),text(48,455,'SWISS INTERNATIONAL',15)]
  elif id=='bauhaus':
   a += [rect(480,50,230,230,accent),f'<circle cx="470" cy="300" r="120" fill="#dfac31"/>',f'<path d="M690 450H410L690 170Z" fill="#294e8c"/>',text(45,120,'ways',82,weight='700'),text(45,206,'of seeing',62,weight='700'),text(48,300,'FIELD NOTES',18),line(48,340,330,340),text(48,385,'Type, shape and space.',20),text(48,445,'Read the study',18)]
  elif id=='neobrutalist':
   a += [rect(66,76,670,340,ink),rect(48,58,670,340,'#fff',stroke=ink,sw=4),text(80,145,'WAYS OF',58,weight='700'),text(80,215,'SEEING.',70,weight='700'),text(80,269,'Type, shape and space.',23),rect(88,315,230,55,ink),rect(80,307,230,55,accent,stroke=ink,sw=3),text(103,342,'Read the study',22),f'<circle cx="610" cy="180" r="65" fill="{accent}" stroke="{ink}" stroke-width="4"/>']
  elif id=='brutalist':
   a += [text(35,70,'FIELD_NOTES / INDEX',22,font=mono),line(35,91,760,91),text(35,165,'WAYS OF SEEING',49,font=mono,weight='700'),text(35,225,'A study in type, shape and space.',23,font=mono),text(35,300,'[1] READ THE STUDY',24,accent,mono,extra='text-decoration="underline"'),text(35,355,'[2] VIEW THE REFERENCES',24,accent,mono,extra='text-decoration="underline"'),line(35,410,760,410),text(35,456,'HTML / STRUCTURE / LINKS',17,font=mono)]
  else:
   radius=20 if id=='material' else 0
   if id=='material':a+=[rect(405,100,310,306,'#b9b0c7',radius)]
   a += [rect(0,0,800,58,accent),text(38,38,'FIELD NOTES',18,'#fff'),text(48,160,'Ways of',56,weight='700'),text(48,225,'seeing.',56,weight='700'),text(48,282,'Type, shape and space.',22),rect(48,322,220,54,accent,radius),text(75,356,'Read the study',20,'#fff'),rect(395,88,310,306,'#fff',radius),f'<circle cx="550" cy="205" r="82" fill="{accent}" opacity=".7"/>',rect(435,320,220,10,ink,5),rect(435,348,150,8,'#a6afb9',4)]
 elif id in ['synthwave','vaporwave','y2k','aero','glass','neumorphism','skeuomorphic','flash','dramatic']:
  if id=='synthwave':
   a += [f'<circle cx="600" cy="220" r="115" fill="url(#sun)"/>']
   for yy in range(145,315,22):a+=[rect(470,yy,260,6,bg)]
   for x in range(-500,1400,100):a+=[line(400,270,x,500,accent,1)]
   for y in [290,320,365,425,490]:a+=[line(0,y,800,y,accent,1)]
   a += [text(48,140,'Ways of',66,'#f2eaff',weight='700'),text(48,220,'seeing.',76,'#f2eaff',weight='700'),text(48,270,'FIELD NOTES / AFTER DARK',17,accent),text(48,440,'Read the study',22,'#fff')]
  elif id=='vaporwave':
   a += [rect(0,0,800,500,'url(#gloss)')]
   for x in range(0,801,50):a+=[line(x,270,x,500,'#f7d9ff',1)]
   for y in range(270,501,40):a+=[line(0,y,800,y,'#f7d9ff',1)]
   a += [rect(455,85,240,300,'#e7d7f3',stroke='#fff',sw=5),f'<ellipse cx="575" cy="180" rx="55" ry="65" fill="#fbf0e6"/>',rect(535,230,80,110,'#e3d6d0'),rect(510,330,130,24,'#faf1e9'),text(45,140,'Ways of',64,ink,serif),text(45,214,'seeing.',72,ink,serif),text(48,270,'A study in digital nostalgia',19,ink,mono),text(48,428,'Read the study',23,ink,serif)]
  elif id=='y2k':
   a += [f'<ellipse cx="565" cy="260" rx="162" ry="100" transform="rotate(-30 565 260)" fill="none" stroke="url(#metal)" stroke-width="32"/>',rect(35,40,730,72,'url(#metal)',34,ink,1),text(66,88,'FIELD NOTES / 2000',27,ink,weight='700'),text(45,200,'Ways of',66,weight='700',extra='font-style="italic"'),text(45,275,'seeing.',76,weight='700',extra='font-style="italic"'),rect(48,330,230,65,'url(#gloss)',32,'#fff',3),text(75,371,'Read the study',23,'#fff'),line(42,440,758,440,accent,3)]
  elif id=='aero':
   a += [rect(0,0,800,500,'#9dd7eb'),f'<path d="M0 320Q230 165 460 320T800 260V500H0Z" fill="#68a953"/>',f'<path d="M0 390Q280 260 800 400V500H0Z" fill="#378fbd"/>']
   for cx,cy,r in [(610,110,65),(690,210,30),(530,230,20)]:a+=[f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" fill-opacity=".25" stroke="#fff" stroke-opacity=".8"/>']
   a += [text(48,130,'Ways of',66,ink),text(48,205,'seeing.',76,ink),text(48,255,'Type, shape and space.',22,ink),rect(48,310,240,65,'url(#gloss)',30,'#fff',2),text(75,352,'Read the study',23,'#fff')]
  elif id=='glass':
   a += [f'<circle cx="610" cy="165" r="180" fill="{accent}"/>',f'<circle cx="180" cy="420" r="200" fill="#866fa7"/>',rect(75,70,650,350,'#ffffff',25,'#e8f2ff',1).replace('fill="#ffffff"','fill="#ffffff" fill-opacity=".16"'),text(115,125,'FIELD NOTES',17,'#fff'),text(115,220,'Ways of seeing.',58,'#fff'),text(115,272,'A study in type, shape and space.',22,'#fff'),rect(115,315,235,56,'#fff',18).replace('fill="#fff"','fill="#fff" fill-opacity=".25"'),text(143,351,'Read the study',23,'#fff')]
  elif id=='neumorphism':
   a += [rect(67,67,660,365,'#bac5cf',30),rect(53,53,660,365,'#fff',30),rect(60,60,660,365,bg,30),text(100,123,'FIELD NOTES',16),text(100,210,'Ways of seeing.',57),text(100,260,'Type, shape and space.',23),rect(101,310,240,61,'#b9c5ce',18),rect(91,300,240,61,'#f7fbff',18),rect(96,305,240,61,bg,18),text(120,344,'Read the study',23)]
  elif id=='skeuomorphic':
   a += [rect(30,25,740,450,'#372e27',12),rect(45,40,710,420,'url(#wood)',8),rect(85,80,630,330,'#3c3229',7, '#b9a47d',5),rect(104,99,592,290,'#d7c4a3',4),text(140,159,'FIELD NOTES',20,ink,serif),text(140,234,'Ways of seeing.',53,ink,serif),text(140,280,'Type, shape and space.',22,ink,serif),rect(140,309,240,56,'url(#gloss)',9,'#302e2b',4),text(165,345,'Read the study',22,'#fff')]
  elif id=='flash':
   for i in range(11):
    q=i*21;a+=[f'<path d="M{q} {q*.65}L{800-q} {q*.65}L{800-q} {500-q*.65}L{q} {500-q*.65}Z" fill="none" stroke="{ink}" stroke-opacity="{.13+i*.035}" stroke-width="3"/>']
   for x,y in [(0,0),(800,0),(0,500),(800,500)]:a+=[line(x,y,400,250,ink,2)]
   a += [rect(55,90,180,310,ink).replace(f'fill="{ink}"',f'fill="{ink}" fill-opacity=".8"'),rect(575,90,170,310,ink).replace(f'fill="{ink}"',f'fill="{ink}" fill-opacity=".8"'),text(75,130,'FIELD NOTES',17,'#fff',mono),text(75,190,'PROJECTS',17,'#fff',mono),text(75,235,'STUDIES',17,'#fff',mono),text(75,280,'CONTACT',17,'#fff',mono),text(595,130,'SYSTEM / 02',15,'#fff',mono),text(270,443,'Ways of seeing.',30,ink)]
  else:
   a += [f'<path d="M0 370L195 80L380 290L535 120L800 375V500H0Z" fill="#4a4339"/>',f'<circle cx="610" cy="115" r="73" fill="{accent}" opacity=".7"/>',rect(0,330,800,170,bg),text(48,75,'FIELD NOTES',17,accent),text(48,245,'Ways of seeing.',66,'#fff',serif),text(48,400,'Type, shape and space.',24,'#e4d6b8'),line(48,425,750,425,accent),text(48,465,'Read the study',21,accent)]
 elif id in ['victorian','art-nouveau','art-deco','gothic','cottagecore','luxury']:
  a += [rect(28,25,744,450,'none',0,accent,2),rect(40,37,720,426,'none',0,accent,1)]
  if id=='art-deco':
   for offset in [0,16,32]:a+=[f'<path d="M{65+offset} 170V{95+offset}H{250-offset}M{735-offset} 170V{95+offset}H{550+offset}" fill="none" stroke="{accent}" stroke-width="3"/>']
   for x in range(260,550,35):a+=[line(400,55,x,115,accent,1)]
  elif id=='gothic':
   a += [f'<path d="M100 400V210Q100 120 185 65Q270 120 270 210V400M530 400V210Q530 120 615 65Q700 120 700 210V400" fill="none" stroke="{accent}" stroke-width="5"/>']
  elif id in ['art-nouveau','cottagecore','victorian']:
   for x,sign in [(85,1),(715,-1)]:
    a += [f'<path d="M{x} 430C{x+sign*100} 280 {x-sign*70} 210 {x+sign*50} 70" fill="none" stroke="{accent}" stroke-width="3"/>']
    for y in [130,190,250,310,370]:a += [f'<ellipse cx="{x+sign*18}" cy="{y}" rx="23" ry="8" transform="rotate({-sign*35} {x+sign*18} {y})" fill="{accent}" opacity=".65"/>']
  a += [text(400,150,'FIELD NOTES',18,accent,serif,extra='text-anchor="middle" letter-spacing="5"'),text(400,240,'Ways of seeing.',58,ink,serif,extra='text-anchor="middle"'),line(230,274,570,274,accent),text(400,320,'Type, shape and space.',23,ink,serif,extra='text-anchor="middle"'),text(400,398,'Read the study',21,accent,serif,extra='text-anchor="middle"')]
 elif id in ['early-web','terminal','pixel']:
  font=mono if id!='early-web' else serif
  if id=='early-web':
   a += [rect(35,35,730,430,'#fff',0,'#777',2),rect(35,35,730,38,'#173e8b'),text(50,61,'Field Notes — Home',20,'#fff'),text(65,140,'Ways of seeing.',57,ink,font),text(65,195,'A study in type, shape and space.',23,ink,font),rect(65,235,665,100,'#bce3df'),text(90,275,'Read the study',25,accent,font,extra='text-decoration="underline"'),text(90,311,'Projects | References | Contact',20,accent,font),text(65,420,'A small directory for curious readers.',19,ink,font)]
  elif id=='terminal':
   a += [text(40,60,'FIELD_NOTES / SESSION 1',20,accent,mono),text(40,135,'> ways_of_seeing',45,ink,mono),text(40,195,'Type, shape and space.',25,ink,mono),text(40,275,'[1] read_the_study',25,ink,mono),text(40,325,'[2] references',25,ink,mono),text(40,410,'ready_',25,accent,mono)]
  else:
   for x,y in [(530,80),(580,130),(630,180),(580,230),(530,280)]:a+=[rect(x,y,48,48,accent),rect(x+50,y,48,48,ink)]
   a += [text(40,85,'FIELD NOTES',22,ink,mono),text(40,190,'Ways of',52,ink,mono,weight='700'),text(40,255,'seeing.',58,ink,mono,weight='700'),rect(40,330,300,65,ink),rect(46,336,288,53,accent),text(65,371,'Read the study',24,'#fff',mono)]
 elif id in ['memphis','playful','pop-art','collage','grunge']:
  if id=='grunge':
   a += [rect(0,0,800,500,'url(#grain)'),f'<path d="M55 100L580 65L605 275L70 300Z" fill="{ink}"/>']
   for i in range(70):
    x=(i*83)%800;y=(i*47)%500;a+=[rect(x,y,((i*7)%40)+2,2,accent)]
   a += [text(85,170,'WAYS OF',60,bg,weight='700',extra='transform="rotate(-4 85 170)"'),text(95,250,'SEEING.',80,bg,weight='700',extra='transform="rotate(-4 95 250)"'),text(80,355,'Type, shape and space.',26,ink,mono),rect(80,390,240,55,accent),text(100,426,'Read the study',23,'#fff')]
  elif id=='collage':
   a += [rect(430,90,260,300,ink,0).replace('x="430"','transform="rotate(8 560 240)" x="430"'),rect(410,70,260,300,'#e6c486').replace('x="410"','transform="rotate(-8 540 220)" x="410"'),f'<circle cx="540" cy="195" r="75" fill="{accent}"/>',f'<path d="M440 365L540 230L670 365Z" fill="#698277"/>',rect(70,95,400,100,'#fff8ed').replace('x="70"','transform="rotate(-3 270 145)" x="70"'),text(88,165,'Ways of seeing.',49,ink,serif),text(70,260,'Type, shape and space.',24,ink,serif),text(70,405,'Read the study',23,accent,serif)]
  else:
   if id=='pop-art':a+=[rect(430,0,370,500,'url(#dots)')]
   elif id=='memphis':
    a += [f'<path d="M500 35q-25 25 0 50t0 50t0 50" fill="none" stroke="{ink}" stroke-width="8"/>',rect(470,280,200,130,'url(#dots)')]
   a += [f'<circle cx="610" cy="195" r="90" fill="{accent}"/>',f'<path d="M450 390L550 230L710 390Z" fill="#e8b847" stroke="{ink}" stroke-width="5"/>',text(45,95,'FIELD NOTES',18),text(45,180,'Ways of',64,weight='700'),text(45,255,'seeing.',72,weight='700'),text(48,315,'Type, shape and space.',22),rect(48,363,240,57,'#fff',24 if id=='playful' else 0,ink,3),text(72,400,'Read the study',23)]
 else: # Editorial, Nordic, Minimal: distinct compositional emphasis.
  if id=='editorial':
   a += [text(45,65,'FIELD NOTES',18,ink,serif),line(45,83,755,83),text(45,160,'Ways of',70,ink,serif),text(45,235,'seeing.',78,ink,serif),rect(435,115,310,260,accent),f'<circle cx="590" cy="235" r="95" fill="#d2c7a2"/>',text(45,300,'A study in type,',23,ink,serif),text(45,332,'shape and space.',23,ink,serif),line(45,393,755,393),text(45,443,'Read the study',22,ink,serif)]
  elif id=='nordic':
   a += [rect(445,40,315,420,'#c5d0be'),f'<path d="M470 350L550 120L640 350Z" fill="{accent}"/>',rect(547,345,12,75,ink),text(45,100,'FIELD NOTES',17),text(45,205,'Ways of',60),text(45,275,'seeing.',68),text(48,330,'Type, shape and space.',21),text(48,410,'Read the study',21)]
  else:a += [text(60,85,'FIELD NOTES',16),text(60,225,'Ways of seeing.',65),text(60,285,'Type, shape and space.',24),line(60,325,740,325,'#bbb',1),text(60,390,'Read the study',22)]
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" role="img" aria-labelledby="title desc"><title id="title">{e(s["name"])} study illustration</title><desc id="desc">Original educational illustration. {e("; ".join(s["traits"]))}. Not an archival screenshot.</desc><defs>{defs}</defs>'+''.join(a)+'</svg>'
for s in styles:(OUT/'assets'/f'{s["id"]}.svg').write_text(specimen(s))
neutral=next(s for s in styles if s['id']=='minimal')
(OUT/'assets/neutral.svg').write_text(specimen(neutral))

def link(url,label):return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(label)}</a>'
def header(prefix='',active='styles'):
 tabs=[('index.html','Styles','styles'),('timeline.html','Timeline','timeline'),('construction.html','Construction','construction'),('resources.html','Resources','resources')]
 nav=''.join(f'<a href="{prefix}{url}"'+(' aria-current="page"' if key==active else '')+f'>{label}</a>' for url,label,key in tabs)
 return f'''<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="tab-bar"><a class="brand" href="{prefix}index.html" aria-label="Design Study home"><span class="brand-orb" aria-hidden="true"></span><span>Design Study</span></a><button class="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="main-nav"><span></span><span></span><span></span></button><nav id="main-nav" class="main-nav" aria-label="Main navigation">{nav}</nav></div><div class="sub-bar"><span>Visual history &amp; practical design</span><a href="{prefix}index.html#style-library">Browse all 32 styles</a></div></header>'''
def footer(prefix=''):
 return f'''<footer class="site-footer"><a href="{prefix}index.html">Design Study</a><p>Original study illustrations. Historical references belong to their respective creators.</p><a href="{prefix}resources.html#about">Sources &amp; scope</a></footer>'''
def page(title,body,prefix='',active='styles'):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Explore design styles through short illustrated lessons, historical references, visual vocabulary, and practical construction."><title>{e(title)} | Design Study</title><link rel="stylesheet" href="{prefix}assets/site.css"></head><body>{header(prefix,active)}<main id="main">{body}</main>{footer(prefix)}<script src="{prefix}assets/site.js" defer></script></body></html>'''

def tile(s,prefix=''):
 return f'''<a class="style-tile" href="{prefix}styles/{s['id']}/" data-style data-search="{e((s['name']+' '+s['group']+' '+s['kind']+' '+' '.join(s['traits'])).lower())}"><img src="{prefix}assets/{s['id']}.svg" alt="{e(s['name'])}: {e(', '.join(s['traits']))}" width="800" height="500" loading="lazy"><div class="tile-title"><h3>{e(s['name'])}</h3><span>View study</span></div><p>{e(s['era'])}</p></a>'''

intro='''<section class="home-intro"><div class="intro-copy"><p class="kicker">An illustrated learning collection</p><h1>Design styles,<br>from print to the web.</h1><p class="lede">Learn where a look comes from, what makes it recognizable, and how to build it yourself.</p><a class="aqua-button" href="styles/y2k/">Start with Y2K</a><a class="text-action" href="timeline.html">Explore the timeline</a></div><div class="intro-art" aria-label="Three original style studies"><img class="hero-back" src="assets/swiss.svg" alt="Swiss study with a red block and disciplined typographic grid" width="800" height="500"><img class="hero-mid" src="assets/y2k.svg" alt="Y2K study with chrome forms and a glossy capsule button" width="800" height="500"><img class="hero-front" src="assets/grunge.svg" alt="Grunge study with distressed lettering and rough texture" width="800" height="500"></div></section><div class="news-strip"><strong>Inside each study</strong><span>Origins · Visual vocabulary · Examples · Construction · Practice</span></div>'''
groups=['Print foundations','Web eras','Digital styles','Contemporary directions']
lib='<section id="style-library" class="library"><div class="section-heading"><div><h2>Explore the styles</h2><p>Historical movements, web eras, and contemporary directions. Each label tells you which.</p></div><label class="search-label">Find a style<input id="style-search" type="search" placeholder="Try Swiss, wood, collage…" autocomplete="off"></label></div><p id="filter-count" class="small" role="status">32 illustrated studies</p>'
for group in groups:
 lib+=f'<section class="gallery-group"><h2>{group}</h2><div class="style-grid">'+''.join(tile(s) for s in styles if s['group']==group)+'</div></section>'
lib+='<p id="empty-search" hidden>No styles match. Try a broader term or clear your search.</p></section>'
(OUT/'index.html').write_text(page('Design styles, from print to the web',intro+lib))

images={
 'y2k':('https://www.webdesignmuseum.org/uploaded/fullscreen/the-kasander-film-company-2002.png','Kasander Film Company, 2002',M+'all-websites/the-kasander-film-company-2002'),
 'collage':('https://www.webdesignmuseum.org/uploaded/fullscreen/the-kasander-film-company-2002.png','Kasander Film Company, 2002',M+'all-websites/the-kasander-film-company-2002'),
 'dramatic':('https://www.webdesignmuseum.org/uploaded/fullscreen/troy-2004.png','Troy, 2004',M+'gallery/troy-2004'),
 'flash':('https://www.webdesignmuseum.org/uploaded/fullscreen/douglas-arthur-2002.png','Douglas Arthur, 2002',M+'flash-websites/douglas-arthur-2002'),
 'skeuomorphic':('https://www.webdesignmuseum.org/uploaded/timeline/apple/apple-2001.png','Apple, 2001',M+'gallery/apple-2001'),
}
chapters=[('overview','Overview'),('origins','Origins'),('vocabulary','Visual vocabulary'),('examples','Examples'),('construction','Construction')]
for i,s in enumerate(styles):
 d=OUT/'styles'/s['id'];d.mkdir(parents=True,exist_ok=True)
 nav=''.join(f'<a href="#{id}" data-chapter="{id}">{label}</a>' for id,label in chapters)
 traits=''.join(f'<li><span class="trait-number">{n+1}</span><p>{e(t)}</p></li>' for n,t in enumerate(s['traits']))
 examples=''.join(f'<li>{link(url,label)}<p class="small">'+('Historical website or archive collection.' if 'webdesignmuseum' in url else 'Context, examples, or a contemporary teaching interpretation.')+'</p></li>' for label,url in s['examples'])
 image=''
 if s['id'] in images:
  src,label,url=images[s['id']]
  image=f'<figure class="archive-figure"><a href="{url}" target="_blank" rel="noopener"><img src="{src}" alt="Archived {e(label)} website screenshot" loading="lazy" class="archive-image" data-external-image></a><figcaption>{e(label)}. Screenshot via Web Design Museum; rights remain with the original creators. <a href="{url}" target="_blank" rel="noopener">Open the archive record</a>.</figcaption></figure>'
 elif s['group']=='Print foundations':
  image='<p class="context-note">These influences began before websites. Follow the reference for historical context and specimens; the illustration above is an original digital interpretation.</p>'
 else:image='<p class="context-note">The illustration above demonstrates this direction; it is not a historical screenshot. References below provide context and examples.</p>'
 build=''.join(f'<li>{e(t)}</li>' for t in s['build'])
 body=f'''<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="../../index.html">Styles</a><span>/</span><span>{e(s['name'])}</span></nav><section class="study-hero"><figure><img id="specimen" src="../../assets/{s['id']}.svg" data-styled="../../assets/{s['id']}.svg" data-neutral="../../assets/neutral.svg" data-style-name="{e(s['name'])}" alt="Original {e(s['name'])} study: {e('; '.join(s['traits']))}" width="800" height="500"><figcaption id="specimen-caption">Original study illustration, not an archival screenshot.</figcaption><button id="compare-neutral" class="silver-button" aria-pressed="false">Compare with neutral</button></figure><div class="study-heading"><p class="kicker">{e(s['group'])}</p><h1>{e(s['name'])}</h1><p class="era">{e(s['era'])}</p><p>{e(s['kind'])}</p><div class="palette" aria-label="Illustrative palette">{''.join(f'<span style="background:{c}" aria-label="{c}"></span>' for c in s['colors'])}</div><p class="small">A starting palette, not a historical rule.</p></div></section><div class="lesson-layout"><aside><nav class="chapters" aria-label="Lesson sections">{nav}</nav><p class="small">Choose any section. All studies are open.</p></aside><article class="lesson-content">
<section id="overview" data-panel><h2>Recognize the approach</h2><p>{e(s['origin'].split('. ')[0]+'.')}</p><h3>Look for</h3><ul class="plain-list">{''.join('<li>'+e(t)+'</li>' for t in s['traits'])}</ul><h3>Your learning goal</h3><p>Describe the visual decisions before choosing a tool. Then make one small example that uses them deliberately.</p><a class="silver-button next-section" href="#origins">Next: Origins</a></section>
<section id="origins" data-panel><h2>Where it comes from</h2><p>{e(s['origin'])}</p><dl class="origin-facts"><div><dt>Period or influence</dt><dd>{e(s['era'])}</dd></div><div><dt>What this label describes</dt><dd>{e(s['kind'])}</dd></div></dl><p class="small">Dates describe broad influences or visibility. Styles overlap and return; this is not a sequence of replacements.</p><p>{link(s['source'],'Read the background reference')}</p><a class="silver-button next-section" href="#vocabulary">Next: Visual vocabulary</a></section>
<section id="vocabulary" data-panel><h2>Read the visual vocabulary</h2><ol class="trait-list">{traits}</ol><p>Compare the illustration with its neutral version. Notice changes in type, shape, spacing, surface, and emphasis while the core words stay similar.</p><p>{link(T+'vocabulary.html','Review typography terms')} · {link(T+'roadmap/choosing-type.html','Practice choosing type')}</p><a class="silver-button next-section" href="#examples">Next: Examples</a></section>
<section id="examples" data-panel><h2>Examples and historical references</h2>{image}<ul class="reference-list">{examples}</ul><h3>What to examine</h3><p>Look at the heading, one control, the image treatment, and the reading order. Explain which decisions establish the style and which make the page usable.</p><a class="silver-button next-section" href="#construction">Next: Construction</a></section>
<section id="construction" data-panel><h2>How to construct it</h2><ol class="build-steps">{build}</ol><h3>Small practice task</h3><p>{e(s['exercise'])}</p><h3>Before you expand it</h3><p>Test the result at its intended size, on a narrow screen, and with keyboard focus. Preserve editable layers and record the source and license of acquired assets.</p><a href="../../construction.html">Find the tools and tutorials</a></section>
</article></div>'''
 prev=styles[i-1] if i else None;nxt=styles[i+1] if i+1<len(styles) else None
 body+='<nav class="study-pagination" aria-label="Other styles">'+(f'<a href="../{prev["id"]}/"><span>Previous study</span><strong>{e(prev["name"])}</strong></a>' if prev else '<a href="../../index.html">All styles</a>')+(f'<a href="../{nxt["id"]}/"><span>Next study</span><strong>{e(nxt["name"])}</strong></a>' if nxt else '<a href="../../index.html">Back to all styles</a>')+'</nav>'
 (d/'index.html').write_text(page(s['name'],body,'../../'))

# Timeline: relationships and approximate influences, explicitly not a literal birth-date ranking.
body='<section class="page-intro"><p class="kicker">Context before categories</p><h1>A timeline of influences</h1><p class="lede">Print movements, web eras, and contemporary interpretations overlap. Use these dates as orientation, not exact invention dates.</p></section><div class="timeline">'
for label,condition in [('Before the web',lambda s:s['year']<1990),('The early and expressive web',lambda s:1990<=s['year']<2010),('Modern digital directions',lambda s:s['year']>=2010)]:
 body+=f'<section><h2>{label}</h2>'
 for s in sorted(filter(condition,styles),key=lambda s:s['year']):
  body+=f'<a class="timeline-entry" href="styles/{s["id"]}/#origins"><span class="timeline-date">{e(s["era"])}</span><img src="assets/{s["id"]}.svg" alt="Original {e(s["name"])} study" loading="lazy" width="800" height="500"><div><h3>{e(s["name"])}</h3><p>{e(s["kind"])}</p></div></a>'
 body+='</section>'
body+='</div>'
(OUT/'timeline.html').write_text(page('Timeline',body,active='timeline'))

techniques=[
 ('Composition','swiss','Arrange first; decorate second.','Set the information order, alignment edges, and focal point before selecting effects.',[['Design principles — freeCodeCamp','https://www.freecodecamp.org/news/design-principles-a-list-of-the-principles-of-design/'],['Choosing Type roadmap',T+'roadmap/choosing-type.html']],'Rearrange the same title, paragraph, and image in two layouts. Explain where the eye goes first.'),
 ('Shapes and illustration','bauhaus','Build a reusable shape vocabulary.','Use vector paths for maps, frames, ornaments, and icons. Keep stroke weights and perspective consistent.',[['Inkscape basic tutorial','https://inkscape.org/doc/tutorials/basic/tutorial-basic.html']],'Draw a frame, a divider, and a button shape with the same visual rules.'),
 ('Collage and image layers','collage','Keep the pieces editable.','Masks let you combine photographs and textures without permanently erasing their source layers.',[['GIMP layer masks','https://www.gimp.org/tutorials/community/Layer_Masks/'],['Photopea layer styles','https://www.photopea.com/learn/layer-styles']],'Combine three original fragments, then export each moving element separately.'),
 ('Textures and painting','grunge','Study light as well as grain.','A convincing material needs a coherent light direction, edge treatment, and level of detail at its final size.',[['Krita basic concepts','https://docs.krita.org/en/user_manual/getting_started/basic_concepts.html'],['Krita brush texture','https://docs.krita.org/en/reference_manual/brushes/brush_settings/texture.html'],['ambientCG materials','https://ambientcg.com/'],['Poly Haven textures','https://polyhaven.com/']],'Make a clean button and a weathered one. Preserve the same silhouette and label.'),
 ('Motion and sound','flash','Storyboard the sequence.','Plan anticipation, movement, arrival, and feedback. Place impact sounds at the contact point rather than at the start of the animation.',[['The 12 principles of animation','https://www.adobe.com/creativecloud/animation/discover/principles-of-animation.html'],['GSAP getting started','https://gsap.com/resources/get-started/'],['Audacity editing','https://support.audacityteam.org/basics/audacity-editing'],['Browser autoplay rules','https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay']],'Sketch three frames for a heavy door closing. Write where the hinge and impact sounds belong.'),
 ('3D and rendered scenes','dramatic','Choose a still render or a live scene.','A rendered background with separate interface layers can create depth without a fully real-time 3D environment.',[['Blender features and learning entry point','https://www.blender.org/features/'],['Blender and Three.js portfolio course — video','https://www.freecodecamp.org/news/creative-web-development-with-threejs-and-blender/']],'Model one simple panel, light it, and render it at its final display size before building a whole world.')]
body='<section class="page-intro"><p class="kicker">From a reference to something you made</p><h1>Construction skills</h1><p class="lede">Choose the smallest technique that produces the effect. Most styles combine artwork, layout, and interaction.</p></section><div class="techniques">'
for title,id,short,desc,refs,exercise in techniques:
 body+=f'<section class="technique"><img src="assets/{id}.svg" width="800" height="500" alt="Original {e(title.lower())} study illustration" loading="lazy"><div><h2>{title}</h2><h3>{short}</h3><p>{desc}</p><ul>'+''.join('<li>'+link(u,t)+'</li>' for t,u in refs)+f'</ul><p class="practice"><strong>Try it:</strong> {exercise}</p></div></section>'
body+='</div>'
(OUT/'construction.html').write_text(page('Construction',body,active='construction'))

body='<section class="page-intro"><p class="kicker">Read, inspect, then make</p><h1>Resources and references</h1><p class="lede">A source trail for every study, plus a route into typography, archives, and practical tools.</p></section><section class="resource-about" id="about"><h2>How this guide is put together</h2><p>The 20 Design Lab Workshop directions are the starting set. Twelve additional studies cover other historical and digital approaches. Short overviews, practical exercises, and SVG specimens are original work for this guide.</p><p>StyleShift provides introductory movement context. Web Design Museum provides historical website records. Typography Learning connects the vocabulary to practice. These labels include movements, eras, techniques, and moods; they are not equivalent categories.</p><p>The desktop navigation is an original CSS interpretation of <a href="https://www.webdesignmuseum.org/gallery/apple-2001" target="_blank" rel="noopener">Apple’s 2001 website</a>: silver tabs, fine stripes, inset edges, and blue selected controls. No Apple logo or original navigation artwork is copied.</p><p>Original study illustrations are labeled separately from externally hosted historical screenshots. Archive images remain the work of their respective creators. A source link is not a reuse license. Remote archive images may be unavailable; the archive-record link remains usable.</p></section><section class="resource-index"><h2>Study references</h2>'
for s in styles:
 body+=f'<div class="resource-row"><h3><a href="styles/{s["id"]}/">{e(s["name"])}</a></h3><div>'+link(s['source'],'Background reference')+'<ul>'+''.join('<li>'+link(u,t)+'</li>' for t,u in s['examples'])+'</ul></div></div>'
body+='</section><section class="resource-about"><h2>Keep exploring</h2><ul><li>'+link('https://styleshift.design/','StyleShift: switch styles while learning design')+'</li><li>'+link(M+'exhibitions','Web Design Museum: historical collections')+'</li><li>'+link('https://web.archive.org/','Wayback Machine: inspect captured websites')+'</li><li>'+link('https://webflow.com/web-design-art-history','Web design and art history')+'</li><li>'+link(T+'resources.html','Typography Learning: reading list')+'</li></ul></section>'
(OUT/'resources.html').write_text(page('Resources',body,active='resources'))
(OUT/'assets/catalogue.json').write_text(json.dumps([dict(id=s['id'],name=s['name'],group=s['group']) for s in styles]))
print(f'Built {len(styles)} style lessons, 4 guide pages, and {len(styles)+1} original SVG illustrations.')
