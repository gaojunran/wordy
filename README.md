# wordy

## Description

👍🏻 A simple command-line wrapper for [youdao](https://github.com/longcw/youdao).

⭐️ Support consecutively querying multiple words, and save them to CSV file.

## Usage

### With [uv](https://docs.astral.sh/uv/) (Recommended)
```bash
git clone https://github.com/gaojunran/wordy.git
cd wordy
uv install # need uv first
uv run main.py
```

### Without uv
```bash
git clone https://github.com/gaojunran/wordy.git
cd wordy
pip install .
python main.py
```

Type in the words you want to query. Directly you can get a colorful result(Supported by [youdao](https://github.com/longcw/youdao)).

We also support extra options/arguments in [youdao](https://github.com/longcw/youdao), just replace 

```bash
>>> -c
>>> -d word
```

### Notice

📢 Run in real terminal instead of PyCharm/VS Code's built-in terminal.

##  TODO

- [ ] Transform into a package which can be installed and run in terminal.
