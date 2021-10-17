"""General utilities"""


def get_parameters(function, **kwargs):
    """
    Return a list of parameters from a SSM function, like
    describe_parameters or get_parameters_by_path.
    """
    next_token = ""
    response = function(**kwargs)
    parameter_list = response["Parameters"]
    while "NextToken" in response:
        next_token = response["NextToken"]
        kwargs["NextToken"] = next_token
        response = function(**kwargs)
        parameter_list.extend(response["Parameters"])
    return parameter_list
