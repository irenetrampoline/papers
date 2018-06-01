# How to use this repo

## Publish paper writeups

In `writeups/` directory, there should be a file called `today.md`. If not, copy `template.md`

```cp template.md today.md```

Make changes into `today.md` including title of authors and paper. Include summary and notes in the body of text. Note that authors are intended to be FirstName1 LastName1, FirstName2 LastName2, etc. 

When you're ready to publish, run

```python publish.py```

from the main directory level. Note that script assumes you are publishing from today's date.

Changes should appear in `README.md` and the writeup will be automatically created in `writeups/`.

## Description of files and directories

`instruct.md` contains these instructions

`README.md` contains master list of papers and links to writeups

`publish.py` is a script to publish today's writeup in `writeups/today.md`

`reorder.py` is a one-time use script to reverse the ordering of dates in `README.md`

`writeups/` contains all of the paper writeups

`pdfs/` contains all of the PDFs of cited papers

`img/` contains images used for writeups