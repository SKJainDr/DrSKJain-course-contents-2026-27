"""
mkdocs build hook.

1. Prepends a "Back to BHP301 Course Page" banner to the top of every
   documentation page. On each of the 18 experiment pages, this banner also
   links directly to the printable Lab Record & Viva-Voce Booklet PDF, so a
   student working through the user guide can jump straight to that
   experiment's printable sheets.
2. Appends a consistent author / contact block to the bottom of every
   documentation page's rendered content (so it is present in the on-screen
   page, in the search index, and in any "print page" / export of the page —
   not just in the global site footer).
"""

FOOTER_MD = """

---

<div class="page-author-footer" markdown="1">

**Author & Maintainer:** Dr. S. K. Jain, Associate Professor in Physics, Department of Applied Sciences and Humanities, Invertis University, Bareilly, India
📧 [sanjeev.j@invertis.org](mailto:sanjeev.j@invertis.org)

&copy; 2026 Author. All rights reserved.

</div>
"""


def on_page_markdown(markdown, page, config, files):
    """Prepend a back-to-course banner (plus, on experiment pages, a direct
    link to the printable booklet) and append the author/contact footer to
    the raw markdown of every page before it is rendered to HTML."""
    segments = [s for s in page.file.url.split("/") if s and s != "."]
    up = len(segments) + 1
    prefix = "../" * up

    is_experiment = page.file.src_uri.startswith("experiments/")
    booklet_link = ""
    if is_experiment:
        booklet_link = (
            ' &middot; [📝 Open Lab Record & Viva-Voce Booklet (PDF)]'
            f'({prefix}assets/lab-record-booklet-em.pdf){{target=_blank}} '
            '<small>(print just this experiment\'s pages when you sit down '
            'at the simulator)</small>'
        )

    header_md = (
        '<div class="back-to-course-banner" markdown="1">'
        f'&larr; [Back to BHP301 Course Page]({prefix}courses/bhp301/index.html) '
        f'&middot; [Launch Simulator]({prefix}labs/advanced-electricity-magnetism-lab.html){{target=_blank}}'
        f'{booklet_link}'
        "</div>\n\n"
    )
    return header_md + markdown.rstrip() + "\n" + FOOTER_MD
