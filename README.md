# CamerataMusica.com

At [cameratamusica.com](https://cameratamusica.com/) and [colinbrislawn.github.io/CamerataMusica/](http://colinbrislawn.github.io/CamerataMusica/)

This is built with [Pelican](http://docs.getpelican.com/) and deployed to GitHub pages with GitHub actions and previewed with Cloudflare pages.

---

Here's how to set up the build environment (Linux, OSX, WSL):

```bash
conda create --name pelican480 python=3.7 pelican=4.8.0 ghp-import markdown
conda activate pelican480
```

Then run `pelican -lr` to build the site and serve it at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

Here's how to make those big, beautiful background images:

- find high-def images that are wide, with artists in the center (because narrow screens crop the sides)
- export low quality at `1950px` wide, with the name `slug-large.jpg`
- crop to 4:3
- export high quality at `400px` wide, with the name `slug400.jpg`
- add to page with this markdown (`Bannerposition` is `top` by default)

```markdown
Status: hidden
Banner: ./images/2017-2018/clancy-newman-cello-large.jpg
Bannerposition: center
```
