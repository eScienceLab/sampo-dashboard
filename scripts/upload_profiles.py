import os
import re
import validators
import requests
import argparse

from dotenv import load_dotenv
from hashlib import md5
from rdflib import Graph, URIRef, Literal, XSD, RDF, OWL
from urllib.parse import urljoin


parser = argparse.ArgumentParser(description="Parse profile Ro Crate and upload graph to Jena Fuseki instance")
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()
load_dotenv()

g = Graph()
profile_class = URIRef("http://www.w3.org/ns/dx/prof/Profile")

with open("profile_urls.txt", "r") as file:
    profile_urls = [line.strip() for line in file if line.strip()]

for url in profile_urls:
    if not validators.url(url):
        raise ValueError(f"{url} is not an URL")

    headers = {
        "Accept": "application/ld+json, application/json"
    }

    try:
        response = requests.head(url, headers=headers, allow_redirects=True)
    except requests.RequestException as e:
        raise ValueError(f"Unable to reach {url} (Error: {e})")
    
    # Fallback
    if response.status_code >= 400:
        response = requests.get(url, headers=headers)

    content_type = response.headers.get("Content-Type", "").lower()
    if "json" not in content_type:
        raise ValueError(f"{url} does not return JSON-LD (Content type: {content_type})")

    temp_g = Graph()
    base_iri = urljoin(url, '.') if url.endswith("ro-crate-metadata.json") else f"{url.rstrip('/')}/"
    temp_g.parse(url, format="json-ld", publicID=base_iri)
    if any(temp_g.subjects(RDF.type, profile_class)):
        g += temp_g
    else:
        raise ValueError(f"No profile entity found in {url}")

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
if not args.dry_run:
    FUSEKI_ENDPOINT = os.getenv('FUSEKI_UPLOAD_ENDPOINT')
    FUSEKI_PASSWORD = os.getenv('FUSEKI_PASSWORD')

    response = requests.put(FUSEKI_ENDPOINT, data=ttl_data, 
                            headers={"Content-Type": "text/turtle"}, 
                            auth=("admin", FUSEKI_PASSWORD))
    response.raise_for_status()
