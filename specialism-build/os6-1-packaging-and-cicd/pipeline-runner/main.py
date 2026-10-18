def run_pipeline(stages):
    # stages is a list of pairs: (name, check). check is a function that gives back True or False.
    # Run the stages in order. Stop at the first one that gives back False.
    # Give back a dictionary:
    #   {"ran": [names of stages that were run, in order],
    #    "passed": True if every stage passed, else False,
    #    "failed_at": the name of the stage that failed, or None}
    return None


def report_line(result):
    # Give back "Pipeline passed" when result["passed"] is True.
    # Otherwise give back "Pipeline stopped at <name>", for example: Pipeline stopped at test
    return None
