from retrying import retry
from alchemyapi_python import alchemyapi
alchemy = alchemyapi.AlchemyAPI()

def full_enrich(flavor, data):
    """
    INPUT:
        flavor -> which version of the call, i.e. text, url or html.
        data -> the data to analyze, either the text, the url or html code.
    OUTPUT: dictonary containing alchemy api responce
    """
    d = {}
    d['document_sentiment'] = document_sentiment(flavor, data)
    d['entities_sentiment'] = entities(flavor, data, sentiment=0)
    d['concepts'] = concepts(flavor, data)
    d['keywords_sentiment'] = keywords(flavor, data, sentiment=0)
    d['category'] = category(flavor, data)
    d['taxonomy'] = taxonomy(flavor, data)
    d['author'] = author(flavor, data)
    return(d)

# retry settings
sman = 2

@retry(stop_max_attempt_number=sman)
def entities(flavor, data, sentiment=0):
    data = alchemy.entities(flavor=flavor, data=data, options={'sentiment': sentiment})
    return data['entities']

@retry(stop_max_attempt_number=sman)
def concepts(flavor, data):
    data = alchemy.concepts(flavor, data)
    if 'concepts' in data:
        return data['concepts']

@retry(stop_max_attempt_number=sman)
def keywords(flavor, data, sentiment=0):
    data = alchemy.keywords(flavor, data, {'sentiment': sentiment})
    if 'keywords' in data:
        return data['keywords']

@retry(stop_max_attempt_number=sman)
def category(flavor, data):
    data = alchemy.category(flavor, data)    
    return data

@retry(stop_max_attempt_number=sman)
def taxonomy(flavor, data):
    data = alchemy.taxonomy(flavor, data)
    if 'taxonomy' in data:
        return data['taxonomy']

@retry(stop_max_attempt_number=sman)
def author(flavor, data):
    data = alchemy.author(flavor, data)
    if 'author' in data:
        return data['author']

@retry(stop_max_attempt_number=sman)
def document_sentiment(flavor, data):
    data = alchemy.sentiment(flavor, data)
    if 'docSentiment' in data:
        return data['docSentiment']
