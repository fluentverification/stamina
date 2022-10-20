# STAMINA - STochastic Approximate Model-checker for INfinite-state Analysis

[![Website](https://img.shields.io/website?down_message=https%3A%2F%2Fstaminachecker.org&style=social&up_message=https%3A%2F%2Fstaminachecker.org&url=https%3A%2F%2Fstaminachecker.org)](https://staminachecker.org) ![License](https://img.shields.io/github/license/fluentverification/stamina-storm)

STAMINA, the STochastic Approximate Model-checker for INfinite-state Analysis, is a tool for analyizing large and infinite state spaces to provide probability values within a user-specified boundary. STAMINA is actually two programs: one integrated with the PRISM model checker and one integrated with the STORM model checker. The latter, STAMINA/STORM is under most active development and written in C++. The former, STAMINA/PRISM is written in Java and supports only the first two iterations of the STAMINA algorithm.

## STAMINA/STORM

STAMINA/STORM is located at [https://github.com/fluentverification/stamina-storm](https://github.com/fluentverification/stamina-storm) and included in this repository as a submodule. It supports STAMINA 2.0+ algorithms and supports CTMCs and DTMCs. It supports PRISM model files and CSL properties files, and will soon support JANI files. Features slated for inclusion in STAMINA/STORM are as follows:

| Feature                         | Status                  | Approx. Date  (pre-release) |
|---------------------------------|-------------------------|-----------------------------|
| Dynamic Programming             | Finished                | N/A                         |
| Multithreading                  | In-progress             | November or December 2022   |
| "Greedy" (priority) exploration | In-progress             | November or December 2022   |
| State "prefetching" (threading) | TBD                     | TBD                         |
| State ownership by value        | TBD                     | TBD                         |

## STAMINA/PRISM

STAMINA/PRISM is located at [https://github.com/fluentverification/stamina-prism](https://github.com/fluentverification/stamina-prism) and integrates with the PRISM modelchecker. It supports the STAMINA 1.0 and 2.0 algorithms and supports only CTMCs and PRISM model files/CSL properties files.

## How to use this repository

This repository is a *wrapper* repository which contains links to STAMINA-STORM and STAMINA-PRISM as submodules. Therefore, in order to use this repository, you must use the `--recursive` option when cloning the repository down as described in [this GitHub article](https://github.blog/2016-02-01-working-with-submodules/).

*If you have built the contents of the two submodules*, you can use the `installcontrol` script to install and/or uninstall both STAMINA/STORM and STAMINA/PRISM.

```bash
installcontrol install # Installs both STAMINA/STORM and STAMINA/PRISM
installcontrol uninstall # Uninstalls both STAMINA/STORM and STAMINA/PRISM
```

### To Build STAMINA/PRISM

Assuming you have installed PRISM, simply `cd` into the `stamina` folder and run `make` with the `PRISM_HOME` variable set

```bash
export PRISM_HOME=<path/to/prism>
cd stamina-prism/stamina
make PRISM_HOME=$PRISM_HOME -j$(nproc --ignore=1) # Uses all processors but one to make. Omit this flag if you only want single-threaded building
```

### To build STAMINA/STORM

This version of STAMINA requires STORM to already be installed. Once that is done, simply use `cmake` and `make` respectively. If STORM is installed in a shared library path, the `STORM_PATH` variable is optional

```bash
cd stamina-storm
mkdir build && cd build
cmake .. -DCMAKE_CXX_COMPILER=$(which clang++) -DSTORM_PATH=$STORM_PATH # Omit if STORM is installed globally
make -j$(nproc --ignore=1)
```

## The `stamina` executable

The `stamina` executable is a small Python 3.7+ script included in this repository, which passes options into the `pstamina` and `sstamina` executables respectively. It uses the `--storm` and `--prism` flags to do this.

```bash
# This invocation of the script uses the sstamina executable and therefore the options for sstamina
stamina --storm $MODEL_FILE $PROPERTIES_FILE [OPTIONS...]
# Whereas this invocation uses the pstamina executable and the options for pstamina
stamina --prism $MODEL_FILE $PROPERTIES_FILE [OPTIONS...]
```

Please refer to the [wiki](https://staminachecker.org/wiki) for documentation on options.

# A Note on Versioning

STAMINA will soon be re-doing its versioning. 2.0 will become 0.2.0, 1.0 will become 0.1.0, etc., to keep with more modern versioning standards and not jump version numbers too quickly.
