[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/mzfr/liffy/graphs/commit-activity)


# gtfo

A tool purely written in python3 to search binaries on [GTFOBins](https://gtfobins.github.io/) and [LOLBAS](https://lolbas-project.github.io/).

## Usage

```bash
usage: gtfo [-h] (-b BINS | -e EXE | -w LINK | -ls {bins,exe})

optional arguments:
  -h, --help            show this help message and exit
  -b BINS, --bins BINS  Search binaries on GTFOBins
  -e EXE, --exe EXE     Search Windows exe on LOLBAS
  -w LINK, --link LINK  links to the page of bins/exe
  -ls {bins,exe}, --list {bins,exe}
                        list all the available binaries
```

## Examples

* __Searching GTFOBins__

![](Images/bin.png)

* __Searching lolbas__

![](Images/exe.png)

* __List exe__

![](Images/list-exe.png)

* __List binaries__

![](Images/list-bins.png)

* __Errors__ :smile:

![](Images/errors.png)

## Credits

The original repo https://github.com/mzfr/gtfo
