Python cli to generate random numbers using nanoid with a custom alphabet.

## Installation

```bash
pip install -r deps.txt
```

## Usage

```bash
python rgen.py --help

Usage: rgen.py [OPTIONS]

Options:
  -s, --size INTEGER     Size of the string  [default: 10]

  -a, --alphabet TEXT    Alphabet to use  [default: a-z + 0-9]

  -u, --use-uppercase    Use uppercase in alphabet

  -p, --use-punctuation  Use punctuation in alphabet

  --help                 Show this message and exit.
```
