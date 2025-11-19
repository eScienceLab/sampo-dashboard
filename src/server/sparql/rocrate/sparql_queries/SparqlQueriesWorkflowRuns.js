const perspectiveID = 'workflowRuns'

export const workflowRunProperties = `
    {
      ?id owl:sameAs/ns11:name ?prefLabel__id .
      BIND(?prefLabel__id AS ?prefLabel__prefLabel)
      BIND(CONCAT("/${perspectiveID}/page/", REPLACE(STR(?id), "^.*\\\\/workflowRun\\\\/(.+)$", "$1")) AS ?prefLabel__dataProviderUrl)
      ?id owl:sameAs ?uri .
      BIND(?uri as ?uri__dataProviderUrl)
      BIND(?uri as ?uri__prefLabel)
    }
    UNION
    {
      ?id owl:sameAs/ns11:agent ?agent__id .
      ?agent__id ns11:name ?agent__prefLabel .
      BIND(?agent__id AS ?agent__dataProviderUrl)
    }
    UNION
    {
      ?id owl:sameAs/ns11:startTime ?startTime__id .
      BIND(CONCAT(STR(DAY(?startTime__id)), "/", STR(MONTH(?startTime__id)), "/", STR(YEAR(?startTime__id))) as ?startTime__prefLabel)
    }
    UNION
    {
      ?id owl:sameAs/ns11:endTime ?endTime__id .
      BIND(CONCAT(STR(DAY(?endTime__id)), "/", STR(MONTH(?endTime__id)), "/", STR(YEAR(?endTime__id))) as ?endTime__prefLabel)
    }
    UNION
    {
      ?id owl:sameAs/ns11:instrument ?instrument__id .
      ?instrument__id ns11:name ?instrument__prefLabel .
      BIND(?instrument__id AS ?instrument__dataProviderUrl)
    }
    UNION
    {
      ?id owl:sameAs/ns11:object ?object__id .
      ?object__id ns11:name ?object__prefLabel .
      BIND(?object__id AS ?object__dataProviderUrl)
    }
    UNION
    {
      ?id owl:sameAs/ns11:result ?result__id .
      ?result__id ns11:name ?result__prefLabel .
      BIND(?result__id AS ?result__dataProviderUrl)
    }
    UNION
    {
      ?id owl:sameAs/ns11:description ?description__id .
      BIND(?description__id AS ?description__prefLabel)
    }
`
