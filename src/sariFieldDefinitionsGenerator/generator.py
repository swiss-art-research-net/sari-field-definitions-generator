import yaml
from pathlib import Path
from pybars import Compiler

UNIVERSAL = 0
RESEARCHSPACE = 1
METAPHACTS = 2

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
    else:
        templateFile = Path(__file__).parent / './templates/universal.handlebars'
    
    with templateFile.open() as f:
        templateSource = f.read()

    compiler = Compiler()
    template = compiler.compile(templateSource)
    try:
        output = template(source)
        return output
    except:
        raise Exception("Could not generate definitions")

