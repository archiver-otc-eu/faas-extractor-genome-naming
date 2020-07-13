import json

NEW = ['sample_name', 'chromosome', 'sequencing_platform', 'mapping_algorithm', 'population', 'analysis_group', 'date']
OLD = ['sample_name', 'chromosome', 'sequencing_platform', 'mapping_algorithm', 'project_name', 'date']

def handle(req: bytes):
    """handle a request to the function
    Args:
        req (str): request body
    """
    args = json.loads(req)

    name_tokens = args["fileName"].split(".")[:-1]
    L = OLD if len(name_tokens) == 6 else NEW

    return json.dumps({"xattrs": dict(zip(L, name_tokens))})
