# General Torsion Explorer

## Setup Your Environment:
linux/wsl:
```shell
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

windows:
```shell
python3 -m venv venv
./venv/bin/activate.ps1
pip install -r requirements.txt
```

## Run examples
```shell
python3 ./examples.py
```

# Important Note
[here](./GEMINI_EXPLINATION.md) is an explination by gemini of the different represntations for knots and finding there knot group generators and relations


## TODO
- get snappy (knot db) parser working so we can look at general knots for any algorithm we think might have potential (the most obvious test to show that it isn't working is trying to look at the figure eight knot that is being produced by `get_knot_data` titled `K4_1` is obviously wrong since the relations should be like what is in the examples.py file)
- create an initial fuzzer to just start trying things for late improvement