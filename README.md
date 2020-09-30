# NFR to JMETER base template
Convert NFR document into a base JMeter template.
This simple python script takes an API throughput NFR in an excel file and converts into a Jmeter template which can then be enhanced with payload and other information. It is created to reduce the timeframe required to create new scripts.

Use the baseprofile_template.xlsx to create your NFR requirements. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to execute the script

```
1: You will need to install python YAML package
2: You will need to install python xlrd package
3: python 3.5
```

### Execution

```
1: Use the baseprofile_template.xlsx to create your NFR requirements. Do not change the xlsx file name. Currently it is hardcoded.
2: Once above prequisites are setup, execute the convert.py python script
```

## Improvements

* Pass NFR template as a parameter to the conversion script 
## Authors

* **Harinder Seera** - *Initial work* - [OzPerf](https://ozperf.com/)

If you would like to contribute to this project, please reachout to me.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
