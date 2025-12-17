import psycopg2
from psycopg2 import Error
import cred


def help():
    print("---------------------------")
    print("All commands:")
    print("list_flavours")
    print("list_entries")
    print("amount_spent")
    print("---------------------------")


def get_connection():
    """Helper function to create a database connection"""
    return psycopg2.connect(user=cred.USR,
                           password=cred.PASS,
                           host="127.0.0.1",
                           port="5432",
                           database="redbull-tracker")


def list_flavours(args):
    try:
        connection = get_connection()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT naam FROM flavours")
        records = cursor.fetchall()
    
        for record in records:
            print(record[0])
    finally:
        cursor.close()
        connection.close()



def list_entries(args):
    try:
        connection = get_connection()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM entries")
        records = cursor.fetchall()
        for record in records:
            for line in record:
                print(line, end=" | ")
            print()
    finally:
        cursor.close()
        connection.close()

def amount_spent(args):
    try:
        connection = get_connection()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT SUM(amount) FROM entries")
        records = cursor.fetchall()[0][0]
        print(records)
        return records
    
    finally:
        cursor.close()
        connection.close()


def register(subparsers):
    p1 = subparsers.add_parser(
        "flavours",
        help="list all added flavours",
        description="list all added flavours",
        aliases=["lf"])
    p1.set_defaults(func=list_flavours)

    p2 = subparsers.add_parser(
        "entries",
        help="Provides a list of all added entries",
        description="list all entries",
        aliases=["le"]
    )

    p2.set_defaults(func=list_entries)

