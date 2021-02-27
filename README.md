# API NFR Conversion To JMETER Base Template
![Language Python](https://img.shields.io/badge/%20Language-python-blue.svg) [![MIT License](http://img.shields.io/badge/License-MIT-blue.png)](LICENSE)

[![GitHub Last Commits](https://img.shields.io/github/last-commit/hseera/nfrtojmx.svg)](https://github.com/hseera/nfrtojmx/commits/) [![GitHub Size](https://img.shields.io/github/repo-size/hseera/nfrtojmx.svg)](https://github.com/hseera/nfrtojmx/)
[![Open GitHub Issue](https://img.shields.io/badge/Open-Incident-brightgreen.svg)](https://github.com/hseera/nfrtojmx/issues/new/choose)
[![GitHub Open Issues](https://img.shields.io/github/issues/hseera/nfrtojmx?color=purple)](https://github.com/hseera/nfrtojmx/issues?q=is%3Aopen+is%3Aissue)
[![GitHub Closed Issues](https://img.shields.io/github/issues-closed/hseera/nfrtojmx?color=purple)](https://github.com/hseera/nfrtojmx/issues?q=is%3Aclosed+is%3Aissue)


Convert NFR document into a base JMeter template.
This simple python script takes an API throughput NFR in an excel file and converts into a Jmeter template which can then be enhanced with payload and other information. It is created to reduce the timeframe required to create new scripts.

Use the baseprofile_template.xlsx to create your NFR requirements. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to execute the script


* Install python [YAML](https://pypi.org/project/PyYAML/#files) package
* Install python [xlrd](https://pypi.org/project/xlrd/#files) package
* python >=3.5


### Execution

```
1: Use the baseprofile_template.xlsx to create your NFR requirements. Do not change the xlsx file name. 
Currently it is hardcoded.
2: Once above prequisites are setup, execute the convert.py python script. 
Make sure the basetemplate file is in the same folder as the convert.py script
```

### Output
Following is a screenshot of what you will get when you run the python script passing the basetemplate excel file.

The NFR excel file will first be converted to a YAML file which will then be converted to JMX. 

![Alt text](/images/Screenshot.png?raw=true "Optional Title")

## Improvements

* Pass NFR template as a parameter to the conversion script
* Have a capability down the track to just use a YAML file as an NFR document instead of excel
* Remove the hardcoded concurrency value and replace it with dynamic value

## Contribute

If you would like to contribute to this project, please reachout to me. Issues and pull requests are welcomed too.

## Author
[<img id="github" src="./images/github.png" width="50" a="https://github.com/hseera/">](https://github.com/hseera/)    [<img src="./images/linkedin.png" style="max-width:100%;" >](https://www.linkedin.com/in/hpseera) [<img id="twitter" src="./images/twitter.png" width="50" a="twitter.com/HarinderSeera/">](https://twitter.com/@HarinderSeera) <a href="https://twitter.com/intent/follow?screen_name=harinderseera"> <img src="https://img.shields.io/twitter/follow/harinderseera.svg?label=Follow%20@harinderseera" alt="Follow @harinderseera" /> </a>          [![GitHub followers](https://img.shields.io/github/followers/hseera.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/hseera?tab=followers)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
