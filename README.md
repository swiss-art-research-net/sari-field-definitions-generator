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

```yaml
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

Then, load and compile it using the generator

```python
from sariFieldDefinitionsGenerator import generator

inputFile = './fieldDefinitions.yml'
model = generator.loadSourceFromFile(inputFile)

output = generator.generate(model, generator.METAPHACTS)

print(output)
```
