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
`
