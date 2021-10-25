from . import Session
from .models import TABLES

def print_db():
    """Prints all of the records to the command line."""
    
    session = Session()

    print()
    for table in TABLES:
        print(f'{f"{table.__tablename__.upper()}S":-^30}')
        for record in session.query(table).all():
            print(record)
    print()


if __name__ == '__main__':
    print_db()
    