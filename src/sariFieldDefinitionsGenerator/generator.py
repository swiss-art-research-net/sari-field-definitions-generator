import yaml
from pathlib import Path
from pybars import Compiler

UNIVERSAL = 0
RESEARCHSPACE = 1
METAPHACTS = 2
JSON = 3

def loadSourceFromFile(file):
    try:
        with open (file, 'r') as f:
            source = yaml.safe_load(f.read())
            return source
    except:
        raise Exception("Could not read " + file)
    

def generate(source, output=UNIVERSAL):
    if output == METAPHACTS:
        templateFile = Path(__file__).parent / './templates/metaphacts.handlebars'
    elif output == RESEARCHSPACE:
        templateFile = Path(__file__).parent / './templates/researchspace.handlebars'
    elif output == JSON:
        templateFile = Path(__file__).parent / './templates/json.handlebars'
    else:
        templateFile = Path(__file__).parent / './templates/universal.handlebars'
    
    with templateFile.open() as f:
        templateSource = f.read()

    # TODO: Escape quotes when generating JSON
    if output == JSON:
        for i in range(len(source['fields'])):
            if 'queries' in source['fields'][i]:
                for queryIndex, query in enumerate(source['fields'][i]['queries']):
                    for queryType in query.keys():
                        escapedQuery = source['fields'][i]['queries'][queryIndex][queryType].replace('"','\\"')
                        source['fields'][i]['queries'][queryIndex][queryType] = escapedQuery


    compiler = Compiler()
    template = compiler.compile(templateSource)
    try:
        output = template(source)
        return output
    except:
        raise Exception("Could not generate definitions")

