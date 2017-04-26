The Camerata Musica website!

http://cameratamusica.com/

(Also http://colinbrislawn.github.io/CamerataMusica/)

This is built with [Pelican](http://docs.getpelican.com/) and deployed with Travis-CI [![Build Status](https://travis-ci.org/colinbrislawn/CamerataMusica.svg?branch=master)](https://travis-ci.org/colinbrislawn/CamerataMusica)

---

Here's how to set up an build environment:
```
conda create --name pelican pelican ghp-import markdown
source activate pelican
```

Here's how to test the site locally:
```
pelican content --debug --autoreload  --output output --settings pelicanconf.py &
pushd output; python -m pelican.server; popd
```
Then view your preview here: http://127.0.0.1:8000/
