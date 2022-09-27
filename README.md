# STAMINA

[https://staminachecker.org](https://staminachecker.org)

STAMINA, the STochastic Approximate Model-checker for INfinite-state Analysis, is a tool for analyizing large and infinite state spaces to provide probability values within a user-specified boundary. STAMINA is actually two programs: one integrated with the PRISM model checker and one integrated with the STORM model checker. The latter, STAMINA/STORM is under most active development and written in C++. The former, STAMINA/PRISM is written in Java and supports only the first two iterations of the STAMINA algorithm.

## STAMINA/STORM

STAMINA/STORM is located at [https://github.com/fluentverification/stamina-storm](https://github.com/fluentverification/stamina-storm) and included in this repository as a submodule. It supports STAMINA 2.0+ algorithms and supports CTMCs and DTMCs. It supports PRISM model files and CSL properties files, and will soon support JANI files. Features slated for inclusion in STAMINA/STORM are as follows:

| Feature                         | Status                  | Approx. Date              |
|---------------------------------|-------------------------|---------------------------|
| Dynamic Programming             | Finished                | N/A                       |
| Multithreading                  | In-progress             | November or December 2022 |
| "Greedy" (priority) exploration | In-progress             | November or December 2022 |
| State "prefetching" (threading) | TBD                     | TBD                       |

## STAMINA/PRISM

STAMINA/PRISM is located at [https://github.com/fluentverification/stamina-prism](https://github.com/fluentverification/stamina-prism) and integrates with the PRISM modelchecker. It supports the STAMINA 1.0 and 2.0 algorithms and supports only CTMCs and PRISM model files/CSL properties files.

## How to use this repository

This repository is a *wrapper* repository which contains links to STAMINA-STORM and STAMINA-PRISM as submodules. Therefore, in order to use this repository, you must use the `--recursive` option when cloning the repository down as described in [this GitHub article](https://github.blog/2016-02-01-working-with-submodules/).

*If you have built the contents of the two submodules*, you can use the `installcontrol` script to install and/or uninstall both STAMINA/STORM and STAMINA/PRISM.

```
installcontrol install # Installs both STAMINA/STORM and STAMINA/PRISM
installcontrol uninstall # Uninstalls both STAMINA/STORM and STAMINA/PRISM
```
