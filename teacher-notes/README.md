# Teacher Notes

Each teacher's shareable material lives in their own course subfolder here,
so updating one course never touches anything else in the repository:

```
teacher-notes/
  bas101/
    links.txt   <- web links (GitHub Pages, videos, Drive links, ...)
    files/      <- actual files to share (PDF, DOCX, PPTX, images, ...)
  bas151/
    links.txt
    files/
  bhp301/
    links.txt
    files/
  mpy301/
    links.txt
    files/
  mpy351/
    links.txt
    files/
  voi001/
    links.txt
    files/
```

Each course's `index.html` page pulls both live from this repository
(via `assets/teacher-notes.js`) every time the page is opened - so a
teacher edits `links.txt` or adds/removes a file in `files/` for their own
course, commits, and the change is visible to students immediately. No
other page or file needs to be touched.

See the instructions at the top of any course's `links.txt` for the exact
steps and the link-line format, and each course's `files/README.md` for
the file-sharing side.

Note: the automatic file listing in `files/` uses GitHub's public API,
which is rate-limited for anonymous requests (60/hour per visitor IP).
This is normally more than enough for a class site, but if it's ever
exceeded, the file list briefly stops appearing (links.txt content still
shows) until the limit resets.
