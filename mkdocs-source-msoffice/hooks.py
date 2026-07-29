"""
mkdocs build hook for the MS Office Lab Quest — User Guide.

1. Prepends a "Back to MS Office Lab Quest" banner (with a direct "Launch
   the Lab" link) to the top of every documentation page.
2. Appends a consistent author / contact block to the bottom of every
   page's rendered content.
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
    """Prepend a back-to-lab banner and append the author/contact footer to
    the raw markdown of every page before it is rendered to HTML."""
    segments = [s for s in page.file.url.split("/") if s and s != "."]
    # This guide is built to labs/mso-office-lab/guide/ (3 levels below the
    # repo root), so every page needs 3 extra "../" beyond its own depth to
    # reach the repo root, from which the lab app's own path is known.
    up = len(segments) + 3
    prefix = "../" * up

    header_md = (
        '<div class="back-to-course-banner" markdown="1">'
        f'&larr; [Back to MS Office Lab Quest]({prefix}labs/mso-office-lab/index.html) '
        f'&middot; [Launch the Lab]({prefix}labs/mso-office-lab/index.html){{target=_blank}}'
        "</div>\n\n"
    )
    return header_md + markdown.rstrip() + "\n" + FOOTER_MD
