# SARI Field Definitions Generator

A generator for Metaphacts/ResearchSpace field definitions

## Installations

install using pip

```sh
pip install sari-field-definitions-generator
```

## Usage

Define field definitions as a Python dict or in an external yaml file:

```yaml
prefix: http://rs.swissartresearch.net/instances/fields/

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
        - valueSet: '{value set query}'
          
    - ...
```

Then, load and compile it using the generator

```python
from sariFieldDefinitionsGenerator import generator

inputFile = './fieldDefinitions.yml'
outputFile = '../ldp/assets/fieldDefinitions.trig'

model = generator.loadSourceFromFile(inputFile)

output = generator.generate(model, generator.METAPHACTS)

with open(outputFile, 'w') as f:
    f.write(output)
```

Available templates are:
- `generator.METAPHACTS` for Metaphacts Open Source Platform
- `generator.RESEARCHSPACE` for ResearchSpace
- `generator.UNIVERSAL` for both platforms
- `generator.JSON` for a JSON representation
- `generator.INLINE` for a Backend Template version