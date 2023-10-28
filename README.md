# growatt-load-shifter

![License](https://img.shields.io/badge/License-MIT-blue.svg)

**growatt-load-shifter** is a Python script that sends an API call when batteries are fully charged, enabling control over various loads. It's a versatile solution for managing energy usage.

## Data Input

This script retrieves data from a local InfluxDB, which can be filled with data from tools like [Grott](https://github.com/johanmeijer/grott) for local data logging. Alternatively, you can use [growattServer](https://pypi.org/project/growattServer/), which fetches data directly from Growatt servers. Keep in mind that Growatt's API may change, which could affect compatibility. Grott, while more complex to set up, offers stability and reliability once configured.

## Usage

1. Configure your InfluxDB connection and load control scripts in the script's configuration file.
2. Install dependecies (not that many)
3. Run the script `python3 growatt_shifter/main.py` 

## Load Control Scripts

The current version of the script supports Sonoff switches using the Node.js package [ewelink-api](https://www.npmjs.com/package/ewelink-api). However, this script can be easily customized to work with other scripts, making it adaptable for controlling a wide range of loads.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to [Grott](https://github.com/johanmeijer/grott) and [growattServer](https://pypi.org/project/growattServer/) for their effort for data extraction and collection.

