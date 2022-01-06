
import sys
from google.cloud import storage

def list_buckets_by_label( labels ):
    client = storage.Client()
    buckets = client.list_buckets()

    output = list()
    for bucket in buckets:
        if match_labels( bucket, labels ):
            output.append( bucket.name )
        else:
            next                
    
    return output
    
def match_labels( entity, labels ):
    for name in labels:
        if entity.labels.get( name ) != labels[name]:            
            return False
               
    return True

def help():
    return """Return the buckets names that matchs a set of labels"""


# Always for storage now

def get_label():   
    args = sys.argv
    script = args.pop(0)
    entity = args.pop(0)

    labels = {}

    for arg in args:
        name, value = arg.split('=')
        labels[name] = value
        
    output = list_buckets_by_label( labels )

    if len( output ) == 1:
        print( output.pop())
    else:
        print( output )   

    sys.exit()


if __name__ == '__main__':
    get_label()

