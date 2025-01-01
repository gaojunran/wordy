#!/usr/bin/env python3
import json
import sqlite3
import sys
import subprocess
from pathlib import Path

import pandas as pd
from youdao import main as youdao_main
from questionary import confirm

def run_yd_with_args(*args):
    sys.argv = sys.argv[:1]
    sys.argv.extend(args)
    youdao_main.main()
    sys.argv = sys.argv[:1]

def parse_json(json_data: str):
    data = json.loads(json_data)
    try:
        return "\n".join(data["basic"]["explains"])
    except KeyError:
        return ""

def to_csv():
    db_path = Path.home() / ".dict_youdao" /  "youdao.db"
    # print(db_path)
    if not db_path.exists():
        print("Youdao database not found.")
        return
    conn = sqlite3.connect(str(db_path))

    query = "SELECT id, keyword, json_data FROM word"
    df = pd.read_sql_query(query, conn)
    df["translation"] = df["json_data"].apply(lambda x: parse_json(x))
    df.drop(columns=["json_data"], inplace=True)
    df.to_csv("./typst-template/youdao.csv", index=False)
    conn.close()
    print("Done. Now you can run with --pdf to generate PDF.")

def to_pdf():
    try:
        subprocess.run(["typst", "compile", "./typst-template/main.typ", "./wordlist.pdf"], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to compile PDF. Have you installed typst? Or have you run with --csv first?")
    else:
        print("Done. You can find the PDF in the current directory.")



def main():
    options = sys.argv[1:]
    if not options:
        while True:
            word = input(">>> ").strip()
            if word:
                run_yd_with_args(word)
                if not confirm("Save?").ask():
                    run_yd_with_args("-d", word)
    elif options[0] == "--csv":
        to_csv()
        return
    elif options[0] == "--pdf":
        to_pdf()
        return
    else:
        run_yd_with_args(*options)  # run youdao with args
        return



if __name__ == "__main__":
    main()
    # to_csv()