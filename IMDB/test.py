import re

str = """
<script type="application/ld+json">{
  "@context": "http://schema.org",
  "@type": "Movie",
  "url": "/title/tt8332922/",
  "name": "A Quiet Place Part II",
  "image": "https://m.media-amazon.com/images/M/MV5BMmE3OGY2NzMtMGJmOS00NGViLWI4NjYtMjhlNTMxZjA5MDExXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg",
  "genre": [
    "Horror",
    "Thriller"
  ],
  "contentRating": "PG-13",
  "actor": [
    {
      "@type": "Person",
      "url": "/name/nm1289434/",
      "name": "Emily Blunt"
    },
    {
      "@type": "Person",
      "url": "/name/nm8075925/",
      "name": "Millicent Simmonds"
    },
    {
      "@type": "Person",
      "url": "/name/nm0614165/",
      "name": "Cillian Murphy"
    },
    {
      "@type": "Person",
      "url": "/name/nm7415871/",
      "name": "Noah Jupe"
    }
  ],
  "director": {
    "@type": "Person",
    "url": "/name/nm1024677/",
    "name": "John Krasinski"
  },
  "creator": [
    {
      "@type": "Person",
      "url": "/name/nm1399714/",
      "name": "Scott Beck"
    },
    {
      "@type": "Person",
      "url": "/name/nm1024677/",
      "name": "John Krasinski"
    },
    {
      "@type": "Person",
      "url": "/name/nm1456816/",
      "name": "Bryan Woods"
    },
    {
      "@type": "Organization",
      "url": "/company/co0775256/"
    },
    {
      "@type": "Organization",
      "url": "/company/co0023400/"
    },
    {
      "@type": "Organization",
      "url": "/company/co0071240/"
    },
    {
      "@type": "Organization",
      "url": "/company/co0149632/"
    }
  ],
"""

s = re.findall(r"\"genre\": \[(.*?)\]", str, re.S)
print(s)