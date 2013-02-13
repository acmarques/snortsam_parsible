# Snortsam-Parsible

A tool to parse snortsam's log files and output relevant events - blocking, extending blocks and unblocking - to a Mysql database. Use it if you need a central visibility of your snortsam firewall blocks. 

It's written in [Python](http://http://python.org/) and uses [Parsible](https://github.com/Yipit/parsible) as core engine for following snortsam's log in realtime.


## Usage
=========

```bash
./snortsam_parsible.py execute --log-file /var/log/mylog
```

A log file is available at log/snortsam_parsible.log. To add debug messages regarding errors add the `--debug True` option to your command line arguments.

To enable batch processing mode, just append `--batch-mode True` to your command line invocation. This can be useful for backfilling data or doing ad hoc analysis of old files.

For a complete list of options:
```bash
./snortsam_parsible.py execute --help
```

## Requirements
================

* Linux
* Python 2.6+







