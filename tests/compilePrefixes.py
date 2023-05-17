#!/usr/bin/env python3

import sys

FILES_TO_MODIFY = (
    "storm_prism_compare/models_finite"
    , "test_stamina/models/models_and_properties"
)

CASE_STUDY_PREFIX_VARIABLE="$CASE_STUDY_PREFIX"

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"Requires exactly one argument! Got {len(sys.argv) - 1}", file=sys.stderr)
        sys.exit(1)
    caseStudyPrefix = sys.argv[1]
    for fName in FILES_TO_MODIFY:
        f = open(f"{fName}.uncompiled", 'r')
        content = f.read()
        f.close()
        # Replace the prefix variable with the actual path
        compiledContent = content.replace(CASE_STUDY_PREFIX_VARIABLE, caseStudyPrefix)
        fComp = open(fName, 'w')
        fComp.write(compiledContent)
        fComp.close()


