# Tornado: ThinkPad Fan Control

Tornado is a utility software to manage the fan speed on ThinkPad laptops.

## Installation

Install the package using the following command:

```bash
$ sudo add-apt-repository ppa:sugarcoat/ppa
$ sudo apt update
$ sudo apt install tornado
```

## Usage

### Syntax

**(LEVEL, LOW, HIGH)**

- ***LEVEL*** is the fan level to use (0-7 | 127 [full-speed] with thinkpad_acpi).
- ***LOW*** is the temperature at which to step down to the previous level.
- ***HIGH*** is the temperature at which to step up to the next level.

All numbers are integers.

```bash
$ tornado
```

### Run with configuration file
Create a `config` file that includes **(`level`, `low`, `high`)**.
```
(5, 0, 40)
(7, 39, 60)
(127, 59, 512)
```

Execute the command for the changes to take effect:
```bash
$ tornado /path/to/config
```
