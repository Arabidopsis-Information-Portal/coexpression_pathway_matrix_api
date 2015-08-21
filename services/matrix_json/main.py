import services.common.tools as tools

def search(args):
    """
    Return the sequence of a gene
    """

    # Request the file
    tools.get_data(args['type'], args['name'], args['threshold'])

    
    
def list(args):
    raise Exception('Does not provide any kind of list.')
