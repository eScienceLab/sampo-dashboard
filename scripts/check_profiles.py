import re

from hashlib import md5
from rdflib import Graph, URIRef, Literal, XSD, RDF, OWL
from urllib.parse import urljoin


g = Graph()
profile_class = URIRef("http://www.w3.org/ns/dx/prof/Profile")

with open("profile_urls.txt", "r") as file:
    profile_urls = [line.strip() for line in file if line.strip()]

for url in profile_urls: 
    g.parse(url, format="json-ld", publicID=urljoin(url, '.'))

datetime_pattern = re.compile(r"^-?\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:\d{2})?$")
date_pattern = re.compile(r"^-?\d{4}-\d{2}-\d{2}$")
time_pattern = re.compile(r"^\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:\d{2})?$")

# Add type to datetime, date and time data
for s, p, o in g.triples((None, None, None)):
    typed_o = None

    if datetime_pattern.match(o):
        typed_o = Literal(o, datatype=XSD.dateTime)
    elif date_pattern.match(o):
        typed_o = Literal(o, datatype=XSD.date)
    elif time_pattern.match(o):
        typed_o = Literal(o, datatype=XSD.time)

    if typed_o is not None:
        g.add((s, p, typed_o))
        g.remove((s, p, o))

    if p == RDF.type and o == profile_class:
        id = md5(s.encode('utf-8')).hexdigest()
        new_s = URIRef(f"http://example.org/data/profile/{id}") # TODO: Change URI
        g.add((new_s, RDF.type, o))
        g.add((new_s, OWL.sameAs, s))

ttl_data = g.serialize(format="turtle")
