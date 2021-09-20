The Camerata Musica website!

https://cameratamusica.com/

(Also http://colinbrislawn.github.io/CamerataMusica/)

This is built with [Pelican](http://docs.getpelican.com/) and deployed to GitHub pages with GitHub actions and previewed with Cloudflare pages.

---

Here's how to set up the build environment:
```
conda create --name pelican python=3.7 pelican ghp-import markdown
conda activate pelican
```

Here's how to test the site locally (Linux):
```
pelican -lr & sleep 2; open http://127.0.0.1:8000/
```
Then view your preview here: http://127.0.0.1:8000/

---

Here's how to make those big, beautiful background images:
- find high-def images that are wide, with artists in the center (because narrow screens crop the sides) 
- export low quality at `1950px` wide, with the name `slug-large.jpg`
- crop to 4:3
- export high quality at `400px` wide, with the name `slug400.jpg`
- add to page with this markdown (`Bannerposition` is `top` by default)
```
Status: hidden
Banner: ./images/2017-2018/clancy-newman-cello-large.jpg
Bannerposition: center
```
