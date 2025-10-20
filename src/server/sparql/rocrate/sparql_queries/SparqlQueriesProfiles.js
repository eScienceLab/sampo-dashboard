const perspectiveID = 'profiles'

export const profileProperties = `
    {
      ?id owl:sameAs/ns11:name ?prefLabel__id .
      BIND(?prefLabel__id AS ?prefLabel__prefLabel)
      BIND(CONCAT("/${perspectiveID}/page/", REPLACE(STR(?id), "^.*\\\\/profile\\\\/(.+)$", "$1")) AS ?prefLabel__dataProviderUrl)
      ?id owl:sameAs ?uri .
      BIND(?uri as ?uri__dataProviderUrl)
      BIND(?uri as ?uri__prefLabel)
    }
    UNION
    {
      ?id owl:sameAs/ns11:identifier ?identifier__id .
      BIND(?identifier__id AS ?identifier__prefLabel)
      BIND(?identifier__id as ?identifier__dataProviderUrl)
    }
    UNION
    {
      ?id owl:sameAs/ns11:version ?version__id .
      BIND(?version__id AS ?version__prefLabel)
    }
    UNION
    {
      ?id owl:sameAs/ns11:datePublished ?date__id .
      BIND(?date__id AS ?date__prefLabel)
    }
    UNION
    {
      ?id owl:sameAs/ns11:author ?author__id .
      ?author__id ns11:name ?author__prefLabel .
    }
    UNION
    {
      # keyword placeholder (TODO)
    }
`
