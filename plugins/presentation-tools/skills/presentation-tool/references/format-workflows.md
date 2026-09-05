# PPTX and Beamer execution

Read for new projects, missing tooling, or unavailable rendering. Inspect the
actual environment before choosing a route; another skill or engine may not be
installed. Use existing authorization for setup and keep dependencies local to
the project where possible.

## PPTX

1. Establish slide size, required editability, notes, and template constraints.
   Use the existing project library or an available presentation tool that can
   preserve those features. With neither configured, prefer an already installed
   `python-pptx` or `PptxGenJS`; do not install both.
2. For an existing template, confirm the tool can open and preserve it before
   editing. With `python-pptx`, open the supplied file with `Presentation(path)`
   and save to a new output path. For a new deck, use its default presentation or
   create a PptxGenJS presentation, set the slide size, and add native objects.
   Do not assume a library for creating decks can import an existing template.
3. Build a representative slide first, including the required chart, table, or
   notes. Check that these remain editable before expanding the deck. A zip/XML
   inspection or successful save alone does not verify rendered layout.
4. Render a copy through an available PowerPoint, LibreOffice, or artifact
   renderer, then inspect every slide. For an installed `soffice`, a PDF preview
   can be produced with:

   ```bash
   soffice --headless --convert-to pdf --outdir preview deck.pptx
   ```

   Confirm the new PDF exists and inspect it; retain the editable PPTX as the
   deliverable. Conversion does not replace checks of native objects and notes.

## Beamer

1. Reuse the supplied `.tex`, theme, bibliography, engine, and build command.
   For a new project, start with the `beamer` document class and only required
   packages. Select an installed engine compatible with the language and fonts;
   Chinese text needs suitable CJK support rather than assumed Latin fonts.
2. Use frames with one main idea, `fragile` for verbatim code, and restrained
   overlays. Keep assets local and citations tied to supplied material.
3. Compile with the existing command. With no project command, use an available
   `latexmk` and its matching engine option, such as `-pdf`, `-xelatex`, or
   `-lualatex`. Check build errors, unresolved references, missing fonts/assets,
   and overfull boxes; render and inspect the resulting PDF.

## Missing tools or incomplete verification

If a compatible generator is missing, identify the smallest setup needed and
apply it within existing permissions. If setup is unavailable, provide useful
source and precise build instructions, but mark the requested artifact incomplete;
do not present source as a finished PPTX or PDF. Preserve the requested format.

If generation works but no renderer is available, still produce the artifact and
perform available structural checks. Report layout as unverified and name the
remaining render check. Never claim a visual pass from file existence alone.

## Primary references

- [python-pptx: opening and saving presentations](https://python-pptx.readthedocs.io/en/latest/user/presentations.html)
- [PptxGenJS: creating a presentation](https://gitbrent.github.io/PptxGenJS/docs/quick-start/)
- [LibreOffice: command-line conversion](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html)
- [latexmk: build automation and engine options](https://ctan.org/pkg/latexmk)
