# SARI Field Definitions Generator

A generator for Metaphacts/ResearchSpace field definitions

## Requirements

pybars3
yaml

## Installations

install using pip

```sh
pip install sariFieldDefinitionsGenerator
```

## Usage


Define field definitions as a Python dict or in an external yaml file:
```
prefix: http://rs.swissartresearch.net/instances/fields/
container: http://www.metaphacts.com/ontologies/platform#fieldDefinitionContainer

fields:

    - id: {unique identifier}
      label: {label}
      description: {description}
      dataType: {datatype}
      domain: {domain}
      range: {range}
      minOccurs: #
      maxOccurs: #
      queries:
        - ask: '{ask query}'
        - delete: '{delete query}'
        - insert: '{insert query}'
        - select: '{select query}'
          
    - ...
```

