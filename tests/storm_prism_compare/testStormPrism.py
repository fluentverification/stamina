#!/usr/bin/env python3
import sys
import subprocess
import os

def testStorm(mod, prop):
    cmd = f"storm --prism {mod} --prop {prop} -pc"
    try:
        processOut = subprocess.run(cmd, shell=True, capture_output=True)
        # print("Process out: ", processOut.stdout)
        output = processOut.stdout.decode("utf-8")
        for line in output.split("\n"):
            print(f"Line: {line}")
            if line.startswith("Result (for initial states):"):
                result = line.replace("Result (for initial states):", "").strip()
                return result
    except subprocess.CalledProcessError as e:
        print(f"Warning: got error {e}", file=sys.stderr)

def testPrism(mod, prop):
    cmd = f"prism {mod} {prop}"
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")
    for line in output.split("\n"):
        # print(f"Line: {line}")
        if line.startswith("Result:"):
            result = line.replace("Result:", "").strip()
            return result

if __name__=="__main__":
    if len(sys.argv) == 1:
        print("Requires at least one argument: model/properties list file!", file=sys.stderr)
        sys.exit(1)
    elif len(sys.argv) > 2:
        print(f"Warning: too many input parameters. Will ignore: {sys.argv[3:]}", file=sys.stderr)
    listFile = open(sys.argv[1], 'r')
    with open("output.txt", 'a') as f:
        f.write("STORM,PRISM\n")
    for line in listFile:
        modelFile, propFile = line.split(' ')
        modelFile = modelFile.strip()
        propFile = propFile.strip()
        resultStorm = testStorm(modelFile, propFile)
        resultPrism = testPrism(modelFile, propFile)
        with open("output.txt", 'a') as f:
            f.write(f"{resultStorm},{resultPrism}\n")
    listFile.close()

