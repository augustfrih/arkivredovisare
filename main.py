import sqlite3
from globals import DATABASE_PATH
from src.markdown import create_processtrad_table_if_not_exists


def main():
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    create_processtrad_table_if_not_exists(cur)

if __name__ == "__main__":
    main()
