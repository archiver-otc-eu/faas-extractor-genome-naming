import os
import json

NEW = ['sample_name', 'chromosome', 'sequencing_platform', 'mapping_algorithm', 'population', 'analysis_group', 'date']
OLD = ['sample_name', 'chromosome', 'sequencing_platform', 'mapping_algorithm', 'project_name', 'date']

def handle(req: bytes):
    """handle a request to the function
    Args:
        req (str): request body
    """
    args = json.loads(req)

    path = args["filePath"]
    name = os.path.basename(path)
    name_tokens = name.split(".")[:-1]
    L = OLD if len(name_tokens) == 6 else NEW

    return json.dumps({"json": {"genome": dict(zip(L, name_tokens))}})
